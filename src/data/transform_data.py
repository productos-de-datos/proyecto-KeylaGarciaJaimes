
def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    #raise NotImplementedError("Implementar esta función")
    import pandas as pd
    
    for i in range(1995,2022):
        if i == 2016 or i==2017:
            df_xls=pd.read_excel('data_lake/landing/{}.xls'.format(i),index_col=None, header=None)
            df = df_xls.dropna(axis=0, thresh=10)
            df = df.iloc[1:]
            df=df[df.columns[0:25]]
            df[0]=pd.to_datetime(df[0], format="%Y/%m/%d")
            df.to_csv('data_lake/raw/{}.csv'.format(i), encoding='utf-8', index=False, header=True)

        else:
            df_xls=pd.read_excel ('data_lake/landing/{}.xlsx'.format(i),index_col=None, header=None)
            df = df_xls.dropna(axis=0, thresh=10)
            df = df.iloc[1:]
            df=df[df.columns[0:25]]
            df[0]=pd.to_datetime(df[0], format="%Y/%m/%d")
            df.to_csv('data_lake/raw/{}.csv'.format(i), encoding='utf-8', index=False, header=True)   


if __name__ == "__main__":
    import doctest
    transform_data()

    doctest.testmod()
