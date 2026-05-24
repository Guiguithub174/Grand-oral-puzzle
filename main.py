import pygame

class GameClass:
    def __init__(game):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        game.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
        game.SCREEN_WIDTH, game.SCREEN_HEIGHT = game.screen.get_size()
        game.clock = pygame.time.Clock()
        game.running = True

    def update(game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game.running = False

    def draw(game):
        game.screen.fill((125,15,150))
        pygame.draw.rect(game.screen,"black",[25,25,game.SCREEN_WIDTH-50,game.SCREEN_HEIGHT-50])
        pygame.draw.rect(game.screen,"gray",[40,40,game.SCREEN_WIDTH-80,game.SCREEN_HEIGHT-80])
        

game = GameClass()

while game.running:
    game.update()
    game.draw()
    pygame.display.flip()
    game.clock.tick(60)


pygame.quit()