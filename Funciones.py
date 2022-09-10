import pandas as pd
import csv
# Funcion de busqueda por equipo
def gen_busqueda():
    lineas = pd.read_csv('mantenimiento.csv')
    df = pd.DataFrame(lineas)
    equipo = input('Ingrese equipo a buscar\n')
    resultado = df[df['equipo']==equipo]
    return (resultado)
# Funcion de busqueda por operario
def busqueda_op():
    lineas = pd.read_csv('mantenimiento.csv')
    df = pd.DataFrame(lineas)
    operario = input('Ingrese nombre del operario\n')
    resultado = df[df['operario']==operario]
    return (resultado)
# Funcion de calculo hs totales trabajadas
def calc_hstrab():
    lineas = pd.read_csv('mantenimiento.csv')
    df = pd.DataFrame(lineas)
    suma = df['hs trabajadas'].sum()
    print('Esta opcion devuelve la sumatoria de las hs registradas en el archivo')
    print('Hs totales:', suma)
# Funcion de visualizacion      
def ver_archivo():
    lineas = pd.read_csv('mantenimiento.csv')
    print (lineas)
# Funcion de agregado de datos
def add_datos():
    header = ['equipo', 'hs trabajadas', 'tarea', 'operario']
    csvfile = open('mantenimiento.csv', 'a', newline='')
    writer= csv.DictWriter(csvfile,fieldnames=header)
    equipo = input('Ingrese equipo\n')
    tarea = input('Ingrese tarea\n')
    operario = input('Ingrese operario\n')
    hs_trab = input('Ingrese horas\n')
    nueva_fila = {'equipo':(equipo), 'tarea': (tarea), 'operario': (operario), 'hs trabajadas': (hs_trab)}
    writer.writerow(nueva_fila)
    csvfile.close
    print('Informacion almacenada')
