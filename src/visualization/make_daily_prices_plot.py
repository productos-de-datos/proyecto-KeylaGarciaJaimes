def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    #raise NotImplementedError("Implementar esta función")

    import pandas as pd
    import matplotlib.pyplot as plt
   
    df_csv=pd.read_csv("data_lake/business/precios-diarios.csv")
    df_csv["fecha"] = pd.to_datetime(df_csv["fecha"])

    grafica = df_csv.plot("fecha", 'precio')

    grafica.set_xlabel('fecha', fontsize=14)
    grafica.set_ylabel('precio', fontsize=14)
    grafica.set_title("Precios Promedios Diarios", fontsize=18)
    grafica.legend('PromDiario')

    plt.savefig("data_lake/business/reports/figures/daily_prices.png")


if __name__ == "__main__":
    import doctest

    make_daily_prices_plot()

    doctest.testmod()
