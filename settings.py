import pygame
from os import path

WIDTH = 800
HEIGHT = 600
FPS = 60
POWERUP_TIME = 5000
HS_FILE = "highscore.txt"

# define color
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LILAC = (229, 204, 255)
MINT = (204, 255, 229)
WHITE = (255, 255, 255)
ORANGE = (255, 178, 102)
DARK_PURPLE = (91, 50, 65)
BACKGROUND_COLOUR = ORANGE

font_name = pygame.font.match_font("Arial")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# set up assets folders
game_folder = path.dirname(__file__)

# Load all game graphics

# Intro
intro_mr_1 = pygame.image.load(path.join(game_folder, 'intro_mr_1.png')).convert()
introscreen_rect = intro_mr_1.get_rect()
intro_mr_2 = pygame.image.load(path.join(game_folder, 'intro_mr_2.png')).convert()
intro_mr_3 = pygame.image.load(path.join(game_folder, 'intro_mr_3.png')).convert()
intro_mr_4 = pygame.image.load(path.join(game_folder, 'intro_mr_4.png')).convert()
intro_sg_1 = pygame.image.load(path.join(game_folder, 'intro_sg_1.png')).convert()
intro_sg_2 = pygame.image.load(path.join(game_folder, 'intro_sg_2.png')).convert()
intro_sg_3 = pygame.image.load(path.join(game_folder, 'intro_sg_3.png')).convert()
intro_sg_4 = pygame.image.load(path.join(game_folder, 'intro_sg_4.png')).convert()

# basic character with two sizes
player1_img = pygame.image.load(path.join(game_folder, 'sg_l.png')).convert()
sg_l_img = pygame.transform.scale(player1_img, (73, 118))
big_sg_l_img = pygame.transform.scale(player1_img, (109, 177))
big_sg_l_img.set_colorkey(DARK_PURPLE)
sg_l_img.set_colorkey(DARK_PURPLE)

player1r_img = pygame.image.load(path.join(game_folder, 'sg_r.png')).convert()
sg_r_img = pygame.transform.scale(player1r_img, (73, 118))
big_sg_r_img = pygame.transform.scale(player1r_img, (109, 177))
big_sg_r_img.set_colorkey(DARK_PURPLE)
sg_r_img.set_colorkey(DARK_PURPLE)

player2_img = pygame.image.load(path.join(game_folder, 'mr_l.png')).convert()
mr_l_img = pygame.transform.scale(player2_img, (73, 118))
big_mr_l_img = pygame.transform.scale(player2_img, (109, 177))
big_mr_l_img.set_colorkey(DARK_PURPLE)
mr_l_img.set_colorkey(DARK_PURPLE)

player2r_img = pygame.image.load(path.join(game_folder, 'mr_r.png')).convert()
mr_r_img = pygame.transform.scale(player2r_img, (73, 118))
big_mr_r_img = pygame.transform.scale(player2r_img, (109, 177))
big_mr_r_img.set_colorkey(DARK_PURPLE)
mr_r_img.set_colorkey(DARK_PURPLE)

sg_lives = pygame.image.load(path.join(game_folder, 'sg_lives.png')).convert()
sg_lives_mini_img = pygame.transform.scale(sg_lives, (26, 21))
sg_lives_mini_img.set_colorkey(DARK_PURPLE)

mr_lives = pygame.image.load(path.join(game_folder, 'mr_lives.png')).convert()
mr_lives_mini_img = pygame.transform.scale(mr_lives, (25, 19))
mr_lives_mini_img.set_colorkey(DARK_PURPLE)

# invincible
sg_l_invincible = pygame.image.load(path.join(game_folder, 'sg_l_invincible.png')).convert()
sg_l_invincible_img = pygame.transform.scale(sg_l_invincible, (75, 118))
big_sg_l_invincible_img = pygame.transform.scale(sg_l_invincible, (112, 177))
big_sg_l_invincible_img.set_colorkey(DARK_PURPLE)
sg_l_invincible_img.set_colorkey(DARK_PURPLE)

