import re

class Regex:
    NUM = r"\d+(\.\d+)?"
    PLUS = r"\+"
    MINUS = r"\-"
    STAR = r"\*"
    SLASH = r"/"

with open('Calc1.stk', "r") as arquivo:
    pilha = []
    tokens = []
    resultado_final = None

    for elemento in arquivo:
        elemento = elemento.rstrip()

        try:
            if re.match(Regex.NUM, elemento):
                tokens.append(('NUM', elemento))
                pilha.append(float(elemento))
            elif re.match(Regex.PLUS, elemento):
                tokens.append(('OP', 'PLUS'))
                operador2 = pilha.pop()
                operador1 = pilha.pop()
                resultado = operador1 + operador2
                pilha.append(resultado)
                resultado_final = resultado
            elif re.match(Regex.MINUS, elemento):
                tokens.append(('OP', 'MINUS'))
                operador2 = pilha.pop()
                operador1 = pilha.pop()
                resultado = operador1 - operador2
                pilha.append(resultado)
                resultado_final = resultado
            elif re.match(Regex.STAR, elemento):
                tokens.append(('OP', 'STAR'))
                operador2 = pilha.pop()
                operador1 = pilha.pop()
                resultado = operador1 * operador2
                pilha.append(resultado)
                resultado_final = resultado
            elif re.match(Regex.SLASH, elemento):
                tokens.append(('OP', 'SLASH'))
                operador2 = pilha.pop()
                operador1 = pilha.pop()
                resultado = operador1 / operador2
                pilha.append(resultado)
                resultado_final = resultado
            else:
                raise ValueError(f"Unexpected character: {elemento}")
        except ValueError as erro:
            print(f"Error: {erro}")
            break

    print("Tokens:")
    for token in tokens:
        print(f"Token [type={token[0]}, lexeme={token[1]}]")

    if resultado_final is not None:
        print(int(resultado_final))
