import random
import sys, pygame
from pygame.locals import *
pygame.init()


size = width, height = 1080, 720


screen = pygame.display.set_mode(size)
pygame.display.set_caption("SerpentEchelleRemake")
clock = pygame.time.Clock()

#COULEURS
WHITE = (255,255,255)
green = (0, 255, 0)
dark_blue = (0, 0, 128)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
grey = (128,128,128)

# TEXTE
font = pygame.font.Font('freesansbold.ttf', 32)
fontmid = pygame.font.Font('freesansbold.ttf', 24)
fontsmall = pygame.font.Font('freesansbold.ttf', 16)
text = font.render('Lancer le dé', True, WHITE)
textRect = text.get_rect()
textRect.center = (850,650)

text2 = font.render('Lancement du dé...', True, WHITE)
text2Rect = text2.get_rect()
text2Rect.center = (850,650)

textJ1 = font.render("C'est au tour du J1 !", True, red)
textJ1Rect = textJ1.get_rect()
textJ1Rect.center = (850,250)

textJ2 = font.render("C'est au tour du J2 !", True, blue)
textJ2Rect = textJ2.get_rect()
textJ2Rect.center = (850,250)

dmdJoker1 = fontmid.render("Vous êtes sur la même case que le J2, Que voulez vous faire ?", True, WHITE)
dmdJoker1Rect = dmdJoker1.get_rect()
dmdJoker1Rect.center = (450,300)

dmdJoker2 = fontmid.render("Vous êtes sur la même case que le J1, Que voulez vous faire ?", True, WHITE)
dmdJoker2Rect = dmdJoker2.get_rect()
dmdJoker2Rect.center = (450,300)

reponse1 = fontsmall.render("Avancer de 5 cases", True, WHITE)
reponse1Rect = reponse1.get_rect()
reponse1Rect.center = (150,375)

reponse2 = fontsmall.render("Faire reculer de 5 cases", True, WHITE)
reponse2Rect = reponse2.get_rect()
reponse2Rect.center = (450,375)

reponse3 = fontsmall.render("Ne pas utiliser le Joker", True, WHITE)
reponse3Rect = reponse3.get_rect()
reponse3Rect.center = (750,375)

dmd2Joker = fontmid.render("Vous croiser la route d'un serpent, Que voulez vous faire ?", True, WHITE)
dmd2JokerRect = dmd2Joker.get_rect()
dmd2JokerRect.center = (450,300)

answer1 = fontsmall.render("Amadouer le serpent", True, WHITE)
answer1Rect = answer1.get_rect()
answer1Rect.center = (300,375)

answer2 = fontsmall.render("Ne pas utiliser le Joker", True, WHITE)
answer2Rect = answer2.get_rect()
answer2Rect.center = (600,375)

VictoireJ1 = font.render("Le J1 a gagner !", True, red)
VictoireJ1Rect = VictoireJ1.get_rect()
VictoireJ1Rect.center = (450,300)

VictoireJ2 = font.render("Le J2 a gagner !", True, blue)
VictoireJ2Rect = VictoireJ2.get_rect()
VictoireJ2Rect.center = (450,300)

                                            # DEFINITION DU TABLEAU
COL_HEIGHT = 600
COL_WIDTH = 5
COL_POSX = 0
COL_POSY = 115

LINE_HEIGHT = 5
LINE_WIDTH = 605
LINE_POSX = 0
LINE_POSY = 715

# FOND DU TABLEAUX
CASE_SIZE = 55
POSITION_PLATEAU = (5,120)

def get_plateau_number_order():
    plateau = [[0 for i in range(10)] for y in range(10)]
    x = 9
    y = 0
    count = 0
    for i in range(100):
        count += 1
        plateau[x][y] = count
        if x % 2 != 0:
            y += 1
        else:
            y -= 1
        if y > 9 and x % 2 != 0:
            x -= 1
            y = 9
        if y < 0 and x % 2 == 0:
            x -= 1
            y = 0
    return plateau

