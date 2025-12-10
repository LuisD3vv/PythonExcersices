import csv,os

archivo = 'cotizacion.csv'
salida = 'minimosYmaximos.csv'
ruta = os.path.join(os.path.dirname(__file__))


def quitarComas(valor):
    flotante = valor.replace(',','.')
    return float(flotante)

os.system("clear")
def fichero():
    ibex = []
    try:
        with open(os.path.join(ruta,archivo),'r',encoding='utf-8-sig') as file:
            csv_reader = csv.reader(file, delimiter=';')
            for i in csv_reader:
                # Tratar con lineas vacias
                if not i:
                    continue
                # mayor a un rango mayor o igual
                if len(i) >= 6:
                    ibex.append({
                        "Nombre":i[0],
                        "Final":i[1],
                        "Maximo":i[2],
                        "Minimo":i[3],
                        "Volumen":i[4],
                        "Efectivo":i[5]
                        })
    except FileNotFoundError:
        print("El archivo introducido no existe.")
    return ibex

def exportdata(opcion):   
    '''Obtener  el maximo, minimo yu media de dada columna'''
    match opcion:
        case 'Final':
            columna = 'Final'
        case 'Maximo':
            columna = 'Maximo'
        case 'Minimo':
            columna = "Minimo"
        case 'volumen':
            columna = "Volumen"
        case 'Efectivo':
            columna = "Efectivo"
        case _:
            print("opcion no disponible.")
    resultados = fichero()
    maymen = []
    promedio = 0
    elementos = 0
    for valor in resultados:
        if valor[columna] in ['Final',"Efectivo",'Máximo','Minimo','Volumen']:
            continue
        elementos += 1
        promedio += quitarComas(valor[columna])
        maymen.append(quitarComas(valor[columna]))
    try:
        # solo necesario para guadar cambios 
        with open(os.path.join(ruta,salida),'w',encoding='utf-8-sig') as file:
            csv_writer = csv.writer(file)

    except FileNotFoundError:
        print("El archivo introducido no existe.")
    finally:
        print(f"Valores basados en la columna elegida -> {columna}")
        print(f'El valor minimo es: {min(maymen)} ')
        print(f'El valor maximo es: {max(maymen)}')
        print(f'El promedio es: {round(promedio / elementos)}')

print("""
        Que columna deseas conocer: 
        | Final Máximo Mínimo Volumen Efectivo |
        """)
usuario = input(">> ").capitalize()
exportdata(usuario)