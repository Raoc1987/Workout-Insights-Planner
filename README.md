# Workout Insights \& Planner

## Demo

* Imagem de exemplo (EDA): veja docs/eda\_volume\_semanais.png.
* Artefatos: docs/weekly\_metrics.csv e docs/recommendations.csv.

## Quickstart

1. Criar ambiente e instalar:

   * pip install -e .
   * pip install pandas matplotlib seaborn pydantic jupyter nbconvert

2. Executar notebook EDA:

   * jupyter nbconvert --to notebook --execute notebooks/01\_eda.ipynb --output docs/01\_eda\_executed.ipynb

3. Artefatos:

   * docs/weekly\_metrics.csv
   * docs/recommendations.csv
   * docs/eda\_volume\_semanais.png.

## Como funciona

* src/workout\_insights/core.py: ingestão (load\_workouts), métricas semanais (weekly\_metrics), deteção de platô (detect\_plateau) e recomendações (recommend\_progression).
* notebooks/: 01\_eda (exploração e figuras), 02\_model (platôs e recomendações), 03\_report (relato final).
* data/: dados de entrada (raw/).
* docs/: artefatos para partilha (csv, figuras, notebooks executados).

## Contribuição

* Sugestões e PRs bem-vindos; abre issues com contexto e exemplo mínimo reprodutível para facilitar revisão, que é prática comum em repositórios populares.​
* 
* Ver CONTRIBUTING.md para padrões de código e fluxo de PR quando disponível.

## Licença e Citação



* Licença: ver LICENCE.
* Citação: Ver CITATION.cff.
