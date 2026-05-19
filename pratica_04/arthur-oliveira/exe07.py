estudantes = ["Ana", "Bruno", "Carla", "Daniel"]
procurado = "Carla"

encontrado = False

for estudante in estudantes:
    if estudante == procurado:
        encontrado = True
        break 

if encontrado:
    print(f"{procurado} está presente.")
else:
    print(f"{procurado} não foi encontrado.")


procurado2 = "Lucas"
if procurado2 in estudantes:
    print(f"{procurado2} está presente.")
else:
    print(f"{procurado2} não foi encontrado.")