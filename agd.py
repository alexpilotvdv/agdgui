# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import serial

connected = False
ser = serial.Serial("COM4", 115200)
while not connected:
    serin = ser.read()
    print('serin= ' + str(serin))
    connected = True
    #пример работы с портом
for i in range(300):
    pt=ser.read()
    print('port= ' + str(pt))

ser.close()

WIDTH = 360  # ширина игрового окна
HEIGHT = 480 # высота игрового окна
FPS = 30 # частота кадров в секунду
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AGD")
clock = pygame.time.Clock()

# Цикл игры
running = True
while running:

    # Ввод процесса (события)
    # Обновление
    # Визуализация (сборка)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
    # держим цикл на правильной скорости
    clock.tick(FPS)
    # Рендеринг
    screen.fill(BLACK)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
