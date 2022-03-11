import pygame

pygame.init()
pygame.font.init() 
WIDTH, HEIGHT = 500, 542
WIDTH2, HEIGHT2 = 81, 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Woordle")

BLACK = (18, 18, 19)
BALLS = (24, 24, 25)
BOXCLR = (58, 58, 60)
WHITE = (255, 255, 255)

myfont = pygame.font.SysFont('Times-Roman', 37, bold=True)
textsurface = myfont.render('Woordle', True, WHITE)
text_width = textsurface.get_rect().width

input = ''
row = 0
culm = 1
textCulm = 1

run = True
while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input = input[:-1]
                elif event.key == pygame.K_0: # I hate this
                    if len(input) == 5 and textCulm < 6:
                        textCulm += 1
                        answer = input
                        inputFont = pygame.font.SysFont('Arial', 54, bold=True)
                        answerDisplay = inputFont.render(answer.upper(), True, WHITE)
                        WIN.blit(answerDisplay,( 95, 66))
                        input = ''
                elif len(input) < 5 and event.key:
                    input += event.unicode

        WIN.fill(BLACK)

        inputFont = pygame.font.SysFont('Arial', 54, bold=True)
        inputDisplay = inputFont.render("   ".join(input.upper()), True, WHITE)
        WIN.blit(inputDisplay,( 95, 66 * textCulm))

        WIN.blit(textsurface,((WIDTH / 2) - (text_width / 2), 10))
        #pygame.draw.rect(WIN, BALLS, pygame.Rect(75, 60, 350, 420))

        for culm in range(1,7):
            for row in range(0,5):
                y = WIDTH2 + (row * 68)
                x = HEIGHT2 * culm * 1.1
                pygame.draw.rect(WIN, BOXCLR, pygame.Rect(y, x, 62, 62), 2)
                  
        pygame.display.flip()
        pygame.display.update()

pygame.quit
exit()

