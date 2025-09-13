def interseccion(lista_1,lista_2):
    for lista_1, lista_2 in zip(lista_1,lista_2):
        print(f"{lista_1}, lo conocen por, '{lista_2}'")

lista_1 = ['Mexico','Francia','china','peru','usa']
lista_2 = ['narcos','peste a culo y torre eifel','tecnologia','palomas','armas y guerra' ]

interseccion(lista_1,lista_2)