with open('Calc1.stk', "r") as arquivo:
    pilha = []
    tokens = []

    for elemento in arquivo:
        elemento = elemento.rstrip()

        try:
            if elemento.isdigit():
                tokens.append(('NUM', elemento))
                pilha.append(int(elemento))
            elif elemento in ['+', '-', '*', '/']:
                tokens.append(('OP', elemento))
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
            else:
                raise ValueError(f"Unexpected character: {elemento}")
        except ValueError as e:
            print(f"Error: {e}")
            break

    print("Tokens:")
    for token in tokens:
        print(f"Token [type={token[0]}, lexeme={token[1]}]")

    print(resultado_final)