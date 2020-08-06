import pygame
from mob import *
from player import *
from screens import *
from settings import *
from os import path
import random

# initialize pygame and create window
pygame.init()
# sound
pygame.mixer.init()
pygame.display.set_caption("Lofi Adventures")

# turning the game loop into a class
class Game:
    def __init__(self):
        self.running = True
        self.start = True
        self.game_over = False
        self.last_update = 0
        self.pause = False
        self.load_data()
        self.bg = pokemon_bg
        self.bg_rect = pokemon_bg_rect
        self.stage1 = 0
        self.stage2 = 0
        self.stage3 = 0
        self.mobs_paused_speedy = 0
        self.pow_paused_speedy = 0

    def new(self):
        self.start = False
        self.stage1 = 0
        self.stage2 = 0
        self.stage3 = 0
        self.mobs_paused_speedy = 0
        self.pow_paused_speedy = 0
        self.mob_speed = 3
        self.pow_speed = 3
        self.score = 0
        self.player = Player(choice)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.mobs = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        for i in range(2):
            self.new_mob(self.mob_speed)
        for j in range(1):
            self.new_powerup(self.pow_speed)

    def load_data(self):
        if path.isfile(HS_FILE):
            f = open(path.join(game_folder, HS_FILE), 'r')
            value = f.readline()
            if value == '':
                self.highscore = 0
            else:
                self.highscore = int(float(value))
        else:
            f = open(path.join(game_folder, HS_FILE), 'w')
            self.highscore = 0

    def update(self):
        self.all_sprites.update()
        self.player.unfreeze(self.mobs, self.mob_speed + 3)

        # increase the number of mobs and powerups with time
        now = pygame.time.get_ticks()
        if now - self.last_update > 10000:
            self.mob_speed += 0.3
            self.pow_speed += 0.4
            self.new_mob(self.mob_speed)
            for mob in self.mobs:
                mob.speedy += 0.3
            for pow in self.powerups:
                pow.speedy += 0.4
            self.last_update = now

        # check to see if a mob hit the player
        mob_hits = pygame.sprite.spritecollide(self.player, self.mobs, True, pygame.sprite.collide_circle)
        for hit in mob_hits:
            self.new_mob(self.mob_speed)
            if not self.player.shield and not self.player.invincible:
                self.player.reset()
                self.player.hide()
                self.player.lives -= 1
                # hit_sound.play()
            if self.player.shield:
                if self.player.dir == 'left':
                    if self.player.choice == 1 and self.player.big:
                        self.player.image = big_sg_l_img
                    elif self.player.choice == 1 and not self.player.big:
                        self.player.image = sg_l_img
                    elif self.player.choice != 1 and self.player.big:
                        self.player.image = big_mr_l_img
                    else:
                        self.player.image = mr_l_img
                else:
                    if self.player.choice == 1 and self.player.big:
                        self.player.image = big_sg_r_img
                    elif self.player.choice == 1 and not self.player.big:
                        self.player.image = sg_r_img
                    elif self.player.choice != 1 and self.player.big:
                        self.player.image = big_mr_r_img
                    else:
                        self.player.image = mr_r_img
            self.player.shield = False
            expl = Explosion(hit.rect.center, "lg")
            explosion_sound.play()
            self.all_sprites.add(expl)


        # check to see if player hit a powerup
        powerup_hits = pygame.sprite.spritecollide(self.player, self.powerups, True, pygame.sprite.collide_circle)
        for hit in powerup_hits:
            if hit.type == 'extra life':
                self.player.lives += 1
                if self.player.lives >= 3:
                    self.player.lives = 3
                self.new_powerup(self.pow_speed)
            if hit.type == 'speed boost':
                self.player.speed_boost()
                if self.player.speed >= 11:
                    self.player.speed = 11
                self.new_powerup(self.pow_speed)
            if hit.type == 'shield' and not self.player.shield:
                self.player.reset_buff()
                self.player.shield = True
                if self.player.dir == 'left':
                    if self.player.choice == 1:
                        if self.player.big:
                            self.player.image = big_sg_l_shield_img
                        else:
                            self.player.image = sg_l_shield_img
                    else:
                        if self.player.big:
                            self.player.image = big_mr_l_shield_img
                        else:
                            self.player.image = mr_l_shield_img
                else:
                    if self.player.choice == 1:
                        if self.player.big:
                            self.player.image = big_sg_r_shield_img
                        else:
                            self.player.image = sg_r_shield_img
                    else:
                        if self.player.big:
                            self.player.image = big_mr_r_shield_img
                        else:
                            self.player.image = mr_r_shield_img

                self.new_powerup(self.pow_speed)
            if hit.type == 'time freeze':
                for mob in self.mobs:
                    mob.speedy = 1
                    mob.rot_speed = 8
                self.new_powerup(self.pow_speed)
            if hit.type == 'slow' and not self.player.invincible:
                self.player.speed_slow_down()
                if self.player.speed < 2:
                    self.player.speed = 2
                self.new_powerup(self.pow_speed)
            if hit.type == 'invincible':
                self.player.time_invincible()
                self.new_powerup(self.pow_speed)
            if hit.type == 'big':
                self.player.big_debuff()
                self.new_powerup(self.pow_speed)

            drink_sound.play()
        if self.player.lives == 0:
            # hit_sound.play()
            self.game_over = True

        if self.score == 0:
            stage_sound.play()
            self.stage1 = pygame.time.get_ticks()
            self.mobs_paused_speedy = self.mob_speed
            self.pow_paused_speedy = self.pow_speed

        if self.score > 0:
            if pygame.time.get_ticks() - self.stage1 < 2000:
                for mob in self.mobs:
                    mob.speedy = 0
                    mob.rect.x = 1000
                    mob.rect.y = 1000

                for pow in self.powerups:
                    pow.speedy = 0
                    pow.rect.x = 1000
                    pow.rect.y = 1000

                self.score = 1

            for mob in self.mobs:
                mob.speedy = self.mobs_paused_speedy
                mob.rect.x += int(mob.speedx)
                mob.rect.y += int(mob.speedy)

            for pow in self.powerups:
                pow.speedy = self.pow_paused_speedy
                pow.rect.y += int(pow.speedy)

        # changing backgrounds/mobs (minecraft)
        if int(self.score) == STAGE_1_to_2:
            stage_sound.play()
            self.stage2 = pygame.time.get_ticks()
            self.mobs_paused_speedy = self.mob_speed
            self.pow_paused_speedy = self.pow_speed

        if STAGE_2_to_3 > self.score > STAGE_1_to_2:
            self.bg = minecraft_bg
            self.bg_rect = minecraft_bg_rect
            for mob in self.mobs:
                mob.image_orig = pygame.transform.scale(creeper_img, (80, 80))
                mob.image_orig.set_colorkey(DARK_PURPLE)
                mob.radius = 22
            if pygame.time.get_ticks() - self.stage2 < 2000:
                draw_text(screen, 'STAGE 2: MINECRAFT', 48, WIDTH/2, 180)
                for mob in self.mobs:
                    mob.speedy = 0
                    mob.rect.x = 1000
                    mob.rect.y = 1000

                for pow in self.powerups:
                    pow.speedy = 0
                    pow.rect.x = 1000
                    pow.rect.y = 1000

                self.score = STAGE_1_to_2 + 1

            for mob in self.mobs:
                mob.speedy = self.mobs_paused_speedy
                mob.rect.x += int(mob.speedx)
                mob.rect.y += int(mob.speedy)

            for pow in self.powerups:
                pow.speedy = self.pow_paused_speedy
                pow.rect.y += int(pow.speedy)

        # changing backgrounds/mobs (mario)
        if int(self.score) == STAGE_2_to_3:
            stage_sound.play()
            self.stage3 = pygame.time.get_ticks()
            self.mobs_paused_speedy = self.mob_speed
            self.pow_paused_speedy = self.pow_speed

        if self.score > STAGE_2_to_3:
            self.bg = mario_bg
            self.bg_rect = mario_bg_rect
            for mob in self.mobs:
                mob.image_orig = pygame.transform.scale(goomba_img, (75, 75))
                mob.radius = 20
                mob.image_orig.set_colorkey(DARK_PURPLE)
            if pygame.time.get_ticks() - self.stage3 < 2000:
                draw_text(screen, 'STAGE 3: SUPER MARIO BROS', 48, WIDTH/2, 180)

                for mob in self.mobs:
                    mob.speedy = 0
                    mob.rect.x = 1000
                    mob.rect.y = 1000

                for pow in self.powerups:
                    pow.speedy = 0
                    pow.rect.x = 1000
                    pow.rect.y = 1000

                self.score = STAGE_2_to_3 + 1

            for mob in self.mobs:
                mob.speedy = self.mobs_paused_speedy
                mob.rect.x += int(mob.speedx)
                mob.rect.y += int(mob.speedy)

            for pow in self.powerups:
                pow.speedy = self.pow_paused_speedy
                pow.rect.y += int(pow.speedy)

    def new_mob(self, speed):
        m = Mob()
        self.all_sprites.add(m)
        self.mobs.add(m)
        m.speedy += speed

    def new_powerup(self, speed):
        p = Pow()
        self.all_sprites.add(p)
        self.powerups.add(p)
        p.speedy += speed

    def draw(self):
        screen.blit(self.bg, self.bg_rect)
        self.all_sprites.draw(screen)

        # score on the top
        draw_text(screen, str(int(self.score)), 18, WIDTH / 2, 10)

        # lives on the top
        if self.player.choice == 1:
            draw_lives(screen, WIDTH - 100, 6, self.player.lives, sg_lives_mini_img)
        else:
            draw_lives(screen, WIDTH - 100, 6, self.player.lives, mr_lives_mini_img)

        # pause button
        pause_button.set_colorkey(DARK_PURPLE)
        pause_button_rect.x = 0
        exit_button_rect.y = 0
        screen.blit(pause_button, pause_button_rect)

        if int(self.score) == 0:
            g.stage1 = pygame.time.get_ticks()

        if pygame.time.get_ticks() - g.stage1 < 2000:
            draw_text(screen, 'STAGE 1: POKEMON', 48, WIDTH/2, 180)


        click = pygame.mouse.get_pressed()
        if button_hovered1(pause_button_rect, pause_button):
            if click[0] == 1:
                click_sound.play()
                g.pause = show_pause_screen()[0]
                g.start = show_pause_screen()[1]


