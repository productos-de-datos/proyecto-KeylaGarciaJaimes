def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    #raise NotImplementedError("Implementar esta función")

    import pandas as pd
   
    df_csv=pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    df_csv["fecha"] = pd.to_datetime(df_csv["fecha"])
    df_csv=df_csv.groupby(pd.Grouper(key="fecha", freq="M")).mean().reset_index()
    df_csv[["fecha", "precio"]].to_csv("data_lake/business/precios-mensuales.csv", encoding="utf-8", index=False)


if __name__ == "__main__":
    import doctest
    compute_monthly_prices()

    doctest.testmod()
