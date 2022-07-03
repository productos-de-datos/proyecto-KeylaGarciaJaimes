# pylint: disable=invalid-name
# pylint: disable=unsubscriptable-object

from skforecast.ForecasterAutoreg import ForecasterAutoreg
from skforecast.ForecasterAutoregCustom import ForecasterAutoregCustom
from skforecast.ForecasterAutoregMultiOutput import ForecasterAutoregMultiOutput
from skforecast.model_selection import grid_search_forecaster
from skforecast.model_selection import backtesting_forecaster

def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    #raise NotImplementedError("Implementar esta función")
 import pandas as pd

    df_csv = pd.read_csv("data_lake/cleansed/precios-horarios.csv",
        sep=",",         # separador de campos  
        )
    df_csv["fecha"] = pd.to_datetime(df_csv["fecha"])
    df_csv = df_csv.rename(columns={'fecha':'x', 'precio':'y'})
    df_csv = df_csv.asfreq('MS')
    df_csv = df_csv.sort_index()

    # Split data into train-test
    # ==============================================================================
    steps = 36
    data_train = df_csv[:-steps]
    data_test  = df_csv[-steps:]

# Create and train forecaster
# ==============================================================================
forecaster = ForecasterAutoreg(
                regressor = RandomForestRegressor(random_state=123),
                lags = 6
                )

forecaster.fit(y=data_train['y'])
forecaster
   


if __name__ == "__main__":
    import doctest

    doctest.testmod()
