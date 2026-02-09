import os

def rigthrute(file):
    return os.path.join(os.path.dirname(__file__),file)

file = "source.txt"
destin = "destination.txt"

# El with puede manejar dos archivos al mismo tiempo
try:
    with open(rigthrute(file),"r") as file1, open(rigthrute(destin),"a") as file2:
        palabras = []
        for i in file1.read():
            palabras.append(i)
        file2.writelines(palabras)
except FileExistsError:
    print("No exite el archivo")