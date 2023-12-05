import pygame
import csv, random, sys, time, os
pygame.init() # initialise pygame
global level

def questions():
    if level == "KS1":
        qs = ["Give an example of a command", "1/2 of 12", "What's a noun?", "9+2"]
    elif level == "KS2":
        qs = ["11 x 12", "Define adjective" "Antonym for sad", "3/5 of 25"]
    elif level == "KS3":
        qs = ["List 5 shakespeare plays", "10/6 divide by 5/2", "What is juxtoposition?" , "2x = x- 3, what is x?"]



def game():
    pygame.init()
    score = 0
    screenwidth = 500
    screenheight = 480
    Window = pygame.display.set_mode((screenwidth,screenheight)) # the size of the square progarm, adjustable?
    pygame.display.set_caption("Pygame learning") # The name of the program

    WalkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png')]
    WalkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png')]
    BG = pygame.image.load('Background.jpg')
    Character = pygame.image.load('Standing.png')
    #animation for the movement - they are called animation spirits

    #This is for the background music and sound effects
    #use the sound function fr
    clock = pygame.time.Clock()
    beam_sound = pygame.mixer.Sound('Fly.wav')
    hurt_sound = pygame.mixer.Sound('Ping.wav')
    BG_music = pygame.mixer.music.load('Music.mp3')
    #Now that the program knows what music I want, i need to constantly play it
    pygame.mixer.music.play(-1)
    #-1 so it plays even after the music finishes (loops)


    #The atributes of my character started to get very messy being in the main program
    #I decided to put them in a class because I felt that object oriented programming was the neatest way to layout my character's traits
    #Since I wanted to add enemies, a class was a great way to chain my characters together and let them interact with eachother
    #With a class, I could collect my fields a lot easier. Must add self. to every attribute
    class Gamer():
        def __init__(self, x,y,Width,Height):
            self.x = x
            self.y = y
            self.Width = Width
            self.Height = Height
            self.Speed = 8
            self.Jumping = False
            self.JumpFar = 10
            self.Left = False
            self.Right = False
            self.WalkCount = 0
            self.Standing = True
            self.HitBox = (self.x + 20,self.y +2,28,60)
            self.Visable = True
            self.Health = 15
            #see below for hitbox
            #pygame.draw.rect(Window, (0,0,0), self.HitBox,2)
            
        def draw(self, Window):
            if self.WalkCount +1 >=18: # every sprite will have 3 frames so 6x3 is 18, otherwise there won't be enough space
                self.WalkCount = 0
            if not(self.Standing):
                if self.Left:
                    Window.blit(WalkLeft[self.WalkCount//3], (self.x,self.y)) # need x and y so we know where to move from
                    self.WalkCount += 1
                elif self.Right:
                    Window.blit(WalkRight[self.WalkCount//3], (self.x,self.y))
                    self.WalkCount += 1
            else:
                #Window.blit(Character, (self.x,self.y))
                if self.Left:
                    Window.blit(WalkLeft[0], (self.x, self.y))
                else:
                    Window.blit(WalkRight[0], (self.x, self.y))

        def hurt(self):
            game_over = """
    ███╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
    ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝"""
            #I'm reseting the players position
            #When program freezes to show player damage, it doesn't constantly collide+ cause unfair damage
            self.x = 50 
            self.y = 400
            #In the case where I collide with the enemy when i'm landing a jump and the coordinates reset
            #I will go off-screen when the coordinate reset happens if i'm mid-jump so I need to reset jump if hurt
            self.Jumping = False
            self.JumpFar = 10
            self.WalkCount = 0
            if self.Health >0:
                self.Health = self.Health - 1
                font1 = pygame.font.SysFont('arial', 100, True)
                text = font1.render('-5', 1, (255,0,0))
                Window.blit(text, (250 - (text.get_width()/2),200))
                #the above puts the etxt in the middle
                pygame.display.update()
                tk = 0
                while tk < 100:
                    pygame.time.delay(5)
                    tk = tk + 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            tk = 101
                            pygame.quit()
            else:
                #This will print game over on the screen
                game_over_font = pygame.font.SysFont('arial', 100)
                GT_fot = game_over_font.render(game_over, 1, (128,0,0))
                Window.blit(GT_fot, (250 - (GT_fot.get_width()/2),200))
                pygame.display.update()
                print(game_over)
                pygame.quit()
            # After we are hit we are going to display a message to the screen for
            # a certain period of time
                
            #I wanted my character to have the ability to get hurt so I put a hitbox on it
            #the draw.rect will let me see the hitbox so I know if i need to adjust it to fit my characters size
            self.HitBox = (self.x + 20,self.y + 2,28,60)
            #pygame.draw.rect(Window, (0,0,0), self.HitBox,2)
            

    #Part of the game means being able to shoot projectiles
    #I thought shooting beams from characters eyes was the best way to go
    class Beam():
        def __init__(self,x,y,Radius,Colour,Facing):
    # this determines the dimentions, colour and direction of the beam (attributes)
            self.x = x # tracking the beam the same way we track the characters
            self.y = y
            self.Radius = Radius
            self.Colour = Colour
            self.Facing = Facing
            self.Velocity = 15 * Facing
            
        def draw(self,Window):
            pygame.draw.circle(Window, self.Colour, (self.x, self.y) , self.Radius)
            # I want my beam to be oval shaped so I'm using .circle function
            # This will draw the bullet in pygame

    class mastermind():
        #like with the character, we have to program the animation by using sprites
        WalkRight = [pygame.image.load('VR1.png'), pygame.image.load('VR2.png'), pygame.image.load('VR3.png'), pygame.image.load('VR4.png'), pygame.image.load('VR5.png'), pygame.image.load('VR6.png'), pygame.image.load('VR7.png'), pygame.image.load('VR8.png')]
        WalkLeft = [pygame.image.load('VL1.png'), pygame.image.load('VL2.png'), pygame.image.load('VL3.png'), pygame.image.load('VL4.png'), pygame.image.load('VL5.png'), pygame.image.load('VL6.png'), pygame.image.load('VL7.png'), pygame.image.load('VL8.png')]
        #like with the character, this enemy has a ton of attributes alongside its starting location
        #We need to stop the enemy from moving off the screen for an infinite period of time.

        def __init__(self,x,y ,Width, Height, End):
            self.x = x
            self.y = y
            self.Width = Width
            self.Height = Height
            self.End = End
            self.WalkCount = 0
            self.Path = [x, End]
            self.Velocity = 2
            self.HitBox = (self.x + 20,self.y + 2,28,60)
            self.health = 10
            self.visable = True
            #once health is over, we want to remove this enemy
            # These are all attributes in the class

        def draw(self,Window):
            self.Movement()
            if self.visable == True:
                if self.WalkCount +1  >= 18:
                    self.WalkCount = 0 # remember we need to reset the animation after it moves

                if self.Velocity > 0:
                    Window.blit(self.WalkRight[self.WalkCount//3], (self.x, self.y))
                    self.WalkCount += 1 # incrementing walkcount by 1 in the direction of movement
                else:
                    Window.blit(self.WalkLeft[self.WalkCount//3], (self.x, self.y))
                    self.WalkCount += 1 
                #This will be the hitbox. The red layer will stay the same
                #Everytime the enemy gets shot, the green layer will go down until all health is gone
                pygame.draw.rect(Window, (255,0,0), (self.HitBox[0], self.HitBox[1]-20, 50, 10 ))
                #above, 50- ect...: if health is 10, 50-(5*(10-10)) = 50, meaning a full health bar,
                #As the health decreases, the answer to the subtraction increases therefore more being removed from the health bar
                #hitbox [] is o and 1, x (doesn't need moving) y (moving up by 20 pixels above our character (so health bar is directly above head)
                # 50 and 10 is width and height of the health bar
                #colour red because this is when the enemery is running out of health
                pygame.draw.rect(Window, (0,255,0), (self.HitBox[0], self.HitBox[1] - 20, 50 - ((50/10) * (10 - self.health)), 10))
                self.HitBox = (self.x + 20,self.y + 2,28,60)

        def Movement(self):
            if self.Velocity >0: # is the movement positive?
                if self.x < self.Velocity + self.Path[1]:
                    self.x += self.Velocity
                else:
                    self.Velocity = self.Velocity * -1
                    self.x += self.Velocity
                    self.WalkCount = 0
            else:
                if self.x > self.Path[0] - self.Velocity:
                    self.x += self.Velocity # yeah you'd think we'd be subracting but remember since velocity is already negaitive a = and - makes a -
                else:
                    self.Velocity = self.Velocity * -1
                    self.WalkCount = 0
        #in the case that the enemy/ alien has been injured, a print statement will show up on the running script in the background
        def hurt(self):
            print("Mastermind has been injured")
            if self.health > 0: # you can't hurt him anymore when he's dead :(
                #this will ensure that you only hurt him if he still has life (dark IK)
                self.health = self.health - 1
            else:
                print("Mastermind is dead, that's brutal")
                self.visable = False
        
    #This is the class for the enemy which will eventually be able to damage the character when colliding with it
    class Enemies():
        #like with the character, we have to program the animation by using sprites
        WalkRight = [pygame.image.load('BR1.png'), pygame.image.load('BR2.png'), pygame.image.load('BR3.png'), pygame.image.load('BR4.png'), pygame.image.load('BR5.png'), pygame.image.load('BR6.png'), pygame.image.load('BR7.png'), pygame.image.load('BR8.png')]
        WalkLeft = [pygame.image.load('BL1.png'), pygame.image.load('BL2.png'), pygame.image.load('BL3.png'), pygame.image.load('BL4.png'), pygame.image.load('BL5.png'), pygame.image.load('BL6.png'), pygame.image.load('BL7.png'), pygame.image.load('BL8.png')]
        #like with the character, this enemy has a ton of attributes alongside its starting location
        #We need to stop the enemy from moving off the screen for an infinite period of time.
        def __init__(self,x,y ,Width, Height, End):
            self.x = x
            self.y = y
            self.Width = Width
            self.Height = Height
            self.End = End
            self.WalkCount = 0
            self.Path = [x, End]
            self.Velocity = 2
            self.HitBox = (self.x + 20,self.y + 2,28,60)
            self.health = 10
            self.visable = True
            #once health is over, we want to remove this enemy
            # These are all attributes in the class


        def draw(self,Window):
            self.Movement()
            if self.visable == True:
                if self.WalkCount +1  >= 18:
                    self.WalkCount = 0 # remember we need to reset the animation after it moves

                if self.Velocity > 0:
                    Window.blit(self.WalkRight[self.WalkCount//3], (self.x, self.y))
                    self.WalkCount += 1 # incrementing walkcount by 1 in the direction of movement
                else:
                    Window.blit(self.WalkLeft[self.WalkCount//3], (self.x, self.y))
                    self.WalkCount += 1 
                #This will be the hitbox. The red layer will stay the same
                #Everytime the enemy gets shot, the green layer will go down until all health is gone
                pygame.draw.rect(Window, (255,0,0), (self.HitBox[0], self.HitBox[1]-20, 50, 10 ))
                #above, 50- ect...: if health is 10, 50-(5*(10-10)) = 50, meaning a full health bar,
                #As the health decreases, the answer to the subtraction increases therefore more being removed from the health bar
                #hitbox [] is o and 1, x (doesn't need moving) y (moving up by 20 pixels above our character (so health bar is directly above head)
                # 50 and 10 is width and height of the health bar
                #colour red because this is when the enemery is running out of health
                pygame.draw.rect(Window, (0,255,0), (self.HitBox[0], self.HitBox[1] - 20, 50 - ((50/10) * (10 - self.health)), 10))
                self.HitBox = (self.x + 20,self.y + 2,28,60)

            
            #pygame.draw.rect(Window, (0,0,0), self.HitBox,2)
    #because the character will eventually be able to hurt the enemy using a beam, the enemy must also have a hitbox
            
    #The enemy will always be moving back and forward
        def Movement(self):
            if self.Velocity >0: # is the movement positive?
                if self.x < self.Velocity + self.Path[1]:
                    self.x += self.Velocity
                else:
                    self.Velocity = self.Velocity * -1
                    self.x += self.Velocity
                    self.WalkCount = 0
            else:
                if self.x > self.Path[0] - self.Velocity:
                    self.x += self.Velocity # yeah you'd think we'd be subracting but remember since velocity is already negaitive a = and - makes a -
                else:
                    self.Velocity = self.Velocity * -1
                    self.WalkCount = 0
        #in the case that the enemy/ alien has been injured, a print statement will show up on the running script in the background
        def hurt(self):
            print("Enemy has been injured")
            if self.health > 0: # you can't hurt him anymore when he's dead :(
                #this will ensure that you only hurt him if he still has life (dark IK)
                self.health = self.health - 1
            else:
                print("Enemy is dead, that's brutal")
                self.visable = False
            


    def Redraw_Game_Window():

        #like the character, the enemy will need an update of animation everytime it moves to get a good flowing animation
        Window.blit(BG,[0,0])# 0,0 is the left corner of screen so whole background projected
        text = text_font.render("Score: " + str(score),1,(0,0,0))# renders score onto the screen with the selected features in text_fonts
        Window.blit(text, (390,10))#draws the text + positon of the text
        text_font_bob = pygame.font.SysFont('arial', 10, True)
        text_bob = text_font_bob.render("Health remaining: " + str(Bob.Health),1,(255,0,0))
        Window.blit(text_bob, (200, 10))
                
        Bob.draw(Window)
        #Alien = Enemies(100, 400, 64, 64, 470) #  the 470 is where they will end and turn around
        Alien.draw(Window)
        Villain.draw(Window)
        for Shot in Shots:
            Shot.draw(Window)
        
        pygame.display.update ()

    #############################################################################
    #Program started here
    #Bob is the character - just an easier name to type

    text_font = pygame.font.SysFont('arial', 30, True, True)# type of font, size, bold?, italics?
    Bob = Gamer(400,400,64,64)
    Alien = Enemies(100, 400, 64, 64, 450) # 450 means what coordinates he'll end up at
    Villain = mastermind(200, 400,64,64, 450)
    Shooting = 0
    Shots = []
    RunProgram = True
    while RunProgram: # loop, below is a 'clock'
        clock.tick(27) # time in millerseconds, how quickly your program will react to your command/movement
        
        #This is the collision between the character and the enemy.
        #Same as the beam shots but tailored to hurt the man
        if Alien.visable == True: # if we've killed the Enemy, we don't want more collisions
            if Bob.HitBox[1] < Alien.HitBox[1] + Alien.HitBox[3] and Bob.HitBox[1] + Bob.HitBox[3] > Alien.HitBox[1]:
                if Bob.HitBox[0] + Bob.HitBox[2] > Alien.HitBox[0] and Bob.HitBox[0] < Alien.HitBox[0] + Alien.HitBox[2]:
                    Bob.hurt()
                    score = score -2
        elif Villain.visable == True: # if we've killed the Enemy, we don't want more collisions
            if Bob.HitBox[1] < Villain.HitBox[1] + Villain.HitBox[3] and Bob.HitBox[1] + Bob.HitBox[3] > Villain.HitBox[1]:
                if Bob.HitBox[0] + Bob.HitBox[2] > Villain.HitBox[0] and Bob.HitBox[0] < Villain.HitBox[0] + Villain.HitBox[2]:
                    Bob.hurt()
                    score = score -2
            
                
    #I don'twant to shoot an endless supply of beams
    #If I shoot 3 times then I will have to wait a few millerseconds before I can shoo again.
        if Shooting >0:
            Shooting += 1
            if Shooting > 3:
                Shooting = 0

        #Like when we press a button to make a character move, another event is shooting the beam
    ### first part - checks that we are above the bottom of the rectangle of the alien
    ### second part - checks to make sure that we are below the top of the rectangle

        for Shot in Shots:
            if Alien.visable == True:
                if Shot.y - Shot.Radius < Alien.HitBox[1] + Alien.HitBox[3] and Shot.y + Shot.Radius > Alien.HitBox[1]:
                    # check to see if bullet is in the same y coordinate checking the top of bullet
                    if Shot.x + Shot.Radius > Alien.HitBox [0] and Shot.x - Shot.Radius < Alien.HitBox[0] + Alien.HitBox[2]:
                        # until, [0] which is our x coord, this mean we are on the right side of the left side of the rectangle
                        Alien.hurt()
                        # calling above function but tailoring it to the Alien
                        hurt_sound.play()
                        score = score + 1
                        Shots.pop(Shots.index(Shot))# deleting the bullet once hit

        for Shot in Shots:
            if Villain.visable == True:
                if Shot.y - Shot.Radius < Villain.HitBox[1] + Villain.HitBox[3] and Shot.y + Shot.Radius > Villain.HitBox[1]:
                    # check to see if bullet is in the same y coordinate checking the top of bullet
                    if Shot.x + Shot.Radius > Villain.HitBox [0] and Shot.x - Shot.Radius < Villain.HitBox[0] + Villain.HitBox[2]:
                        # until, [0] which is our x coord, this mean we are on the right side of the left side of the rectangle
                        Villain.hurt()
                        # calling above function but tailoring it to the Alien
                        hurt_sound.play()
                        score = score + 1
                        Shots.pop(Shots.index(Shot))
                    
            if Shot.x < 500 and Shot.x > 0:
    # making the bullets vanish when reach end of screen rather than going on forever which may make program crash
                Shot.x += Shot.Velocity

            else:
                Shots.pop(Shots.index(Shot))
                 
         
    # events i.e. if i move the mouse or click a button on they keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # hit the red x in corner
                RunProgram = False # program is no longer running

                
    #don't use events for const movement as events only happen once
        KeyboardButtons = pygame.key.get_pressed()

        if KeyboardButtons[pygame.K_SPACE] and Shooting ==0:
            # shoting sets a basic timer so that multiple hots aren't being fired at once (see 'for shots' section)
            beam_sound.play()
            if Bob.Left:
                Facing = -1
            else:
                Facing = 1
            if len(Shots)< 3:
                # divide by 2 so bullet comes from middle of character, not from left or right side, 6 is the radius
                Shots.append(Beam(round(Bob.x + Bob.Width //2), round(Bob.y + Bob.Height//2), 6, (255,0,0), Facing))
                #redefining the properties of the beam
            Shooting = 1

                
        if KeyboardButtons[pygame.K_LEFT]and Bob.x > Bob.Speed:
            #since then we have removed the global variables and put \n\ the attriutes in a def init
            #so add 'Bob.' because that stores the info of where character is at the start of game
            Bob.x-= Bob.Speed
            Bob.Left = True
            Bob.Right = False
            Bob.Standing = False
        elif KeyboardButtons[pygame.K_RIGHT]and Bob.x < screenwidth - Bob.Width - Bob.Speed: # x<screenwidth will stop the character from going off screen, - width so we can still see the character
            Bob.x+= Bob.Speed
            Bob.Left = False
            Bob.Right = True
            Bob.Standing = False
        else:
            Bob.Standing = True
            Bob.WalkCount = 0
            
        if not(Bob.Jumping): # we don't want to be enable up or down when jumping
            if KeyboardButtons[pygame.K_UP]:
                Bob.Jumping = True
                Bob.Right = False
                Bob.Left = False
                Bob.WalkCount = 0
        else:
            if Bob.JumpFar >= -10:
                Negative = 1
                if Bob.JumpFar <0:
                    Negative = -1
                Bob.y -= (Bob.JumpFar ** 2)/2 * Negative #**2 means squared, divide by 2 after so we don't get a huge jump upwards, /2 so we move up, *Negative so we can move down
                Bob.JumpFar -= 1 # by 1 because we slowly move down, this can be changed
            else:
                Bob.Jumping = False
                Bob.JumpFar = 10

        Redraw_Game_Window()
        
    pygame.quit() # closes the program down
    #ambar was here

def rules():
    win = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Story window")

    run = True

    while run:
        pygame.time.delay(100)

    #if player choses to leave game they can exit as normal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    #once the player has understood the rules, they opt to press spacebar
    #this shuts the story window and will then open the next window
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            run = False

        win.fill((127,127,127))

        storyA = "ATTENTION:"
        storyB = """The jungle you and your team have been 
    exploring has been infected by a virus. 
    This virus only impacts men..."""
        storyC = """The virus is getting out of hand and has 
    made all the men hostile."""
        storyD = """Fortunatly, HQ have sent over a vaccine!
    (About time...)"""
        storyE  = """You, a female, need to stop your team from
    hurting you until the vaccine gets to them."""
        storyF = """ The countdown is on. Which will run out first,
    the timer, or your health?"""
        storyG = """PRESS SPACE TO CONTINUE """
        TextFont = pygame.font.SysFont('arial', 10, True)
        text = TextFont.render(storyA, 1, (255,255,255))
        win.blit(text, (250 - (text.get_width()/2),50))

        text = TextFont.render(storyB, 1, (255,255,255))
        win.blit(text, (250 - (text.get_width()/2),100))

        text = TextFont.render(storyC, 1, (255,255,255))
        win.blit(text, (250 - (text.get_width()/2),150))

        text = TextFont.render(storyD, 1, (255,255,255))
        win.blit(text, (250 - (text.get_width()/2),200))

        text = TextFont.render(storyE, 1, (255,255,255))
        win.blit(text, (250 - (text.get_width()/2),250))

        text = TextFont.render(storyF, 1, (255,255,255))
        win.blit(text, (250 - (text.get_width()/2),300))

        text = TextFont.render(storyG, 1, (255,255,255))
        win.blit(text, (250 - (text.get_width()/2),350))
        #the above puts the etxt in the middle
        pygame.display.update()

    pygame.quit()
    game()
    
def make_account():

    #before a user will be able to make an account, the managers of explore learning would need to give permission
    #Permission can only be given by the two of explore's manager's via their employee code.
    codex = input("Enter manager's employee code to proceed:")
    if codex == "78356" or "13576":
        next_steps()
    elif codex != "78356" or "13576": # its not registering this for some reason
        #quit("Invalid code. Goodbye")
        #sys.exit("Invalid code. Goodbye")
        print("Invalid code. Goodbye")
        exit()
        

def next_steps():
    # The program is collecting data regarding the player
    # This will help create a username
    # It will also allow the program to tailor the game towards the player itself
    # i.e. The difficulty of the game's questions and time allowed
    forename = input("Please enter player's forename:")
    surname = input("Please enter player's surname:")
    birth_year = int(input("Please enter player's full year of birth:"))
    time = int(input("Please enter the time limit (seconds) for the player:"))
    level = input("What level? KS1, KS2 OR KS3")

    #creating a username by manipulainng the strings using the information already given
    username = forename + surname + str(birth_year)
    print ("\n\
Player's username:" , username)

    password = input("\n\
Please enter new password:")
    password_Verification = input("Please re-enter password:")

#This loop here makes sure that the password is the same both times
#If both passwords are not the same, it will keep asking to re-fill unitl they both match
    while password != password_Verification:
        print("\n\
Passwords don't match. Please re-enter password:")
        password = input("Please enter new password:")
        password_Verification = input("Please re-enter password:")
    
#This print statement is the confirmation that the sign up has been sucsessfull
    byeeee = input("\n\
Thank you for signing up. Please re-load page to log in.")
    quit()

#creating/opening a file using the append mode to store the names of the users
#Every row will have a detail about the player in the order username, password ect.
#Appending so it just adds extra detail about they player or creates a new record if no details exist.
    with open ("UserDetails.csv" , "a" , newline="")as UserInfo:
        UserInfoWriter = csv.writer(UserInfo)
        UserInfoWriter.writerow([username, password,surname,forename,birth_year,time,level,score])
    UserInfo.close()

    return username
    return score




def Menu (): # code starts here

# The menu will introduce the player to the program by taking login details
    welcome = """Time Blitz: 2021

Let's see what you've got.

First, the boring stuff...
"""
    
    #Due to this part here, The code will print the welcome with a type writing effect
    #It will do so, character by character rather than all at once
    #The time.sleep function will determine the writing speed.
    for char in welcome:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
   
    haveaccount = input("Do you already have an account with us?").lower()

    if haveaccount == "yes":
        print("\n\
Great, We need your username and password:")
        #Unfortunantly I was unable to use the getpass module to hide my password as my device hasn't got the resources
        #However, if i did, it would be written like this:
        #password = getpass.getpass("Enter passowrd")
        username = input("\n\
Please enter username:")
        password = input("Please enter password:")

    # checking that player is an authenticated player by reading the lines in the external CSV file

        StoreUserDetails = []
        with open ("UserDetails.csv", "r" , newline="") as UserInfo:
            person  = csv.reader(UserInfo)
            
            #Here, the program is writing details 
            for row in person:
                personA = row[0]
                StoreUserDetails.append(personA)
        UserInfo.close()
            
        if username in StoreUserDetails: # it won't let me in irregardless
            
            print("Great. You're all set up!")
            rules()
            #make a call to the subrountine where the game is played 

        else:
            byeeee = input("\n\
Thats not an authenticated user. Please reload page.")
            exit()
            
    #providing user with option to sign up should they want to make an account
    # if yes, it jumps to the subroutine that makes accounts
    else:
        sign_up = input("Would you like to sign up?").lower()
        if sign_up == "yes":
            make_account()

        else:
            byeee = input("Not a problem, have a good day.")
            exit()

Menu()


