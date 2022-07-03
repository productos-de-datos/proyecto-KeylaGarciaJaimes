"""función encargada de crear el data lake y sus subcarpetas"""


def create_data_lake():

    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    """

    import os

    os.mkdir("data_lake")

    directory = ["landing", "raw", "cleansed", "business"]

    for subdir in directory:
        os.mkdir(os.path.join("data_lake", subdir))

    dir_business = [
        "business/reports",
        "business/features",
        "business/reports/figures",
        "business/forecasts",
    ]

    for subdir in dir_business:
        os.mkdir(os.path.join("data_lake", subdir))


if __name__ == "__main__":
    import doctest

    create_data_lake()
    doctest.testmod()
