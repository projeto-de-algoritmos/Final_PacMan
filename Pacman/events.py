from pygame import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame import mouse

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
    return False