def create_plateau():
    count = 0
    plateau = []
    rows = 10
    lines = 10
    for i in range(rows):
        line = []
        for j in range(lines):
            position_x_case = POSITION_PLATEAU[0] + (j * CASE_SIZE) + (5 * j)
            position_y_case = POSITION_PLATEAU[1] + (i * CASE_SIZE) + (5 * i)
            case = pygame.draw.rect(screen, (0,255,0), pygame.Rect(position_x_case, position_y_case, CASE_SIZE, CASE_SIZE))
            count += 1
            line.append(case)
        plateau.append(line)
    number_plateau = get_plateau_number_order()
    plateau_state = []

    for i in range(len(plateau)):
        line_state = []
        for j in range(len(plateau[0])):
            count_text = font.render(f"{number_plateau[i][j]}", True, WHITE)
            count_rect = count_text.get_rect()
            count_rect.center = plateau[i][j].center
            screen.blit(count_text, count_rect)
            line_state.append({
                "case": plateau[i][j],
                "nombre": number_plateau[i][j]
            })
        plateau_state.append(line_state)
    # QUADRILLAGE DU TABLEUX
    pygame.draw.rect(screen, (180,180,180), [COL_POSX, COL_POSY, COL_WIDTH, COL_HEIGHT ])
    pygame.draw.rect(screen, (180,180,180), [LINE_POSX, LINE_POSY, LINE_WIDTH, LINE_HEIGHT])
    Increase = 60
    for i in range(10):
        pygame.draw.rect(screen, (180,180,180), [COL_POSX + Increase, COL_POSY, COL_WIDTH, COL_HEIGHT])
        pygame.draw.rect(screen, (180,180,180), [LINE_POSX, LINE_POSY - Increase, LINE_WIDTH, LINE_HEIGHT])
        Increase += 60
    return plateau_state

def find_case_by_number(plateau, nombre):
    for i in range(len(plateau)):
        for j in range(len(plateau[0])):
            if plateau[i][j]["nombre"] == nombre:
                return plateau[i][j]["case"]
    return None

snakeladder = {
    "calque": pygame.image.load("snake-ladder-calque.png").convert_alpha(),
    "affichage": True
}

                                            # DEFINITION DU DE

images = ["Dé 1.png", "Dé 2.png", "Dé 3.png", "Dé 4.png", "Dé 5.png", "Dé 6.png"]

dice = {
    "value": 1,
    "image": pygame.image.load(images[0]).convert_alpha(),
    "animated": False
}

                                            # DEFINITIONS DES JOUEURS

PlayerModel = 20

player_one = {
    "name": "1",
    "case": 1,
    "x": POSITION_PLATEAU[0],
    "y": POSITION_PLATEAU[1],
    "width": PlayerModel,
    "height": PlayerModel,
    "color": red,
    "joker": 3,
}

player_two = {
    "name": "2",
    "case": 1,
    "x": POSITION_PLATEAU[0]+10,
    "y": POSITION_PLATEAU[1],
    "width": PlayerModel,
    "height": PlayerModel,
    "color": blue,
    "joker": 3,
}

def draw_player(player):
    return pygame.draw.rect(screen, player["color"], [player["x"], player["y"], player["width"], player["height"]])

def deplacement_joueur(joueur, dice_value):
    retenue = 0
    joueur["case"] += dice_value
    if joueur["case"] > 100:
        retenue = joueur["case"] - 100
        joueur["case"] -= retenue*2
        case = find_case_by_number(plateau, joueur["case"])
        joueur["x"] = case.centerx - 10
        joueur["y"] = case.centery - 10
        print(f"J{joueur['name']} a rebondit sur la case 100 de {retenue} case(s) et se retrouve à la case {joueur['case']}.")
    else:
        case = find_case_by_number(plateau, joueur["case"])
        joueur["x"] = case.centerx - 10
        joueur["y"] = case.centery - 10
        print(f"J{joueur['name']} a fait {dice_value} et se retrouve à la case {joueur['case']}.")


                                            # DEFINITION DES REGLES DE BASES

