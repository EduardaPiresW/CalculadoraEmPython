try:
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero: "))
except ValueError:
    print("Erro: Digite apenas numeros")
    exit()

while True: 
    op = input("Qual operacao deseja? (+, -, *, /): ")
    if op in ["+", "-", "*", "/"]:
        break
    print("Operacao invalida. Tente Novamente.")

if op == "+":
    resultado = n1 + n2
elif op == "-":
    resultado = n1 - n2
elif op == "*":
    resultado = n1 * n2
elif op == "/":
    if n2 == 0:
        print("Erro: Divisao po zero nao e permitido.")
    else:
        resultado = n1 / n2

resultadof = f"{resultado:.2f}" .rstrip("0").rstrip(".")
    
print(f"{n1} {op} {n2} = {resultadof}")