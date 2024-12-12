import pygame
from chrarac import characs


pygame.init()

#creating window
SCREEN_width=1000
SCREEN_height=600
#window maker
screen= pygame.display.set_mode((SCREEN_width,SCREEN_height))
pygame.display.set_caption("Le_brawler")

#frameratew / slowdown
oras = pygame.time.Clock()
fps = 30

#colors
Yellow=(255,255,0)
white=(255,255,255)
red=(255,0,0)

#game time
intro_count=3
last_count_time=pygame.time.get_ticks()
#score
score=[0,0]
round_over=False
round_time_cooldown=2000

#sprite data
#player
naides_s=162
naides_scale=2
nai_offset=[50,80]
Player_data=[naides_s, naides_scale,nai_offset]

#bot
neco_s=149
neco_scale=2
neco_offset=[50,50]
bot_data=[neco_s, neco_scale,neco_offset]

#background
bi_imahe = pygame.image.load("img/bo.jpg").convert_alpha()

#sprite charac
#player
Player_sheet=pygame.image.load("img/charac/sp_all.png").convert_alpha()

#bot
bot_sheet=pygame.image.load("img/charac/neco_all.png").convert_alpha()


#text
victory_imh=pygame.image.load("font/victory.png").convert_alpha()



#sprite frame
Player_frame=[6,6,2,4,4,3,5]
bot_frame=[6,6,2,5,5,3,5]

#fonts
count_text=pygame.font.Font("font/turok.ttf", 80)
score_text=pygame.font.Font("font/turok.ttf", 30)
#draw text
def text_draw(text,font,text_col,x,y):
    img=font.render(text,True,text_col)

    screen.blit(img,(x,y))
#draw background
def draw_bi():
    scale_bi = pygame.transform.scale(bi_imahe,(SCREEN_width,SCREEN_height))
    screen.blit(scale_bi, (0,0))

#health bar
#x&y=pixel
def buhay_bar(buhay,x,y):
    ratio=buhay/100
    #border
    pygame.draw.rect(screen,white,(x-2,y-2,405,35))
    #red health
    pygame.draw.rect(screen,red,(x,y,400,30))
    #health bar
    pygame.draw.rect(screen,Yellow,(x,y,400*ratio,30))


#character
player= characs(1,200,310, False,Player_data, Player_sheet ,Player_frame)
bot= characs(2,700,310, True,bot_data, bot_sheet ,bot_frame)


#window/loop/run
run=True
while run:
    #fps
    oras.tick(fps)

    #im background
    draw_bi()

    #menu
 



    #health bar
    buhay_bar(player.buhay,20,20)
    buhay_bar(bot.buhay,580,20)
    #score show
    text_draw("Player 1: "+str(score[0]),score_text,red,20,60)
    text_draw("Player 2: "+str(score[1]),score_text,red,580,60)

    #game time
    if intro_count<=0:
    #moves charac
        player.move(SCREEN_width, SCREEN_height, screen, bot, round_over)
        bot.move(SCREEN_width, SCREEN_height, screen, player, round_over)
    else:
        #draw text
        text_draw(str(intro_count),count_text,red,SCREEN_width/2,SCREEN_height/3)
        if(pygame.time.get_ticks()-last_count_time)>=1000:
            intro_count-=1
            last_count_time=pygame.time.get_ticks()
            #print(intro_count)

    #draw animation

    player.update()
    bot.update()

    #characs 
    player.draw(screen)
    bot.draw(screen)

    #check game is over
    if round_over==False:
        #check if the charrac is alive
        if player.alive==False:
            score[1]+=1
            round_over=True
            round_over_time=pygame.time.get_ticks()
            print(score)
        elif bot.alive==False:
            score[0]+=1
            round_over=True
            round_over_time=pygame.time.get_ticks()
            print(score)
    else:
        #display text
        screen.blit(victory_imh,(200,150))
       
        #reset the game
        if pygame.time.get_ticks()-round_over_time>round_time_cooldown:
            round_over=False
            intro_count=3
            player= characs(1,200,310, False,Player_data, Player_sheet ,Player_frame)
            bot= characs(2,700,310, True,bot_data, bot_sheet ,bot_frame)


    #closin
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update 
    pygame.display.update()


print("window success!")
pygame.quit()

