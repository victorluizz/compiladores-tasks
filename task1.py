

with open('Calc1.stk', "r") as arquivo:
    pilha = []

    for elemento in arquivo:

        elemento = elemento.rstrip()
        
        if elemento.isdigit():
            pilha.append(int(elemento))
        else:
            operador2 = pilha.pop()
            operador1 = pilha.pop()

            if elemento == "+":
                resultado = operador1 + operador2
            elif elemento == "-":
                resultado = operador1 - operador2
            elif elemento == "*":
                resultado = operador1 * operador2
            elif elemento == "/":
                resultado = operador1 / operador2

            pilha.append(resultado)
            resultado_final = resultado

print(resultado_final)








