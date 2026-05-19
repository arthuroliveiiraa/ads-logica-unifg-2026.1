nomes_brutos = ["Porronto", "Pimpolho", "Queiroz"]

nomes_padronizados = []

for nome in nomes_brutos:
    nome_limpo = nome.strip().title()
    nomes_padronizados.append(nome_limpo)

print(nomes_padronizados)


print("Total de nomes:", len(nomes_padronizados))