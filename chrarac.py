import pygame

class characs():
	def __init__(self,fighter ,x, y, flip,data, sprite_i, sprite_frame):
		#animation
		self.fighter=fighter
		self.size = data[0]
		self.frame_scale = data[1]
		#position
		self.offset=data[2]
		#animation list

		self.flip=flip
		self.animation_list = self.sprite_load(sprite_i, sprite_frame)
		#sprite list
		self.action=0
		self.sprite_index=0
		
		self.imahe=self.animation_list[self.action][self.sprite_index]
		self.up_time=pygame.time.get_ticks()
		


		
		
		self.rect=pygame.Rect((x,y,80,180))
		self.runnin=False

		#fall/gravity
		self.vel_y=0
		#jump
		self.talon = False

		#figth
		self.attackin=False
		self.attk_type=0
		self.attk_time=0
		#hit animation
		self.dma=False
		self.buhay=100
		self.alive=True
		
	#prite animation
	def sprite_load(self,sprite_i,sprite_frame):
		#extract im
		animation_list = []
		for y, animation in enumerate(sprite_frame):
			temp_list=[]
			for x in range(animation):
				temp_im=sprite_i.subsurface(x*self.size,y*self.size,self.size,self.size)
				temp_list.append(pygame.transform.scale(temp_im,(self.size*self.frame_scale,self.size*self.frame_scale)))
			animation_list.append(temp_list)
		#print(animation_list)
		return animation_list
		
	def move(self,screen_width,screen_height,surface,hit,round_over):
		speed =10
		fall =2
		dx = 0
		dy = 0
		#ground position
		pos = 20
		#reset move
		self.runnin=False
		self.attk_type=0

		key=pygame.key.get_pressed()

		#attack only once
		if self.attackin == False and self.alive==True and round_over==False:


			#keys
		#charac move
		#character 1
			if self.fighter==1:

				if key[pygame.K_a]:
					dx = -speed
					self.runnin=True
				if key[pygame.K_d]:
					dx = speed
					self.runnin=True

				#jump
				if key[pygame.K_w] and self.talon == False:
					self.vel_y =-30
					self.talon=True

				#attack
				if key[pygame.K_s] or key[pygame.K_r]:
					self.attack(hit)

					#attack type
					if key[pygame.K_s]:
						self.attk_type=1

					if key[pygame.K_r]:
						self.attk_type=2
			#character 2/bot 
			if self.fighter==2:

				if key[pygame.K_LEFT]:
					dx = -speed
					self.runnin=True
				if key[pygame.K_RIGHT]:
					dx = speed
					self.runnin=True

				#jump
				if key[pygame.K_UP] and self.talon == False:
					self.vel_y =-30
					self.talon=True

				#attack
				if key[pygame.K_DOWN] or key[pygame.K_PERIOD]:
					self.attack(hit)

					#attack type
					if key[pygame.K_DOWN]:
						self.attk_type=1

					if key[pygame.K_PERIOD]:
						self.attk_type=2




		#fall gravity
		self.vel_y+= fall
		dy+=self.vel_y

		#border/stay on screen

		if self.rect.left+dx<0:
			dx = - self.rect.left
		if self.rect.right +dx>screen_width:
			dx = screen_width-self.rect.right

		#jump
		if self.rect.bottom+dy>screen_height -pos:
			self.vel_y = 0
			self.talon = False
			dy=screen_height-pos-self.rect.bottom

		#face each other
		if hit.rect.centerx > self.rect.centerx:
			self.flip=False
		else:
			self.flip=True

		#attack cooldown
		if self.attk_time>0:
			self.attk_time-=1

		#position
		self.rect.x += dx
		self.rect.y += dy

	#animation move
	#()=list location of sprite
	def update(self):
		#action
		#kill animation
		if self.buhay<=0:
			self.buhay=0
			self.alive=False
			self.update_action(6)
		#hit
		elif self.dma==True:
			self.update_action(5)
		#attackin
		elif self.attackin==True:
			if self.attk_type==1:
				self.update_action(3)
			elif self.attk_type==2:
				self.update_action(3)

		#jump
		elif self.talon==True:
			self.update_action(2)
		#run
		elif self.runnin==True:
			self.update_action(1)
		else:
			self.update_action(0)
		#frame pixel/speed
		anim_frame=2000
		#update sprite/animate
		self.imahe = self.animation_list[self.action][self.sprite_index]
		#animate

		if pygame.time.get_ticks() > self.up_time-anim_frame :
			self.sprite_index+=1
			self.anim_frame=pygame.time.get_ticks()
		#loop
		if self.sprite_index>=len(self.animation_list[self.action]):
			#if charac die
			if self.alive==False:
				self.sprite_index=len(self.animation_list[self.action])-1
			#loop animation
			else:
				self.sprite_index=0

				#attack animation
				if self.action==3 or self.action==4:
					self.attackin=False
					self.attk_time=20
				#dma taken animation
				if self.action == 5:
					self.dma=False

	#attackin move
	def attack(self,hit):
		if self.attk_time==0:
			self.attackin=True
			attack_m = pygame.Rect(self.rect.centerx - (2*self.rect.width*self.flip),
				self.rect.y,2*self.rect.width,self.rect.height)
			#collidin/hit
			if attack_m.colliderect(hit.rect):
				#print('hit')
				#damage
				hit.buhay -=10
				hit.dma = True

			#pygame.draw.rect(surface, (0,255,0),attack_m)

	#new sprite checker
	def update_action(self,new_action):
		if new_action != self.action:
			self.action = new_action

			#update the animation 
			self.sprite_index=0
			self.up_time=pygame.time.get_ticks()



	#draw
	def draw(self,surface):
		imh=pygame.transform.flip(self.imahe, self.flip, False)

		#pygame.draw.rect(surface,(255,0,0),self.rect)

		surface.blit(self.imahe,(self.rect.x -(self.offset[0]*self.frame_scale)
			,self.rect.y-(self.offset[1]*self.frame_scale)))