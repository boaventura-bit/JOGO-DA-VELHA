import tkinter as tk
from tkinter import messagebox
import random

# Função para inicializar o jogo
def iniciar_jogo(modo):
    global jogador_atual, modo_de_jogo
    jogador_atual = "X"
    modo_de_jogo = modo
    for linha in range(3):
        for coluna in range(3):
            botoes[linha][coluna].config(text="", state=tk.NORMAL)

# Função para verificar se há um vencedor
def verificar_vencedor():
    for i in range(3):
        if (botoes[i][0]["text"] == botoes[i][1]["text"] == botoes[i][2]["text"] != "") or \
           (botoes[0][i]["text"] == botoes[1][i]["text"] == botoes[2][i]["text"] != ""):
            return True
    if (botoes[0][0]["text"] == botoes[1][1]["text"] == botoes[2][2]["text"] != "") or \
       (botoes[0][2]["text"] == botoes[1][1]["text"] == botoes[2][0]["text"] != ""):
        return True
    return False

# Função para verificar se há empate
def verificar_empate():
    for linha in range(3):
        for coluna in range(3):
            if botoes[linha][coluna]["text"] == "":
                return False
    return True

# Função para desabilitar todos os botões
def finalizar_jogo():
    for linha in range(3):
        for coluna in range(3):
            botoes[linha][coluna].config(state=tk.DISABLED)

# Função para o clique do jogador
def clique_botao(linha, coluna):
    global jogador_atual
    if botoes[linha][coluna]["text"] == "" and botoes[linha][coluna]["state"] == tk.NORMAL:
        botoes[linha][coluna]["text"] = jogador_atual
        if verificar_vencedor():
            messagebox.showinfo("Fim de Jogo", f"Jogador {jogador_atual} venceu!")
            finalizar_jogo()
        elif verificar_empate():
            messagebox.showinfo("Fim de Jogo", "Empate!")
            finalizar_jogo()
        else:
            jogador_atual = "O" if jogador_atual == "X" else "X"
            if modo_de_jogo == "PC" and jogador_atual == "O":
                jogada_pc()

# Função para o PC fazer uma jogada aleatória
def jogada_pc():
    opcoes = [(linha, coluna) for linha in range(3) for coluna in range(3) if botoes[linha][coluna]["text"] == ""]
    if opcoes:
        linha, coluna = random.choice(opcoes)
        botoes[linha][coluna]["text"] = "O"
        if verificar_vencedor():
            messagebox.showinfo("Fim de Jogo", "PC venceu!")
            finalizar_jogo()
        elif verificar_empate():
            messagebox.showinfo("Fim de Jogo", "Empate!")
            finalizar_jogo()
        else:
            global jogador_atual
            jogador_atual = "X"

# Configuração da janela principal
janela = tk.Tk()
janela.title("Jogo da Velha")

# Variáveis do jogo
jogador_atual = "X"
modo_de_jogo = "Player"
botoes = [[None, None, None] for _ in range(3)]

# Criação da grade de botões
for linha in range(3):
    for coluna in range(3):
        botoes[linha][coluna] = tk.Button(janela, text="", font=("Arial", 20), width=5, height=2,
                                          command=lambda l=linha, c=coluna: clique_botao(l, c))
        botoes[linha][coluna].grid(row=linha, column=coluna)

# Botões para selecionar o modo de jogo
frame_modos = tk.Frame(janela)
frame_modos.grid(row=3, column=0, columnspan=3)

botao_player = tk.Button(frame_modos, text="2 Jogadores", command=lambda: iniciar_jogo("Player"))
botao_player.pack(side=tk.LEFT)

botao_pc = tk.Button(frame_modos, text="Contra o PC", command=lambda: iniciar_jogo("PC"))
botao_pc.pack(side=tk.LEFT)

# Iniciar o loop principal da interface gráfica
iniciar_jogo("Player")
janela.mainloop()
