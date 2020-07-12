import pygame
import random
from os import path
from settings import *


class Player(pygame.sprite.Sprite):
    # sprite of the player
    def __init__(self, choice):
        pygame.sprite.Sprite.__init__(self)
        self.choice = choice
        if choice == 1:
            self.image = sg_l_img
        else:
            self.image = mr_l_img
        self.rect = self.image.get_rect()
        self.radius = 32
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 25
        self.speedx = 0
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.speed = 5
        self.power_time = pygame.time.get_ticks()
        self.freeze_time = pygame.time.get_ticks()
        self.slow_time = pygame.time.get_ticks()
        self.invincible_time = pygame.time.get_ticks()
        self.shield = False
        self.invincible = False
        self.big = False
        self.big_time = pygame.time.get_ticks()
        self.temp_centerx = 0
        self.temp_bottom = 0
        self.dir = 'left'

    def update(self):
        # timeout for speed boost
        if pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            if self.speed > 5:
                self.speed -= 3
                self.power_time = pygame.time.get_ticks()

        # timeout for slow debuff
        if pygame.time.get_ticks() - self.slow_time > POWERUP_TIME:
            if self.speed < 5:
                self.speed += 3
                self.slow_time = pygame.time.get_ticks()

        # timeout for invincible buff
        if pygame.time.get_ticks() - self.invincible_time > POWERUP_TIME:
            self.invincible = False
            self.invincible_time = pygame.time.get_ticks()

        # unhide if hidden
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.invincible = False
            if self.choice == 1:
                if self.big:
                    self.image = big_sg_l_img
                else:
                    self.image = sg_l_img
            else:
                if self.big:
                    self.image = big_mr_l_img
                else:
                    self.image = mr_l_img
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 25

        # timeout for big debuff
        if self.big and pygame.time.get_ticks() - self.big_time > POWERUP_TIME:
            self.temp_bottom = self.rect.bottom
            self.temp_centerx = self.rect.centerx
            self.big = False
            self.image = pygame.transform.scale(self.image, (73, 118))
            self.rect = self.image.get_rect()
            self.radius = 32
            self.rect.centerx = self.temp_centerx
            self.rect.bottom = self.temp_bottom
            self.big_time = pygame.time.get_ticks()

        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -(self.speed)
            self.dir = 'left'
            if self.choice == 1:
                if self.big:
                    if self.invincible:
                        self.image = big_sg_l_invincible_img
                    elif self.shield:
                        self.image = big_sg_l_shield_img
                    elif self.speed > 5:
                        self.image = big_sg_l_fast_img
                    elif self.speed < 5:
                        self.image = big_sg_l_slow_img
                    else:
                        self.image = big_sg_l_img
                else:
                    if self.invincible:
                        self.image = sg_l_invincible_img
                    elif self.shield:
                        self.image = sg_l_shield_img
                    elif self.speed > 5:
                        self.image = sg_l_fast_img
                    elif self.speed < 5:
                        self.image = sg_l_slow_img
                    else:
                        self.image = sg_l_img
            else:
                if self.big:
                    if self.invincible:
                        self.image = big_mr_l_invincible_img
                    elif self.shield:
                        self.image = big_mr_l_shield_img
                    elif self.speed > 5:
                        self.image = big_mr_l_fast_img
                    elif self.speed < 5:
                        self.image = big_mr_l_slow_img
                    else:
                        self.image = big_mr_l_img
                else:
                    if self.invincible:
                        self.image = mr_l_invincible_img
                    elif self.shield:
                        self.image = mr_l_shield_img
                    elif self.speed > 5:
                        self.image = mr_l_fast_img
                    elif self.speed < 5:
                        self.image = mr_l_slow_img
                    else:
                        self.image = mr_l_img

        if keystate[pygame.K_RIGHT]:
            self.speedx = self.speed
            self.dir = 'right'
            if self.choice == 1:
                if self.big:
                    if self.invincible:
                        self.image = big_sg_r_invincible_img
                    elif self.shield:
                        self.image = big_sg_r_shield_img
                    elif self.speed > 5:
                        self.image = big_sg_r_fast_img
                    elif self.speed < 5:
                        self.image = big_sg_r_slow_img
                    else:
                        self.image = big_sg_r_img
                else:
                    if self.invincible:
                        self.image = sg_r_invincible_img
                    elif self.shield:
                        self.image = sg_r_shield_img
                    elif self.speed > 5:
                        self.image = sg_r_fast_img
                    elif self.speed < 5:
                        self.image = sg_r_slow_img
                    else:
                        self.image = sg_r_img
            else:
                if self.big:
                    if self.invincible:
                        self.image = big_mr_r_invincible_img
                    elif self.shield:
                        self.image = big_mr_r_shield_img
                    elif self.speed > 5:
                        self.image = big_mr_r_fast_img
                    elif self.speed < 5:
                        self.image = big_mr_r_slow_img
                    else:
                        self.image = big_mr_r_img
                else:
                    if self.invincible:
                        self.image = mr_r_invincible_img
                    elif self.shield:
                        self.image = mr_r_shield_img
                    elif self.speed > 5:
                        self.image = mr_r_fast_img
                    elif self.speed < 5:
                        self.image = mr_r_slow_img
                    else:
                        self.image = mr_r_img

        self.rect.x += self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def reset(self):
        self.speedx = 0
        self.speed = 5
        if self.choice == 1:
            self.image = sg_l_img
        else:
            self.image = mr_l_img
        self.rect = self.image.get_rect()
        self.radius = 32
        self.freeze_time = pygame.time.get_ticks()
        self.slow_time = pygame.time.get_ticks()
        self.big_time = pygame.time.get_ticks()
        self.shield = False
        self.big = False

    def unfreeze(self, mobs, orig_speed):
        # timeout for freeze
        if pygame.time.get_ticks() - self.freeze_time > POWERUP_TIME:
            for mob in mobs:
                mob.speedy = orig_speed
                mob.rot_speed = random.randrange(80, 120)
            self.freeze_time = pygame.time.get_ticks()

    def hide(self):
        # hide the player temporarily
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)
        self.invincible = True

    def speed_boost(self):
        self.reset_buff()
        self.speed += 3
        self.power_time = pygame.time.get_ticks()
        if self.dir == 'left':
            if self.choice == 1:
                if self.big:
                    self.image = big_sg_l_fast_img
                else:
                    self.image = sg_l_fast_img
            else:
                if self.big:
                    self.image = big_mr_l_fast_img
                else:
                    self.image = mr_l_fast_img
        else:
            if self.choice == 1:
                if self.big:
                    self.image = big_sg_r_fast_img
                else:
                    self.image = sg_r_fast_img
            else:
                if self.big:
                    self.image = big_mr_r_fast_img
                else:
                    self.image = mr_r_fast_img

    def speed_slow_down(self):
        self.reset_buff()
        self.speed -= 3
        self.slow_time = pygame.time.get_ticks()
        if self.dir == 'left':
            if self.choice == 1:
                if self.big:
                    self.image = big_sg_l_slow_img
                else:
                    self.image = sg_l_slow_img
            else:
                if self.big:
                    self.image = big_mr_l_slow_img
                else:
                    self.image = mr_l_slow_img
        else:
            if self.choice == 1:
                if self.big:
                    self.image = big_sg_r_slow_img
                else:
                    self.image = sg_r_slow_img
            else:
                if self.big:
                    self.image = big_mr_r_slow_img
                else:
                    self.image = mr_r_slow_img

    def time_invincible(self):
        self.reset_buff()
        self.invincible = True
        self.invincible_time = pygame.time.get_ticks()
        if self.dir == 'left':
            if self.choice == 1:
                if self.big:
                    self.image = big_sg_l_invincible_img
                else:
                    self.image = sg_l_invincible_img
            else:
                if self.big:
                    self.image = big_mr_l_invincible_img
                else:
                    self.image = mr_l_invincible_img
        else:
            if self.choice == 1:
                if self.big:
                    self.image = big_sg_r_invincible_img
                else:
                    self.image = sg_r_invincible_img
            else:
                if self.big:
                    self.image = big_mr_r_invincible_img
                else:
                    self.image = mr_r_invincible_img

    def big_debuff(self):
        self.big = True
        self.temp_centerx = self.rect.centerx
        self.temp_bottom = self.rect.bottom
        self.image = pygame.transform.scale(self.image, (109, 177))
        self.rect = self.image.get_rect()
        self.radius = 50
        self.rect.centerx = self.temp_centerx
        self.rect.bottom = self.temp_bottom
        self.big_time = pygame.time.get_ticks()

    def reset_buff(self):
        self.invincible = False
        self.shield = False
        self.speed = 5


# power ups
# ideas:
# shields
# extra life
# boost speed
class Pow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'shield', 'shield', 'shield', 'shield',
                                   'extra life', 'extra life',
                                   'speed boost', 'speed boost', 'speed boost', 'speed boost', 'speed boost',
                                   'time freeze', 'time freeze',
                                   'slow', 'slow', 'slow',
                                   'invincible',
                                   'big', 'big'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 2)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        wait_distance = random.randint(1500, 4000)
        if self.rect.top > HEIGHT + wait_distance or self.rect.left < -75 or \
                self.rect.right > WIDTH + 75:
            self.type = random.choice(['shield', 'shield', 'shield', 'shield', 'shield',
                                       'extra life', 'extra life',
                                       'speed boost', 'speed boost', 'speed boost', 'speed boost', 'speed boost',
                                       'time freeze', 'time freeze',
                                       'slow', 'slow', 'slow',
                                       'invincible',
                                       'big', 'big'])
            self.image = powerup_images[self.type]
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.radius = int(self.rect.width / 2)
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-150, -100)
