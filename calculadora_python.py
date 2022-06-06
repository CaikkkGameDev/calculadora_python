# Cauculadora em Python
#######################


# Perguntar pro usuario o tipo de operação
# Perguntar o primeiro numero
# Perguntar o segundo numero
# Calcular o resultado
# Imprimir na tela

while True:
 operacao = input('qual operação (+, -, *, /) você quer fazer ou \'Q\' para sair?')
 if operacao == 'q' or operacao == 'Q':
     break
 elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
     num1 = int(input('digite o primeiro numero:'))
     num2 = int(input('digite o segundo numero:'))
 else:
     print('operação é invalida')

 if operacao == '+':
     total = num1 + num2
     print(total)

 elif operacao == '-':
     total = num1 - num2
     print(total)

 elif operacao == '*':
     total = num1 * num2
     print(total)

 elif operacao == '/':
     total = num1 / num2
     print(total)