def deplacement_echelle(joueur):
    if joueur["case"] == 8:
        joueur["case"] = 13
    elif joueur["case"] == 18:
        joueur["case"] = 65
    elif joueur["case"] == 27:
        joueur["case"] = 46
    elif joueur["case"] == 60:
        joueur["case"] = 61
    elif joueur["case"] == 68:
        joueur["case"] = 89
    case = find_case_by_number(plateau, joueur["case"])
    joueur["x"] = case.centerx - 10
    joueur["y"] = case.centery - 10
    print(f"J{joueur['name']} a pris une echelle et se retrouve à la case {joueur['case']}.\n")


def deplacement_serpent(joueur):
    if joueur["case"] == 48:
        joueur["case"] = 28
    elif joueur["case"] == 66:
        joueur["case"] = 24
    elif joueur["case"] == 74:
        joueur["case"] = 52
    elif joueur["case"] == 79:
        joueur["case"] = 59
    elif joueur["case"] == 83:
        joueur["case"] = 19
    elif joueur["case"] == 96:
        joueur["case"] = 76
    case = find_case_by_number(plateau, joueur["case"])
    joueur["x"] = case.centerx - 10
    joueur["y"] = case.centery - 10
    print(f"J{joueur['name']} a croisé la route d'un serpent et se retrouve à la case {joueur['case']}.\n")

def positioncheck(joueur):
    global can_pressed,condition_joker2,WinJ1,WinJ2
    Bas_Echelle = [8, 18, 27, 60, 68]
    Tete_Serpent = [48, 66, 74, 79, 83, 96]
    for i in Bas_Echelle:
        if joueur["case"] == i:
            deplacement_echelle(joueur)
    for j in Tete_Serpent:
        if joueur["case"] == j:
            condition_joker2 = True
    if joueur["case"] == 100:
        if joueur['name'] == '1':
            WinJ1 = True
        elif joueur['name'] == '2':
            WinJ2 = True
    print(f" condition_joker2 est {condition_joker2}")


def joker(joueur, adversaire):
    global condition_joker
    if joueur["joker"] > 0:
        Case_joker = pygame.draw.rect(screen, dark_blue, [77, 275, 750, 50 ])
        Case_joker1 = pygame.draw.rect(screen, grey, [50, 350, 200, 50 ])
        Case_joker2 = pygame.draw.rect(screen, grey, [350, 350, 200, 50 ])
        Case_joker3 = pygame.draw.rect(screen, grey, [650, 350, 200, 50 ])
        if joueur['name'] == '1':
            screen.blit(dmdJoker1, dmdJoker1Rect)
        else: 
            screen.blit(dmdJoker2, dmdJoker2Rect)
        screen.blit(reponse1, reponse1Rect)
        screen.blit(reponse2, reponse2Rect)
        screen.blit(reponse3, reponse3Rect)
        pygame.time.get_ticks() // 1000
        if event.type == MOUSEBUTTONDOWN and event.button == 1 and Case_joker1.collidepoint(pos):
            joueur["case"] += 5
            case = find_case_by_number(plateau, joueur["case"])
            joueur["x"] = case.centerx - 10
            joueur["y"] = case.centery - 10
            joueur["joker"] -=1
            print(f"J{joueur['name']} utilise son Joker et décide d'avancer de 5 cases.\nJoker restant (J{joueur['name']}) : {joueur['joker']}\nPosition J{joueur['name']} = Case {joueur['case']}\n")
            positioncheck(joueur)
            transition(joueur)

        elif event.type == MOUSEBUTTONDOWN and event.button == 1 and Case_joker2.collidepoint(pos):
            adversaire["case"] -= 5
            case = find_case_by_number(plateau, adversaire["case"])
            adversaire["x"] = case.centerx - 10
            adversaire["y"] = case.centery - 10
            joueur["joker"] -=1
            print(f"J{joueur['name']} utilise son Joker et décide de faire reculer J{adversaire['name']} de 5 cases.\nJoker restant (J{joueur['name']}) : {joueur['joker']}\nPosition J{adversaire['name']} = Case {adversaire['case']}\n")
            positioncheck(adversaire)
            transition(joueur)

        elif event.type == MOUSEBUTTONDOWN and event.button == 1 and Case_joker3.collidepoint(pos):
            print(f"J{joueur['name']} a décider de ne rien faire.\nJoker restant (J{joueur['name']}) : {joueur['joker']}\n")
            transition(joueur)
    elif joueur["joker"] == 0:
        print(f"J{joueur['name']} n'a plus de joker.\n")
        transition(joueur)

