from pygame import init as i, display, FULLSCREEN

i()
screen     =    display.set_mode(flags=FULLSCREEN)
deminsions =    [screen.get_width(), screen.get_height()]
x = True