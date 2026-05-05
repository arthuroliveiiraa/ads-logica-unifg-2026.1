
def torque_kloss(s, s_max, torque_max):
    if s == 0:
        return 0  
    return (2 * torque_max) / ((s / s_max) + (s_max / s))

frequencia = float(input("Frequência (Hz): "))
polos = int(input("Número de polos (par): "))
torque_max = float(input("Torque máximo (Nm): "))
s_max = float(input("Escorregamento máximo (ex: 0.2): "))



if polos <= 0 or polos % 2 != 0:
    print("Número de polos inválido! Tem que ser par e positivo.")
    exit()


Ns = (120 * frequencia) / polos
print(f"\nVelocidade síncrona: {Ns:.0f} RPM\n")

passo = int(Ns // 20)


for N in range(0, int(Ns) + 1, passo):

    s = (Ns - N) / Ns
    torque = torque_kloss(s, s_max, torque_max)



    barras = int(torque / torque_max * 50)
    print(f"{N:4} RPM | {'#' * barras} ({torque:.2f} Nm)")