import pygame
import os
import time
import random
from tkinter import simpledialog
import pickle
pygame.init()
pygame.display.set_caption("Space Machine")
branco = (255, 255, 255)
red = (255, 0, 0)
fundo = pygame.image.load("assets/bg.jpg")
tamanho = (1000, 563)
cor_fundo = (128, 128, 128)
som_fundo = pygame.mixer.Sound("assets/Space_Machine_Power.mp3")
icone = pygame.image.load("assets/space.png")
pygame.display.set_icon(icone)
pygame.mixer.music.load("assets/Space_Machine_Power.mp3")
pygame.mixer_music.play(-1)
clock = pygame.time.Clock()
display = pygame.display.set_mode(tamanho)
pygame.mixer.music.load("assets/Space_Machine_Power.mp3")
pygame.mixer_music.play(-1)
estrelas = []
tamanho_letra = 20
fonte = pygame.font.Font(None, tamanho_letra)
texto_1 = "Pressione F10 para Salvar os Pontos"
posicao_texto_1 = (1, 1)
texto_2 = "Pressione F11 para Carregar os Pontos"
posicao_texto_2 = (1, 15)
texto_3 = "Pressione F12 para Deletar os Pontos"
posicao_texto_3 = (1, 30)
running = True
while running:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_F10:
                    with open("points.pkl", "wb") as arquivo:
                        pickle.dump(estrelas, arquivo)
                    print("Pontos salvos!")
                elif event.key == pygame.K_F11:
                    try:
                        with open("points.pkl", "rb") as arquivo:
                            estrelas = pickle.load(arquivo)
                        print("Pontos carregados!")
                    except FileNotFoundError:
                        print("Arquivo de pontos não encontrado.")
                elif event.key == pygame.K_F12:
                    estrelas = []
                    print("Pontos deletados!")
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                item = simpledialog.askstring("Space", "Nome da Estrela: ")
                print(item)
                if item is None:
                    item = "desconhecido"
                estrelas.append((pos, item))
        def escrita(texto, cor, posicao):
            texto_renderizado = fonte.render(texto, True, cor)
            display.blit(texto_renderizado, posicao)
        display.blit(fundo, (0, 0))
        
        escrita(texto_1, branco, posicao_texto_1)
        escrita(texto_2, branco, posicao_texto_2)
        escrita(texto_3, branco, posicao_texto_3)

        for pos, item in estrelas:
            pygame.draw.circle(display, branco, pos, 3)
            texto_superficie = fonte.render(item + " - " + str(pos), True, branco)
            texto_rect = texto_superficie.get_rect()
            texto_rect.center = (pos[0], pos[1] - 20)
            display.blit(texto_superficie, texto_rect)
        if len(estrelas) >= 2:
            pontos = [pos for pos, item in estrelas]
            pygame.draw.lines(display, branco, False, pontos, 2)

            for i in range(len(estrelas) - 1):
                po1 = estrelas[i][0]
                po2 = estrelas[i+1][0]
                soma = po1[0] + po2[0] + po1[1] + po2[1]
                meio_x = (po1[0] + po2[0]) // 2
                meio_y = (po1[1] + po2[1]) // 2
                texto_soma = fonte.render(str(soma), True, red)
                texto_soma_rect = texto_soma.get_rect()
                texto_soma_rect.center = (meio_x, meio_y)
                display.blit(texto_soma, texto_soma_rect)

        pygame.display.update()
        clock.tick(75)
    except Exception as e:
        print("Ocorreu um erro:", e)
pygame.quit()


