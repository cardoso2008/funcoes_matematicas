def seno_taylor(x, k):
    soma = 0
    termo = x

    for n in range(k):
        soma += termo
        termo = -termo * x * x / ((2*n+2)*(2*n+3))

    return soma


pi = 3.141592653589793
graus = 90

radianos = graus * pi / 180

resultado = seno_taylor(radianos, 15)

print("Seno de 90 graus ≈", resultado)