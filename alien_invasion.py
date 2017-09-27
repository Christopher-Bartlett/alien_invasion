"""

Space_invaders.py

"""

import pygame
import random
import time
import math

class colors:
    black	=	(  0,	0,   0)
    white 	=	(255, 255, 255)
    blue	=	(  0,   0, 255)
    green	=	(  0, 255,   0)
    red         =	(255,   0,   0)
    yellow	=	(255, 255,   0)
    purple	=	(255,   0, 255)
    cyan	=	(  0, 255, 255)

class settings:
    # --- Global settings --- #
    screenwidth = 900
    screenheight = 700
    pi = math.pi

pygame.init()
SCREEN = pygame.display.set_mode([settings.screenwidth, settings.screenheight])
pygame.mouse.set_visible(False)

class images:
    # --- Open image files --- #
    # - Player image - #
    player_img = pygame.image.load("images/playerspaceship.png").convert()
    player_img.set_colorkey(colors.white)

    # - Alien image - #
    alien_img = pygame.image.load("images/alienspaceship.png").convert()
    alien_img.set_colorkey(colors.white)
    alien_img = pygame.transform.flip(alien_img, False, True)
    tough_alien_img = pygame.image.load("images/alienspaceshipstrong.png").convert()
    tough_alien_img.set_colorkey(colors.white)
    tough_alien_img = pygame.transform.flip(tough_alien_img, False, True)

    # Array of alien types with characteristics in order of [image, lives, speed]
    alien_chars = [[alien_img, 1, 2], [tough_alien_img, 2, 1]]

    # - Asteroid images - #
    ast_lrg_gry_img = pygame.image.load("images/asteroidlargegrey.png").convert()
    ast_lrg_gry_img.set_colorkey(colors.white)
    ast_med_gry_img = pygame.image.load("images/asteroidmediumgrey.png").convert()
    ast_med_gry_img.set_colorkey(colors.white)
    ast_sml_gry_img = pygame.image.load("images/asteroidsmallgrey.png").convert()
    ast_sml_gry_img.set_colorkey(colors.white)

    ast_lrg_brn_img = pygame.image.load("images/asteroidlargebrown.png").convert()
    ast_lrg_brn_img.set_colorkey(colors.white)
    ast_med_brn_img = pygame.image.load("images/asteroidmediumbrown.png").convert()
    ast_med_brn_img.set_colorkey(colors.white)
    ast_sml_brn_img = pygame.image.load("images/asteroidsmallbrown.png").convert()
    ast_sml_brn_img.set_colorkey(colors.white)

    ast_lrg_red_img = pygame.image.load("images/asteroidlargered.png").convert()
    ast_lrg_red_img.set_colorkey(colors.white)
    ast_med_red_img = pygame.image.load("images/asteroidmediumred.png").convert()
    ast_med_red_img.set_colorkey(colors.white)
    ast_sml_red_img = pygame.image.load("images/asteroidsmallred.png").convert()
    ast_sml_red_img.set_colorkey(colors.white)

    ast_gry_list = [ast_sml_gry_img,
                    ast_med_gry_img,
                    ast_lrg_gry_img]
    ast_brn_list = [ast_sml_brn_img,
                    ast_med_brn_img,
                    ast_lrg_brn_img]
    ast_red_list = [ast_sml_red_img,
                    ast_med_red_img,
                    ast_lrg_red_img]
    ast_color_list = [ast_gry_list,
                      ast_brn_list,
                      ast_red_list]

    # - Power up images - #
    heart_img = pygame.image.load("images/heartonelife.png").convert()
    heart_img.set_colorkey(colors.black)

    lose_life_img = pygame.image.load("images/goldskull.png").convert()
    lose_life_img.set_colorkey(colors.white)

    max_health_img = pygame.image.load("images/heartfulllives.png").convert()
    max_health_img.set_colorkey(colors.black)

    fast_bullets_img = pygame.image.load("images/fastbullets.png").convert()
    fast_bullets_img.set_colorkey(colors.black)

    laser_img = pygame.image.load("images/laser.png").convert()
    laser_img.set_colorkey(colors.black)

    force_field_img_1 = pygame.image.load("images/forcefieldsingle.png").convert()
    force_field_img_1.set_colorkey(colors.black)

    force_field_img_2 = pygame.image.load("images/forcefielddouble.png").convert()
    force_field_img_2.set_colorkey(colors.black)

    force_field_img_3 = pygame.image.load("images/forcefieldtriple.png").convert()
    force_field_img_3.set_colorkey(colors.black)

    world_shield_img = pygame.image.load("images/worldshield.png").convert()
    world_shield_img.set_colorkey(colors.black)

    freeze_img = pygame.image.load("images/freeze.png").convert()
    freeze_img.set_colorkey(colors.black)

    nuke_img = pygame.image.load("images/nuke.png").convert()
    nuke_img.set_colorkey(colors.black)

    dbl_str_bullet_img = pygame.image.load("images/doublestrength.png").convert()
    dbl_str_bullet_img.set_colorkey(colors.black)

    coin_img = pygame.image.load("images/coin.png").convert()
    coin_img.set_colorkey(colors.white)

    bullet_block_img = pygame.image.load("images/block.png").convert()
    bullet_block_img.set_colorkey(colors.white)

    rmv_item_img = pygame.image.load("images/removeitems.png").convert()
    rmv_item_img.set_colorkey(colors.black)

    reset_bonus_img = pygame.image.load("images/reseticon.png").convert()
    reset_bonus_img.set_colorkey(colors.black)

    pwrup_imgs = [heart_img, lose_life_img, max_health_img, fast_bullets_img, laser_img,
                  world_shield_img, freeze_img, nuke_img, dbl_str_bullet_img,
                  force_field_img_1, force_field_img_2, force_field_img_3, coin_img,
                  bullet_block_img, rmv_item_img, reset_bonus_img]

