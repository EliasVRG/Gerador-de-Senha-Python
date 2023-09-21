import random
import tkinter as tk
from tkinter import Entry, Label, Button
import pyperclip

# Função para gerar a senha
def gerar_senha():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    comprimento = int(comprimento_entry.get())
    senha = ""
    for i in range(comprimento):
        senha += random.choice(caracteres)
    senha_label.config(text="Senha gerada: " + senha)
    senha_copiavel.set(senha)  # Configurar a senha no valor da variável

# Função para copiar a senha para a área de transferência
def copiar_senha():
    senha = senha_copiavel.get()
    pyperclip.copy(senha)

# Configurar a janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas")

# Alterar a cor de fundo da tela
janela.configure(bg="lightblue")

# Rótulo e campo de entrada para o comprimento da senha
comprimento_label = Label(janela, text="Digite o comprimento da senha desejada: ", bg="lightblue")
comprimento_label.pack()
comprimento_entry = Entry(janela)
comprimento_entry.pack()

# Botão para gerar a senha
gerar_botao = Button(janela, text="Gerar Senha", command=gerar_senha)
gerar_botao.pack()

# Rótulo para exibir a senha gerada
senha_label = Label(janela, text="", bg="lightblue")
senha_label.pack()

# Variável para armazenar a senha gerada
senha_copiavel = tk.StringVar()

# Botão para copiar a senha
copiar_botao = Button(janela, text="Copiar Senha", command=copiar_senha)
copiar_botao.pack()

# Iniciar a janela principal
janela.mainloop()
