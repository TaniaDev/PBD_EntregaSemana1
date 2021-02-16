n = int(input())
while n > 0:
    mina = input()
    diamante = 0
    cont = 0
    for i in mina:
        if i == '<':
            cont += 1 # O "inicio" (<) do diamante
        elif i == '>':
            if (cont - 1) >= 0: # Caso o cont seja negativo, significa que não há diamantes a serem formados 
                cont -= 1 # Caso o cont seja positivo, significa que o "inicio" (<) dos diamantes podem ser fechados com seus respectivos "finais" (>),
                diamante += 1 # Formando então um diamante
    print(diamante)
    n -= 1