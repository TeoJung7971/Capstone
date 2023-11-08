import pygame
from pygame import mixer
from music import playsound, playmusic, stopmusic, getmixerargs, initMixer

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

scene_counter = 0

#Screen Size
size_width = 1280
size_height = 720

win_wid_cen = size_width / 2 - 100
win_hei_cen = size_height / 2 -40

size   = [1280, 720]
size_ver = [720, 1280]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Capstone Project")

background = pygame.image.load("BLACK_BACKGROUND.png")

SCENE1 = pygame.image.load("SCENE1.png")

SCENE2 = pygame.image.load("SCENE2.png")

FACE1 = pygame.image.load("FACE1.jpeg")

FACE2 = pygame.image.load("FACE2.png")

done = False

clock = pygame.time.Clock()


# myFont = pygame.font.SysFont( "arial", 30, True, False)        
# text_Title= myFont.render("Pygame Text Test", True, WHITE)

# def ct(font, size, text, color):
#     mf = pygame.font.Font(font, size)

#     t = mf.render(text, True, color)

#     return t 

def ct(size, text, color):
    mf = pygame.font.SysFont("arial", size, True, False)

    t = mf.render(text, True, color)

    return t 


def draw_scene1():
    #print("This is Scene 1")
    txt = ct(40, "Hello Everyone!", BLACK)
    screen.blit(txt, (win_wid_cen,win_hei_cen))


def draw_scene2():
    #print("This is scene 2")
    txt2 = ct(40, "Now we Start!", BLACK)
    screen.blit(txt2, (win_wid_cen,win_hei_cen))

# try:
#     initMixer()
#     filename = 'MUSIC_DEMO.mp3'
#     playmusic(filename)

# except KeyboardInterrupt:   # to stop playing, press "ctrl-c"
#     stopmusic()
#     print("\nPlay Stopped by user")

# except Exception:
#     print("unknown error")

mixer.init()
mixer.music.load('MUSIC_DEMO.mp3')
mixer.music.play()

while not done:

    clock.tick(30)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

        elif event.type == pygame.MOUSEBUTTONDOWN:
            scene_counter += 1

    screen.fill(WHITE)

    if scene_counter == 0:
        draw_scene1()
    elif scene_counter == 1:
        draw_scene2()
    elif scene_counter == 2:
        screen.blit(SCENE1, (0,0))
        screen.blit(FACE1, (400,0))
    elif scene_counter == 3:
        screen.blit(SCENE2, (0,0))
        screen.blit(FACE2, (515, 90))
        txt2 = ct(20, "I'm totally COLLAPSED", WHITE)
        screen.blit(txt2, (180,510))
    elif scene_counter > 3:
        scene_counter = 0

    pygame.display.update()

pygame.QUIT