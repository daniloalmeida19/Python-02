nome = str(input("Digite seu nome: "))
if nome == "Danilo":
    print("Que nome bonito!")
elif nome == "pedro" or nome == "Jão" or nome == "joão":
    print("tenha um bom dia, {}".format(nome))
elif nome == "Maria":
    print("Que nome bonito!")
else:
    print("Seu nome é tão bonito quanto Danilo!")
