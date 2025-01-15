# questao2.py
def fibonacci(numero):
    a, b = 0, 1
    sequencia = [a, b]

    while b < numero:
        a, b = b, a + b
        sequencia.append(b)

    if numero in sequencia:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."


numero_informado = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
resultado = fibonacci(numero_informado)
print(resultado)