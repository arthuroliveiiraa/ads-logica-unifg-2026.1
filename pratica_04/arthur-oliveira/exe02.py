nome_completo = "Chapolin Silva Corolado"


partes = nome_completo.split()
print(partes)


nome_hifenado = "-".join(partes)
print(nome_hifenado)


primeiro = partes[0]
ultimo = partes[-1]
print(f"Primeiro: {primeiro} | Último: {ultimo}")