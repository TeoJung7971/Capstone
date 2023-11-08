import pygame as pg

#Initializing Game Engine
pg.init()

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

# Set the height and width of the screen
size   = [1280, 720]
screen = pg.display.set_mode(size)

#Background image
background = pg.image.load("SCENE1.png")
  
pg.display.set_caption("Capstone Project")
  
#Loop until the user clicks the close button.
done = False
clock = pg.time.Clock()

# Font 객체 생성
myFont = pg.font.SysFont( "arial", 30, True, False)        

# Text를 surface에 그리기, 안티알리어싱, 검은색
text_Title= myFont.render("Pygame Text Test", True, WHITE)
     

while not done:
  
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    #FPS 설정 보통 10, 30, 60 중 하나를 택함: 클수록 CPU 사용량 증가
    clock.tick(10)
     
    # Main Event Loop
    for event in pg.event.get(): # User did something
        if event.type == pg.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
  
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
      
    # Clear the screen and set the screen background
    screen.fill(BLACK)
 
    '''
    Your Work.....
    '''
    # 6 - draw the screen elements
    screen.blit(background, (0,0))

    # 7 - update the screen
    pg.display.flip()

    # 8 - loop through the events
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_e:

                screen.fill(BLACK)


                # Rect 생성

                text_Rect = text_Title.get_rect()

            

                # 가로 가운데, 세로 50 위치

                text_Rect.centerx = round(size[0] / 2)

                text_Rect.y = 50

            

                # Text Surface SCREEN에 복사하기, Rect 사용

                screen.blit(text_Title, text_Rect)
            

                # 작업한 스크린의 내용을 갱신하기

                pg.display.flip()


                # 1초에 60번의 빈도로 순환하기

                clock.tick(60)

                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_r:

                            background = pg.image.load("SCENE2.png")

        # check if the event is the X button 
        if event.type==pg.QUIT:
            # if it is quit the game
            pg.quit() 
            exit(0)
    # pg.draw.polygon(screen, GREEN, [[30, 150], [125, 100], [220, 150]], 5)
    # pg.draw.polygon(screen, GREEN, [[30, 150], [125, 100], [220, 150]], 0)
    # pg.draw.lines(screen, RED, False, [[50, 150], [50, 250], [200, 250], [200, 150]], 5)
    # pg.draw.rect(screen, BLACK, [75, 175, 75, 50], 5)
    # pg.draw.rect(screen, BLUE, [75, 175, 75, 50], 0)
    # pg.draw.line(screen, BLACK, [112, 175], [112, 225], 5)
    # pg.draw.line(screen, BLACK, [75, 200], [150, 200], 5)
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pg.display.flip()