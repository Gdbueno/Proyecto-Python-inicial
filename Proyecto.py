# -----------------------------
# Proyecto Python
# Autor: Guillermo Bueno
# Version: 1.0
# guillermodavidbueno@gmail.com
# -----------------------------

from Funciones import *

if __name__ == '__main__':
    print ('**PROYECTO PYTHON INICIAL**')
    while True:
        opciones = '''\n
        Menu:
        1. Consulta por equipo
        2. Consulta por operario
        3. Agregar registro
        4. Visualizar
        5. Hs totales trabajadas
        6. Salir
        Opcion Seleccionada:'''
        while True:
            opcion = input(opciones)
            if opcion.isdigit():
                break
            else:
                print ('Seleccione otra opcion')
        opcion = int(opcion)
        if opcion == 1:
            # Consulta por equipo
            print (gen_busqueda())
        elif opcion == 2:
            # Consulta por operario
            print (busqueda_op())
        elif opcion == 3:
            # Agregar registro
            add_datos()
        elif opcion == 4:
            # Visualizar csv
            ver_archivo()
        elif opcion == 5:
            # Calculo de hs totales
            calc_hstrab()
        elif opcion == 6:
            # Finalizar programa
            break
        else:
            print('Ingrese otra opcion')
