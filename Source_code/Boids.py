import config
from Helper import *
from config import *
class Boids:
    def __init__(self, pos, vel, acc, color=pygame.Color(0, 100, 255)):
        self.x = pos[0]
        self.y = pos[1]
        self.Velocity_x = vel[0]
        self.Velocity_y = vel[1]
        self.Acceleration_x = acc[0]
        self.Acceleration_y = acc[1]
        self.PerceptionRadius = 50
        self.AvoidRadius = 100
        self.SeparationRadius = 20
        self.heading = 90
        self.maxSpeed = 150
        self.minSpeed = 100
        self.alpha = random.randint(100, 255)
        self.descending = random.randint(0, 1)
        self.effect_time = pygame.time.get_ticks()
        self.img = pygame.image.load(CWD+'/assets/image/boid.png').convert_alpha()
        self.Color = color
        fill(self.img, self.Color)
        self.rotated = pygame.transform.rotate(
            self.img, -self.heading)
        self.rect = self.rotated.get_rect(
            center=(self.x, self.y))
        self.HeadingPoints = []

    def draw(self, screen):
        self.effect_time = pygame.time.get_ticks()
        self.transparent_effect(0.05)
        # if len(self.HeadingPoints) > 0:
        #     pygame.draw.line(screen, self.Color, (self.x, self.y),
        #                     self.HeadingPoints[-1],1)
        #     self.HeadingPoints = []
        screen.blit(self.rotated, self.rect)

    def transparent_effect(self, loop_time=0.01):
        loop_time = loop_time * 1000
        if (last_time - self.effect_time) <= loop_time and self.descending == True:
            self.rotated.set_alpha(self.alpha)
            self.alpha -= 155/loop_time
            if self.alpha < 100:
                self.descending = False
            return 
        else:
            self.effect_time = pygame.time.get_ticks()
        if (last_time - self.effect_time) <= loop_time and self.descending == False:
            self.rotated.set_alpha(self.alpha)
            self.alpha += 155/loop_time
            if self.alpha > 255:
                self.descending = True
            return
        else:
            self.effect_time = pygame.time.get_ticks()

    def get_neighbors(self):
        neighbors = []
        neighbors_in_protected = []
        for boid in config.Flock:
            if boid != self:
                dist = (self.y-boid.y)**2 + \
                    (self.x-boid.x)**2
                if dist < self.PerceptionRadius**2:
                    neighbors.append(boid)
                if dist < self.SeparationRadius**2:
                    neighbors_in_protected.append(boid)
        return neighbors, neighbors_in_protected
    
    def get_nearby_obstacle(self):
        nearby_obstacle = []
        for obstacle in config.Obstacle:
                dist = (self.y-obstacle.y)**2 + \
                    (self.x-obstacle.x)**2
                if dist < (self.AvoidRadius+obstacle.AvoidRadius)**2:
                    nearby_obstacle.append(obstacle)
        return nearby_obstacle
    
    def obstacle_avoidance(self, obstacles):
        avoidForce_x = 0
        avoidForce_y = 0
        for obstacle in obstacles:
            self.HeadingPoints = get_Acollision_heading((self.x,self.y),self.heading,self.AvoidRadius,(obstacle.x,obstacle.y),obstacle.AvoidRadius)
            avoidForce_x += (self.HeadingPoints[-1][0] - self.x) *avoidF
            avoidForce_y += (self.HeadingPoints[-1][1] - self.y) *avoidF
        return avoidForce_x,avoidForce_y

    def separation(self, neighbors):
        separationForce_x = 0 
        separationForce_y = 0
        for boid in neighbors:
            separationForce_x += (self.x - boid.x) * config.separationF
            separationForce_y += (self.y - boid.y) * config.separationF
        return separationForce_x,separationForce_y

    def alignment(self, neighbors):
        alignmentForce_x = 0
        alignmentForce_y = 0
        for boid in neighbors:
            alignmentForce_x += boid.Velocity_x
            alignmentForce_y += boid.Velocity_y
        if len(neighbors) > 0:
            alignmentForce_x = alignmentForce_x/len(neighbors)
            alignmentForce_y = alignmentForce_y/len(neighbors)
            alignmentForce_x = (alignmentForce_x - self.Velocity_x)*config.alignmentF
            alignmentForce_y = (alignmentForce_y - self.Velocity_y)*config.alignmentF
        return alignmentForce_x,alignmentForce_y

    def cohesion(self, neighbors):
        cohesionForce_x = 0
        cohesionForce_y = 0
        for boid in neighbors:
            cohesionForce_x += boid.x
            cohesionForce_y += boid.y
        if len(neighbors) > 0:
            cohesionForce_x = cohesionForce_x/len(neighbors)
            cohesionForce_y = cohesionForce_y/len(neighbors)
            cohesionForce_x = (cohesionForce_x - self.x)*config.cohesionF
            cohesionForce_y = (cohesionForce_y - self.y)*config.cohesionF
        return cohesionForce_x,cohesionForce_y

    def flock(self):
        neighbors, neighbor_in_protected = self.get_neighbors()
        nearby_obstacle = self.get_nearby_obstacle()
        Force_x = 0
        Force_y = 0
        RForce_x = 0
        RForce_y = 0
        if config.alignment_toggle == True:
            RForce_x,RForce_y = self.alignment(neighbors)
            Force_x += RForce_x
            Force_y += RForce_y
        if config.cohesion_toggle == True:
            RForce_x, RForce_y = self.cohesion(neighbors)
            Force_x += RForce_x
            Force_y += RForce_y
        if config.separation_toggle == True:
            RForce_x, RForce_y = self.separation(neighbor_in_protected)
            Force_x += RForce_x
            Force_y += RForce_y
        if config.avoid_toggle == True:
            RForce_x, RForce_y = self.obstacle_avoidance(nearby_obstacle)
            Force_x += RForce_x
            Force_y += RForce_y
        return Force_x,Force_y
    
    def update(self):
        # update location
        if config.alignment_toggle == True or config.cohesion_toggle == True or config.separation_toggle == True or config.avoid_toggle == True:
            self.Acceleration_x,self.Acceleration_y = self.flock()
            self.Velocity_x += self.Acceleration_x
            self.Velocity_y += self.Acceleration_y
        speed = math.sqrt(self.Velocity_x**2+self.Velocity_y**2)
        # Enforce min and max speeds
        if speed < self.minSpeed:
            self.Velocity_x = (self.Velocity_x/speed)*self.minSpeed
            self.Velocity_y = (self.Velocity_y/speed)*self.minSpeed
        if speed > self.maxSpeed:
            self.Velocity_x = (self.Velocity_x/speed)*self.maxSpeed
            self.Velocity_y = (self.Velocity_y/speed)*self.maxSpeed


        # # Make Boid avoid screen edge
        # if self.x < config.screenMargin:
        #     self.Velocity_x = self.Velocity_x + config.screenF
        # elif self.x > Width - config.screenMargin:
        #     self.Velocity_x = self.Velocity_x - config.screenF
        # if self.y < config.screenMargin:
        #     self.Velocity_y = self.Velocity_y + config.screenF
        # elif self.y > Height - config.screenMargin:
        #     self.Velocity_y = self.Velocity_y - config.screenF

        # Move Boid to Otherside of the screen when go out of bound
        if self.x < 0:
            self.x = Width
        elif self.x > Width:
            self.x = 0
        if self.y < 0:
            self.y = Height
        elif self.y > Height:
            self.y = 0



        self.x += self.Velocity_x*TimeStep
        self.y += self.Velocity_y*TimeStep

        self.heading = np.degrees(np.arctan2(
                self.Velocity_y,self.Velocity_x))
        self.rotated = pygame.transform.rotate(
            self.img, -self.heading)
        self.rect = self.rotated.get_rect(
            center=(self.x, self.y))
        
class obstacle:
    def __init__(self, pos, radius, Color=pygame.Color(0, 40, 70)):
        self.x = pos[0]
        self.y = pos[1]
        self.AvoidRadius = radius
        self.RadiusOffset = 10
        self.color = Color
        self.image = None
        if self.image == None:
            self.ORect = pygame.Rect(0,0,2*radius,2*radius)
            self.ORect.center = (self.x, self.y)
        else:
            self.ORect = self.image.get_rect()
            self.ORect.height = radius*2
            self.ORect.width = radius*2
            self.ORect.center = (self.x, self.y)
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),radius=self.AvoidRadius - self.RadiusOffset)

def update_timestep():
    global TimeStep, last_time
    TimeStep = (pygame.time.get_ticks()-last_time)/1000
    last_time = pygame.time.get_ticks()

def fill(surface, color):
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))
