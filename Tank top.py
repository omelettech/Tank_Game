import pygame
import random
import sys

def drawscreen():
	screen.fill(bg)
	#health
	if health>0:
		pygame.draw.rect(screen,(0,0,0),(4,29,health+1,21), 4)
		pygame.draw.rect(screen,(255,0,0),(5,30,health,20))
	pygame.draw.line(screen,(255,0,0),(pos[0],pos[1]),(pos[2],pos[3]),2)
	#tank	
	pygame.draw.rect(screen,(255,0,0),(p_pos[0],p_pos[1],60,50))

	#bullet
	pygame.draw.rect(screen,(0,255,0),(b_pos[0],b_pos[1],10,20))
	pygame.draw.rect(screen,(255,0,0),(p_pos[0]+25,p_pos[1]-20,10,20))
	#enemy
	pygame.draw.rect(screen,(0,0,255),(enemy_list[0],enemy_list[1],enemy_size,enemy_size))
	pygame.draw.rect(screen,(0,0,255),(enemy_list[2],enemy_list[3],enemy_size,enemy_size))
	pygame.draw.rect(screen,(0,0,255),(enemy_list[4],enemy_list[5],enemy_size,enemy_size))
	#text
	textsurf=myfont.render(str(score),False,(0,0,0))
	healthsurf=myfont.render('Health',False,(255,255,255))
	screen.blit(textsurf,(0,0))
	screen.blit(healthsurf,(7,25))






pygame.init()
pygame.display.set_caption('Tank Top')
fontsize=24
myfont = pygame.font.SysFont('arial', fontsize)
health=60
i=0
w=600
h=600
pos=[0,500,w,500]
p_pos=[w/2,525]
b_pos = [p_pos[0]+25,p_pos[1]-20]
enemy_size=25
enemy_count=3
enemy_posx=random.randint(10,w-enemy_size-10)
enemy_posy=0
enemy_list=[]
bg=(255,255,255)
speed=10
enemy_speed=1
score = 0
clock = pygame.time.Clock()

while i !=3:
	enemy_posx=random.randint(10,w-enemy_size-10)
	enemy_posy=0
	enemy_list.append(enemy_posx)
	enemy_list.append(enemy_posy)
	i+=1




screen = pygame.display.set_mode((w,h))

game_over=False
#mainloop
while not game_over:
	clock.tick(120)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	


	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and p_pos[0]>0:
		p_pos[0]-=speed/2.5
	elif keys[pygame.K_RIGHT] and p_pos[0]+60<w:
		p_pos[0]+=speed/2.5

	b_pos[1]-=speed


	if b_pos[1]<0:
		b_pos = [p_pos[0]+25,p_pos[1]-20]

	if enemy_list[1]>=0:
		enemy_list[1]+=enemy_speed
		if enemy_list[1]>h:
			enemy_list[1]=0
			enemy_list[0]=random.randint(10,w-enemy_size-10)
			health-=20

	if enemy_list[3]>=0:
		enemy_list[3]+=enemy_speed
		if enemy_list[3]>h:
			enemy_list[3]=0
			enemy_list[2]=random.randint(10,w-enemy_size-10)
			health-=20

	if enemy_list[5]>=0:
		enemy_list[5]+=enemy_speed
		if enemy_list[5]>h:
			enemy_list[5]=0
			enemy_list[4]=random.randint(10,w-enemy_size-10)
			health-=20



	while i<6:
		if (enemy_list[i]>=b_pos[0] and enemy_list[i]<=b_pos[0]+10) or (b_pos[0]>=enemy_list[i] and b_pos[0]<=enemy_list[i]+enemy_size):
			if (enemy_list[i+1]>=b_pos[1] and enemy_list[i+1]<=b_pos[1]+20) or (b_pos[1]>=enemy_list[i+1] and b_pos[1]<=enemy_list[i+1]+enemy_size):
				enemy_list[i+1]=0
				enemy_list[i]=random.randint(10,w-enemy_size-10)
				score+=1
		i+=2

	i=0
	if health<=0:
		screen.fill((255,255,255))
		game_over=True
		break
	else:
		drawscreen()	
	
	pygame.display.update()

	
#side loop
while game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	myfont = pygame.font.SysFont('Comic Sans MS', 72)
	outsurf=myfont.render("Game Over",False,(0,0,0))
	scoresurf = myfont.render('Score: ',False,(0,0,0))
	scoresurf2= myfont.render(str(score),False,(0,0,0))
	screen.blit(outsurf,(100,250))
	screen.blit(scoresurf,(100,350))
	screen.blit(scoresurf2,(375,350))
	pygame.display.update()




	