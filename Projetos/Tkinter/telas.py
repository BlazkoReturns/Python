import tkinter as tk

# 1. Cria a janela principal (a "raiz" da aplicação)
#    Por convenção, chamamos esta variável de 'root' ou 'janela'
janela = tk.Tk()

# 2. Define um título para a janela
janela.title("Meu Primeiro App GUI")

# 3. Define um tamanho inicial para a janela (largura x altura)
janela.geometry("400x300") 

# 4. Inicia o "loop principal" da aplicação
#    Esta linha é essencial. Ela "liga" a janela,
#    faz com que ela fique aberta e esperando por
#    interações do usuário (cliques, digitação, etc.).
janela.mainloop()

# O código abaixo desta linha só será executado DEPOIS que a janela for fechada.
print("A janela foi fechada, o programa terminou.")
