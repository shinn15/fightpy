import pygame

SCREEN_width=1000
SCREEN_height=600

imahe_s=150
imahe_w=150


screen= pygame.display.set_mode((SCREEN_width,SCREEN_height))
pygame.display.set_caption("Le_brawler")

bi_imahe = pygame.image.load("img/bo.jpg").convert_alpha()
imahe=pygame.image.load("img/charac/naiwalk.png").convert_alpha()

frame=6

index=0
oras=pygame.time.get_ticks()


def draw_bi():
    scale_bi = pygame.transform.scale(bi_imahe,(SCREEN_width,SCREEN_height))
    screen.blit(scale_bi, (0,0))



rect = pygame.Rect(5, 5, 150, 198)

def update():
	

	#if self.index >= len(imahe):
    
            #self.index = 0




run=True

while run:
	draw_bi()
	update()



	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	pygame.display.update()



pygame.quit()
