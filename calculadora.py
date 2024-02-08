import tkinter as tk

def calcular():
    try:
        resultado.set(eval(entrada.get()))
    except Exception as e:
        resultado.set('Erro')

def limpar_tela():
    entrada.delete(0, tk.END)
    resultado.set('')

janela = tk.Tk()
janela.title('Calculadora Simples')

entrada = tk.Entry(janela, width=20)
entrada.grid(row=0, column=0, columnspan=4)

resultado = tk.StringVar()
tk.Label(janela, textvariable=resultado).grid(row=1, column=0, columnspan=4)

botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=',  '+'
]

row_val = 2
col_val = 0

for botao in botoes:
    tk.Button(janela, text=botao, command=lambda b=botao: entrada.insert(tk.END, b) if b != '=' else calcular()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(janela, text='Limpar tela', command=limpar_tela).grid(row=row_val, column=col_val, columnspan=4)
janela.mainloop()