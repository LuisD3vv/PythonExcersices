def media(*args): # mejor usar el args
    resultado = sum(args)
    return resultado / 3
llamada = media(2,3,5)
print(llamada)