sg_r_invincible = pygame.image.load(path.join(game_folder, 'sg_r_invincible.png')).convert()
sg_r_invincible_img = pygame.transform.scale(sg_r_invincible, (75, 118))
big_sg_r_invincible_img = pygame.transform.scale(sg_r_invincible, (112, 177))
big_sg_r_invincible_img.set_colorkey(DARK_PURPLE)
sg_r_invincible_img.set_colorkey(DARK_PURPLE)

mr_l_invincible = pygame.image.load(path.join(game_folder, 'mr_l_invincible.png')).convert()
mr_l_invincible_img = pygame.transform.scale(mr_l_invincible, (73, 118))
big_mr_l_invincible_img = pygame.transform.scale(mr_l_invincible, (109, 177))
big_mr_l_invincible_img.set_colorkey(DARK_PURPLE)
mr_l_invincible_img.set_colorkey(DARK_PURPLE)

mr_r_invincible = pygame.image.load(path.join(game_folder, 'mr_r_invincible.png')).convert()
mr_r_invincible_img = pygame.transform.scale(mr_r_invincible, (73, 118))
big_mr_r_invincible_img = pygame.transform.scale(mr_r_invincible, (109, 177))
big_mr_r_invincible_img.set_colorkey(DARK_PURPLE)
mr_r_invincible_img.set_colorkey(DARK_PURPLE)

# shield
sg_l_shield = pygame.image.load(path.join(game_folder, 'sg_l_shield.png')).convert()
sg_l_shield_img = pygame.transform.scale(sg_l_shield, (73, 122))
big_sg_l_shield_img = pygame.transform.scale(sg_l_shield, (109, 183))
big_sg_l_shield_img.set_colorkey(DARK_PURPLE)
sg_l_shield_img.set_colorkey(DARK_PURPLE)

sg_r_shield = pygame.image.load(path.join(game_folder, 'sg_r_shield.png')).convert()
sg_r_shield_img = pygame.transform.scale(sg_r_shield, (73, 122))
big_sg_r_shield_img = pygame.transform.scale(sg_r_shield, (109, 183))
big_sg_r_shield_img.set_colorkey(DARK_PURPLE)
sg_r_shield_img.set_colorkey(DARK_PURPLE)

mr_l_shield = pygame.image.load(path.join(game_folder, 'mr_l_shield.png')).convert()
mr_l_shield_img = pygame.transform.scale(mr_l_shield, (73, 122))
big_mr_l_shield_img = pygame.transform.scale(mr_l_shield, (109, 183))
big_mr_l_shield_img.set_colorkey(DARK_PURPLE)
mr_l_shield_img.set_colorkey(DARK_PURPLE)

mr_r_shield = pygame.image.load(path.join(game_folder, 'mr_r_shield.png')).convert()
mr_r_shield_img = pygame.transform.scale(mr_r_shield, (73, 122))
big_mr_r_shield_img = pygame.transform.scale(mr_r_shield, (109, 183))
big_mr_r_shield_img.set_colorkey(DARK_PURPLE)
mr_r_shield_img.set_colorkey(DARK_PURPLE)

# slow
sg_l_slow = pygame.image.load(path.join(game_folder, 'sg_l_slow.png')).convert()
sg_l_slow_img = pygame.transform.scale(sg_l_slow, (73, 118))
big_sg_l_slow_img = pygame.transform.scale(sg_l_slow, (109, 177))
big_sg_l_slow_img.set_colorkey(DARK_PURPLE)
sg_l_slow_img.set_colorkey(DARK_PURPLE)

sg_r_slow = pygame.image.load(path.join(game_folder, 'sg_r_slow.png')).convert()
sg_r_slow_img = pygame.transform.scale(sg_r_slow, (73, 118))
big_sg_r_slow_img = pygame.transform.scale(sg_r_slow, (109, 177))
big_sg_r_slow_img.set_colorkey(DARK_PURPLE)
sg_r_slow_img.set_colorkey(DARK_PURPLE)

mr_l_slow = pygame.image.load(path.join(game_folder, 'mr_l_slow.png')).convert()
mr_l_slow_img = pygame.transform.scale(mr_l_slow, (73, 118))
big_mr_l_slow_img = pygame.transform.scale(mr_l_slow, (109, 177))
big_mr_l_slow_img.set_colorkey(DARK_PURPLE)
mr_l_slow_img.set_colorkey(DARK_PURPLE)

