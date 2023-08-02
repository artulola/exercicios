dist = float(input("Digite a distância em quilômetros:"))
tempo = float(input("Digite o tempo em minutos:"))

vel = (dist * 1000) / (tempo * 60)

print("Velocidade média em m/s:", vel)