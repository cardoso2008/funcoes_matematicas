import fatorial

def calcular_e(n):
    if n < 0:
        print("ERROR: NUMERO NEGATIVO")
        return None
    soma = 0
    for i in range(0,n+1):
        soma+=1/ fatorial.calcular_fatorial(i)    
    return soma

numero=10

print(calcular_e(numero))