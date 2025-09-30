import pygame , sys
from pygame import *

pygame.init()
clock = pygame.time.Clock()

Screen_widht = 1200
Screen_heigth = 800
POSITION_PLATEAU = (5, 5)
CASE_SIZE = 70
pygame.display.set_caption('Serpent et Echelle')
screen = pygame.display.set_mode([Screen_widht, Screen_heigth])

def create_plateau():
    plateau = []
    rows = 10
    columns = 10
    for i in range(rows):
        liste=[]
        for j in range(columns):
            position_x_case = POSITION_PLATEAU[0] + (i * CASE_SIZE) + (5 * i)
            position_y_case = POSITION_PLATEAU[1] + (j * CASE_SIZE) + (5 * j)
            case = pygame.draw.rect(screen, (58,230,79,90), pygame.Rect(position_x_case, position_y_case, CASE_SIZE, CASE_SIZE))
            liste.append(case)
        plateau.append(liste)
    return plateau

class Joueur(pygame.sprite.Sprite):

    def __init__(self):
        super(Joueur, self).__init__()
        self.surf = pygame.Surface((20,25))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(10, 690)
        # self.position = [800, 0]

    def update(self, pressed_keys):
        if pressed_keys[K_z]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_d]:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_q]:
            self.rect.move_ip(-5, 0)
        # if pressed_keys[K_s]:
        #     self.rect.move_ip(0, 5)
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Screen_widht:
            self.rect.right = Screen_widht
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= Screen_heigth:
            self.rect.bottom = Screen_heigth

class Rival(pygame.sprite.Sprite):

    def __init__(self):
        super(Rival, self).__init__()
        self.surf = pygame.Surface((20,25))
        self.surf.fill((0,0,255))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(10, 720)
        # self.position = [800, 0]

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Screen_widht:
            self.rect.right = Screen_widht
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= Screen_heigth:
            self.rect.bottom = Screen_heigth
        

J1 = Joueur()
J2 = Rival()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            


    screen.fill((192,192,192))
        
    plateau_jeu = create_plateau()

    #   le plateau de jeu
    # pygame.draw.rect(screen, (58,230,79,90), (0,0,750,750))

    #   grillage horizontale
    pygame.draw.rect(screen, (255,255,255), (0,0,750,5))
    pygame.draw.rect(screen, (255,255,255), (0,75,750,5))
    pygame.draw.rect(screen, (255,255,255), (0,150,750,5))
    pygame.draw.rect(screen, (255,255,255), (0,225,750,5))
    pygame.draw.rect(screen, (255,255,255), (0,300,750,5))
    pygame.draw.rect(screen, (255,255,255), (0,375,750,5))
    pygame.draw.rect(screen, (255,255,255), (0,450,750,5))
    pygame.draw.rect(screen, (255,255,255), (0,525,750,5))
    pygame.draw.rect(screen, (255,255,255), (0,600,750,5))
    pygame.draw.rect(screen, (255,255,255), (0,675,750,5))
    pygame.draw.rect(screen, (255,255,255), (0,750,750,5))
    pygame.draw.rect(screen, (255,255,255), (0,825,750,5))

    #   grillage verticale
    pygame.draw.rect(screen, (255,255,255), (0,0,5,750))
    pygame.draw.rect(screen, (255,255,255), (75,0,5,750))
    pygame.draw.rect(screen, (255,255,255), (150,0,5,750))
    pygame.draw.rect(screen, (255,255,255), (225,0,5,750))
    pygame.draw.rect(screen, (255,255,255), (300,0,5,750))
    pygame.draw.rect(screen, (255,255,255), (375,0,5,750))
    pygame.draw.rect(screen, (255,255,255), (450,0,5,750))
    pygame.draw.rect(screen, (255,255,255), (525,0,5,750))
    pygame.draw.rect(screen, (255,255,255), (600,0,5,750))
    pygame.draw.rect(screen, (255,255,255), (675,0,5,750))
    pygame.draw.rect(screen, (255,255,255), (750,0,5,755))

    # x,y = pygame.mouse.get_pos()
    # print(x,y)

    touche_appuyee = pygame.key.get_pressed()

    J1.update(touche_appuyee)
    J2.update(touche_appuyee)
    clock.tick(60)

    screen.blit(J1.surf, J1.rect)
    screen.blit(J2.surf, J2.rect)
    pygame.display.flip()
