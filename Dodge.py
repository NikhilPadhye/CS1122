"""
Kathryn Scheunemann
Nikhil Padhye
This program creates a game in which a user runs side to side along a
ground in attempt to avoid the blocks which are falling down trying to
crush the user. The objective of this game is to avoid being crushed
for as long of a period of time as possible.

In addition, the names of our other group members are not present due
to their lack of efforts in trying to help make this game.
"""
 
import pygame, random, sys

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


class Player_character(pygame.sprite.Sprite):
    '''The object moves in the x direction and attempts
       to avoid the oncoming blocks'''
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
        self.gameOver = False #The game is not over
        # Set height, width, color
        self.image = pygame.Surface([15, 15])
        self.image.fill(RED)
        # Set initial location of object
        self.rect = self.image.get_rect()#Makes it a rectangular object
        self.rect.y = 585
        self.rect.x = 294
        self.change_x = 0 #The change in x variable
     
    def changespeed(self, x, y):#Changes the x location of the player character by the parameter passed (1 or -1)
        """ Change the speed of the player. """
        self.change_x += 5 * x # Moves left and right
    def update(self):
        """ Update the blockposition. """
        # Move left/right
        if self.rect.x <= 15 and self.change_x == -1:#Prevents from going out of bounds
            self.change_x = 0
        if self.rect.x >= 585 and self.change_x == 1:#Prevents from going out of bounds
            self.change_x = 0
        self.rect.x += self.change_x #actually changes the x's position
 
        # Check and see if player_character collides with block
        collidesWithBlock = pygame.sprite.spritecollide(self, self.blocks, False)
        for collision in collidesWithBlock: #For the collision
            all_buckets.empty()#Empty everything
            self.gameOver = False#GAME IS OVER!
            for Block in moveable_objects:#removes all the block objects 
                Block.kill()
        
        
            
 
class Block(pygame.sprite.Sprite):
    '''Objects that fall from the top of the screen to the bottom'''
    # Constructor function
    def __init__(self, x, y):
        super().__init__() # Call the parent's constructor
        self.score = 0
        self.image = pygame.Surface([25, 25])
        self.image.fill(BLACK)
 
        # Set initial location of object
        self.rect = self.image.get_rect()
        self.rect.y = 10 #Starting y position
        self.rect.x = random.randint(1,575)#Random x position that would be at any  
 
        self.change_y = 5 # Falling down increment
    
    def update(self):
        self.rect.y += self.change_y #Moves the block down by 5
 
        # Checks if the block runs into the ground
        block_hit_list = pygame.sprite.spritecollide(self, self.buckets, False)
        addBlock = random.randint(1,2)#random int to check if there will be a new block created
        if self.rect.y == 50 and addBlock == 1: #If the block is at the y =50 position and the random int was = 1 then new block 
            new_player()
        if self.rect.y == 350 and addBlock == 2:#f the block is at the y =350 position and the random int was = 2 then new block
            new_player()
        if self.rect.y == 600:#Hits the block
            self.score += 1#one attempted implementation of score
        for block in block_hit_list:
            if self.rect.x >= 0 and self.rect.x<=498:
               self.rect.y = 10 #Set it back to the top
            
 
 
class Ground(pygame.sprite.Sprite):
    """ The floor of the map """
    def __init__(self, x, y, width, height, color):
        """ Constructor for the bucket that the player can run into. """
        # Call the parent's constructor
        super().__init__()
        self.image = pygame.Surface([width, height])#Size of ground       
        self.image.fill(color)#Color of ground
        self.score = 0 #Second implementation of score
        self.rect = self.image.get_rect()#Makes it a rectangle object
        self.rect.y = y#Sets its top left y position
        self.rect.x = x#sets its top left x position
 
pygame.init()# Call this function so the Pygame library can initialize itself
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])#height and width of screen
pygame.display.set_caption('Dodge the blocks!')#Message at top of game screen
moveable_objects = pygame.sprite.Group()#All moving object list
groundFloor = pygame.sprite.Group()#list of one element the floor
all_buckets = pygame.sprite.Group()#All the blocks in one list
floor = Ground(0, 600, 600, 200, BLACK)#Creates the ground
groundFloor.add(floor)#Adds it to the ground list
moveable_objects.add(floor)#Adds it to the moving object list
curr_player = Block(30, 30)#Creates the first block
curr_player.buckets = groundFloor#Creates the ground = to the block's bucket to see if it collided with it
all_buckets.add(curr_player)#Adds the block to the all block 
moveable_objects.add(curr_player)#adds the block to the all moving objects list
curr_user = Player_character(30,30)#current user moving x
curr_user.blocks = all_buckets#Used to check for collisions
moveable_objects.add(curr_user)#Adds the user into the list of all collisions
time = pygame.time.Clock()#Sets timer for frame rate 

done = True

high_score = 0

def printScore(score):#Printing the score if it was done correctly
    font = pygame.font.Font(None, 36)
    line = font.render("Score: " + str(score), 1, (50, 50, 50))
    curr_line = line.get_rect()
    curr_line.centerx = 100
    screen.blit(line, curr_line)
def new_player():#Method used to create new blocks
    player2 = Block(15,15)
    player2.buckets = groundFloor
    all_buckets.add(player2)
    moveable_objects.add(player2)
score = 0
time.tick()#attept for 3rd scoring scheme
while not curr_user.gameOver:
    #if pygame.time.get_ticks()*1000 % 10 == 0:
#        new_player()
    for event in pygame.event.get():#Checks for user key logs
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:#Keyheld down
            if event.type == pygame.K_f:#Random leave key
                done = True
            if event.key == pygame.K_LEFT:#Move left
                curr_user.changespeed(-1, 0)
            elif event.key == pygame.K_RIGHT:#Move right
                curr_user.changespeed(1, 0)
 
        elif event.type == pygame.KEYUP:#tapping the keys
            if event.type ==pygame.K_f:
                done = True
            if event.key == pygame.K_LEFT:#Move left
                curr_user.changespeed(1, 0)
            elif event.key == pygame.K_RIGHT:#Move right
                curr_user.changespeed(-1, 0)
    moveable_objects.update()#Updates every moving object 
    screen.fill(WHITE)#Screen is white
    moveable_objects.draw(screen)#Draws the moving objects onto the screen
    #Attempted to make the score be based on the time
    #alive, but wasnt able to successfully implement.
 #   printScore(time.pygames.time.get_ticks()*1000%1)
 
    pygame.display.flip()

    time.tick(60)#Frame rate
while True:
    #Failed Thanks for Playing message :(
    font = pygame.font.Font(None, 50)
    line = font.render("Thanks For Playing!", 1, (50, 50, 50))
    curr_line = line.get_rect()
    curr_line.centerx = 300
    curr_line.centery = 400
    screen.blit(line, curr_line)

    moveable_objects.draw(screen)

    
pygame.quit() #Ends game 
