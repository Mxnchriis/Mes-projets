# Démo Pong

import random
import sys, pygame
pygame.init()

size = width, height = 1080, 720
speed = [5, 5]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

PALETTE_HEIGHT = 100
PALETTE_WIDTH = 20

WHITE = (255,255,255)

font = pygame.font.SysFont(None, 48)



player_one = {
    "name": "One",
    "x": 0,
    "y":200,
    "width": PALETTE_WIDTH,
    "height": PALETTE_HEIGHT,
    "score": 0,
}


player_two = {
    "name": "Two",
    "x": width - 30,
    "y":200,
    "width": PALETTE_WIDTH,
    "height": PALETTE_HEIGHT,
    "score": 0,
}

ball = {
    "x": width// 2,
    "y": height // 2,
    "radius": 15,
    "direction_x": random.choice([1, -1]),
    "direction_y": random.choice([1, -1])
}

def draw_score():
    img_player_one = font.render(str(player_one["score"]), True, (255,255,255))
    img_player_two = font.render(str(player_two["score"]), True, (255,255,255))
    screen.blit(img_player_one, (50,50))
    screen.blit(img_player_two, (width - 60, 50))
def draw_ball():
    return pygame.draw.circle(screen, WHITE,( ball["x"], ball["y"]), ball["radius"])

def draw_player(player):
    return pygame.draw.rect(screen, WHITE, [player["x"], player["y"], player["width"], player["height"]])

def display_player_position(player):
    print(f"player(name={player['name']}, x={player['x']}, y={player['y']}, width={player['width']}, height={player['height']})", end=" ")

def display_ball_position():
    print(f"ball(x={ball['x']}, y={ball['y']})", end=" ")

def update_ball_position():
    # Changer la direction quand la balle arrive au sommet
    # Arriver sur les bordures : Position x devient 0 ou taille de mon écran soit 640
    # Arriver au sommet : Position y devient 0 ou taille de mon écran soit 480
    ball["x"] = ball["x"] + (ball["direction_x"] * speed[0])
    ball["y"] = ball["y"] + (ball["direction_y"] * speed[1])
    if ball["x"] <= (0 + 15) or ball["x"] >= (width - 15):
        if ball["x"] <= (0 + 15):
            player_two["score"] += 1
        if  ball["x"] >= (width - 15):
            player_one["score"] += 1
        ball["x"] = width// 2
        ball["y"] = height // 2
        ball["direction_x"] = random.choice([1, -1])
        ball["direction_y"] = random.choice([1, -1])
        

    if ball["y"] <= (0 + 15) or ball["y"] >= (height - 15):
        ball["direction_y"] *= -1

def do_overlap(ball: pygame.Rect, player: pygame.Rect):
    return ball.colliderect(player)    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    keys = pygame.key.get_pressed()
    # display_ball_position()
    draw_ball()
    print("")
    if keys[pygame.K_s]:
        if player_one["y"] < (height - PALETTE_HEIGHT):
            player_one["y"] += speed[1]
    if keys[pygame.K_z]:
        if player_one["y"] > 0:
            player_one["y"] -= speed[1]
    
    if keys[pygame.K_DOWN]:
        if player_two["y"] < (height - PALETTE_HEIGHT):
            player_two["y"] += speed[1]
    if keys[pygame.K_UP]:
        if player_two["y"] > 0:
            player_two["y"] -= speed[1]

    update_ball_position()
    screen.fill(black)
    player_one_rect = draw_player(player_one)
    player_two_rect = draw_player(player_two)
    ball_rect = draw_ball()
    draw_score()
    print(ball_rect)
    print(player_one_rect)
    if do_overlap(ball_rect, player_one_rect):
        ball["direction_x"] = 1
    if do_overlap(ball_rect, player_two_rect):
        ball["direction_x"] = -1


    pygame.display.flip()
    clock.tick(144)
    