g = Game()
while g.running:
    if g.start:
        choice = show_start_screen(g)
        g.start = False
        g.new()

    if g.game_over:
        show_go_screen(g)
        g.game_over = False
        g.new()

    # keep loop running at the right speed
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g.running = False

    g.draw()

    if not g.pause:
        g.update()
        g.score += 0.2

    pygame.display.flip()

pygame.quit()

# ------------------------------------------------------------------------------
# OLD VERSION (NO CLASSES)

# # helper functions
# def new_mob(speed: int):
#     m = Mob()
#     all_sprites.add(m)
#     mobs.add(m)
#     m.speedy += speed
#
#
# def new_powerup():
#     p = Pow()
#     all_sprites.add(p)
#     powerups.add(p)


# game loop
# start = True
# game_over = False
# last_update = 0
# running = True
# pause = False
# while running:
#     if start:
#         show_start_screen()
#         start = False
#         speed = 3
#         all_sprites = pygame.sprite.Group()
#         mobs = pygame.sprite.Group()
#         powerups = pygame.sprite.Group()
#         player = Player()
#         all_sprites.add(player)
#         for i in range(5):
#             new_mob(speed)
#         for j in range(3):
#             new_powerup()
#         score = 0
#     if game_over:
#         show_go_screen(score)
#         game_over = False
#         speed = 3
#         all_sprites = pygame.sprite.Group()
#         mobs = pygame.sprite.Group()
#         powerups = pygame.sprite.Group()
#         player = Player()
#         all_sprites.add(player)
#         for i in range(5):
#             new_mob(speed)
#         for j in range(3):
#             new_powerup()
#         score = 0
#     # keep loop running at the right speed
#     clock.tick(FPS)
#     # process input(events)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # draw/render
#     # screen.fill(BACKGROUND_COLOUR)
#     screen.blit(background, background_rect)
#     all_sprites.draw(screen)
#     draw_text(screen, str(int(score)), 18, WIDTH / 2, 10)
#     draw_lives(screen, WIDTH - 100, 5, player.lives, lives_mini_img)
#
#     # pause button
#     pause_button = pygame.Rect(5, 5, 50, 50)
#     pygame.draw.rect(screen, RED, pause_button)
#     click = pygame.mouse.get_pressed()
#     if button_hovered(pause_button, (255, 153, 153)):
#         if click[0] == 1:
#             pause = show_pause_screen()[0]
#             start = show_pause_screen()[1]
#
#     # update
#     if not pause:
#         all_sprites.update()
#         player.unfreeze(mobs, speed + 3)
#
#         # increase the number of shurikens with time
#         now = pygame.time.get_ticks()
#         if now - last_update > 6000:
#             speed += 1
#             new_mob(speed)
#             for mob in mobs:
#                 mob.speedy += 1
#             last_update = now
#
#         # check to see if a mob hit the player
#         mob_hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
#         for hit in mob_hits:
#             new_mob(speed)
#             if not player.shield and not player.invincible:
#                 player.hide()
#                 player.lives -= 1
#                 player.reset()
#             player.shield = False
#
#         # check to see if player hit a powerup
#         powerup_hits = pygame.sprite.spritecollide(player, powerups, True, pygame.sprite.collide_circle)
#         for hit in powerup_hits:
#             if hit.type == 'extra life':
#                 player.lives += 1
#                 if player.lives >= 3:
#                     player.lives = 3
#                 new_powerup()
#             if hit.type == 'speed boost':
#                 player.speed_boost()
#                 if player.speed >= 11:
#                     player.speed = 11
#                 new_powerup()
#             if hit.type == 'shield' and not player.shield:
#                 player.shield = True
#                 new_powerup()
#             if hit.type == 'time freeze':
#                 for mob in mobs:
#                     mob.speedy = 1
#                     mob.rot_speed = 8
#                 new_powerup()
#             if hit.type == 'slow' and not player.invincible:
#                 player.speed_slow_down()
#                 if player.speed < 2:
#                     player.speed = 2
#                 new_powerup()
#             if hit.type == 'invincible':
#                 player.time_invincible()
#                 new_powerup()
#
#         if player.lives == 0: # and not death_explosion.alive():
#             game_over = True
#
#         score += 0.2
#
#     pygame.display.flip()


