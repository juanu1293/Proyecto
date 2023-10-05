import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets . Note ’None ’
# in place of application token , and no username or password :
client = Socrata("www.datos.gov.co", None)


def consultar(limite_registros, departamento):
    results = client.get("gt2j-8ykr", limit=limite_registros, departamento_nom=departamento)

    results_df = pd.DataFrame.from_records(results)
    return results_df


def filtrar_datos(datos_consultados):
    datos_filtrados = datos_consultados[['ciudad_municipio_nom', 'departamento_nom', 'edad', 'fuente_tipo_contagio', 'estado']]
    return datos_filtrados
