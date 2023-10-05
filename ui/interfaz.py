from prettytable import PrettyTable


def mensaje_bienvenida():
    print("""
    |----------------------------------------------------------------------|
    | BIENVENIDO AL SISTEMA DE CONSULTA DE CASOS DE COVID - 19 EN COLOMBIA |
    |----------------------------------------------------------------------|    
    """
          )


def menu_principal():
    mensaje_bienvenida()
    limite_registros = input("Digite limite registro: ")
    departamento = input("Digite Departamento: ").upper()
    return [limite_registros, departamento]


def mostrar_datos(datos_df):
    pretty = PrettyTable()
    pretty.field_names = ['ciudad_municipio_nom', 'departamento_nom', 'edad', 'fuente_tipo_contagio', 'estado']
    for registro in range(len(datos_df)):
        pretty.add_row([
            datos_df.loc[registro, 'ciudad_municipio_nom'],
            datos_df.loc[registro, 'departamento_nom'],
            datos_df.loc[registro, 'edad'],
            datos_df.loc[registro, 'fuente_tipo_contagio'],
            datos_df.loc[registro, 'estado'],
        ])
    print(pretty)