class Player(pygame.sprite.Sprite):
    """ This is the player """
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.max_lives = 10
        self.lives = self.max_lives # PLAYER LIVES CHANGE BACK TO 10

    def update(self):
        """ - Move player position - """
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

        # - Keep player inside screen - #
        if self.rect.right > settings.screenwidth:
            self.rect.right = settings.screenwidth
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > settings.screenheight - 40:
            self.rect.bottom = settings.screenheight - 40
        if self.rect.top < 0:
            self.rect.top = 0

class Bullet(pygame.sprite.Sprite):
    """ Bullets to shoot aliens """
    def __init__(self, width, height, color, speed, strength):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.timer = 0
        self.strength = strength

    def update(self):
        # - Move bullet position - #
        self.rect.y -= self.speed

class Alien(pygame.sprite.Sprite):
    """ Aliens to shoot appear to top of screen """
    def __init__(self, image, lives, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(settings.screenwidth - 50)
        self.rect.y = -50

        self.lives = lives
        self.speed = speed
        self.timer = 0

    def update(self):
        # - Move Alien position - #
        self.rect.y += self.speed

class Asteroid(pygame.sprite.Sprite):
    """ Class for asteroids """
    def __init__(self, image, lives):
        super().__init__()
        self.original_image = image
        self.image = self.original_image
        self.lives = lives + 1
        self.rect = self.image.get_rect()
        self.angle = 0
        self.direction = random.choice([1, -1])

        # - Random position of asteroid - #
        self.rect.x = random.randrange(0, settings.screenwidth)
        self.rect.y = -self.rect.height
        # - Drift of asteroid in x axis - #
        self.dx = random.choice([-3, -2, -1, 1, 2, 3])
        self.saved_dx = self.dx
        # - Speed of asteroid in y axis - #
        self.dy = random.randrange(1, 4)
        self.saved_dy = self.dy

        self.timer = 0

    def freeze(self):
        self.saved_direction = self.direction
        self.direction = 0
        self.saved_dx = self.dx
        self.saved_dy = self.dy
        self.dx = 0
        self.dy = 0

    def update(self):
        # - Rotate asteroid - #
        center_pos = self.rect.center
        self.angle += self.direction
        if self.angle == 360 or self.angle == -360:
            self.angle = 0
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = center_pos

        # - Move asteroid across screen - #
        self.rect.x += self.dx
        self.rect.y += self.dy

class Power_up(pygame.sprite.Sprite):
    """ Class for game power-ups """
    def __init__(self, image):
        super().__init__()
        # - Choose power up at random - #
        self.image = image

        # - Initialise power-up - #
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, settings.screenwidth - 10)
        self.rect.y = -10
        self.speed = 1
        self.timer = 0

    def update(self):
        self.rect.y += self.speed

