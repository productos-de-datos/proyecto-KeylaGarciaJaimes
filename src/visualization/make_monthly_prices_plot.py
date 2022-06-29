def make_monthly_prices_plot():
    import pandas as pd
    import matplotlib.pyplot as plt

    df_csv=pd.read_csv("data_lake/business/precios-mensuales.csv")
    df_csv["fecha"] = pd.to_datetime(df_csv["fecha"])

    grafica = df_csv.plot("fecha", 'precio')

    grafica.set_xlabel('fecha', fontsize=14)
    grafica.set_ylabel('precio', fontsize=14)
    grafica.set_title("Precios Promedios Mensual", fontsize=18)
    grafica.legend('PromMens')

    plt.savefig("data_lake/business/reports/figures/monthly_prices.png")


if __name__ == "__main__":
    import doctest

    make_monthly_prices_plot()

    doctest.testmod()
