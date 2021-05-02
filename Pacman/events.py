from pygame import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP,K_DOWN
from pygame import mouse
from config import screen, board, movement, player

def treats_event(event) -> bool:
    """treats pygame events
            Parameters:
                    event (Event): pygame event
            Returns:
                    True (bool): quit game
                    False (bool): stay playing
    """
    if event.type == QUIT:
        return True
    elif event.type == MOUSEBUTTONDOWN:
        x, y = mouse.get_pos()
    elif event.type == KEYDOWN:
        if event.key == K_LEFT:
            player.control(-movement,0)
        if event.key == K_RIGHT:
            player.control(movement,0)
        if event.key == K_UP:
            player.control(0,-movement)
        if event.key == K_DOWN:
            player.control(0,movement)
    elif event.type == KEYUP:
        if event.key == K_LEFT:
            player.control(movement,0)
        if event.key == K_RIGHT:
            player.control(-movement,0)
        if event.key == K_UP:
            player.control(0,movement)
        if event.key == K_DOWN:
            player.control(0,-movement)

    return False