class Laser(pygame.sprite.Sprite):
    """ Laser weapon if power up gained """
    def __init__(self, width, height, color):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color

        self.original_image = pygame.Surface([width, self.height])
        self.original_image.fill(color)
        self.rect = self.original_image.get_rect()

    def update(self):
        center_posx = self.rect.centerx
        bottom_pos = self.rect.bottom
        if self.height < 200:
            self.height += 3
        if self.height >= 200:
            bottom_pos -= 3
        self.image = pygame.transform.scale(self.original_image, [self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.centerx = center_posx
        self.rect.bottom = bottom_pos

class Force_field(pygame.sprite.Sprite):
    """ Force field if power up gained """
    def __init__(self, width, height, pos, strength):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.strength = strength

    def update(self, pos):
        self.rect.center = pos

    def draw(self, screen):
        pygame.draw.arc(screen, colors.cyan, self.rect, 0, settings.pi, 2)

class World_shield(pygame.sprite.Sprite):
    """ Force field to protect planet """
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([settings.screenwidth + 200, 50])
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = settings.screenheight - 100

    def draw(self, screen):
        pygame.draw.arc(screen, colors.purple, self.rect, 0, settings.pi, 3)

class Wave(pygame.sprite.Sprite):
    """
    Class to produce wave outward from player
    Used for freeze wave and nuke weapons

    Freeze wave stuns all objects on screen
    Nuke destorys all objects on screen
    """
    def __init__(self, pos):
        super().__init__()
        self.width = 10
        self.height = 10
        self.original_image = pygame.Surface([self.width, self.height])
        self.rect = self.original_image.get_rect()
        self.rect.center = pos

    def update(self):
        # Get surface center
        center_pos = self.rect.center
        # Transform surface size
        self.width += 4
        self.height += 4
        self.image = pygame.transform.scale(self.original_image, [self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.center = center_pos
        self.radius = int(self.width / 2)

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, self.rect.center, self.radius, 3)

class Game(object):
    """ This is an instance of the game """
    def __init__(self):
        # --- Game attributes --- #
        self.score = 0
        self.aliens_escaped = 0
        self.decide_aliens_escaped = 25
        self.coin_counter = 0

        self.game_over = False
        self.name = ""

        self.playerbulletspeed = 3
        self.playerbulletstrength = 1
        self.bullet_color = colors.white

        self.fastbullets = False
        self.choose_fastbullets = False
        self.counter_fastbullets = 0

        self.laser = False
        self.choose_laser = False
        self.counter_laser = 0

        self.force_field = False

        self.world_shield = False
        self.choose_world_shield = False
        self.counter_world_shield = 0

        self.freeze = False
        self.choose_freeze = False
        self.counter_freeze = 0
        self.freeze_wave_shoot = False

        self.nuke = False
        self.choose_nuke = False
        self.counter_nuke = 0
        self.nuke_wave_shoot = False

        self.doublestrengthbullets = False
        self.choose_doublestrengthbullets = False
        self.counter_doublestrengthbullets = 0

        self.bullet_jam = False
        self.bullet_jam_timer = 0

        # --- Get previous high score --- #
        file = open("highscore.txt")
        self.high_score = []
        for line in file:
            line = line.strip()
            self.high_score.append(line)
        file.close()

        # --- Sprite lists --- #
        self.all_sprites_list = pygame.sprite.Group()
        self.player_list = pygame.sprite.Group()
        self.player_bullet_list = pygame.sprite.Group()
        self.alien_list = pygame.sprite.Group()
        self.alien_bullet_list = pygame.sprite.Group()
        self.asteroids_list = pygame.sprite.Group()
        self.power_up_list = pygame.sprite.Group()
        self.laser_list = pygame.sprite.Group()
        self.force_field_list = pygame.sprite.Group()
        self.world_shield_list = pygame.sprite.Group()

        # --- Create the sprites ---#
        # - Create the player - #
        self.player = Player(images.player_img)
        self.player_list.add(self.player)

    def process_events(self):
        """ Process game events """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
                if not self.game_over:
                    if not self.bullet_jam:
                        if self.choose_laser:
                            laser = Laser(4, 10, colors.red)
                            laser.rect.centerx = self.player.rect.centerx
                            laser.rect.bottom = self.player.rect.top
                            self.all_sprites_list.add(laser)
                            self.laser_list.add(laser)
                            self.player_fix_pos = self.player.rect.center
                        if self.choose_freeze:
                            self.freeze_wave = Wave(self.player.rect.center)
                            self.freeze_wave_shoot = True
                            self.choose_freeze = False
                        if self.choose_nuke:
                            self.nuke_wave = Wave(self.player.rect.center)
                            self.nuke_wave_shoot = True
                            self.choose_nuke = False
                        else:
                            bullet = Bullet(4, 10, self.bullet_color, self.playerbulletspeed, self.playerbulletstrength)
                            bullet.rect.centerx = self.player.rect.centerx
                            bullet.rect.bottom = self.player.rect.top
                            self.all_sprites_list.add(bullet)
                            self.player_bullet_list.add(bullet)

            if event.type == pygame.KEYDOWN:
                if not self.game_over:
                    if self.fastbullets:
                        if event.key == pygame.K_s:
                            self.choose_fastbullets = True
                            self.counter_fastbullets -= 1
                            self.playerbulletspeed = 8
                            self.fastbulletstime = time.time()
                    if self.laser:
                        if event.key == pygame.K_l:
                            self.choose_laser = True
                            self.counter_laser -= 1
                            self.lasertime = time.time()
                    if self.world_shield:
                        if event.key == pygame.K_w:
                            self.choose_world_shield = True
                            self.counter_world_shield -= 1
                            self.planet_shield = World_shield()
                            self.world_shield_list.add(self.planet_shield)
                            self.worldshieldtime = time.time()
                    if self.freeze:
                        if event.key == pygame.K_f:
                            self.choose_freeze = True
                            self.counter_freeze -= 1
                    if self.nuke:
                        if event.key == pygame.K_n:
                            self.choose_nuke = True
                            self.counter_nuke -= 1
                    if self.doublestrengthbullets:
                        if event.key == pygame.K_d:
                            self.choose_doublestrengthbullets = True
                            self.counter_doublestrengthbullets -= 1
                            self.playerbulletstrength = 2
                            self.bullet_color = colors.purple
                            self.doublestrengthbulletstime = time.time()

                if self.game_over:
                    if event.unicode.isalpha():
                        self.name += event.unicode
                    if event.key == pygame.K_SPACE:
                        self.name += " "
                    if event.key == pygame.K_BACKSPACE:
                        self.name = self.name[:-1]
                    if len(self.name) > 25:
                        self.name = self.name[:-1]
                    if event.key == pygame.K_RETURN:
                        file = open("highscore.txt", "w")
                        file.write("Space Invaders\nName: " + self.name + "\n" + self.new_high_score)
                        file.close()
                        self.score = 0
                        self.name = ""
        return False

    def run_logic(self):
        """ Update game mechanics """

        if not self.game_over:

            # ----- SPRITE MOVEMENT ----- #
            # - Move all sprites - #
            self.all_sprites_list.update()
            self.player_list.update()

            if self.counter_fastbullets == 0:
                self.fastbullets = False
            if self.counter_laser == 0:
                self.laser = False
            if self.counter_world_shield == 0:
                self.world_shield = False
            if self.counter_freeze == 0:
                self.freeze = False
            if self.counter_nuke == 0:
                self.nuke = False
            if self.counter_doublestrengthbullets == 0:
                self.doublestrengthbullets = False

            if self.coin_counter == 5:
                self.player.max_lives += 10
                self.player.lives += 1
                self.coin_counter = 0

            if self.force_field:
                self.force_field_list.update(self.player.rect.center)

            # - Game and power up timing - #
            if self.choose_fastbullets:
                if time.time() - self.fastbulletstime > 10:
                    self.choose_fastbullets = False
                    self.playerbulletspeed = 3

            if self.choose_doublestrengthbullets:
                if time.time() - self.doublestrengthbulletstime > 10:
                    self.choose_doublestrengthbullets = False
                    self.playerbulletstrength = 1
                    self.bullet_color = colors.white

            if self.choose_laser: # DOES PLAYER GET POINTS FOR HITTING OBJECTS WITH LASER?????
                for laser in self.laser_list:
                    laser.update()
                    if laser.height < 200:
                        self.player.rect.center = self.player_fix_pos
                    laser_hit_list = pygame.sprite.spritecollide(laser, self.asteroids_list, True)
                    laser_hit_list = pygame.sprite.spritecollide(laser, self.alien_list, True)
                    laser_hit_list = pygame.sprite.spritecollide(laser, self.alien_bullet_list, True)
                    if time.time() - self.lasertime > 10:
                        self.choose_laser = False

            # Does freeze wave hit enemy or enemy bullets
            # Timer initiated to halt enemies for some time
            if self.freeze_wave_shoot:
                self.freeze_wave.update()
                if (self.freeze_wave.rect.top < 0 and
                    self.freeze_wave.rect.bottom > settings.screenheight - 40 and
                    self.freeze_wave.rect.right > settings.screenwidth and
                    self.freeze_wave.rect.left < 0):
                        self.freeze_wave_shoot = False
                wave_hit_alien_list = pygame.sprite.spritecollide(self.freeze_wave, self.alien_list, False)
                for alien in wave_hit_alien_list:
                    alien.speed = 0
                    alien.timer = time.time()
                wave_hit_alien_bullet_list = pygame.sprite.spritecollide(self.freeze_wave, self.alien_bullet_list, False)
                for bullet in wave_hit_alien_bullet_list:
                    bullet.speed = 0
                    bullet.timer = time.time()
                wave_hit_powerup_list = pygame.sprite.spritecollide(self.freeze_wave, self.power_up_list, False)
                for powerup in wave_hit_powerup_list:
                    powerup.speed = 0
                    powerup.timer = time.time()
                wave_hit_asteroid_list = pygame.sprite.spritecollide(self.freeze_wave, self.asteroids_list, False)
                for asteroid in wave_hit_asteroid_list:
                    if asteroid.direction != 0:
                        asteroid.freeze()
                    asteroid.timer = time.time()

            # Timing for frozen enemies
            for alien in self.alien_list:
                if alien.speed == 0:
                    if time.time() - alien.timer > 10:
                        alien.speed = 1
            for bullet in self.alien_bullet_list:
                if bullet.speed == 0:
                    if time.time() - bullet.timer > 10:
                        bullet.speed = -3
            for powerup in self.power_up_list:
                if powerup.speed == 0:
                    if time.time() - powerup.timer > 10:
                        powerup.speed = 1
            for asteroid in self.asteroids_list:
                if asteroid.dx == 0 and asteroid.dy == 0:
                    if time.time() - asteroid.timer > 10:
                        asteroid.dx = asteroid.saved_dx
                        asteroid.dy = asteroid.saved_dy
                        asteroid.direction = asteroid.saved_direction

            # Does nuke freeze wave hit enemy or enemy bullets
            if self.nuke_wave_shoot:
                self.nuke_wave.update()
                if self.nuke_wave.rect.top < 0 and self.nuke_wave.rect.bottom > settings.screenheight - 40 and self.nuke_wave.rect.right > settings.screenwidth and self.nuke_wave.rect.left < 0:
                    self.nuke_wave_shoot = False
                wave_hit_alien_list = pygame.sprite.spritecollide(self.nuke_wave, self.alien_list, True)
                wave_hit_alien_bullet_list = pygame.sprite.spritecollide(self.nuke_wave, self.alien_bullet_list, True)
                wave_hit_powerup_list = pygame.sprite.spritecollide(self.nuke_wave, self.power_up_list, True)
                wave_hit_asteroid_list = pygame.sprite.spritecollide(self.nuke_wave, self.asteroids_list, True)

            # ----- IS GAME OVER? ----- #
            # - If no lives left game over - #
            if self.player.lives < 1:
                self.game_over = True

            # - If too many aliens escape game over - #
            if self.aliens_escaped >= self.decide_aliens_escaped:
                self.game_over = True

            # ---- DOES A POWER UP APPEAR ----- #
            yes = random.randrange(750)
            if yes == 0:
                choice = random.choice(images.pwrup_imgs)
                #choice = random.choice([9,10,11])
                #power_up = Power_up(images.pwrup_imgs[15])
                power_up = Power_up(choice)
                self.all_sprites_list.add(power_up)
                self.power_up_list.add(power_up)

            # ----- MAKE ENEMIES ----- #
            # - Decide whether to make an alien - #
            yes = random.randrange(150)
            if yes == 0:
                alien_type = random.choice([0, 1])
                image = images.alien_chars[alien_type][0]
                lives = images.alien_chars[alien_type][1]
                speed = images.alien_chars[alien_type][2]
                alien = Alien(image, lives, speed)
                self.all_sprites_list.add(alien)
                self.alien_list.add(alien)

            # - Does the alien shoot - #
            for alien in self.alien_list:
                if alien.speed == 0:
                    yes = 1
                else:
                    yes = random.randrange(200)
                    #yes = 1
                    if yes == 0:
                        alien_bullet = Bullet(4, 10, colors.green, -3, 1)
                        alien_bullet.rect.centerx = alien.rect.centerx
                        alien_bullet.rect.top = alien.rect.bottom
                        self.all_sprites_list.add(alien_bullet)
                        self.alien_bullet_list.add(alien_bullet)

            # ----- MAKE ASTEROIDS ----- #
            # - Decide whether to make asteroid - #
            yes = random.randrange(500)
            #yes = 1
            if yes == 0:
                choice = random.choice(images.ast_color_list)
                lives = random.randrange(3)
                asteroid = Asteroid(choice[lives], lives)
                self.all_sprites_list.add(asteroid)
                self.asteroids_list.add(asteroid)

            # ---- GAME COLLISIONS ----- #
            # --- Check if player bullets hit anything --- #
            for bullet in self.player_bullet_list:
                # - Check if bullet hits an alien - #
                player_hit_list = pygame.sprite.spritecollide(bullet, self.alien_list, False)
                for alien in player_hit_list:
                    self.score += 1
                    alien.lives -= bullet.strength
                    if alien.lives < 1:
                        self.alien_list.remove(alien)
                        self.all_sprites_list.remove(alien)
                    self.player_bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)

                # - Check if bullet hits an asteroid - #
                asteroid_hit_list = pygame.sprite.spritecollide(bullet, self.asteroids_list, False)
                for asteroid in asteroid_hit_list:
                    asteroid.lives -= bullet.strength
                    if asteroid.lives < 0:
                        self.asteroids_list.remove(asteroid)
                        self.all_sprites_list.remove(asteroid)
                    self.player_bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)

                # - Check if bullet hits alien bullet - #
                bullet_hit_list = pygame.sprite.spritecollide(bullet, self.alien_bullet_list, True)
                for bullet_clash in bullet_hit_list:
                    self.player_bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)

                # - Check if bullet flies off screen - #
                if bullet.rect.y < -10:
                    self.player_bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)

            # --- Check if alien bullet hits player --- #
            for bullet in self.alien_bullet_list:
                alien_hit_list = pygame.sprite.spritecollide(bullet, self.player_list, False)

                # - If alien hits player lower player lives - #
                for player in alien_hit_list:
                    self.alien_bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                    self.player.lives -= bullet.strength

                # - Check if alien hits asteroid - #
                alien_hit_asteroid = pygame.sprite.spritecollide(bullet, self.asteroids_list, True)
                for alien in alien_hit_asteroid:
                    self.alien_bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)

                # - Check if alien bullet flies off screen - #
                if bullet.rect.top > settings.screenheight - 40:
                    self.alien_bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)

            # - Check if player hits asteroid - #
            player_hit_asteroid = pygame.sprite.spritecollide(self.player, self.asteroids_list, True)
            for asteroid in player_hit_asteroid:
                self.player.lives -= 1

            # - Check if player hits alien - #
            player_hit_alien = pygame.sprite.spritecollide(self.player, self.alien_list, True)
            for alien in player_hit_alien:
                self.player.lives -= 1

            # - Check if asteroid hits an alien - #
            asteroid_hit_alien = pygame.sprite.groupcollide(self.asteroids_list, self.alien_list, False, True)

            # ----- POWER UP BENEFITS ----- #
            # - Check if player gets a power up - #
            power_up_hit = pygame.sprite.spritecollide(self.player, self.power_up_list, True)
            for bonus in power_up_hit:
                if bonus.image == images.heart_img:
                    if self.player.lives == self.player.max_lives:
                        pass
                    else:
                        self.player.lives += 1
                elif bonus.image == images.lose_life_img:
                    self.player.lives -= 1
                elif bonus.image == images.max_health_img:
                    self.player.lives = 10
                elif bonus.image == images.fast_bullets_img:
                    self.fastbullets = True
                    self.counter_fastbullets += 1
                elif bonus.image == images.laser_img:
                    self.laser = True
                    self.counter_laser += 1
                elif bonus.image == images.force_field_img_1:
                    if not self.force_field:
                        self.force_field = True
                        self.shield = Force_field(self.player.rect.width + 3, self.player.rect.height + 3, self.player.rect.center, 1)
                        self.force_field_list.add(self.shield)
                        self.forcefieldtime = time.time()
                elif bonus.image == images.force_field_img_2:
                    if not self.force_field:
                        self.force_field = True
                        self.shield = Force_field(self.player.rect.width + 3, self.player.rect.height + 3, self.player.rect.center, 2)
                        self.force_field_list.add(self.shield)
                        self.forcefieldtime = time.time()
                elif bonus.image == images.force_field_img_3:
                    if not self.force_field:
                        self.force_field = True
                        self.shield = Force_field(self.player.rect.width + 3, self.player.rect.height + 3, self.player.rect.center, 3)
                        self.force_field_list.add(self.shield)
                        self.forcefieldtime = time.time()
                elif bonus.image == images.world_shield_img:
                    self.world_shield = True
                    self.counter_world_shield += 1
                elif bonus.image == images.freeze_img:
                    self.freeze = True
                    self.counter_freeze += 1
                elif bonus.image == images.nuke_img:
                    self.nuke = True
                    self.counter_nuke += 1
                elif bonus.image == images.dbl_str_bullet_img:
                    self.doublestrengthbullets = True
                    self.counter_doublestrengthbullets += 1
                elif bonus.image == images.coin_img:
                    self.coin_counter += 1
                elif bonus.image == images.bullet_block_img:
                    if not self.bullet_jam:
                        self.bullet_jam = True
                        self.bullet_jam_timer = time.time()
                elif bonus.image == images.rmv_item_img:
                    self.counter_fastbullets = 0
                    self.counter_laser = 0
                    self.counter_world_shield = 0
                    self.counter_freeze = 0
                    self.counter_nuke = 0
                    self.counter_doublestrengthbullets = 0
                elif bonus.image == images.reset_bonus_img:
                    self.force_field = False
                    self.choose_fastbullets = False
                    self.playerbulletspeed = 3
                    self.choose_doublestrengthbullets = False
                    self.playerbulletstrength = 1
                    self.choose_laser = False
                    self.choose_world_shield = False
                    self.choose_freeze = False
                    self.choose_nuke = False

            # Trick bonus - jam bullets for period of time
            if self.bullet_jam:
                if time.time() - self.bullet_jam_timer > 3: # TIMER FOR BULLET JAM
                    self.bullet_jam = False

            # - Does object hit force field shield - #
            if self.force_field:
                force_field_hit_alienbullets = pygame.sprite.spritecollide(self.shield, self.alien_bullet_list, True)
                force_field_hit_asteroids = pygame.sprite.spritecollide(self.shield, self.asteroids_list, True)
                force_field_hit_aliens = pygame.sprite.spritecollide(self.shield, self.alien_list, True)
                if len(force_field_hit_alienbullets) > 0 or len(force_field_hit_asteroids) > 0 or len(force_field_hit_aliens) > 0:
                    self.shield.strength -= len(force_field_hit_alienbullets) + len(force_field_hit_asteroids) + len(force_field_hit_aliens)
                    if self.shield.strength < 1 or time.time() - self.forcefieldtime > 10:
                        self.force_field = False
                        self.force_field_list.remove(self.shield)

            # - Does object hit planet shield - #
            if self.choose_world_shield:
                world_shield_hit_alienbullets = pygame.sprite.spritecollide(self.planet_shield, self.alien_bullet_list, True)
                world_shield_hit_asteroids = pygame.sprite.spritecollide(self.planet_shield, self.asteroids_list, True)
                world_shield_hit_aliens = pygame.sprite.spritecollide(self.planet_shield, self.alien_list, True)
                if time.time() - self.worldshieldtime > 5:
                    self.choose_world_shield = False

            # ----- DO OBJECTS OR ALIENS FLY OFF SCREEN? ----- #
            # - Check if alien escapes past player - #
            for alien in self.alien_list:
                if alien.rect.top > settings.screenheight - 40:
                    self.alien_list.remove(alien)
                    self.all_sprites_list.remove(alien)
                    self.aliens_escaped += 1

            # - Check if asteroid flies off screen - #
            for asteroid in self.asteroids_list:
                if asteroid.rect.top > settings.screenheight - 40:
                    self.asteroids_list.remove(asteroid)
                    self.all_sprites_list.remove(asteroid)

            # - Check if power up flies off screen - #
            for bonus in self.power_up_list:
                if bonus.rect.top > settings.screenheight - 40:
                    self.power_up_list.remove(bonus)
                    self.all_sprites_list.remove(bonus)

    def display_frame(self, screen):
        """ Update screen display """
        # - Blank screen - #
        screen.fill(colors.black)

        # - Draw game over screen - #
        if self.game_over:
            font = pygame.font.SysFont("calibri", 25)
            if self.score > int(self.high_score[2]):
                # - Save new high score - #
                self.new_high_score = str(self.score)
                text = font.render("New High Score! Enter Name:", True, colors.red)
                text2 = font.render(self.name, True, colors.red)

            else:
                # - Re-initialise game on mouse click
                if self.player.lives == 0:
                    text2 = font.render("You ran out of lives!", True, colors.red)
                elif self.aliens_escaped >= self.decide_aliens_escaped:
                    text2 = font.render("Too many aliens escaped!", True, colors.red)
                text3 = font.render("Click to restart", True, colors.red)
                font = pygame.font.SysFont("impact", 100)
                text = font.render("GAME OVER", True, colors.red)
                center_x = (settings.screenwidth // 2) - (text3.get_width() // 2)
                center_y = (settings.screenheight // 2) + text.get_height() + text2.get_height()
                screen.blit(text3, [center_x, center_y])

            center_x = (settings.screenwidth // 2) - (text.get_width() // 2)
            center_y = (settings.screenheight // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

            center_x = (settings.screenwidth // 2) - (text2.get_width() // 2)
            center_y = (settings.screenheight // 2) + (text.get_height() // 2)
            screen.blit(text2, [center_x, center_y])

        # - Draw game graphics - #
        if not self.game_over:
            # - Move all sprites - #
            self.all_sprites_list.draw(screen)

            # - Display sprite images - #
            screen.blit(self.player.image, [self.player.rect.x, self.player.rect.y])
            for alien in self.alien_list:
                screen.blit(alien.image, [alien.rect.x, alien.rect.y])
            for asteroid in self.asteroids_list:
                screen.blit(asteroid.image, [asteroid.rect.x, asteroid.rect.y])

            if self.force_field:
                self.shield.draw(screen)

            if self.choose_world_shield:
                self.planet_shield.draw(screen)

            if self.freeze_wave_shoot:
                self.freeze_wave.draw(screen, colors.blue)

            if self.nuke_wave_shoot:
                self.nuke_wave.draw(screen, colors.yellow)

            # - Bottom of screen for score and lives display - #
            pygame.draw.rect(screen, colors.black, [0, settings.screenheight - 40, settings.screenwidth, settings.screenheight])
            pygame.draw.line(screen, colors.white, [0, settings.screenheight - 40], [settings.screenwidth, settings.screenheight - 40], 2)

            font = pygame.font.SysFont("impact", 20)

            # - Divide bottom of screen into sections - #
            box_size = settings.screenwidth // 4
            subbox_size = box_size // 6

            score_pos_x = 10

            escaped_pos_x = box_size + 10

            items_pos_x = (2 * box_size)

            # - Display aliens killed - #
            score_text = font.render("Destroyed: " + str(self.score), True, colors.red)

            # - Display how may aliens escaped - #
            escaped_text = font.render("Escaped: " + str(self.aliens_escaped) + "/" + str(self.decide_aliens_escaped), True, colors.red)

            # - Display what items are available - #
            items_text = font.render("Bonus:", True, colors.red)

            # - Display lives left - #
            lives_text = font.render("Lives: " +
                                     str(self.player.lives) +
                                     "/" +
                                     str(self.player.max_lives), True, colors.red)

            text_pos_y = settings.screenheight - score_text.get_height() - 5

            # - Display which keys to press for weapon choice - #
            font = pygame.font.SysFont("arial", 10)
            fastbullets_counter_text = font.render(str(self.counter_fastbullets), True, colors.red)
            laser_counter_text = font.render(str(self.counter_laser), True, colors.red)
            world_shield_counter_text = font.render(str(self.counter_world_shield), True, colors.red)
            freeze_counter_text = font.render(str(self.counter_freeze), True, colors.red)
            nuke_counter_text = font.render(str(self.counter_nuke), True, colors.red)
            doublestrengthbullets_counter_text = font.render(str(self.counter_doublestrengthbullets), True, colors.red)

            # - Bonus images positions - #
            fastbullets_pos_x = items_pos_x + items_text.get_width() + 10
            laser_pos_x = fastbullets_pos_x + images.fast_bullets_img.get_width() + 10
            world_shield_pos_x = laser_pos_x + images.laser_img.get_width() + 10
            freeze_pos_x = world_shield_pos_x + images.world_shield_img.get_width() + 10
            nuke_pos_x = freeze_pos_x + images.freeze_img.get_width() + 10
            doublestrengthbullets_pos_x = nuke_pos_x + images.nuke_img.get_width() + 10

            lives_pos_x = settings.screenwidth - lives_text.get_width() - 10

            # - Bonus counter number text positions - #
            counter_text_pos_y = text_pos_y - (fastbullets_counter_text.get_height() // 2)

            fastbullets_counter_pos_x = fastbullets_pos_x - fastbullets_counter_text.get_width()
            laser_counter_pos_x = laser_pos_x - laser_counter_text.get_width()
            world_shield_counter_pos_x = world_shield_pos_x - world_shield_counter_text.get_width()
            freeze_counter_pos_x = freeze_pos_x - freeze_counter_text.get_width()
            nuke_counter_pos_x = nuke_pos_x - nuke_counter_text.get_width()
            doublestrengthbullets_counter_pos_x = doublestrengthbullets_pos_x - doublestrengthbullets_counter_text.get_width()

            # - Bonus keyboard choices - #
            fastbullets_key_text = font.render("S", True, colors.red)
            laser_key_text = font.render("L", True, colors.red)
            world_shield_key_text = font.render("W", True, colors.red)
            freeze_key_text = font.render("F", True, colors.red)
            nuke_key_text = font.render("N", True, colors.red)
            doublestrengthbullets_key_text = font.render("D", True, colors.red)

            # - Bonus keyboard key text positions - #
            keyboard_text_pos_y = text_pos_y + (fastbullets_key_text.get_height() // 2)

            fastbullets_key_text_pos_x = fastbullets_pos_x - fastbullets_key_text.get_width()
            laser_key_text_pos_x = laser_pos_x - laser_key_text.get_width()
            world_shield_key_text_pos_x = world_shield_pos_x - world_shield_key_text.get_width()
            freeze_key_text_pos_x = freeze_pos_x - freeze_key_text.get_width()
            nuke_key_text_pos_x = nuke_pos_x - nuke_key_text.get_width()
            doublestrengthbullets_key_text_pos_x = doublestrengthbullets_pos_x - doublestrengthbullets_key_text.get_width()

            # - Blit game info to screen - #
            screen.blit(score_text, [score_pos_x, text_pos_y])

            screen.blit(escaped_text, [escaped_pos_x, text_pos_y])

            screen.blit(items_text, [items_pos_x, text_pos_y])

            screen.blit(images.fast_bullets_img, [fastbullets_pos_x, text_pos_y])
            screen.blit(fastbullets_counter_text, [fastbullets_counter_pos_x, counter_text_pos_y])
            screen.blit(fastbullets_key_text, [fastbullets_key_text_pos_x, keyboard_text_pos_y])

            screen.blit(images.laser_img, [laser_pos_x, text_pos_y])
            screen.blit(laser_counter_text, [laser_counter_pos_x, counter_text_pos_y])
            screen.blit(laser_key_text, [laser_key_text_pos_x, keyboard_text_pos_y])

            screen.blit(images.world_shield_img, [world_shield_pos_x, text_pos_y])
            screen.blit(world_shield_counter_text, [world_shield_counter_pos_x, counter_text_pos_y])
            screen.blit(world_shield_key_text, [world_shield_key_text_pos_x, keyboard_text_pos_y])

            screen.blit(images.freeze_img, [freeze_pos_x, text_pos_y])
            screen.blit(freeze_counter_text, [freeze_counter_pos_x, counter_text_pos_y])
            screen.blit(freeze_key_text, [freeze_key_text_pos_x, keyboard_text_pos_y])

            screen.blit(images.nuke_img, [nuke_pos_x, text_pos_y])
            screen.blit(nuke_counter_text, [nuke_counter_pos_x, counter_text_pos_y])
            screen.blit(nuke_key_text, [nuke_key_text_pos_x, keyboard_text_pos_y])

            screen.blit(images.dbl_str_bullet_img, [doublestrengthbullets_pos_x, text_pos_y])
            screen.blit(doublestrengthbullets_counter_text, [doublestrengthbullets_counter_pos_x, counter_text_pos_y])
            screen.blit(doublestrengthbullets_key_text, [doublestrengthbullets_key_text_pos_x, keyboard_text_pos_y])

            screen.blit(lives_text, [lives_pos_x, text_pos_y])

        pygame.display.flip()

def main():
    """ Main program loop """

    done = False
    clock = pygame.time.Clock()

    # - Create an instance of the game - #
    game = Game()

    # - Main event loop - #
    while not done:

        # - Process events - #
        done = game.process_events()

        # - Game logic - #
        game.run_logic()

        # - Draw frame - #
        game.display_frame(SCREEN)

        # - Pause for next screen - #
        clock.tick(60)

    # - Close window in exit - #
    pygame.quit()

# - Call main function to begin - #
if __name__ == '__main__':
    main()
