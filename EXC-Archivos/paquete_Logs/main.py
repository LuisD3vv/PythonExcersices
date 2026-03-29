from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent
file = BASE / "errors.log"
output_error = 'EXC-Archivos/paquete_Logs/output_errors.txt'


try:
    conteo = defaultdict(int)
    detalle_error = []
    with open(file) as file, open(output_error,'w') as output:
        for line in file.readlines():
            separado = line.split(" ")
            conteo[separado[2]]+=1
            if separado[2] == "ERROR":
                detalle_error.append({"ERROR":separado[3:]})
        for error in detalle_error:
            for i,k in error.items():
                output.writelines((i+ ": " + " ".join(k)))
except FileNotFoundError:
    print("No se encontro el archivo")

print(f"Cantidad de Detalles detectados: {dict(conteo)}")



