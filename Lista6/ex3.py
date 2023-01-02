import pandas as pd
import glob

metricas = ["CBO", "LCO", "LOC", "WMC"]

def formar_df(df_lista: list, coluna="COL1") -> pd.DataFrame:
    serie = pd.concat(df_lista)
    serie = serie.groupby(serie[coluna]).sum()
    return serie


def forma_serie(metrica: str) -> pd.DataFrame:
    dados = []

    def corrigir_dados() -> None:
        for i in dados[:2]:
            i["COL1"] = i["COL1"].str.replace("org.springframework.", "spring-", regex=False)

    for csv in glob.iglob(f"{metrica}*.csv"):
        temp_df = pd.read_csv(csv)
        dados.append(temp_df)

    corrigir_dados()

    serie = formar_df(dados)
    return serie


solucao = [forma_serie(metrica) for metrica in metricas]

solucao = pd.concat(solucao).groupby("COL1").sum().drop_duplicates()
solucao.to_csv("all_metrics.csv")

print(solucao)