mr_r_slow = pygame.image.load(path.join(game_folder, 'mr_r_slow.png')).convert()
mr_r_slow_img = pygame.transform.scale(mr_r_slow, (73, 118))
big_mr_r_slow_img = pygame.transform.scale(mr_r_slow, (109, 177))
big_mr_r_slow_img.set_colorkey(DARK_PURPLE)
mr_r_slow_img.set_colorkey(DARK_PURPLE)

# speed+
sg_l_fast = pygame.image.load(path.join(game_folder, 'sg_l_fast.png')).convert()
sg_l_fast_img = pygame.transform.scale(sg_l_fast, (75, 118))
big_sg_l_fast_img = pygame.transform.scale(sg_l_fast, (112, 177))
big_sg_l_fast_img.set_colorkey(DARK_PURPLE)
sg_l_fast_img.set_colorkey(DARK_PURPLE)

sg_r_fast = pygame.image.load(path.join(game_folder, 'sg_r_fast.png')).convert()
sg_r_fast_img = pygame.transform.scale(sg_r_fast, (75, 118))
big_sg_r_fast_img = pygame.transform.scale(sg_r_fast, (112, 177))
big_sg_r_fast_img.set_colorkey(DARK_PURPLE)
sg_r_fast_img.set_colorkey(DARK_PURPLE)

mr_l_fast = pygame.image.load(path.join(game_folder, 'mr_l_fast.png')).convert()
mr_l_fast_img = pygame.transform.scale(mr_l_fast, (73, 118))
big_mr_l_fast_img = pygame.transform.scale(mr_l_fast, (109, 177))
big_mr_l_fast_img.set_colorkey(DARK_PURPLE)
mr_l_fast_img.set_colorkey(DARK_PURPLE)

mr_r_fast = pygame.image.load(path.join(game_folder, 'mr_r_fast.png')).convert()
mr_r_fast_img = pygame.transform.scale(mr_r_fast, (73, 118))
big_mr_r_fast_img = pygame.transform.scale(mr_r_fast, (109, 177))
big_mr_r_fast_img.set_colorkey(DARK_PURPLE)
mr_r_fast_img.set_colorkey(DARK_PURPLE)


# mobs and backgrounds
shuriken_img = pygame.image.load(path.join(game_folder, 'pokeball_mob.png')).convert()
background = pygame.image.load(path.join(game_folder, 'pokemon_background.png')).convert()
background_rect = background.get_rect()

# game over screen
goscreen = pygame.image.load(path.join(game_folder, 'gameover.png')).convert()
goscreen_rect = goscreen.get_rect()
highscore_button = pygame.image.load(path.join(game_folder, 'highscore.png')).convert()
highscore_button_rect = highscore_button.get_rect()
congrats = pygame.image.load(path.join(game_folder, 'congrats.png')).convert()
congrats_rect = congrats.get_rect()
playagain = pygame.image.load(path.join(game_folder, 'playagain.png')).convert()
playagain_rect = playagain.get_rect()
playagain_hov = pygame.image.load(path.join(game_folder, 'playagain_hover.png')).convert()
playagain_hov_rect = playagain_hov.get_rect()
exitgame = pygame.image.load(path.join(game_folder, 'exitgame.png')).convert()
exitgame_rect = exitgame.get_rect()
exitgame_hov = pygame.image.load(path.join(game_folder, 'exitgame_hover.png')).convert()
exitgame_hov_rect = exitgame_hov.get_rect()

# pause screen
pausescreen = pygame.image.load(path.join(game_folder, 'pausescreen.png')).convert()
startscreen = pygame.image.load(path.join(game_folder, 'startscreen.png')).convert()
startscreen_rect = startscreen.get_rect()
pause_button = pygame.image.load(path.join(game_folder, 'pause_button.png')).convert()
pause_button_rect = pause_button.get_rect()
pausescreen_rect = pausescreen.get_rect()

# start screen
mr_circle = pygame.image.load(path.join(game_folder, 'mr_circle.png')).convert()
mr_circle_rect = mr_circle.get_rect()
sg_circle = pygame.image.load(path.join(game_folder, 'sg_circle.png')).convert()
sg_circle_rect = sg_circle.get_rect()
mr_move = pygame.image.load(path.join(game_folder, 'mr_move.png')).convert()
mr_move_rect = mr_move.get_rect()
sg_move = pygame.image.load(path.join(game_folder, 'sg_move.png')).convert()
sg_move_rect = sg_move.get_rect()

