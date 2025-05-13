print("-=-=-=-=-CALCULADORA CIENTIFICA-=-=-=-=-")
import math

while True:

    escolha = input(
    "começar a calculadora (-sim- ou -nao-): "
).strip().lower()

    print("\nOperações disponíveis:")
    print("(+) Adição")
    print("(-) Subtração")
    print("(*) Multiplicação")
    print("(/) Divisão")
    print("(sen) Seno")
    print("(cos) Cosseno")
    print("(tan) Tangente")

    operação = input("escolha a operação desejada: ").strip().lower()

    if operação in ["+", "-", "*", "/"]:
        numeros = []

        while True:
            try:
                numero = float(input(
                    "digite um numero"
                ))
                numeros.append(numero)
            except ValueError:
                print(
                    "desculpa digite um numero valido"
                )

            continuar = input(
                "voce quer colocar mais um numero a contagem? (sim ou nao): "
                ).strip().lower()
            
            if continuar == 'nao':
                print('descupa ocorreu um erro:')
                break

        if not numeros:
            print("nehum numero adicionado: ")
            continue

        resultado = numeros[0]

        for num in numeros[1:]:
            if operação == "+":
                resultado += num

            elif operação == "-":
                resultado -= num

            elif operação == "*":
                resultado *= num

            elif operação == "/":
                if num == 0:

                    print("Erro: divisão por zero!")
                    break
                resultado /= num

        print("resultado:", resultado)

    if operação in ["sen", "cos", "tan"]:
        try:
            angulo = float(input(
                "digite o angulo em graus"
            ))
            rad = math.radians(angulo)

            if operação == "sen":
                resultado = math.sin(rad)

            elif operação == "cos":
                resultado = math.cos(rad)

            elif operação == "tan":
                resultado = math.tan(rad)
            
            print(f"Resultado de {operação}({angulo}°):", resultado)

        except ValueError:
            print("Por favor, digite um valor numérico válido para o ângulo.")

    else:
        print("Operação inválida, tente novamente.")

    continuar = input("Deseja fazer outra operação? (sim ou nao): ").strip().lower()

    if continuar == "nao":
        print("Encerrando a calculadora. Até logo!")
        break