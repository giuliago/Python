import operator
import os

paises = {
}

def verifica(error_msg = "Entrada inválida"):
    paises_nome = input("Entre com o país: ")
    if paises_nome.isdigit():
        print(error_msg)
        return verifica()
    paises_nome = paises_nome.title()
    for key in paises:
        if paises_nome == key:
            print("País já listado.")
            return verifica()
    return paises_nome

def ask_float(msg, error_msg = "Valor inválido"):	
    try:
        number = float(input(msg))
    except ValueError:
        print(error_msg)
        return ask_float(msg)
    return number	

def atribui():
    paises_nome = verifica()       
    paises_pib = ask_float("Entre com o PIB: ")
    paises[paises_nome] = paises_pib

def print_organizado():
    sorted_paises = list(reversed(sorted(paises.items(), key=operator.itemgetter(1))))
    for key, value in sorted_paises:
        print(key + ": " + str(value))

def soma_pib():
    result = 0
    for key in paises:
        result += paises[key]
    return result

def mostra_pais(pais):
    x = False
    for key in paises:
        if key == pais.title():
            print("PIB: " + str(paises[key]))
            x = True
    if x == False:
        y = input("País não encontrado. Você procurou por: " + pais.title() + "\nDeseja fazer uma nova consulta? S ou N\n")
        if y.upper() == "S":
            return mostra_pais(input("Entre com o país a ser consultado: "))
            
def menu():
    x = "S"
    while(x.upper() == "S"):
        atribui()
        x = input("Deseja continuar? S ou N\n")

    os.system("clear")
    print_organizado()
    print("A soma do PIB é: " + str(soma_pib()))

    x = input("Deseja consultar um país? S ou N\n")
    if x.upper() == "S":
        mostra_pais(input("Entre com o país a ser consultado: "))

menu()