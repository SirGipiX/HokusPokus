import pygame


pygame.init()
pygame.display.set_caption(".....")
size = (1920, 720)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

background = 69, 255, 69
sonic = pygame.image.load("sonic.png")
sonic = pygame.transform.scale(sonic, (99, 99))


position = (0, 0)
speed = 300

while True:
  screen.fill(background)
  screen.blit(sonic, position)
  pygame.display.update()
  clock.tick(30)

  (x, y) = position
  if x < 0 or x > 720:
    speed = -speed
  x = x + speed
  position = (x, y)

