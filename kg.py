#!/usr/bin/env python

import random
import threading
import pygame

stop_event = threading.Event()
font = None
lettercolor = 255, 0, 0
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ltrs = {}


class letter:

    def __init__(self, character, canvas):
        pygame.init()
        self.fontsize = 10
        self.char = character
        self.canvas = canvas

    def update(self):
        if self.fontsize < 1000:
            self.fontsize = int(self.fontsize*1.15)
        self.font = pygame.font.Font(None, self.fontsize)
        self.l = self.font.render(self.char, 1, lettercolor)
        textpos = self.l.get_rect()
        textpos.centerx = self.canvas.get_rect().centerx
        textpos.centery = self.canvas.get_rect().centery
        self.x = textpos[0]
        self.y = textpos[1]

    def reset(self):
        self.fontsize = 10


def init_screen():
    (width, height) = pygame.display.list_modes(0, pygame.FULLSCREEN)[0]
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    pygame.display.set_caption("Keyboard Fun!")
    return screen, width, height


def main():
    pygame.init()
    clock = pygame.time.Clock()

    fps = 30
    bgcolor = 250,250,250
    dirty_rects = []

    # Set full-screen display
    screen, width, height = init_screen()

    # Load images
    background = pygame.image.load("bg.jpg")
    background = background.convert()

    # Drawing canvas
    canvas = pygame.Surface(screen.get_size())
    canvas = canvas.convert()
    canvas.fill(bgcolor)
    screen.blit(canvas, (0,0))

    # Define all the letter objects
    for i in list(characters):
        ltrs[i] = letter(i, canvas)
    random_ltr = pick_random_char()
    
    # Event loop
    while not stop_event.isSet():
        tick = clock.tick(fps)
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop_event.set()
                    print "pygame.QUIT" + stop_event.isSet()
                elif event.type == pygame.KEYDOWN:
                    keypress = parse_key(event.key)
                    if keypress:
                        new_ltr = manage_keypress(keypress, random_ltr.char)
                        if new_ltr:
                            random_ltr.reset()
                            random_ltr = pick_random_char(random_ltr.char)
       
            # Do animations
            random_ltr.update() 

            # Capture dirty portion of screen
            dirty = canvas.subsurface(random_ltr.l.get_rect())
            screen.blit(dirty, (random_ltr.x, random_ltr.y))

            # draw entities
            screen.blit(background, (0,0))
            screen.blit(random_ltr.l, (random_ltr.x,random_ltr.y))

            # flip to display
            pygame.display.update(dirty.get_rect())

        except KeyboardInterrupt:
            stop_event.set()
    pygame.quit()


def pick_random_char(lastchar=None):
    """ Ensures the same letter is not picked twice in a row """
    newrandomletter = random.randint(0,25)
    if lastchar:
        while list(characters)[newrandomletter] == lastchar:
            newrandomletter = random.randint(0,25)
    random_ltr = ltrs[list(characters)[newrandomletter]]
    return random_ltr


def manage_keypress(keypress, letter_on_screen):
    """ determine whether the key pressed matches the screen """
    if keypress==letter_on_screen:
        # play "you did it! You chose Y!" and choose another char
        return True
    else:
        # play "That's an X" or "you chose X"
        # play "find the Y"
        return False


def parse_key(key):
    pressed = pygame.key.get_pressed()

    if (pressed[pygame.K_RCTRL] or pressed[pygame.K_LCTRL]) and \
            pressed[pygame.K_c]:
        stop_event.set()

    if (pressed[pygame.K_a]): return "A"
    if (pressed[pygame.K_b]): return "B"
    if (pressed[pygame.K_c]): return "C"
    if (pressed[pygame.K_d]): return "D"
    if (pressed[pygame.K_e]): return "E"
    if (pressed[pygame.K_f]): return "F"
    if (pressed[pygame.K_g]): return "G"
    if (pressed[pygame.K_h]): return "H"
    if (pressed[pygame.K_i]): return "I"
    if (pressed[pygame.K_j]): return "J"
    if (pressed[pygame.K_k]): return "K"
    if (pressed[pygame.K_l]): return "L"
    if (pressed[pygame.K_m]): return "M"
    if (pressed[pygame.K_n]): return "N"
    if (pressed[pygame.K_o]): return "O"
    if (pressed[pygame.K_p]): return "P"
    if (pressed[pygame.K_q]): return "Q"
    if (pressed[pygame.K_r]): return "R"
    if (pressed[pygame.K_s]): return "S"
    if (pressed[pygame.K_t]): return "T"
    if (pressed[pygame.K_u]): return "U"
    if (pressed[pygame.K_v]): return "V"
    if (pressed[pygame.K_w]): return "W"
    if (pressed[pygame.K_x]): return "X"
    if (pressed[pygame.K_y]): return "Y"
    if (pressed[pygame.K_z]): return "Z"

    return None

if __name__=='__main__':
    main()


