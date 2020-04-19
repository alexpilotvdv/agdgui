# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import serial
import re


ser = serial.Serial("COM5", 115200)

    #пример работы с портом
def getxy():
    rtx = ''
    rty = ''
    pt=str(ser.readline())
    match = re.search('[x]\d{1,3}', pt)
    if match:
        rtx=match[0]
        rtx = rtx[1:]
        #если меньше 0
    match = re.search('[x][-]\d{1,3}', pt)
    if match:
        rtx=match[0]
        rtx = rtx[1:]
    match = re.search('[y]\d{1,3}', pt)
    if match:
        rty=match[0]
        rty = rty[1:]
    match = re.search('[y][-]\d{1,3}', pt)
    if match:
        rty=match[0]
        rty = rty[1:]
    return rtx, rty



WIDTH = 800  # ширина игрового окна
HEIGHT = 600 # высота игрового окна
FPS = 30 # частота кадров в секунду
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ground.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.korr = (HEIGHT / 2)/90
    def update(self,y):
        new_image=self.image
        new_rect=self.image.get_rect()
        new_rect.y = self.rect.y + y
        new_rect.center = (WIDTH / 2, (HEIGHT / 2) + y*self.korr)
        screen.blit(new_image, new_rect)
        #if self.rect.left > WIDTH:
        #    self.rect.right = 0


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("agd.png").convert_alpha()
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
ground = Ground()
player = Player()
all_sprites.add(ground)
all_sprites.add(player)

# Цикл игры
ugol=0
horiz=0
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
            ser.close()
            running = False

     # Обновление



    # Рендеринг
    screen.blit(ground.image, ground.rect)
    #
    #all_sprites.draw(screen)
    #screen.fill(BLUE)
	#Получим данные из com порта
    xr,yr = getxy()
    if yr != '':
        horiz = int(yr)
    if xr != '':
        ugol = int(xr)
        print('y = ' + str(horiz))
    ground.update(horiz)

    player.rot_center(ugol)

    #all_sprites.update()
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