mr_button = pygame.image.load(path.join(game_folder, 'mellowracoon.png')).convert()
mr_button_rect = mr_button.get_rect()
mr_hover = pygame.image.load(path.join(game_folder, 'mellowracoon_hover.png')).convert()
# mr_hover_rect = mr_hover.get_rect()

sg_button = pygame.image.load(path.join(game_folder, 'studygirl.png')).convert()
sg_button_rect = sg_button.get_rect()
sg_hover = pygame.image.load(path.join(game_folder, 'studygirl_hover.png')).convert()
# sg_hover_rect = sg_hover.get_rect()

start_button = pygame.image.load(path.join(game_folder, 'start_button.png')).convert()
start_button_rect = start_button.get_rect()
start_hover = pygame.image.load(path.join(game_folder, 'start_hover.png')).convert()
# start_hover_rect = start_hover.get_rect()

resume_button = pygame.image.load(path.join(game_folder, 'resume_button.png')).convert()
resume_button_rect = resume_button.get_rect()
resume_hover = pygame.image.load(path.join(game_folder, 'resume_hover.png')).convert()

restart_button = pygame.image.load(path.join(game_folder, 'restart_button.png')).convert()
restart_button_rect = resume_button.get_rect()
restart_hover = pygame.image.load(path.join(game_folder, 'restart_hover.png')).convert()

exit_button = pygame.image.load(path.join(game_folder, 'exit_button.png')).convert()
exit_button_rect = resume_button.get_rect()
exit_hover = pygame.image.load(path.join(game_folder, 'exit_hover.png')).convert()

# buff graphics
powerup_images = {}
powerup_images['shield'] = pygame.image.load(path.join(game_folder, 'shield_gold.png')).convert()
powerup_images['extra life'] = pygame.image.load(path.join(game_folder, 'pill_red.png')).convert()
powerup_images['speed boost'] = pygame.image.load(path.join(game_folder, 'bold_silver.png')).convert()
powerup_images['time freeze'] = pygame.image.load(path.join(game_folder, 'freeze.png')).convert()
powerup_images['slow'] = pygame.image.load(path.join(game_folder, 'slow.png')).convert()
powerup_images['invincible'] = pygame.image.load(path.join(game_folder, 'invincible.png')).convert()
powerup_images['big'] = pygame.image.load(path.join(game_folder, 'big.png')).convert()


# helper
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)


def button_hovered1(rectangle, hov_button):
    mouse_pos = pygame.mouse.get_pos()
    hovered = False
    if rectangle.x <= mouse_pos[0] <= rectangle.x + rectangle.width \
            and rectangle.y <= mouse_pos[1] <= rectangle.y + rectangle.height:
        # insert hovered button image
        # hov_button.set_colorkey(WHITE)
        hov_button_rect = hov_button.get_rect()
        hov_button_rect.x = rectangle.x - 86
        hov_button_rect.y = rectangle.y
        screen.blit(hov_button, hov_button_rect)
        hovered = True

    return hovered


def button_hovered2(rectangle, hov_button):
    mouse_pos = pygame.mouse.get_pos()
    hovered = False
    if rectangle.x <= mouse_pos[0] <= rectangle.x + rectangle.width \
            and rectangle.y <= mouse_pos[1] <= rectangle.y + rectangle.height:
        # insert hovered button image
        hov_button.set_colorkey(DARK_PURPLE)
        hov_button_rect = hov_button.get_rect()
        hov_button_rect.x = rectangle.x
        hov_button_rect.y = rectangle.y
        screen.blit(hov_button, hov_button_rect)
        hovered = True

    return hovered


def button_hovered(rectangle, hov_colour):
    mouse_pos = pygame.mouse.get_pos()
    hovered = False
    if rectangle.x <= mouse_pos[0] <= rectangle.x + rectangle.width \
            and rectangle.y <= mouse_pos[1] <= rectangle.y + rectangle.height:
        pygame.draw.rect(screen, hov_colour, rectangle)
        hovered = True

    return hovered
