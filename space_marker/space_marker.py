import pygame
import os
import time
import random
from tkinter import simpledialog

pygame.init()
pygame.display.set_caption("Space Machine")
branco = (255, 255, 255)
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
            
            
            display.blit(fundo, (0, 0))
        
        pygame.display.update()
        clock.tick(75)
    except Exception as e:
        print("Ocorreu um erro:", e)
pygame.quit()


