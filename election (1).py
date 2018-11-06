import os

presidentes = {
19: {"candidato":"Alvaro Dias", "votos":0},
24: {"candidato":"Ciro Gomes", "votos":0},
45: {"candidato":"Geraldo Alckmin", "votos":0},
21: {"candidato":"Jair Bolsonaro", "votos":0}, 
42: {"candidato":"Marina Silva", "votos":0},
13: {"candidato":"Lula", "votos":0}, 
29: {"candidato":"PSTU", "votos":0},
0: {"candidato": "Nulo", "votos":0},
1: {"candidato": "Inicializa", "votos":0}
}

senadores = {
324: {"candidato":"Chico SantAnna", "votos":0},
123: {"candidato":"Cristovam Buarque", "votos":0},
456: {"candidato":"Hélio Queiroz", "votos":0},
754: {"candidato":"Marcelo", "votos":0}, 
967: {"candidato":"Leila do Vôlei", "votos":0},
345: {"candidato":"Professora Amábile", "votos":0}, 
658: {"candidato":"Paulo Roque", "votos":0},
0: {"candidato": "Nulo", "votos":0},
1: {"candidato": "Inicializa", "votos":0}
}

governadores = {
25: {"candidato":"Alberto Fraga", "votos":0},
24: {"candidato":"Alexandre Guerra", "votos":0},
45: {"candidato":"Eliana Pedrosa", "votos":0},
21: {"candidato":"Fátima Sousa", "votos":0}, 
42: {"candidato":"General Paulo Chagas", "votos":0},
0: {"candidato": "Nulo", "votos":0},
1: {"candidato": "Inicializa", "votos":0}
}

def votacao(candidato):
    confirmation = "N"
    while confirmation.upper() == "N":
        num = input("Informe o número do seu candidato: ")
        try:
            num = int(num)
            print("O candidato escolhido foi: ", candidato[num]["candidato"])
            candidato[num]["votos"] += 1
            confirmation = "S"
        except (ValueError, KeyError) as a:
            confirmation = input("Você irá anular seu voto. Confirma? (S/N): ")
            if confirmation.upper() == "S":
                print("Voto anulado.")
                candidato[0]["votos"] += 1

def resultado(candidato):
    tmp = candidato[1]
    candidatos = []
    for key in candidato:
        if tmp["votos"] <= candidato[key]["votos"] and candidato[key]["votos"] != 0 and key != 0:
            tmp = candidato[key]
            candidatos.append(candidato[key])
    if (len(candidatos) > 1):
        print("Empate entre:")
        for i in candidatos:
            print(i['candidato'] + "\nVotos:" + str(i['votos']))        
    else:
        print(tmp["candidato"] + "\nVotos:" + str(tmp["votos"]))

def resultadoSenadores():
    tmp = senadores[1]
    senador = []
    for key in senadores:
        if tmp["votos"] <= senadores[key]["votos"] and senadores[key]["votos"] != 0 and key != 0:
            tmp = senadores[key]
            senador.append(senadores[key])
    if (len(senador) > 2):
        print("Empate entre:")
        for i in senador:
            print(i['candidato'] + "\nVotos:" + str(i['votos']))
    elif len(senador) == 0:
        print(senadores[1]['candidato'] + "\nVotos:" + str(senadores[1]['votos']))
    else:
        for i in senador:
            print(i['candidato'] + "\nVotos:" + str(i['votos']))

def resultadoTotal(candidates):
    for key in candidates:
        if key != 1:
	        print(candidates[key]["candidato"] + " : " + str(candidates[key]["votos"]))


election = True

while election:
    tentativa = 1
    while (tentativa == 1):
        try:
            choice = int(input("---------------------------------\n" +
            "1. Para votar\n" +
            "2. Para sair\n" +
            "---------------------------------\n" +
            "Opção: "))
            if choice == 1:
                choice = int(input("---------------------------------\n" + 
                "1. Presidente\n" + 
                "2. Senador\n" +
                "3. Governador\n" +
                "---------------------------------\n" +
                "Opção: "))
                if(choice == 1):
                    votacao(presidentes)
                elif(choice == 2):
                    votacao(senadores)
                elif(choice == 3):
                    votacao(governadores)
            elif choice == 2:
                election = False
            else:
                print("Masss que burrrooo! Escolha um Número.")	
            tentativa = 0
        except (ValueError, KeyError) as a:
            print("Insira o valor correto")           			

os.system("cls")
print("------------------------Resultado da eleição------------------------")
print("\nPresidente:\n")
resultadoTotal(presidentes)
print("\nSenador:\n")
resultadoTotal(senadores)
print("\nGovernador:\n")
resultadoTotal(governadores)
print("\n--------------------------Presidente------------------------------")
resultado(presidentes)
print("\n---------------------------Senador--------------------------------")
resultadoSenadores()
print("\n--------------------------Governador------------------------------")
resultado(governadores)