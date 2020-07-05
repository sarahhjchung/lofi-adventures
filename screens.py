import pygame
from settings import *


def show_go_screen(g):
    screen.fill(BLACK)
    play_again_button = pygame.Rect(int(WIDTH/2 - 85), int(2*HEIGHT/5 + 140), 180, 50)
    exit_button = pygame.Rect(int(WIDTH/2 - 50), int(2*HEIGHT/3 + 70), 100, 50)
    draw_text(screen, 'SCORE: ' + str(int(g.score)), 40, int(WIDTH/2), int(1*HEIGHT/4))
    draw_text(screen, 'GAME OVER', 64, int(WIDTH/2), int(2*HEIGHT/5))
    draw_text(screen, 'PLAY AGAIN', 28, int(WIDTH/2), int(2*HEIGHT/3))
    draw_text(screen, 'EXIT', 28, int(WIDTH/2), int(2*HEIGHT/3 + 70))
    waiting = True

    if g.score > g.highscore:
        g.highscore = g.score
        draw_text(screen, 'NEW HIGH SCORE!', 40, int(WIDTH/2), 100)
        with open(path.join(game_folder, HS_FILE), 'w') as f:
            f.write(str(g.score))
    else:
        draw_text(screen, 'HIGH SCORE: ' + str(int(g.highscore)), 40, int(WIDTH/2), 100)

    while waiting:

        clock.tick(FPS)

        click = pygame.mouse.get_pressed()
        pygame.draw.rect(screen, GREEN, play_again_button)
        draw_text(screen, 'PLAY AGAIN', 28, int(WIDTH/2), int(2*HEIGHT/3))
        pygame.draw.rect(screen, RED, exit_button)
        draw_text(screen, 'EXIT', 28, int(WIDTH/2), int(2*HEIGHT/3 + 70))
        if button_hovered(play_again_button, (153, 255, 51)):
            draw_text(screen, 'PLAY AGAIN', 28, int(WIDTH/2), int(2*HEIGHT/3))

            if click[0] == 1:
                waiting = False

        elif button_hovered(exit_button, (255, 153, 153)):
            draw_text(screen, 'EXIT', 28, int(WIDTH/2), int(2*HEIGHT/3 + 70))

            if click[0] == 1:
                pygame.quit()
                quit()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def show_start_screen(g):
    screen.fill(BLACK)
    draw_text(screen, 'WELCOME', 64, int(WIDTH/2), int(HEIGHT/7))
    draw_text(screen, 'CHOOSE YOUR CHARACTER', 36, int(WIDTH/2), int(HEIGHT/5 + 40))
    start_button = pygame.Rect(int(WIDTH/2 - 92), int(HEIGHT - 150), 190, 50)
    sarah_button = pygame.Rect(int(WIDTH/2 - 150), int(2*HEIGHT/3 - 125), 100, 100)
    allen_button = pygame.Rect(int(WIDTH/2 + 50), int(2*HEIGHT/3 - 125), 100, 100)
    draw_text(screen, 'High Score: ' + str(int(g.highscore)), 22, 80, 5)

    choice = 0
    sarah_selected = False
    allen_selected = False
    waiting = True
    while waiting:

        clock.tick(FPS)

        click_character = pygame.mouse.get_pressed()
        pygame.draw.rect(screen, RED, sarah_button)
        draw_text(screen, 'SARAH', 28, int(WIDTH/2 - 100), int(2*HEIGHT/3 - 125))
        pygame.draw.rect(screen, ORANGE, allen_button)
        draw_text(screen, 'ALLEN', 28, int(WIDTH/2 + 100), int(2*HEIGHT/3 - 125))
        if button_hovered(sarah_button, (255, 153, 153)):
            draw_text(screen, 'SARAH', 28, int(WIDTH/2 - 100), int(2*HEIGHT/3 - 125))

            if click_character[0] == 1:
                sarah_selected = True
                allen_selected = False
                choice = 1

        elif button_hovered(allen_button, (255, 220, 0)):
            draw_text(screen, 'ALLEN', 28, int(WIDTH/2 + 100), int(2*HEIGHT/3 - 125))

            if click_character[0] == 1:
                allen_selected = True
                sarah_selected = False
                choice = 2

        if sarah_selected or allen_selected:
            click_start = pygame.mouse.get_pressed()
            pygame.draw.rect(screen, GREEN, start_button)
            draw_text(screen, 'START GAME', 28, int(WIDTH/2), int(HEIGHT - 150))
            if button_hovered(start_button, (153, 255, 51)):
                draw_text(screen, 'START GAME', 28, int(WIDTH/2), int(HEIGHT - 150))

                if click_start[0] == 1:
                    waiting = False
                    return choice

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def show_pause_screen():
    pause = True
    reset = False

    restart_button_click = pygame.Rect(340, 340, 92, 32)
    exit_button_click = pygame.Rect(342, 300, 92, 32)
    resume_button_click = pygame.Rect(340, 260, 92, 32)

    waiting = True
    while waiting:

        clock.tick(FPS)

        click = pygame.mouse.get_pressed()

        # insert pause screen image
        pausescreen.set_colorkey(DARK_PURPLE)
        pausescreen_rect.x = 0
        pausescreen_rect.y = 0
        screen.blit(pausescreen, pausescreen_rect)

        # insert resume button image
        resume_button.set_colorkey(WHITE)
        resume_button_rect.x = 254
        resume_button_rect.y = 260
        screen.blit(resume_button, resume_button_rect)

        # insert restart button image
        restart_button.set_colorkey(WHITE)
        restart_button_rect.x = 254
        restart_button_rect.y = 340
        screen.blit(restart_button, restart_button_rect)

        # insert exit button image
        exit_button.set_colorkey(WHITE)
        exit_button_rect.x = 256
        exit_button_rect.y = 300
        screen.blit(exit_button, exit_button_rect)

        # pygame.draw.rect(screen, GREEN, play_again_button)
        # pygame.draw.rect(screen, RED, exit_button)
        # pygame.draw.rect(screen, RED, resume_button_click)

        if button_hovered1(restart_button_click, restart_hover):

            if click[0] == 1:
                waiting = False
                reset = True
                pause = False

        elif button_hovered1(exit_button_click, exit_hover):

            if click[0] == 1:
                pygame.quit()
                quit()

        elif button_hovered1(resume_button_click, resume_hover):

            if click[0] == 1:
                pause = False
                waiting = False

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    return pause, reset
