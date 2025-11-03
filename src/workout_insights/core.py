# src/workout_insights/core.py
from pydantic import BaseModel, Field
import pandas as pd

class WorkoutConfig(BaseModel):
    min_sessions_per_week: int = Field(2, ge=1)
    plateau_weeks: int = Field(3, ge=1)
    progressive_step_pct: float = Field(2.5, ge=0.0, le=10.0)

def load_workouts(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path, parse_dates=["date"])
    expected = {"date", "exercise", "sets", "reps", "weight_kg", "muscle_group"}
    missing = expected - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return df

def weekly_metrics(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["volume"] = df["sets"] * df["reps"] * df["weight_kg"]
    df["week"] = df["date"].dt.isocalendar().week
    out = df.groupby(["week", "muscle_group"], as_index=False).agg(
        sessions=("exercise", "nunique"),
        total_volume=("volume", "sum"),
        avg_intensity=("weight_kg", "mean"),
    )
    return out

def detect_plateau(weekly: pd.DataFrame, cfg: WorkoutConfig) -> pd.DataFrame:
    weekly = weekly.sort_values(["muscle_group", "week"]).copy()
    weekly["plateau"] = False
    for mg in weekly["muscle_group"].unique():
        w = weekly[weekly["muscle_group"] == mg]
        rolling = w["total_volume"].rolling(cfg.plateau_weeks, min_periods=cfg.plateau_weeks)
        stable = (rolling.max() - rolling.min()) <= 1e-6
        weekly.loc[w.index, "plateau"] = stable.fillna(False)
    return weekly

def recommend_progression(weekly: pd.DataFrame, cfg: WorkoutConfig) -> pd.DataFrame:
    recs = []
    for _, row in weekly.iterrows():
        if row["sessions"] < cfg.min_sessions_per_week:
            suggestion = "Adicionar 1 sessão esta semana"
        elif row["plateau"]:
            suggestion = f"Aumentar volume em {cfg.progressive_step_pct}%"
        else:
            suggestion = "Manter plano atual"
        recs.append({"week": row["week"], "muscle_group": row["muscle_group"], "suggestion": suggestion})
    return pd.DataFrame(recs)
