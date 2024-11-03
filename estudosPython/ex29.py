#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada Km acima do limite

velocidade = float(input("Digite a velocidade do carro em Km/h: "))

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 7.00
    print(f"Você foi multado! O valor da multa é R$ {multa:.2f}.")
else:
    print("Você está dentro do limite de velocidade.")