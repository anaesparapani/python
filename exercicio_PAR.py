import time
numero = int(input("Digite um número inteiro positivo: "))

while numero <= 0:
    numero = float(input("Por favor digite um número positivo: "))

if numero % 2 == 0:
    print('"P-A-R!!!"')
else:
    print("Tente outra vez!")    


time.sleep(5)