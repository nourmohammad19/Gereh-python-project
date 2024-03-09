import pygame
import sys
import random
from functions import *

block = []
block_surface = []
block_rect = []
block_number = []
block_number_rect = []
score = 0
high_score = 0



def lost_check():
        flag = 0
        flag1 = True
        for i in range(len(block)):
            if block[i].state == 0:
                flag = 1
            if i not in {3,7,11,15}:
                if block[i].size == block[i+1].size:
                    flag1 = False
            if i not in {12,13,14,15}:
                if block[i].size == block[i+4].size:
                    flag1 = False
        if flag == 0 and flag1:
            return True
        else:
            return False
def set_color(block):
    for i in range(len(block)):
        match block[i].size:
                case 0:
                    block_surface[i].fill((244,235,226))
                case 2:
                    block_surface[i].fill("bisque1")
                case 4:
                    block_surface[i].fill("bisque2")
                case 8:
                    block_surface[i].fill("bisque3")
                case 16:
                    block_surface[i].fill("coral2")
                case 32:
                    block_surface[i].fill("coral3")
                case 64:
                    block_surface[i].fill("coral4")
                case 128:
                    block_surface[i].fill("brown2")
                case 256:
                    block_surface[i].fill("brown3")
                case 512:
                    block_surface[i].fill("brown4")
                case 1024:
                    block_surface[i].fill("lightsteelblue1")
                case 2048:
                    block_surface[i].fill("turquoise1")


#initializing the blocks
for i in range(16):
    b = Block(0,0,[0,0],"red")
    block.append(b)

block = set_pos(block)

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("2048")
clock = pygame.time.Clock()

#creating the surfaces and there rectangles
for i in range(len(block)):
    block_surface.append(pygame.Surface((90,90)))
for i in range(len(block)):
    block_rect.append(block_surface[i].get_rect(topleft = (block[i].pos[0], block[i].pos[1])))


#setting rect pos
def set_rect(block):
    for i in range(len(block_rect)):
        block_rect[i].topleft = (block[i].pos[0], block[i].pos[1])

#fonts
font1 = pygame.font.Font(None , 25)
font2 = pygame.font.Font(None , 100)
font3 = pygame.font.Font(None , 45)

#presenting the scores
score_surface = font1.render("score", True , "black")
score_rect = score_surface.get_rect(center = (510,22))
high_surface = font1.render("best", True , "black")
high_rect = high_surface.get_rect(center = (400,22))

#sounds
lost_sound = pygame.mixer.Sound("2048/lost_music.wav")
wining_sound = pygame.mixer.Sound("2048/winning_sound.wav")
sound_1024 = pygame.mixer.Sound("2048/1024_sound.wav")
sound_512 = pygame.mixer.Sound("2048/512_sound.wav")
sound_256 = pygame.mixer.Sound("2048/256_sound.wav")
sound_128 = pygame.mixer.Sound("2048/128_sound.wav")
sound_64 = pygame.mixer.Sound("2048/64_sound.wav")

#presenting the title
title_surface = font2.render("2048" , True , "bisque3")
title_rect = title_surface.get_rect(center = (100, 35))

#background
background_surface = pygame.Surface((600,600))
background_surface.fill("cornsilk2")

#bluring
blur_surface = pygame.Surface((600,600)).convert_alpha()
blur_surface.fill((100,100,100,200)) 


#templete 
templete_surface = pygame.image.load("2048/templete.jpg").convert_alpha()
templete_surface = pygame.transform.rotozoom(templete_surface,0,5/12)
templete_surface.fill((30, 30, 30 ,128), special_flags=pygame.BLEND_RGB_ADD) 
templete_rect = templete_surface.get_rect(center = (298,301))

#setting the numbers
for i in range(len(block)):
    block_number.append(font3.render(f"{block[i].size}", True, "black"))
    block_number_rect.append(block_number[i].get_rect(center = block_rect[i].center))

    color1 = "cornsilk3"

#random spawning
def random_init():
    for _ in range(2):
        i = random.randint(0,15)
        block[i].size = random.choice([2,4])
        block[i].state = 1
random_init()



first_2048 = True
first_1024 = True
first_512 = True
first_256 = True
first_128 = True
first_64 = True

game_active = False
start_page = True
end_page = False