def joker2(joueur):
    if joueur["joker"] > 0:
        Case2_joker = pygame.draw.rect(screen, dark_blue, [77, 275, 750, 50 ])
        Case2_joker1 = pygame.draw.rect(screen, grey, [200, 350, 200, 50 ])
        Case2_joker2 = pygame.draw.rect(screen, grey, [500, 350, 200, 50 ])
        screen.blit(dmd2Joker, dmd2JokerRect)
        screen.blit(answer1, answer1Rect)
        screen.blit(answer2, answer2Rect)
        pygame.time.get_ticks() // 1000
        if event.type == MOUSEBUTTONDOWN and event.button == 1 and Case2_joker1.collidepoint(pos):
            joueur["case"] +=1
            case = find_case_by_number(plateau, joueur["case"])
            joueur["x"] = case.centerx - 10
            joueur["y"] = case.centery - 10
            joueur["joker"] -=1
            print(f"J{joueur['name']} a amadouer le serpent qui le laisse passer.\nJoker restant (J{joueur['name']}) : {joueur['joker']}\n")
            transition(joueur)
        elif event.type == MOUSEBUTTONDOWN and event.button == 1 and Case2_joker2.collidepoint(pos):
            deplacement_serpent(joueur)
            print(f"J{joueur['name']} a décider de ne rien faire et descend donc le long du serpent.\nJoker restant (J{joueur['name']}) : {joueur['joker']}\n")
            transition(joueur)
    elif joueur["joker"] == 0:
        deplacement_serpent(joueur)
        print(f"J{joueur['name']} n'a plus de joker et descend donc le long du serpent.\n")
        transition(joueur)
        

def transition(joueur):
    global condition_joker,condition_joker2,Joueur1_time,Joueur2_time,can_pressed
    condition_joker = False
    condition_joker2 = False
    if joueur['name'] == '1':
        Joueur1_time = False
        Joueur2_time = True
        can_pressed = True
    else:
        Joueur2_time = False
        Joueur1_time = True
        can_pressed = True
    

snakeladder = pygame.image.load("snake-ladder-calque.png")
largeur_snakeladder = 600
hauteur_snakeladder = 600
snakeladder = pygame.transform.scale(snakeladder, (largeur_snakeladder, hauteur_snakeladder))



