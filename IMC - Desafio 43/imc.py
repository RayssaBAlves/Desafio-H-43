peso = float(input("Digite  o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura * altura)

if (imc < 18.5):
    print("Abaixo do peso")
elif (imc< 25): 
    print("Peso normal")   
elif (imc < 30):
    print("Sobrepeso")
elif (imc < 35):
    print("Obsedidade grau 1")
elif (imc < 40):
    print("Obsedidade grau 2")
else:
    print("Obsedidade grau 3")                             