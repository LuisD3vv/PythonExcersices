from  math import pi
def factura(total,iva=0.21):
    return total * iva


cantidad = int(input("Ingresa la cantidad: "))
iva = float(input("Ingresa el iva: "))
if not iva:
    print(factura(cantidad,iva))
    

def volumen(radio,altura):
    return pi * pow(radio,2) * altura

while True:
    parametro1 = input("Ingresa el radio del circulo: ")
    parametro2 = input("Ingresa la altura del circulo: ")    
    try:
        parametro1 = float(parametro1)
        parametro2 = float(parametro2)
    except:
        print("Ambos valores deben de ser numericos")
    else:
        resultado = volumen(parametro1,parametro2)
        print(f"El volumen del cilindro es: {resultado}")
        break