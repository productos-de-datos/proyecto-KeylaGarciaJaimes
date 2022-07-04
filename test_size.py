"""
Obtener nombres de la carpeta data_lake/raw en una lista.
Hacerlo con un list comprehension.
"""
import pytest
import pandas as pd

# @pytest.fixture(scope='session')


def nombres():
    import os
    import pandas as pd

    lista = []
    for file in os.listdir("data_lake/raw"):
        if file.endswith(".csv"):
            lista.append(file)
    return lista


def test_data_():
    assert1 = nombres()
    expect1 = [
        "1997.csv",
        "1998.csv",
        "1999.csv",
        "2000.csv",
        "2001.csv",
        "2002.csv",
        "2003.csv",
        "2004.csv",
        "2005.csv",
        "2006.csv",
        "2007.csv",
        "2008.csv",
        "2009.csv",
        "2010.csv",
        "2011.csv",
        "2012.csv",
        "2013.csv",
        "2014.csv",
        "2015.csv",
        "2016.csv",
        "2017.csv",
        "2018.csv",
        "2019.csv",
        "2020.csv",
    ]
    print(assert1[10], expect1[10])
    assert expect1[10] == assert1[10]