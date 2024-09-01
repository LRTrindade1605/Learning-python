texto = 'It was a bright cold day in april, and the clock was couting thirteen!'
def exercicio_2(texto):
    contagem = {}
    for caracter in texto:
        contagem.setdefault(caracter, 0)
        contagem[caracter] = contagem[caracter] + 1
    return [contagem]
print(exercicio_2(texto))
