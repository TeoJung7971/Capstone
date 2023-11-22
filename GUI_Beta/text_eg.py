import pygame

line_space = 16
basicfont = pygame.font.SysFont('MorePerfectDOSVGA', 16)

def text_ani(str, tuple):
    x, y = tuple
    y = y*line_space ##shift text down by one line
    char = ''        ##new string that will take text one char at a time. Not the best variable name I know.
    letter = 0
    count = 0
    for i in range(len(str)):
        pygame.event.clear() ## this is very important if your event queue is not handled properly elsewhere. Alternativly pygame.event.pump() would work.
        time.sleep(0.05) ##change this for faster or slower text animation
        char = char + str[letter]
        text = basicfont.render(char, False, (2, 241, 16), (0, 0, 0)) #First tuple is text color, second tuple is background color
        textrect = text.get_rect(topleft=(x, y)) ## x, y's provided in function call. y coordinate amended by line height where needed
        screen.blit(text, textrect)
        pygame.display.update(textrect) ## update only the text just added without removing previous lines.
        count += 1
        letter += 1


text_ani('this is line number 1 ', (0, 1)) # text string and x, y coordinate tuple.
text_ani('this is line number 2', (0, 2))
text_ani('this is line number 3', (0, 3))
text_ani('', (0, 3)) # this is a blank line