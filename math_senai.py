def calcular_pi(n_termos):
    pi_aprox = 0
    denominador = 1
    sinal = 1
    
    for _ in range(n_termos):
        pi_aprox += sinal * (4 / denominador)
        denominador += 2
        sinal *= -1
        
    return pi_aprox

termos = 100000000
valor_pi = calcular_pi(termos)

print(f"Aproximação de PI com {termos} termos: {valor_pi}")
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
