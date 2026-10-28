#O limite de peso de um inventário ´50kg. O jogador está carregando 48kg e tenta pegar um item de 3kg. Use operadores para verificar se o novo peso será menor ou igual ao limite.

peso_atual = 48
item = 3

if peso_atual + item > 50:
    print("Pegar tal item vai deixar ultrapassar o limite de peso.")