# DEFINITION DES CONDITIONS/PARAMETRES
start = True
can_pressed = True
Joueur1_time = True
Joueur2_time = False
condition_joker = False
condition_joker2 = False
WinJ1 = False
WinJ2 = False

                                                # PARTIE BOUCLE

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    # DISPLAY
    screen.fill(black)
    plateau = create_plateau()
    x = 710
    y = 300
    screen.blit(dice["image"], (x, y))
    SLx = 0
    SLy = 120
    screen.blit(snakeladder, (SLx, SLy))

    # MISE EN PLACE DES JOUEURS
    player_one_rect = draw_player(player_one)
    player_two_rect = draw_player(player_two)
    
    # DECORATION TEXTE
    Case_De = pygame.draw.rect(screen, dark_blue, [750, 625, 200, 50 ])

                                                # LOGIQUE DE JEU

    if Joueur1_time:
        screen.blit(textJ1, textJ1Rect)
    elif Joueur2_time:
        screen.blit(textJ2, textJ2Rect)
    if can_pressed:
        Case_de = pygame.draw.rect(screen, dark_blue, [750, 625, 200, 50 ])
        screen.blit(text, textRect)
    elif not can_pressed:
        Case_De = pygame.draw.rect(screen, grey, [695, 625, 310, 50 ])
        screen.blit(text2 , text2Rect)
    # LANCEMENT DE DE
    keys = pygame.key.get_pressed()
    if can_pressed:
        if keys[pygame.K_SPACE] or (event.type == MOUSEBUTTONDOWN and event.button == 1 and Case_De.collidepoint(pos)) and not dice["animated"]:
            can_pressed = False
            dice["animated"] = True
            animation_timer = pygame.time.get_ticks() // 500
        
    if dice["animated"]:
        random_value = random.randint(0,5)
        dice["image"] = pygame.image.load(images[random_value]).convert_alpha()
        dice["value"] = random_value + 1
        current_time = pygame.time.get_ticks() // 500
        if animation_timer != 0 and (current_time - animation_timer) > 3:
            animation_timer = 0
            dice["animated"] = False
            if Joueur1_time:
                deplacement_joueur(player_one, dice["value"])
                current_time = pygame.time.get_ticks() // 1000
                positioncheck(player_one)
                if player_one["case"] == player_two["case"]:
                    if player_one["x"] == player_two["x"] and player_one["y"] == player_two["y"]:
                        player_two["y"] += 15
                    player_one["y"] -= 10
                    condition_joker = True
                
                if not condition_joker and Joueur1_time:
                    if not condition_joker2:
                        Joueur1_time = False
                        Joueur2_time = True
                        can_pressed = True
                else:
                    can_pressed = False
                print(f" Joueur1_time est {Joueur1_time}")

            elif Joueur2_time:
                deplacement_joueur(player_two, dice["value"])
                current_time = pygame.time.get_ticks() // 1000
                positioncheck(player_two)
                if player_one["case"] == player_two["case"]:
                    if player_two["x"] == player_one["x"] and player_two["y"] == player_one["y"]:
                        player_one["y"] -= 10
                    player_two["y"] += 15
                    condition_joker = True 

                if not condition_joker and Joueur2_time:
                    if not condition_joker2:
                        Joueur2_time = False
                        Joueur1_time = True
                        can_pressed = True
                else:
                    can_pressed = False

                print(f" Joueur2_time est {Joueur2_time}")

    if condition_joker:
        if Joueur1_time:
            joker(player_one, player_two)
        else:
            joker(player_two, player_one)

    if condition_joker2:
        if Joueur1_time:
            joker2(player_one)
        else:
            joker2(player_two)
    
    pos = pygame.mouse.get_pos()

    if start == True:
        case = find_case_by_number(plateau, 1)
        start = False
        player_one["x"] = case.centerx
        player_one["y"] = case.centery - 20
        player_two["x"] = case.centerx
        player_two["y"] = case.centery + 5

    if WinJ1:
        can_pressed = False
        Joueur1_time = False
        Joueur2_time = False
        Case_Victoire = pygame.draw.rect(screen, dark_blue, [300, 275, 300, 50 ])
        screen.blit(VictoireJ1, VictoireJ1Rect)

    if WinJ2:
        can_pressed = False
        Joueur1_time = False
        Joueur2_time = False
        Case_Victoire = pygame.draw.rect(screen, red, [300, 275, 300, 50 ])
        screen.blit(VictoireJ2, VictoireJ2Rect)

    pygame.display.flip()
    clock.tick(60) 