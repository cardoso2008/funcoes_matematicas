def calcular_exp(x , termos=10):
    
    resultado = 1
    termo = 1

    for n in range(1, termos+1):
        termo = termo*x/n
        resultado += termo

    return resultado

print(calcular_exp(2))