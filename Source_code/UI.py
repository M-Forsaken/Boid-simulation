import config
from Boids import *
from config import *


class UserInterface:
    def __init__(self):
        # image assets
        self.Menu_button_sheet = pygame.image.load(
            CWD + '/assets/image/settings.png').convert_alpha()
        self.volume_button_sheet = pygame.image.load(
            CWD + '/assets/image/sound_button.png').convert_alpha()
        self.Check_box_sheet = pygame.image.load(
            CWD + '/assets/image/Check_box.png').convert_alpha()
        fill(self.Menu_button_sheet, pygame.Color(0, 100, 255))
        fill(self.volume_button_sheet, pygame.Color(0, 100, 255))
        fill(self.Check_box_sheet, pygame.Color(0, 100, 255))
        self.volume_button = Button((config.Width - 50, 50), get_sheet(
            self.volume_button_sheet, 32, 32, 1.5, 0), 1)
        self.Menu_button = Button((config.Width - 50, 100), get_sheet(
            self.Menu_button_sheet, 32, 32, 1, 0), 1)
        self.Check_separation = Button((self.Menu_button.x - 150, self.Menu_button.y + 50), get_sheet(
            self.Check_box_sheet, 16, 16, 1, 0), 1)
        self.Check_alignment = Button((self.Menu_button.x - 150, self.Check_separation.y + 30), get_sheet(
            self.Check_box_sheet, 16, 16, 1, 0), 1)
        self.Check_cohesion = Button((self.Menu_button.x - 150, self.Check_alignment.y + 30), get_sheet(
            self.Check_box_sheet, 16, 16, 1, 0), 1)
        self.Check_avoidance = Button((self.Menu_button.x - 150, self.Check_cohesion.y + 30), get_sheet(
            self.Check_box_sheet, 16, 16, 1, 0), 1)
        self.Check_boid_add = Button((self.Menu_button.x - 150, self.Check_avoidance.y + 30), get_sheet(
            self.Check_box_sheet, 16, 16, 1, 1), 1)
        self.Check_obs_add = Button((self.Menu_button.x - 150, self.Check_boid_add.y + 30), get_sheet(
            self.Check_box_sheet, 16, 16, 1, 0), 1)
        self.Menu_rect = pygame.Rect(0, 0, 40, 40)
        self.Menu_rect.center = (self.Menu_button.x, self.Menu_button.y)
        self.Drop_down_rect = pygame.Rect(0, 0, 40, 40)
        self.Drop_down_rect.center = (self.Menu_button.x, self.Menu_button.y)
        self.sound = True
        self.On_button = False
        self.menu = False
        self.completed = False
        self.mode = True

        # menu_text variable
        self.alignment_text = menufont.render(
            "Alignment", True, (255, 255, 255), (0, 40, 70))
        self.alignment_text_rect = self.alignment_text.get_rect()
        self.alignment_text_rect.topleft = (
            self.Check_alignment.x + 15, self.Check_alignment.y - 7)

        self.cohesion_text = menufont.render(
            "Cohesion", True, (255, 255, 255), (0, 40, 70))
        self.cohesion_text_rect = self.cohesion_text.get_rect()
        self.cohesion_text_rect.topleft = (
            self.Check_cohesion.x + 15, self.Check_cohesion.y - 7)

        self.separation_text = menufont.render(
            "Separation", True, (255, 255, 255), (0, 40, 70))
        self.separation_text_rect = self.separation_text.get_rect()
        self.separation_text_rect.topleft = (
            self.Check_separation.x + 15, self.Check_separation.y - 7)
        
        self.obs_avoid_text = menufont.render(
            "obs avoidance", True, (255, 255, 255), (0, 40, 70))
        self.obs_avoid_text_rect = self.obs_avoid_text.get_rect()
        self.obs_avoid_text_rect.topleft = (
            self.Check_avoidance.x + 15, self.Check_avoidance.y - 7)
        
        self.add_boid_text = menufont.render(
            "add boid", True, (255, 255, 255), (0, 40, 70))
        self.add_boid_text_rect = self.add_boid_text.get_rect()
        self.add_boid_text_rect.topleft = (
            self.Check_boid_add.x + 15, self.Check_boid_add.y - 7)
        
        self.add_obs_text = menufont.render(
            "add obstacle", True, (255, 255, 255), (0, 40, 70))
        self.add_obs_text_rect = self.add_obs_text.get_rect()
        self.add_obs_text_rect.topleft = (
            self.Check_obs_add.x + 15, self.Check_obs_add.y - 7)

        self.help_text = menufont.render(
            "Press 'H' to hide ", True, (255, 255, 255), (0, 40, 70))
        self.help_text_rect = self.help_text.get_rect()
        self.help_text_rect.center = (
            self.Menu_button.x - 80, self.Menu_button.y + 350)

    def event_handler(self):
        for event in pygame.event.get():
            # Sound Button
            self.volume_button.get_clicked(event)
            if self.volume_button.clicked == True:
                if self.sound == True:
                    self.volume_button.image = get_sheet(
                        self.volume_button_sheet, 32, 32, 1.5, 0)
                    pygame.mixer.music.pause()
                    self.sound = False
                else:
                    self.volume_button.image = get_sheet(
                        self.volume_button_sheet, 32, 32, 1.5, 2)
                    pygame.mixer.music.unpause()
                    self.sound = True
                config.click_sound.play()
                self.On_button = True
            if self.volume_button.hover == True:
                if self.sound == True:
                    self.volume_button.image = get_sheet(
                        self.volume_button_sheet, 32, 32, 1.5, 1)
                else:
                    self.volume_button.image = get_sheet(
                        self.volume_button_sheet, 32, 32, 1.5, 3)
            else:
                if self.sound == True:
                    self.volume_button.image = get_sheet(
                        self.volume_button_sheet, 32, 32, 1.5, 0)
                else:
                    self.volume_button.image = get_sheet(
                        self.volume_button_sheet, 32, 32, 1.5, 2)
            # Menu button
            self.Menu_button.get_clicked(event)
            if self.Menu_button.clicked == True:
                config.click_sound.play()
                self.On_button = True
                if self.menu == False:
                    self.menu = True
                    self.completed = False
                else:
                    self.menu = False
                    self.completed = False
            if self.Menu_button.hover == True:
                self.Menu_button.image = get_sheet(
                    self.Menu_button_sheet, 32, 32, 1, 1)
            else:
                self.Menu_button.image = get_sheet(
                    self.Menu_button_sheet, 32, 32, 1, 0)
            # Check_Box:
            if self.menu == True:
                if self.Drop_down_rect.collidepoint(pygame.mouse.get_pos()) or self.Menu_rect.collidepoint(pygame.mouse.get_pos()):
                    self.On_button = True
                self.Check_separation.get_clicked(event)
                self.Check_alignment.get_clicked(event)
                self.Check_cohesion.get_clicked(event)
                self.Check_avoidance.get_clicked(event)
                self.Check_boid_add.get_clicked(event)
                self.Check_obs_add.get_clicked(event)
                # add object
                if self.Check_boid_add.clicked == True:
                    config.click_sound.play()
                    self.mode = True
                    self.Check_boid_add.image = get_sheet(
                        self.Check_box_sheet, 16, 16, 1, 2)
                    self.Check_obs_add.image = get_sheet(
                        self.Check_box_sheet, 16, 16, 1, 0)
                    
                if self.Check_obs_add.clicked == True:
                    config.click_sound.play()
                    self.mode = False
                    self.Check_boid_add.image = get_sheet(
                        self.Check_box_sheet, 16, 16, 1, 0)
                    self.Check_obs_add.image = get_sheet(
                        self.Check_box_sheet, 16, 16, 1, 2)
                    
                if self.Check_boid_add.hover == True:
                    if self.mode == True:
                        self.Check_boid_add.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 3)
                    else:
                        self.Check_boid_add.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 1)
                else:
                    if self.mode == True:
                        self.Check_boid_add.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 2)
                    else:
                        self.Check_boid_add.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 0)
                        
                if self.Check_obs_add.hover == True:
                    if self.mode == False:
                        self.Check_obs_add.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 3)
                    else:
                        self.Check_obs_add.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 1)
                else:
                    if self.mode == False:
                        self.Check_obs_add.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 2)
                    else:
                        self.Check_obs_add.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 0)
                    
                # obstacle avoidance:
                    if self.Check_avoidance.clicked == True:
                        config.click_sound.play()
                        self.On_button = True
                        if config.avoid_toggle == False:
                            config.avoid_toggle = True
                            self.Check_avoidance.image = get_sheet(
                                self.Check_box_sheet, 16, 16, 1, 2)
                            message = "obstacle avoidance on"
                            config.mess_queue.append(message)
                        else:
                            config.avoid_toggle = False
                            self.Check_avoidance.image = get_sheet(
                                self.Check_box_sheet, 16, 16, 1, 0)
                            message = "obstacle avoidance off"
                            config.mess_queue.append(message)

                    if self.Check_avoidance.hover == True:
                        if config.avoid_toggle == True:
                            self.Check_avoidance.image = get_sheet(
                                self.Check_box_sheet, 16, 16, 1, 3)
                        else:
                            self.Check_avoidance.image = get_sheet(
                                self.Check_box_sheet, 16, 16, 1, 1)
                    else:
                        if config.avoid_toggle == True:
                            self.Check_avoidance.image = get_sheet(
                                self.Check_box_sheet, 16, 16, 1, 2)
                        else:
                            self.Check_avoidance.image = get_sheet(
                                self.Check_box_sheet, 16, 16, 1, 0)
                # separation
                if self.Check_separation.clicked == True:
                    config.click_sound.play()
                    self.On_button = True
                    if config.separation_toggle == False:
                        config.separation_toggle = True
                        self.Check_separation.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 2)
                        message = "separation on"
                        config.mess_queue.append(message)
                    else:
                        config.separation_toggle = False
                        self.Check_separation.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 0)
                        message = "separation off"
                        config.mess_queue.append(message)

                if self.Check_separation.hover == True:
                    if config.separation_toggle == True:
                        self.Check_separation.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 3)
                    else:
                        self.Check_separation.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 1)
                else:
                    if config.separation_toggle == True:
                        self.Check_separation.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 2)
                    else:
                        self.Check_separation.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 0)
                # alignment
                if self.Check_alignment.clicked == True:
                    config.click_sound.play()
                    self.On_button = True
                    if config.alignment_toggle == False:
                        config.alignment_toggle = True
                        self.Check_alignment.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 2)
                        message = "alignment on"
                        config.mess_queue.append(message)

                    else:
                        config.alignment_toggle = False
                        self.Check_alignment.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 0)
                        message = "alignment off"
                        config.mess_queue.append(message)

                if self.Check_alignment.hover == True:
                    if config.alignment_toggle == True:
                        self.Check_alignment.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 3)
                    else:
                        self.Check_alignment.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 1)
                else:
                    if config.alignment_toggle == True:
                        self.Check_alignment.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 2)
                    else:
                        self.Check_alignment.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 0)
                # cohesion
                if self.Check_cohesion.clicked == True:
                    config.click_sound.play()
                    self.On_button = True
                    if config.cohesion_toggle == False:
                        config.cohesion_toggle = True
                        self.Check_cohesion.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 2)
                        message = "cohesion on"
                        config.mess_queue.append(message)
                    else:
                        config.cohesion_toggle = False
                        self.Check_cohesion.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 0)
                        message = "cohesion off"
                        config.mess_queue.append(message)

                if self.Check_cohesion.hover == True:
                    if config.cohesion_toggle == True:
                        self.Check_cohesion.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 3)
                    else:
                        self.Check_cohesion.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 1)
                else:
                    if config.cohesion_toggle == True:
                        self.Check_cohesion.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 2)
                    else:
                        self.Check_cohesion.image = get_sheet(
                            self.Check_box_sheet, 16, 16, 1, 0)
            # Main event
            if event.type == pygame.QUIT:
                config.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    if config.Show_UI == True:
                        config.Show_UI = False
                    else:
                        config.Show_UI = True
            if event.type == pygame.MOUSEBUTTONUP and self.On_button == False:
                if event.button == 1:
                    config.click_sound.play()
                    if self.mode == True:
                        spawn_boid()
                    if self.mode == False:
                        add_obstacle()
            self.On_button = False

    def draw(self, screen):
        if self.menu == True and self.completed == False:
            self.menu_in()
        elif self.menu == False and self.completed == False:
            self.menu_out()
        pygame.draw.rect(screen, pygame.Color(0, 40, 70), self.Drop_down_rect)
        pygame.draw.rect(screen, pygame.Color(0, 50, 100), self.Menu_rect)
        if self.menu == True and self.completed == True:
            self.Check_alignment.draw(screen)
            self.Check_cohesion.draw(screen)
            self.Check_separation.draw(screen)
            self.Check_avoidance.draw(screen)
            self.Check_obs_add.draw(screen)
            self.Check_boid_add.draw(screen)
            screen.blit(self.alignment_text, self.alignment_text_rect)
            screen.blit(self.cohesion_text, self.cohesion_text_rect)
            screen.blit(self.separation_text, self.separation_text_rect)
            screen.blit(self.obs_avoid_text, self.obs_avoid_text_rect)
            screen.blit(self.add_boid_text, self.add_boid_text_rect)
            screen.blit(self.add_obs_text, self.add_obs_text_rect)
            screen.blit(self.help_text, self.help_text_rect)
        self.volume_button.draw(screen)
        self.Menu_button.draw(screen)
        displaytext(screen)
        config.clock.tick(config.FPS)
        fps_counter(screen)

    def menu_in(self):
        a_rate = 10
        if self.Menu_rect.width < 200:
            self.Menu_rect.width += a_rate
            self.Menu_rect.x -= a_rate
            self.Drop_down_rect.width += a_rate
            self.Drop_down_rect.x -= a_rate
        else:
            if self.Drop_down_rect.height < 400:
                self.Drop_down_rect.height += a_rate*2
            else:
                self.completed = True

    def menu_out(self):
        a_rate = 10
        if self.Drop_down_rect.height > 40:
            self.Drop_down_rect.height -= a_rate*2
        else:
            self.Drop_down_rect.height = 40
            if self.Menu_rect.width > 40:
                self.Menu_rect.width -= a_rate
                self.Menu_rect.x += a_rate
                self.Drop_down_rect.width -= a_rate
                self.Drop_down_rect.x += a_rate
            else:
                self.Menu_rect.width = 40
                self.completed = True


