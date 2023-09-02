def linha(numero, layout):
    print(f"{layout}" * numero)

def texto(texto, layout):
    print(f"{layout} {texto}")

def cabecalho(layout):
    texto("Aula Pratica e Inovação", layout)
    texto("Professor: Eduardo", layout)
    texto("Aluno: Vinicius", layout)    
    texto("Python", layout)

def rodape(layout):
    texto(f"")

def tabuada(numero, ate, layout):
    linha(25, layout)
    texto("Tabuada do: %s" % numero, layout)
    linha(25, layout)
    for x in range(0, ate):
        texto("%d X %d = %d" % (numero, (x + 1), (numero * (x + 1))), layout)

for i in range(1, 11):
    if ((i % 2) == 0):
        layout = "*"
        linha(25, layout)
        cabecalho(layout)
        tabuada(i, 10, layout)
        linha(25, layout)
    else:
        layout = "#"
        linha(25, layout)
        cabecalho(layout)
        tabuada(i, 10, layout)
        linha(25, layout)
