import pygame 

from define import *
from util import Util
from text import Text
from food import Food
from barrier import Barrier

#khoi tao 
pygame.init()

#ten cua so
pygame.display.set_caption("Game vượt chướng ngại vật")

#create khung hinh
window_game = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

clock = pygame.time.Clock()
                
            
#eat food
def eating_food():
    global score
    if food.rect.colliderect(Player_rect):
        score += eat_food
        food.set_position()
        pygame.mixer.Sound.play(soundEatFood)
        
#ham va cham 
def player_barrier():
    global totalplay 
    if barrier.rect.colliderect(Player_rect):
        totalplay -= 1
        pygame.mixer.Sound.play(soundGameOver)
        game_over()

#ham game over
def game_over():
    global checkpause
    if totalplay == 0:
        surfacePopup = pygame.Surface((POPUP_WIDTH, POPUP_HEIGHT))
        surfacePopup.fill(COLOR_WHITE)
        textObj.show_game_over_description(surfacePopup)
        textObj.show_game_over(surfacePopup)
        window_game.blit(surfacePopup, ((WINDOW_WIDTH- POPUP_WIDTH)/2 , (WINDOW_HEIGHT - POPUP_HEIGHT)/2))
        food.pause()
        barrier.pause()
        checkpause = True

#init player
imgplayer = pygame.image.load(img_player)
imgplayerjump = pygame.image.load(img_playerjump)
player_surface = imgplayer
Player_rect = imgplayer.get_rect(midbottom=(X_POSITION, Y_POSITION))
jumping = False
#ini run
run = True


#diem so 
score = 0
#init object
textObj = Text()
food = Food()
barrier = Barrier()
checkpause = False
isJump = False
#global variable
totalplay = TOTAL_PLAY

#load img backgroup
backgroup = pygame.image.load(img_bd)
#set trọng lực :
player_trongluc = 0

#sound game
soundBackground    =  pygame.mixer.Sound(music_nen)
soundEatFood       =  pygame.mixer.Sound(music_eat)
soundGameOver      =  pygame.mixer.Sound(music_over)
soundJump          =  pygame.mixer.Sound(music_jump)
pygame.mixer.Sound.play(soundBackground)
while run:
    #init backgroup
    window_game.blit(backgroup, (0,0))

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and checkpause == False:
                if Player_rect.bottom >= 500:
                    pygame.mixer.Sound.play(soundJump)
                    player_trongluc =-20
            #choi lai
            if event.key == pygame.K_SPACE and checkpause == True:
                totalplay = TOTAL_PLAY
                score = 0
                checkpause = False
                food.set_position()
                window_game.blit(player_surface, Player_rect)
    #jump
    player_trongluc +=1
    Player_rect.y += player_trongluc
    if Player_rect.bottom >= 500:
        Player_rect.bottom = 500

    window_game.blit(player_surface, Player_rect) 

    if Player_rect.bottom <= 450:
        player_surface = imgplayerjump
    else:
        player_surface = imgplayer

    #food 
    food.show(window_game)
    food.move()
        
    #barrier 
    barrier.show(window_game)
    barrier.move()
    #hien thi diem so
    textObj.show_score(window_game, score)
    #tinh diem
    eating_food()

    #va cham barrier
    player_barrier()
    #game over
    game_over()
    
     #update lai giao dien
    pygame.display.update()
    clock.tick(30)
pygame.quit()