import pygame
import random

def sign(x):
	if x > 0: return 1
	if x < 0: return -1
	else: return 0

points = []

a = random.random()*2-0.5
b = random.random()*2-0.5
c = random.random()*2-0.5

screen = pygame.display.set_mode((800, 600))

frame = 0
while 1:
	screen.fill((0, 0, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
			points.append([event.pos[0]/400-1, event.pos[1]/300-1, color])


	if frame %100 == 0:
		color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
		points.append([random.random()*2-0.5, random.random()*2-0.5, color])

	for point in points:
		if -1 < point[0] < 1 and -1 < point[1] < 1:
			pygame.draw.circle(screen, point[2], ((point[0]+1)*400, (point[1]+1)*300), 1)

	if points:
		x = points[-1][0]
		y = points[-1][1]
		points.append([y - sign(x)*abs(b*x+c)**0.5, a-x, color])

	pygame.display.update()
	frame += 1