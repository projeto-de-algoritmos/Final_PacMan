from pygame import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP,K_DOWN
from pygame import mouse
from config import screen, board, player_movement, player

def treats_event(event) -> bool:
    """treats pygame events
            Parameters:
                    event (Event): pygame event
            Returns:
                    True (bool): quit game
                    False (bool): stay playing
    """
    def player_control(keys) -> None:
        for key, x, y in keys:
            if event.key == key:
                player.control(x, y)

    if event.type == QUIT:
        return True
    elif event.type == MOUSEBUTTONDOWN:
        x, y = mouse.get_pos()
    elif event.type == KEYDOWN:
        key_down = [(K_LEFT, -player_movement, 0),
                    (K_RIGHT, player_movement, 0),
                    (K_UP, 0, -player_movement),
                    (K_DOWN, 0, player_movement)]
        player_control(key_down)
    elif event.type == KEYUP:
        key_up = [(K_LEFT, player_movement, 0),
                (K_RIGHT, -player_movement, 0),
                (K_UP, 0, player_movement),
                (K_DOWN, 0, -player_movement)]
        player_control(key_up)

    return False