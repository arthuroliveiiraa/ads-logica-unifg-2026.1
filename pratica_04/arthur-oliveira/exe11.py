presentes_bruto = ["  maria ", "joão", "ana clara", "Bruno", "carla"]
consulta = "joão"


presentes = []
for nome in presentes_bruto:
    presentes.append(nome.strip().title())


consulta_padronizada = consulta.strip().title()

print("Lista padronizada:", presentes)


if consulta_padronizada in presentes:
    print(f"{consulta_padronizada} está presente. ")
else:
    print(f"{consulta_padronizada} não está na lista. X")


outra = "Fernando"
if outra in presentes:
    print(f"{outra} está presente. ")
else:
    print(f"{outra} não está na lista. X")