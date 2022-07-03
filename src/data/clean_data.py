# pylint: disable=consider-using-f-string
# pylint: disable=import-outside-toplevel
# pylint: disable=consider-using-with
# pylint: disable=line-too-long
"""Clean_data"""


def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    # raise NotImplementedError("Implementar esta función")

    import pandas as pd

    empty_list = []

    for i in range(1995, 2022):

        df_csv = pd.read_csv("data_lake/raw/{}.csv".format(i))

        empty_list.append(df_csv)

        new_df = pd.concat(empty_list, axis=0, ignore_index=True)
        new_df.columns = [
            "fecha",
            "00",
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
        ]
        new_df["fecha"] = pd.to_datetime(new_df["fecha"], format="%Y-%m-%d")
        df_melted = pd.melt(
            new_df,
            id_vars=["fecha"],
            value_vars=[
                "00",
                "01",
                "02",
                "03",
                "04",
                "05",
                "06",
                "07",
                "08",
                "09",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
            ],
            var_name="hora",
            value_name="precio",
        )
        df_melted["precio"] = df_melted["precio"].fillna(
            df_melted.groupby("fecha")["precio"].transform("mean")
        )
        df_melted.to_csv(
            "data_lake/cleansed/precios-horarios.csv", encoding="utf-8", index=False
        )


if __name__ == "__main__":
    import doctest

    clean_data()

    doctest.testmod()
