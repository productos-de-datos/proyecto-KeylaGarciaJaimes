"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""


from urllib import request


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    #raise NotImplementedError("Implementar esta función")

    import requests

    for i in range(1995,2022):
        if i == 2016 or i==2017:
            url_xls = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xls?raw=true'
            file = requests.get(url_xls, allow_redirects=True)
             #with open(os.path.join("data_lake", "landing"))
            open('data_lake/landing/{}.xls'.format(i), 'wb').write(file.content)
        else: 
            
            url_xlsx = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xlsx?raw=true'
            file = requests.get(url_xlsx, allow_redirects=True)
            open('data_lake/landing/{}.xlsx'.format(i), 'wb').write(file.content)

if __name__ == "__main__":
    import doctest
    ingest_data()
    doctest.testmod()
