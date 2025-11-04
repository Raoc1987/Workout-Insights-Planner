# 🏋️ Workout Insights and Planner
[![build-linux](https://github.com/Raoc1987/Workout-Insights-Planner/actions/workflows/ci.yml/badge.svg)](https://github.com/Raoc1987/Workout-Insights-Planner/actions/workflows/ci.yml)

Ferramenta para análise de treinos semanais, detecção de platôs e recomendações, com notebook reprodutível e CI em GitHub Actions.

## 🚀 Funcionalidades
- 📊 Métricas semanais (volume, séries, repetições)
- 🧠 Detecção de estagnação (platô)
- 💡 Recomendações acionáveis
- 📈 Visualizações automáticas
- ⚙️ Pipeline automatizado (GitHub Actions)

## 📦 Instalação

pip install -r requirements.txt


Requisitos mínimos:

pandas
matplotlib
seaborn
pydantic
jupyter
nbconvert


## ⚡ Quickstart

Executar o notebook 01_eda.ipynb e gravar outputs em docs/:
jupyter nbconvert --to notebook --execute notebooks/01_eda.ipynb --output 01_eda_executed.ipynb --output-dir=docs


Se estás no Windows e preferes forçar imports do pacote em src/ sem empacotar:
set PYTHONPATH=%CD%\src & jupyter nbconvert --to notebook --execute notebooks/01_eda.ipynb --output 01_eda_executed.ipynb --output-dir=docs



## 🖼️ Demo
- Imagem (EDA): [docs/eda_volume_semanais.png](docs/eda_volume_semanais.png)
- Artefatos: [docs/weekly_metrics.csv](docs/weekly_metrics.csv), [docs/recommendations.csv](docs/recommendations.csv), [docs/01_eda_executed.ipynb](docs/01_eda_executed.ipynb)

## 🧭 Como funciona
- notebooks/01_eda.ipynb: carrega dados, calcula métricas semanais, gera figuras e exporta artefatos para docs/
- src/workout_insights/core.py: ingestão com validação de schema e funções de métricas
- data/raw/: CSV de exemplo (example_workouts_and_planner.csv) ou os teus dados
- docs/: outputs prontos para partilha (CSV, PNG e notebook executado)

## 🛠️ Estrutura

├── notebooks/
│ └── 01_eda.ipynb
├── src/
│ └── workout_insights/
│ └── core.py
├── data/
│ └── raw/
│ └── example_workouts_and_planner.csv # opcional (exemplo)
├── docs/
│ ├── weekly_metrics.csv
│ ├── recommendations.csv
│ ├── eda_volume_semanais.png
│ └── 01_eda_executed.ipynb
├── .github/
│ └── workflows/
│ └── ci.yml
├── requirements.txt
└── README.md


## 🔁 Reprodutibilidade e CI
- Cada push/PR para main aciona o workflow que instala dependências, executa notebooks/01_eda.ipynb e publica os artefatos em docs/ como anexos do job[attached_file:1].  
- Mantém caminhos estáveis via pathlib e grava outputs em docs/ para evitar falhas por diretórios inexistentes ou diferenças de maiúsculas/minúsculas no runner Linux[attached_file:1].  
- O badge no topo mostra o estado atual do pipeline em tempo real[attached_file:1].  

## 🤝 Contribuição
- Issues e PRs são bem-vindos; descreve contexto e exemplo mínimo reprodutível[attached_file:1].  
- Mantém mensagens de commit objetivas e pequenas[attached_file:1].  
- Sugestão: adicionar testes com pytest + nbval para validar o notebook em CI[attached_file:1][web:405].  

## 📜 Licença
- Define uma licença (ex.: MIT) e publica o ficheiro LICENSE[attached_file:1].  

## 🧾 Citação
- Adiciona um CITATION.cff para referência adequada em relatórios ou publicações[attached_file:1].  

---
Dicas:
- Se não pretendes versionar docs/01_eda_executed.ipynb, adiciona-o ao .gitignore e deixa o CI publicá-lo como artefato[attached_file:1].  
- Mantém os nomes de ficheiros exatamente como acima (Linux é case‑sensitive)[attached_file:1].  
