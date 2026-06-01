def num(a, b, c, d, e):
    maior = max(a, b, c, d, e)
    menor = min(a, b, c, d, e)

    return maior, menor

# teste 1 -
maior, menor = num(1, 2, 3, 4, 23)
print(f'Maior: {maior}')
print(f'Menor: {menor}')