import numpy as np
import pandas as pd

"""
Unaltered columns:
- CONSULTAS
- ESTCIVMAE
- RACACOR
- ESCMAE2010
- PARTO

These have the same category as listed in the docs:
https://github.com/GOPAD-Datasus/DB_SINASC/blob/main/docs/features.md
"""


def apgar(df: pd.DataFrame) -> np.array:
    conditions = [
        (df["APGAR5"] <= 5),  # 1, 2, 3, 4 e 5
        (df["APGAR5"] <= 7),  # 6 e 7
        (df["APGAR5"] >= 8),  # 8, 9 e 10
    ]

    choices = [1, 2, 3]  # Very bad  # Bad  # Good

    return np.select(conditions, choices, default=np.nan)


def gestacao(df: pd.DataFrame) -> np.array:
    conditions = [
        (df["GESTACAO"] < 3),  # 1 e 2
        (df["GESTACAO"] < 5),  # 3 e 4
        (df["GESTACAO"] == 5),  # 5
        (df["GESTACAO"] == 6),  # 6
    ]

    choices = [1, 2, 3, 4]  # Pre termo extremo  # Pre termo  # Normal  # Pos termo

    return np.select(conditions, choices, default=np.nan)


def peso(df: pd.DataFrame) -> np.array:
    conditions = [(df["PESO"] < 2500), (df["PESO"] < 4000), (df["PESO"] >= 4000)]

    choices = [1, 2, 3]  # Peso baixo  # Peso normal  # Peso alto

    return np.select(conditions, choices, default=np.nan)


def mesprenat(df: pd.DataFrame) -> np.array:
    conditions = [
        (df["MESPRENAT"] <= 3),  # 1, 2 e 3
        (df["MESPRENAT"] <= 6),  # 4, 5 e 6
        (df["MESPRENAT"] <= 9),  # 7, 8 e 9
    ]

    choices = [1, 2, 3]  # Início bom  # Início ruim  # Início extremamente ruim

    return np.select(conditions, choices, default=np.nan)


def idademae(df: pd.DataFrame) -> np.array:
    conditions = [
        (df["IDADEMAE"] <= 20),  # [  , 20]
        (df["IDADEMAE"] <= 29),  # [21, 29]
        (df["IDADEMAE"] <= 35),  # [30, 35]
        (df["IDADEMAE"] > 35),  # [36,   ]
    ]

    choices = [1, 2, 3, 4]  # Início bom  # Início ruim  # Início extremamente ruim

    return np.select(conditions, choices, default=np.nan)


def codocupmae(df: pd.DataFrame) -> np.array:
    conditions = [df["CODOCUPMAE"] == 999992, df["CODOCUPMAE"] != 999992]

    choices = [1, 2]  # Dona de casa  # Não dona de casa (trabalha)

    return np.select(conditions, choices, default=np.nan)


def qtdfilvivo(df: pd.DataFrame) -> np.array:
    conditions = [
        (df["QTDFILVIVO"] == 0),  # 0
        (df["QTDFILVIVO"] <= 2),  # 1 e 2
        (df["QTDFILVIVO"] >= 3),  # 3+
    ]

    choices = [0, 1, 2]  # 0 filhos  # 1 ou 2 filhos  # 3+ filhos

    return np.select(conditions, choices, default=np.nan)


def qtdfilmort(df: pd.DataFrame) -> np.array:
    conditions = [df["QTDFILMORT"] == 0, df["QTDFILMORT"] != 0]

    choices = [0, 1]  # Nenhum filho morto  # 1+ filho(s) morto(s)

    return np.select(conditions, choices, default=np.nan)


def codmunnasc(x):
    return int(str(x)[:1])
