# Workout Insights & Planner

## Demo
Imagem de exemplo (EDA): veja docs/eda_volume_semanais.png.

## Quickstart
1. Criar ambiente e instalar:
   - pip install -e .
   - pip install pandas matplotlib seaborn pydantic jupyter nbconvert
2. Executar notebook EDA:
   - jupyter nbconvert --to notebook --execute notebooks/01_eda.ipynb --output docs/01_eda_executed.ipynb
3. Artefatos:
   - docs/weekly_metrics.csv
   - docs/recommendations.csv

## Como funciona
- src/workout_insights/core.py implementa ingestão, métricas semanais, platô e recomendações.
- notebooks/ orquestra EDA, modelagem e relatório.

## Contribuição
- Issues com “good first issue” e PRs bem-vindos.
- Ver CONTRIBUTING.md.

## Citação
- Ver CITATION.cff.
