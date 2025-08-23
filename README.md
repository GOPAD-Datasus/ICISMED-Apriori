# Paper B: ICISMED | Apriori

## 📌 Overview

> This implementation is focused on the use of Apriori and Kmeans to extract valuable info. about prenatal risk groups 

This repository is based on our paper:  
**"A Hybrid Approach Based on Clustering and Association
Rules to Analyze Sociodemographic Profiles Related to
Newborn Health and Well-being"**   
Authors: Morsoleto, R. et al.  
Presented and accepted at: [ICISMED](https://www.icismed.org/) 2025, waiting publication

## 🚀 Setup

Requirements are described [here](pyproject.toml), and can be 
installed using the command:

```bash
poetry install
```
* Poetry is required to use the above command, for download info visit: [python-poetry.org](https://python-poetry.org/)
## ⚙ Run

```bash
poetry run python main.py
```

## 🔮 Structure

````mermaid
flowchart LR
    a[Pre-processing] --> b[K-means]
    b --> c[Apriori]
    c --> d[Post-processing]
````
- **Pre-processing**: Responsible to handle raw data, removing
missing values, classifying features and preparing it for
K-means
- **K-means**: Uses elbow method to determine the best number 
of clusters, then divides the data
- **Apriori**: Apply basket analysis to identify causes that
lead to high APGAR levels.
- **Post-processing**: Filters unnecessary rules


## ✨ Dataset

The dataset used corresponds to year 2022 and can be downloaded [here](https://github.com/GOPAD-Datasus/DB_SINASC)

## 📝 License
[LGNU](LICENSE) | © GOPAD 2025