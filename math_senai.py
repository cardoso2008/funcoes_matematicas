def calcular_exp(x , termos=10):
    
    resultado = 1
    termo = 1

    for n in range(1, termos+1):
        termo = termo*x/n
        resultado += termo

    return resultado

print(calcular_exp(2))
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
