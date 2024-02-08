import tkinter as tk
from calculadora_funcs import calcular, limpar_tela

def criar_botao(janela, texto, comando, linha, coluna, colunas_span=1, largura=4, altura=2, cor_fundo="lightgray", cor_texto="black"):
    botao = tk.Button(janela, text=texto, command=comando, width=largura, height=altura, bg=cor_fundo, fg=cor_texto)
    botao.grid(row=linha, column=coluna, columnspan=colunas_span, padx=5, pady=5)
    return botao

def criar_label(janela, texto, linha, coluna, colunas_span=4, tamanho_fonte=12):
    label = tk.Label(janela, text=texto, font=("arial", tamanho_fonte))
    label.grid(row=linha, column=coluna, columnspan=colunas_span, pady=5)
    return label

def cria_entry(janela, linha, coluna, colunas_span=4, largura=30):
    entry = tk.Entry(janela, width=largura, font=("Arial", 14))
    entry.grid(row=linha, column=coluna, columnspan=colunas_span, pady=5)
    return entry

def criar_calculadora():
    janela = tk.Tk()
    janela.title("Calculadora")
    janela.geometry("400x600")
    janela.configure(bg="lightblue")

    resultado = tk.StringVar()

    entrada = cria_entry(janela, 1, 0)

    criar_botao(janela, "7", lambda: entrada.insert(tk.END, "7"), 2, 0)
    criar_botao(janela, "8", lambda: entrada.insert(tk.END, "8"), 2, 1)
    criar_botao(janela, "9", lambda: entrada.insert(tk.END, "9"), 2, 2)
    criar_botao(janela, "/", lambda: entrada.insert(tk.END, "/"), 2, 3)

    criar_botao(janela, "4", lambda: entrada.insert(tk.END, "4"), 3, 0)
    criar_botao(janela, "5", lambda: entrada.insert(tk.END, "5"), 3, 1)
    criar_botao(janela, "6", lambda: entrada.insert(tk.END, "6"), 3, 2)
    criar_botao(janela, "*", lambda: entrada.insert(tk.END, "*"), 3, 3)

    criar_botao(janela, "1", lambda: entrada.insert(tk.END, "1"), 4, 0)
    criar_botao(janela, "2", lambda: entrada.insert(tk.END, "2"), 4, 1)
    criar_botao(janela, "3", lambda: entrada.insert(tk.END, "3"), 4, 2)
    criar_botao(janela, "-", lambda: entrada.insert(tk.END, "-"), 4, 3)

    criar_botao(janela, "0", lambda: entrada.insert(tk.END, "0"), 5, 0)
    criar_botao(janela, ".", lambda: entrada.insert(tk.END, "."), 5, 1)
    criar_botao(janela, "=", lambda: calcular(entrada, resultado), 5, 2)  # Corrigido para chamar a função calcular
    criar_botao(janela, "+", lambda: entrada.insert(tk.END, "+"), 5, 3)

    criar_botao(janela, "Limpar Tela", lambda: limpar_tela(entrada, resultado), 6, 0, colunas_span=4, largura=20, altura=4, cor_fundo="red", cor_texto="white")

    resultado_label = criar_label(janela, "", 7, 0, colunas_span=4, tamanho_fonte=16)
    resultado_label.config(textvariable=resultado)

    janela.mainloop()

criar_calculadora()