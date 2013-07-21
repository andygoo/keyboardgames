#!/usr/bin/env python

import threading
import pygame

stop_event = threading.Event()


def init_screen():
    (width, height) = pygame.display.list_modes(0, pygame.FULLSCREEN)[0]
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    pygame.display.set_caption("Keyboard Fun!")
    return screen, width, height


def main():
    pygame.init()

    clock = pygame.time.Clock()
    fps = 30
    y = 0
    dir = 1
    running = 1

    screen, width, height = init_screen()

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250,250,250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello world!", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0,0))
    pygame.display.flip()


    linecolor = 255, 0, 0
    bgcolor = 250,250,250
    #pygame.draw.line(screen, (0, 0, 255), (0, 0), (200, 100))

    # Event loop
    while not stop_event.isSet():
        tick = clock.tick(fps)
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop_event.set()
                    print "pygame.QUIT" + stop_event.isSet()
                elif event.type == pygame.KEYDOWN:
                    parse_key(event.key)


            #screen.fill(bgcolor)
            pygame.draw.line(background, bgcolor, (0, y), (width-1, y))

            y += dir
            if y == 0 or y == height-1: dir *= -1
            pygame.draw.line(background, linecolor, (0, y), (width-1, y))
            screen.blit(background, (0,0))

            pygame.display.flip()
            #screen.blit(background, (0,0))
            #pygame.display.flip()
        except KeyboardInterrupt:
            stop_event.set()
    pygame.quit()


def parse_key(key):
    pressed = pygame.key.get_pressed()

    if (pressed[pygame.K_RCTRL] or pressed[pygame.K_LCTRL]) and \
            pressed[pygame.K_c]:
        stop_event.set()


if __name__=='__main__':
    main()


