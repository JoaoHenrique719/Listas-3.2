# O operador % (módulo) devolve o resto da divisão. Use-o para verificar se o número de moedas de um jogador é par. (Dica: moedas % 2 == 0).

moedas = int(input("Quantas moedas o jogador tem?"))

moedas %= 2

if moedas == 0:

    print("O jogador possui um número de moedas par.")
    
else: 
    print("O jogador possui um número impar de moedas.")
