"""Compute_monthly_prices"""
# pylint: disable=consider-using-f-string
# pylint: disable=import-outside-toplevel
# pylint: disable=consider-using-with
# pylint: disable=line-too-long


import pandas as pd
import matplotlib.pyplot as plt


def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """

    df_csv = pd.read_csv("data_lake/business/precios-mensuales.csv")
    df_csv["fecha"] = pd.to_datetime(df_csv["fecha"])

    grafica = df_csv.plot("fecha", "precio")

    grafica.set_xlabel("fecha", fontsize=14)
    grafica.set_ylabel("precio", fontsize=14)
    grafica.set_title("Precios Promedios Mensual", fontsize=18)
    grafica.legend("PromMens")

    plt.savefig("data_lake/business/reports/figures/monthly_prices.png")


if __name__ == "__main__":
    import doctest

    make_monthly_prices_plot()

    doctest.testmod()
