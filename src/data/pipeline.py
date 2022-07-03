# pylint: disable=consider-using-f-string
# pylint: disable=import-outside-toplevel
# pylint: disable=consider-using-with
# pylint: disable=line-too-long
"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""
import luigi
from luigi import Task, LocalTarget
import ingest_data
import transform_data
import clean_data
import compute_daily_prices
import compute_monthly_prices


class IngestData(Task):
    def output(self):
        return LocalTarget("data_lake/landing/rsl.txt")

    def run(self):
        with self.output().open("w") as outfile:
            ingest_data.ingest_data()


class TransformData(Task):
    def requires(self):
        return IngestData()

    def output(self):
        return LocalTarget("data_lake/raw/rsl2.txt")

    def run(self):
        with self.output().open("w") as outfile:
            transform_data.transform_data()


class CleanData(Task):
    def requires(self):
        return TransformData()

    def output(self):
        return LocalTarget("data_lake/cleansed/rsl3.txt")

    def run(self):
        with self.output().open("w") as outfile:
            clean_data.clean_data()


class DailyPrices(Task):
    def requires(self):
        return CleanData()

    def output(self):
        return LocalTarget("data_lake/business/precios-dia.csv")

    def run(self):
        with self.output().open("w") as outfile:
            compute_daily_prices.compute_daily_prices()


class MontlyPrices(Task):
    def requires(self):
        return CleanData()

    def output(self):
        return LocalTarget("data_lake/business/precios-mes.csv")

    def run(self):
        with self.output().open("w") as outfile:
            compute_monthly_prices.compute_monthly_prices()


class PreciosPromedioMensual(Task):
    def requires(self):
        return [DailyPrices(), MontlyPrices()]


if __name__ == "__main__":
    import doctest

    luigi.run(["PreciosPromedioMensual", "--local-scheduler"])

    doctest.testmod()
