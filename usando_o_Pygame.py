import pygame
pygame.init()

x = 400
y = 300
mover = 30

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Joguinho")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= mover
    if comandos[pygame.K_UP]:
        y += mover
    if comandos[pygame.K_RIGHT]:
        x += mover
    if comandos[pygame.K_LEFT]:
        x -= mover

    janela.fill((0,0,0))
    pygame.draw.circle(janela, (0, 200, 100), (400, 300), 50)
    pygame.display.update()

pygame.quit()
