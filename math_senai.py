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
def calcular_fatorial(n):
     contador=n
     if n <0:
          print("erro: Invalido")
          return None
     if n == 0:
          n=1
          return n
     if n > 0:
         for i in range(1,n):
              contador-=1
              n = n*contador
         return n
