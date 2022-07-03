"""Función que computa los precios promedios diarios"""


def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional



    """
    # raise NotImplementedError("Implementar esta función")

    import pandas as pd

    df_csv = pd.read_csv("data_lake/cleansed/precios-horarios.csv")
    df_csv = df_csv.groupby(["fecha"]).mean().reset_index()
    df_csv[["fecha", "precio"]].to_csv(
        "data_lake/business/precios-diarios.csv", encoding="utf-8", index=False
    )


if __name__ == "__main__":
    import doctest

    compute_daily_prices()
    doctest.testmod()