while True:
    if game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit("You ended the game! ")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    block,score = up(block,score)
                if event.key == pygame.K_DOWN:
                    block,score = down(block,score)
                if event.key == pygame.K_RIGHT:
                    block,score = right(block,score)
                if event.key == pygame.K_LEFT:
                    block,score = left(block,score)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] <= 550 and pos[0] >= 470 and pos[1] >= 65 and pos[1] <= 100:
                    for i in range(len(block)):
                        block[i].size = 0
                        block[i].state = 0
                    score = 0
                    first_2048 = True
                    first_1024 = True
                    first_512 = True
                    first_256 = True
                    first_128 = True
                    first_64 = True
                    random_init()
                if pos[0] <= 460 and pos[0] >= 380 and pos[1] >= 65 and pos[1] <= 100:
                    game_active = False
                    start_page = True  

        #setting the high score
        if score > high_score:
            high_score = score
        #setting the suitable color
        set_color(block)
            

        #preserting the layers
        screen.blit(background_surface,(0,0))
        screen.blit(templete_surface,templete_rect)
        screen.blit(title_surface, title_rect)
        pygame.draw.rect(screen,(150,147,140), (470,10,80,50), border_radius=7)
        pygame.draw.rect(screen,(150,147,140), (339,10,120,50), border_radius=7)
        pygame.draw.rect(screen,"cornsilk3", (470,65,80,35))
        pygame.draw.rect(screen,"cornsilk3", (380,65,80,35))
        screen.blit(score_surface, score_rect)
        screen.blit(high_surface, high_rect)
        for i in range(len(block)):
            if block[i].state == 1:
                screen.blit(block_surface[i],block_rect[i])
                if block[i].size != 0:
                    txtToScreen(f'{block[i].size}', block_rect[i].center, 55, screen, centered=True)
                    #playing the proper sound when reachimg a spicific number
                    if block[i].size == 2048 and first_2048:
                        wining_sound.play()
                        first_2048 = False
                    if block[i].size == 1024 and first_1024:
                        sound_1024.play()
                        first_1024 = False
                    if block[i].size == 512 and first_512:
                        sound_512.play()
                        first_512 = False
                    if block[i].size == 256 and first_256:
                        sound_256.play()
                        first_256 = False
                    if block[i].size == 128 and first_128:
                        sound_128.play()
                        first_128 = False
                    if block[i].size == 64 and first_64:
                        sound_64.play()
                        first_64 = False
        txtToScreen(f'{score}',(510,44),35,screen,"black",centered=True)
        txtToScreen(f'{high_score}',(402,44),35,screen,"black",centered=True)
        txtToScreen("New game",(510,83),22,screen,"black",centered= True)
        txtToScreen("Exit",(420,83),23,screen,"black",centered= True)       

        
    #checking if the player has yet lost
        if lost_check():
            game_active = False
            end_page = True
            lost_sound.play()

    if end_page:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit("YOu ended the game! ")
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] >= 220 and pos[0] <= 370 and pos[1] >= 522 and pos[1] <= 572:
                    game_active = True
                    for i in range(len(block)):
                        block[i].size = 0
                        block[i].state = 0
                    score = 0
                    first_2048 = True
                    first_1024 = True
                    first_512 = True
                    first_256 = True
                    first_128 = True
                    first_64 = True
                    random_init()
                    end_page = False
        screen.blit(background_surface,(0,0))
        screen.blit(templete_surface,templete_rect)
        screen.blit(title_surface, title_rect)
        #pygame.draw.rect(screen,"cyan", (303,109,90,90), border_radius= 3)
        pygame.draw.rect(screen,(150,147,140), (470,30,80,50), border_radius=7)
        pygame.draw.rect(screen,(150,147,140), (339,30,120,50), border_radius=7)
        screen.blit(score_surface, score_rect)
        screen.blit(high_surface, high_rect)
        for i in range(len(block)):
            if block[i].state == 1:
                screen.blit(block_surface[i],block_rect[i])
                if block[i].size != 0:
                    txtToScreen(f'{block[i].size}', block_rect[i].center, 55, screen, centered=True)
        txtToScreen(f'{score}',(510,64),35,screen,"black",centered=True)
        txtToScreen(f'{high_score}',(402,64),35,screen,"black",centered=True)

        screen.blit(blur_surface,(0,0))


        txtToScreen(f"Your score: {score}",(300,300),70,screen,"ghostwhite",centered= True)
        txtToScreen("You lost!",(300,200),75,screen,"ghostwhite",centered= True)

        pygame.draw.rect(screen,"turquoise2",(225,522,150,50),border_radius = 7)
        txtToScreen("New game",(300,548),40,screen,"ghostwhite",centered = True)

    if start_page:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit("You ended the game! ")
            if event.type == pygame.KEYDOWN:
                for i in range(len(block)):
                    block[i].size = 0
                    block[i].state = 0
                    score = 0
                random_init()
                start_page = False
                game_active = True

        screen.blit(background_surface,(0,0))
        screen.blit(templete_surface,templete_rect)
        screen.blit(title_surface, title_rect)
        screen.blit(blur_surface,(0,0))
        txtToScreen("2048",(300,200),330,screen,"bisque3",centered= True)
        txtToScreen("Press any botton to start",(300,550),50,screen,"black",centered= True)

    pygame.display.update()
    clock.tick(60)        