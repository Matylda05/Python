import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1200, 800))
Speed = 1
score = 0
game_start = False
game_over = False
image = pygame.image.load("GO.png")
background = pygame.image.load("tło.jpg") 
image2 = pygame.image.load("play.png")

snow = []
def add_ball():
    x = random.randint(0, 1200)
    y = -40
    snow.append({"x": x, "y": y, "klik":False})

def update():
    for ball in snow:
        ball["y"] += Speed
        pygame.draw.circle(screen, (0,0,0), (ball["x"], ball["y"]), 42)
        pygame.draw.circle(screen, (255,255,255), (ball["x"], ball["y"]), 40)

    snow[:] = [b for b in snow if b["klik"] == False]



clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60) #60 klatek na s
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: 
                mx, my = event.pos
                if not game_start:
                    if 360 <= mx <= 841 and 250 <= my <= 477:
                        game_start = True
                for b in snow:
                    if b["x"] - 40 <= mx <= b["x"] + 40 and b["y"] - 40 <= my <= b["y"] + 40:
                        b["klik"] = True
                        score += 1

    for b in snow:
        if b["y"] > 800 - 40:
            game_over = True
    if score>10:
        Speed = 2
    if score>30:
        Speed = 4
    if score>100:
        Speed=7
    if score>300:
        Speed=10

    screen.blit(background, (0, 0))
    if game_start == False:
        screen.blit(image2, (360, 250))
    else:
        if game_over == False:
            if random.random() < 0.04: 
                add_ball()
            update()
        else:
            screen.blit(image, (320, 120))
            font = pygame.font.SysFont(None, 50)
            text = font.render(f"Score: {score}", True, (255, 255, 255))
            screen.blit(text, (550, 500))

    pygame.display.flip()
print("Score: ", score)
pygame.quit()