# pygame.quit()
# import pygame
# from mob import Mob
# from player import *
# from screens import *
# from setting import *
#
# # initialize pygame and create window
# pygame.init()
# # sound
# pygame.mixer.init()
# pygame.display.set_caption("Eludo")
#
#
# # helper functions
# def new_mob(speed: int):
#     m = Mob()
#     all_sprites.add(m)
#     mobs.add(m)
#     m.speedy += speed
#
#
# def new_powerup():
#     p = Pow()
#     all_sprites.add(p)
#     powerups.add(p)
#
#
# # debuffs
# # slow speed
# # become fat
# # poison/bleeding effect
#
# # game loop
# start = True
# game_over = False
# last_update = 0
# running = True
# pause = False
# while running:
#     if start:
#         show_start_screen()
#         start = False
#         speed = 3
#         all_sprites = pygame.sprite.Group()
#         mobs = pygame.sprite.Group()
#         powerups = pygame.sprite.Group()
#         player = Player()
#         all_sprites.add(player)
#         for i in range(5):
#             new_mob(speed)
#         for j in range(3):
#             new_powerup()
#         score = 0
#     if game_over:
#         show_go_screen(score)
#         game_over = False
#         speed = 3
#         all_sprites = pygame.sprite.Group()
#         mobs = pygame.sprite.Group()
#         powerups = pygame.sprite.Group()
#         player = Player()
#         all_sprites.add(player)
#         for i in range(5):
#             new_mob(speed)
#         for j in range(3):
#             new_powerup()
#         score = 0
#     # keep loop running at the right speed
#     clock.tick(FPS)
#     # process input(events)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#
#     # draw/render
#     # screen.fill(BACKGROUND_COLOUR)
#     screen.blit(background, background_rect)
#     all_sprites.draw(screen)
#     draw_text(screen, str(int(score)), 18, WIDTH / 2, 10)
#     draw_lives(screen, WIDTH - 100, 5, player.lives, lives_mini_img)
#
#     # pause button
#     pause_button = pygame.Rect(5, 5, 50, 50)
#     pygame.draw.rect(screen, RED, pause_button)
#     click = pygame.mouse.get_pressed()
#     if button_hovered(pause_button, (255, 153, 153)):
#         if click[0] == 1:
#             pause = show_pause_screen()[0]
#             start = show_pause_screen()[1]
#
#     # update
#     if not pause:
#         all_sprites.update()
#         player.unfreeze(mobs, speed + 3)
#
#         # increase the number of shurikens with time
#         now = pygame.time.get_ticks()
#         if now - last_update > 6000:
#             speed += 1
#             new_mob(speed)
#             for mob in mobs:
#                 mob.speedy += 1
#             last_update = now
#
#         # check to see if a mob hit the player
#         hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
#         for hit in hits:
#             new_mob(speed)
#             if not player.shield and not player.invincible:
#                 player.hide()
#                 player.lives -= 1
#                 player.reset()
#             player.shield = False
#
#         # check to see if player hit a powerup
#         hits = pygame.sprite.spritecollide(player, powerups, True, pygame.sprite.collide_circle)
#         for hit in hits:
#             if hit.type == 'extra life':
#                 player.lives += 1
#                 if player.lives >= 3:
#                     player.lives = 3
#                 new_powerup()
#             if hit.type == 'speed boost':
#                 player.speed_boost()
#                 if player.speed >= 11:
#                     player.speed = 11
#                 new_powerup()
#             if hit.type == 'shield' and not player.shield:
#                 player.shield = True
#                 new_powerup()
#             if hit.type == 'time freeze':
#                 for mob in mobs:
#                     mob.speedy = 1
#                     mob.rot_speed = 8
#                 new_powerup()
#             if hit.type == 'slow' and not player.invincible:
#                 player.speed_slow_down()
#                 if player.speed < 2:
#                     player.speed = 2
#                 new_powerup()
#             if hit.type == 'invincible':
#                 player.time_invincible()
#                 new_powerup()
#
#         if player.lives == 0: # and not death_explosion.alive():
#             game_over = True
#
#         score += 0.2
#
#     pygame.display.flip()
#
#
# pygame.quit()
