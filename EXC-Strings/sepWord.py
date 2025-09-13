# Codigo que cuenta la cantidad de veces que aparece una palabra
entrada = input("ingresa palabra: ")
entrada_sep = entrada.split()
dic = {p: entrada_sep.count(p) for p in entrada_sep}
for p, cantidad in dic.items():
  print(f"{p} {cantidad}")