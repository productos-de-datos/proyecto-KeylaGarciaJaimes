# pylint: disable=consider-using-f-string
# pylint: disable=import-outside-toplevel
# pylint: disable=consider-using-with
# pylint: disable=line-too-long

"""Modulo de ingestiónd de data"""


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """

    import requests

    for fecha in range(1995, 2022):
        if fecha in (2016, 2017):
            url_xls = "https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xls?raw=true".format(
                fecha
            )
            file = requests.get(url_xls, allow_redirects=True)

            open("data_lake/landing/{}.xls".format(fecha), "wb").write(file.content)
        else:

            url_xlsx = "https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xlsx?raw=true".format(
                fecha
            )
            file = requests.get(url_xlsx, allow_redirects=True)
            open("data_lake/landing/{}.xlsx".format(fecha), "wb").write(file.content)


if __name__ == "__main__":
    import doctest

    ingest_data()
    doctest.testmod()
