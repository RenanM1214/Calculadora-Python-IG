def calcular(entrada, resultado):
    try:
        resultado.set(eval(entrada.get()))
    except:
        resultado.set('Erro')

def limpar_tela(entrada, resultado):
    entrada.delete(0, 'end')
    resultado.set('')
