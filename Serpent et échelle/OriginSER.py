import random
import sys, pygame
pygame.init()


size = width, height = 1080, 720
black = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption("SerpentEchelleBeta")
clock = pygame.time.Clock()

#COULEURS
WHITE = (255,255,255)
green = (0, 255, 0)
dark_blue = (0, 0, 128)
blue = (0, 0, 255)
red = (255, 0, 0)

# TEXTE
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Lancer le dé', True, WHITE)
textRect = text.get_rect()
textRect.center = (850,650)

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
            # print(f"{position_x_case},{position_y_case}")
            count += 1
            line.append(case)
        plateau.append(line)
    # sys.exit()
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


                                            # DEFINITION DU DE

images = ["Dé 1.png", "Dé 2.png", "Dé 3.png", "Dé 4.png", "Dé 5.png", "Dé 6.png"]
# images = pygame.transform.scale(images, (40, 40))

dice = {
    "value": 1,
    "image": pygame.image.load(images[0]).convert_alpha(),
    "animated": False
}

                                            # DEFINITIONS DES JOUEURS

PlayerModel = 20

player_one = {
    "name": "One",
    "case": 1,
    "x": POSITION_PLATEAU[0],
    "y": POSITION_PLATEAU[1],
    "width": PlayerModel,
    "height": PlayerModel,
    "color": red,
    "score": 0,
}

player_two = {
    "name": "Two",
    "case": 1,
    "x": POSITION_PLATEAU[0]+10,
    "y": POSITION_PLATEAU[1],
    "width": PlayerModel,
    "height": PlayerModel,
    "color": blue,
    "score": 0,
}


def deplacement_joueur(joueur, dice_value):
    joueur["case"] += dice_value
    if joueur["case"] > 100:
        joueur["case"] = 100
    case = find_case_by_number(plateau, joueur["case"])
    joueur["x"] = case.centerx
    joueur["y"] = case.centery - 20 if joueur["name"] == "One" else case.centery + 5
    print(joueur["x"], joueur["y"])
    




def draw_player(player):
    return pygame.draw.rect(screen, player["color"], [player["x"], player["y"], player["width"], player["height"]])

do = True
Joueur1_time = True
Joueur2_time = False

                                                # PARTIE BOUCLE

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
            
    # JOUEUR 1 DEPLACEMENT MANUEL
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        if player_one["y"] < (height - PlayerModel):
            player_one["y"] += 1
    if keys[pygame.K_z]:
        if player_one["y"] > 115:
            player_one["y"] -= 1
    if keys[pygame.K_d]:
        if player_one["x"] < (600 - PlayerModel):
            player_one["x"] += 1
    if keys[pygame.K_q]:
        if player_one["x"] > 0:
            player_one["x"] -= 1


    # JOUEUR 2 DEPLACEMENT MANUEL
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        if player_two["y"] < (height - PlayerModel):
            player_two["y"] += 1
    if keys[pygame.K_UP]:
        if player_two["y"] > 115:
            player_two["y"] -= 1
    if keys[pygame.K_RIGHT]:
        if player_two["x"] < (600 - PlayerModel):
            player_two["x"] += 1
    if keys[pygame.K_LEFT]:
        if player_two["x"] > 0:
            player_two["x"] -= 1

    # DISPLAY
    screen.fill(black)
    plateau = create_plateau()

    # DECORATION TEXTE
    Case_Dé = pygame.draw.rect(screen, dark_blue, [750, 625, 200, 50 ])
    screen.blit(text, textRect)

    # LANCEMENT DE DE
    if keys[pygame.K_SPACE] or keys[pygame.MOUSEBUTTONDOWN] and not dice["animated"]:
        pos = pygame.mouse.get_pos()
        dice["animated"] = True
        animation_timer = pygame.time.get_ticks() // 1000
        
    if dice["animated"]:
        random_value = random.randint(0,5)
        dice["image"] = pygame.image.load(images[random_value]).convert_alpha()
        dice["value"] = random_value + 1
        current_time = pygame.time.get_ticks() // 1000
        if animation_timer != 0 and (current_time - animation_timer) > 3:
            animation_timer = 0
            dice["animated"] = False
            if Joueur1_time:
                deplacement_joueur(player_one, dice["value"])
                Joueur1_time = False
                Joueur2_time = True
            elif Joueur2_time:
                deplacement_joueur(player_two, dice["value"])
                Joueur2_time = False
                Joueur1_time = True
    x = 710
    y = 300
    screen.blit(dice["image"], (x, y))
    

    # MISE EN PLACE DES JOUEURS
    player_one_rect = draw_player(player_one)
    player_two_rect = draw_player(player_two)
    if do == True:
        case = find_case_by_number(plateau, 1)
        print(player_one["x"], player_one["y"])
        print(do)
        do = False
        player_one["x"] = case.centerx
        player_one["y"] = case.centery - 20
        player_two["x"] = case.centerx
        player_two["y"] = case.centery +5

    pygame.display.flip()
    clock.tick(60)