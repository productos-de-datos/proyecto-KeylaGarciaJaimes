# pylint: disable=consider-using-f-string
# pylint: disable=import-outside-toplevel
# pylint: disable=consider-using-with
# pylint: disable=line-too-long
"""Transformar datos"""


def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    # raise NotImplementedError("Implementar esta función")
    import pandas as pd

    for i in range(1995, 2022):
        if i in (2016, 2017):
            df_xls = pd.read_excel(
                "data_lake/landing/{}.xls".format(i), index_col=None, header=None
            )
            dframe = df_xls.dropna(axis=0, thresh=10)
            dframe = dframe.iloc[1:]
            dframe = dframe[dframe.columns[0:25]]
            dframe[0] = pd.to_datetime(dframe[0], format="%Y/%m/%d")
            dframe.to_csv(
                "data_lake/raw/{}.csv".format(i),
                encoding="utf-8",
                index=False,
                header=True,
            )

        else:
            df_xls = pd.read_excel(
                "data_lake/landing/{}.xlsx".format(i), index_col=None, header=None
            )
            dframe = df_xls.dropna(axis=0, thresh=10)
            dframe = dframe.iloc[1:]
            dframe = dframe[dframe.columns[0:25]]
            dframe[0] = pd.to_datetime(dframe[0], format="%Y/%m/%d")
            dframe.to_csv(
                "data_lake/raw/{}.csv".format(i),
                encoding="utf-8",
                index=False,
                header=True,
            )


if __name__ == "__main__":
    import doctest

    transform_data()

    doctest.testmod()
