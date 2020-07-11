import pygame
from settings import *


def show_go_screen(g):
    # screen.fill(BLACK)
    # play_again_button = pygame.Rect(int(WIDTH/2 - 85), int(2*HEIGHT/5 + 140), 180, 50)
    # exit_button = pygame.Rect(int(WIDTH/2 - 50), int(2*HEIGHT/3 + 70), 100, 50)
    # draw_text(screen, 'SCORE: ' + str(int(g.score)), 40, int(WIDTH/2), int(1*HEIGHT/4))
    # draw_text(screen, 'GAME OVER', 64, int(WIDTH/2), int(2*HEIGHT/5))
    # draw_text(screen, 'PLAY AGAIN', 28, int(WIDTH/2), int(2*HEIGHT/3))
    # draw_text(screen, 'EXIT', 28, int(WIDTH/2), int(2*HEIGHT/3 + 70))
    waiting = True

    # insert gameover screen image
    goscreen_rect.x = 0
    goscreen_rect.y = 0
    screen.blit(goscreen, goscreen_rect)
    draw_text(screen, str(int(g.score)), 32, 460, 318)

    if g.score > g.highscore:
        g.highscore = g.score
        congrats_rect.x = 215
        congrats_rect.y = 240
        screen.blit(congrats, congrats_rect)
        with open(path.join(game_folder, HS_FILE), 'w') as f:
            f.write(str(g.score))
    else:
        highscore_button_rect.x = 170
        highscore_button_rect.y = 260
        screen.blit(highscore_button, highscore_button_rect)
        draw_text(screen, str(int(g.highscore)), 32, 460, 270)

    while waiting:

        clock.tick(FPS)

        click = pygame.mouse.get_pressed()

        # insert buttons here
        playagain_rect.x = 265
        playagain_rect.y = 380
        screen.blit(playagain, playagain_rect)
        exitgame_rect.x = 265
        exitgame_rect.y = 460
        screen.blit(exitgame, exitgame_rect)

        # pygame.draw.rect(screen, GREEN, play_again_button)
        # draw_text(screen, 'PLAY AGAIN', 28, int(WIDTH/2), int(2*HEIGHT/3))
        # pygame.draw.rect(screen, RED, exit_button)
        # draw_text(screen, 'EXIT', 28, int(WIDTH/2), int(2*HEIGHT/3 + 70))
        if button_hovered2(playagain_rect, playagain_hov):

            if click[0] == 1:
                waiting = False

        elif button_hovered2(exitgame_rect, exitgame_hov):

            if click[0] == 1:
                pygame.quit()
                quit()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def show_start_screen(g):
    # screen.fill(BLACK)
    # draw_text(screen, 'WELCOME', 64, int(WIDTH/2), int(HEIGHT/7))
    # draw_text(screen, 'CHOOSE YOUR CHARACTER', 36, int(WIDTH/2), int(HEIGHT/5 + 40))
    # # start_button = pygame.Rect(int(WIDTH/2 - 92), int(HEIGHT - 150), 190, 50)
    # sarah_button = pygame.Rect(int(WIDTH/2 - 150), int(2*HEIGHT/3 - 125), 100, 100)
    # allen_button = pygame.Rect(int(WIDTH/2 + 50), int(2*HEIGHT/3 - 125), 100, 100)
    # draw_text(screen, 'High Score: ' + str(int(g.highscore)), 22, 80, 5)

    # insert start screen image
    startscreen_rect.x = 0
    startscreen_rect.y = 0
    screen.blit(startscreen, startscreen_rect)
    draw_text(screen, str(int(g.highscore)), 28, 210, 4)

    choice = 0
    sg_selected = False
    mr_selected = False
    waiting = True
    while waiting:

        clock.tick(FPS)

        # insert study girl button
        sg_button.set_colorkey(DARK_PURPLE)
        sg_button_rect.x = 210
        sg_button_rect.y = 368
        screen.blit(sg_button, sg_button_rect)

        # insert mellow racoon button
        mr_button.set_colorkey(DARK_PURPLE)
        mr_button_rect.x = 420
        mr_button_rect.y = 370
        screen.blit(mr_button, mr_button_rect)

        click_character = pygame.mouse.get_pressed()
        if button_hovered2(sg_button_rect, sg_hover):

            if click_character[0] == 1:
                sg_selected = True
                mr_selected = False
                choice = 1

        if button_hovered2(mr_button_rect, mr_hover):

            if click_character[0] == 1:
                mr_selected = True
                sg_selected = False
                choice = 2

        if sg_selected:
            sg_circle.set_colorkey(DARK_PURPLE)
            sg_circle_rect.x = 250
            sg_circle_rect.y = 290
            screen.blit(sg_circle, sg_circle_rect)
            mr_move_rect.x = 460
            mr_move_rect.y = 291
            screen.blit(mr_move, mr_move_rect)

        if mr_selected:
            mr_circle.set_colorkey(DARK_PURPLE)
            mr_circle_rect.x = 463
            mr_circle_rect.y = 290
            screen.blit(mr_circle, mr_circle_rect)
            sg_move_rect.x = 245
            sg_move_rect.y = 291
            screen.blit(sg_move, sg_move_rect)

        if sg_selected or mr_selected:
            click_start = pygame.mouse.get_pressed()
            # pygame.draw.rect(screen, GREEN, start_button)
            # draw_text(screen, 'START GAME', 28, int(WIDTH/2), int(HEIGHT - 150))

            # insert start button
            start_button.set_colorkey(DARK_PURPLE)
            start_button_rect.x = 325
            start_button_rect.y = 480
            screen.blit(start_button, start_button_rect)

            if button_hovered2(start_button_rect, start_hover):
                #draw_text(screen, 'START GAME', 28, int(WIDTH/2), int(HEIGHT - 150))

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