class Button:
    def __init__(self, pos, image, scale):
        self.x, self.y = pos[0], pos[1]
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.smoothscale(
            image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.clicked = False
        self.hover = False

    def get_clicked(self, event):
        self.clicked = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.hover = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.clicked = True
                    return
        else:
            self.hover = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)


def fade_effect(text, duration=0.1):
    fade_time = duration / 2 * 1000
    if (config.last_time - config.start) <= fade_time and config.fade == True:
        text.set_alpha(config.text_alpha)
        config.text_alpha += 255/fade_time
        if (config.text_alpha >= 255):
            config.fade = False
        return text
    else:
        config.start = pygame.time.get_ticks()
    if (config.last_time - config.start) <= fade_time and config.fade == False:
        config.text_alpha -= 255/fade_time
        text.set_alpha(config.text_alpha)
        if config.text_alpha <= 0:
            config.fade = True
            config.completed = True
        return text


def setup_Flock(Boid_num):
    for num in range(Boid_num):
        Boid = Boids(pos=(random.randint(50, Width-50), random.randint(50, Height-50)),
                     vel=(random.randint(-200, 200), random.randint(-200, 200)), acc=(0, 0))
        config.Flock.append(Boid)


def spawn_boid():
    Boid = Boids(pos=pygame.mouse.get_pos(),
                 vel=(random.randint(-200, 200), random.randint(-200, 200)), acc=(0, 0))
    config.Flock.append(Boid)


def add_obstacle():
    config.obs_radius = random.randint(30,50)
    Obs = obstacle(pos=pygame.mouse.get_pos(), radius=config.obs_radius)
    config.Obstacle.append(Obs)


def displaytext(screen):
    if len(config.mess_queue) > 0 and config.completed == True:
        config.start = pygame.time.get_ticks()
        config.text = font.render(config.mess_queue.pop(0), True,
                                  (255, 255, 255), (25, 25, 25))
        config.completed = False
    if config.completed == False:
        fade_effect(config.text, 0.15)
        screen.blit(config.text, config.textRect)


def fps_counter(screen):
    FPS_text = font.render(str(int(clock.get_fps())), True,
                           (255, 255, 255), (25, 25, 25))
    screen.blit(FPS_text, FPS_textRect)


def get_sheet(sheet, width, height, scale, frame=0):
    image = pygame.Surface((width, height), pygame.SRCALPHA)
    image.blit(sheet, (0, 0),
               ((frame*width), 0, width, height))
    image = pygame.transform.smoothscale(image, (width*scale, height*scale))
    return image
