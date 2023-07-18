import random
import pygame
import sys
import math


PROB4 = 0.1


res = 800
size = 150
fps = 30


pygame.init()
sc = pygame.display.set_mode([res, res])
clock = pygame.time.Clock()

mass = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

def newnumber():
    global mass
    resp = False
    m = [i for i in range(16)]
    random.shuffle(m)
    for i in m:
        if mass[i // 4][i % 4] == 0:
            if random.random() > (1 - PROB4):
                mass[i // 4][i % 4] = 4
            else:
                mass[i // 4][i % 4] = 2
            resp = True
            break
    return resp


def toleft():
    global mass
    for i in range(4):
        k = []
        nwmass = []
        for p in range(4):
            if mass[i][p] != 0:
                nwmass.append(mass[i][p])
        for j in range(len(nwmass)):
            if j == len(nwmass) - 1:
                k.append(nwmass[j])
            else:
                if nwmass[j] == nwmass[j + 1]:
                    k.append(nwmass[j] + nwmass[j + 1])
                    nwmass[j] = 0
                    nwmass[j + 1] = 0
                else:
                    k.append(nwmass[j])
        for _ in range(4 - len(k)):
            k.append(0)
        mass[i] = k


def rot90():
    global mass
    mass = [[mass[j][i] for j in range(len(mass))] for i in range(len(mass[0])-1, -1, -1)]


newnumber()
while True:
    sc.fill(pygame.Color("black"))

    f1 = pygame.font.Font(None, 120)

    for i in range(4):
        for j in range(4):
            pygame.draw.rect(sc, (255, 255, 255 - (math.log(mass[j][i] + 1, 2) * 20)),
                             (40 + (40 + size) * i, 40 + (40 + size) * j, size, size))
            sc.blit(f1.render(str(mass[j][i]), True, (0, 0, 120)), (40 + (40 + size) * i, 40 + (40 + size) * j))


    pygame.display.flip()
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        toleft()
        if not newnumber():
            print("Вы проиграли")
            break
        pygame.time.wait(200)
    if key[pygame.K_RIGHT]:
        rot90()
        rot90()
        toleft()
        rot90()
        rot90()
        if not newnumber():
            print("Вы проиграли")
            break
        pygame.time.wait(200)
    if key[pygame.K_DOWN]:
        rot90()
        rot90()
        rot90()
        toleft()
        rot90()
        if not newnumber():
            print("Вы проиграли")
            break
        pygame.time.wait(200)
    if key[pygame.K_UP]:
        rot90()
        toleft()
        rot90()
        rot90()
        rot90()
        if not newnumber():
            print("Вы проиграли")
            break
        pygame.time.wait(200)



