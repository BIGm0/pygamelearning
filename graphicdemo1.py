# -*- coding: utf-8 -*-
"""003_static_blit_pretty_template.py"""
import pygame 
import random
import math
def radians_to_degrees(radians):
    return (radians /math.pi)*180.0
    
def degrees_to_radians(degrees):
    return degrees * (math.pi/180.0)


class PygView(object):
    width = 0
    height = 0
    def __init__(self, width=640, height=400, fps=100):
        """Initialize pygame, window, background, font,...
           default arguments """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        PygView.width = width
        PygView.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()  
        self.background.fill((255,255,255)) # fill background white
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 24, bold=True)
        self.allgroup =pygame.sprite.LayeredUpdates()
        self.ballgroup=pygame.sprite.Group()
        
        Ball.groups=self.allgroup,self.ballgroup
        
        
    def paint(self):
        """painting on the surface"""
        #pygame.draw.arc(self.background, (0,150,0),(725,10,725,420),start,end,1)
        xpoints=[]
        ypoints=[]
        xdist=PygView.width//100
        ydist=PygView.height//100
        for a in range(100):
            xpoints.append(xdist*a)
        for a in range(100):
            ypoints.append(ydist*a)
        for a in range(100):
            pygame.draw.line(self.background, (0,255-int(a*2.55),int(a*2.55)), (0,ypoints[a]),(xpoints[a],PygView.height))
            pygame.draw.line(self.background, (0+int(a*2.55),255-int(a*2.55),int(a*2.55)), (PygView.width,ypoints[a]),(xpoints[a],0))
            pygame.draw.line(self.background, (0+int(a*2.55),255-int(a*2.55),int(a*2.55)), (xpoints[-a],0),(0,ypoints[a]))
        for a in range(1, 100):
            pygame.draw.line(self.background, (0+int(a*2.55),255-int(a*2.55),int(a*2.55)), (xpoints[a],PygView.height),(PygView.width,ypoints[-a]))
        
        
        
        
        
        
            
    def run(self):
        self.paint() 
        myball = Ball(startx=100,starty=100) # creating the Ball object
        myball2= Ball( radius = 10, color=(0,0,150), x=500, y=160,
                    up=pygame.K_w,down=pygame.K_s,left=pygame.K_a,right=pygame.K_d,
                    startx=100,starty=200)
        myball3=Ball( radius = 15, color=(0,0,100), x=500, y=160,
                    up=pygame.K_w,down=pygame.K_s,left=pygame.K_a,right=pygame.K_d,
                    startx=100,starty=300)
        myball4=Ball( radius = 5, color=(0,255,0), x=500, y=160,
                    up=pygame.K_UP,down=pygame.K_DOWN,left=pygame.K_LEFT,right=pygame.K_RIGHT,
                    startx=1300,starty=100)
        myball5=Ball( radius = 10, color=(0,150,0), x=600, y=160,
                    up=pygame.K_UP,down=pygame.K_DOWN,left=pygame.K_LEFT,right=pygame.K_RIGHT,
                    startx=1300,starty=200)
        myball6=Ball( radius = 15, color=(0,100,0), x=700, y=160,
                    up=pygame.K_UP,down=pygame.K_DOWN,left=pygame.K_LEFT,right=pygame.K_RIGHT,
                    startx=1300,starty=300)
        myball7=Ball( radius = 10, color=(100,0,0), x=500, y=160,
                    up=pygame.K_UP,down=pygame.K_DOWN,left=pygame.K_LEFT,right=pygame.K_RIGHT,
                    startx=600,starty=600)
        myball8=Ball( radius = 10, color=(180,0,0), x=500, y=160,
                    up=pygame.K_UP,down=pygame.K_DOWN,left=pygame.K_LEFT,right=pygame.K_RIGHT,
                    startx=650,starty=600)
        myball9=Ball( radius = 10, color=(255,0,0), x=500, y=160,
                    up=pygame.K_UP,down=pygame.K_DOWN,left=pygame.K_LEFT,right=pygame.K_RIGHT,
                    startx=700,starty=600)
                    
                    
        running = True
        while running:
            milliseconds = self.clock.tick(self.fps)
            seconds = milliseconds / 1000.0
            self.playtime += seconds
            #self.draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(
                           #self.clock.get_fps(), " "*5, self.playtime))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
                elif event.type == pygame.KEYDOWN:
                    # keys that you press once and release
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_q: # stopper 
                        for ball in self.ballgroup:
                            ball.x=ball.startx
                            ball.y=ball.starty
                            ball.dx,ball.dy=0,0
                            
            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))
            self.allgroup.update(seconds)
            self.allgroup.draw(self.screen)
            #myball.update(seconds)
            #myball.blit(self.screen) # blitting it
            #tail
            for ball in self.ballgroup:
                if len(ball.tail)>2:
                    for a in range(1,len(ball.tail)):
                        pygame.draw.line(self.screen,ball.color,
                                     ball.tail[a-1],
                                     ball.tail[a],10-a//10)
        pygame.quit()

    def draw_text(self, text):
        """Center text in window"""
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(surface, (50,150))

class Ball(pygame.sprite.Sprite):
    """this is a native pygame sprite but instead a pygame surface"""
    def __init__(self, radius = 5, color=(0,0,200), x=320, y=240,
                    up=pygame.K_w,down=pygame.K_s,left=pygame.K_a,right=pygame.K_d,
                    startx=100,starty=100):
        """create a (black) surface and paint a blue ball on it"""
        self._layer=1
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.upkey=up
        self.downkey=down
        self.leftkey=left
        self.rightkey=right
        self.radius = radius
        self.color = color
        self.startx=startx
        self.starty=starty
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        # create a rectangular surface for the ball 50x50
        self.image = pygame.Surface((2*self.radius,2*self.radius))
        self.image.set_colorkey((0,0,0))    
        pygame.draw.circle(self.image, color, (radius, radius), radius) # draw blue filled circle on ball surface
        self.image = self.image.convert_alpha() # for faster blitting.
        self.rect=self.image.get_rect() 
        # to avoid the black background, make black the transparent color:
        # self.surface.set_colorkey((0,0,0))
        # self.surface = self.surface.convert_alpha() # faster blitting with transparent color
        self.tail=[]
        
    def update(self, seconds):
        pressedkeys = pygame.key.get_pressed() # keys that you can press all the time
        if pressedkeys[self.leftkey]:
                self.dx -=100
        if pressedkeys[self.rightkey]:
                self.dx +=100
        if pressedkeys[self.upkey]:
                self.dy -= 100
        if pressedkeys[self.downkey]:
                self.dy += 100
        self.x += self.dx * seconds
        self.y += self.dy * seconds
        # wrap around screen
        if self.x < 0:
            #self.x = PygView.width
            self.x=0
            self.dx*=-1
        if self.x > PygView.width:
            #self.x = 0
            self.x=PygView.width
            self.dx*=-1
        if self.y < 0:
            #self.y = PygView.height
            self.y=0
            self.dy*=-1
        if self.y > PygView.height:
            #self.y = 0
            self.y=PygView.height
            self.dy*=-1
        self.tail.insert(0,(self.x,self.y))
        self.tail=self.tail[:128]
        self.rect.center=self.x,self.y
            
        
    #def blit(self, ground):
        #"""blit the Ball on the background"""
        #ground.blit(self.surface, ( self.x, self.y))
        
if __name__ == '__main__':
    PygView(1450,815).run() # call with width of window and fps


