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