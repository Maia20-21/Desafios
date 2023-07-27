saldo = int(input("Digite seu saldo bancário"))
valor = int(input("Digite o valor que você deseja retirar da sua conta"))

if valor > saldo: print("Saldo insuficiente para essa transação")
else: print("Saldo retirado. Verifique o valor sacado")