# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import serial

#ser = serial.Serial("COM4", 115200)
#while not connected:
#    serin = ser.read()
#    print('serin= ' + str(serin))
#    connected = True
#    #пример работы с портом
#for i in range(300):
#    pt=ser.read()
#    print('port= ' + str(pt))

#ser.close()

WIDTH = 800  # ширина игрового окна
HEIGHT = 600 # высота игрового окна
FPS = 30 # частота кадров в секунду
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("line.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def rot_center(self, angle):
        w, h = self.image.get_size()
        box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(angle) for p in box]
        min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

        pivot = pygame.math.Vector2(w/2, -h/2)
        pivot_rotate = pivot.rotate(angle)
        pivot_move   = pivot_rotate - pivot
        pos=self.rect
        origin = (pos[0] + min_box[0] - pivot_move[0], pos[1] - max_box[1] + pivot_move[1])

        #center = self.image.get_rect().center
        #self.image = pygame.transform.rotate(self.image, angle)
        #new_rect = rotated_image.get_rect().center
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        rotated_image = pygame.transform.rotate(self.image, angle)
        screen.blit(rotated_image, origin)
        #print(new_rect)
        #screen.blit(rotated_image, self.rect.center)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AGD")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Цикл игры
ugol=0
running = True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    # Обновление
    # Визуализация (сборка)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

     # Обновление
    ugol+=1
    if ugol==360:
        ugol=0


    # Рендеринг
    #
    #all_sprites.draw(screen)
    screen.fill(BLACK)
    player.rot_center(ugol)
    #all_sprites.update()
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
