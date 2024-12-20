import pgzrun,random
TITLE="Alien Shooter"
WIDTH=800
HEIGHT=500
message=""
alien=Actor("alien1")
alien.pos=400,250
def draw():
    screen.clear()
    screen.blit("backgroundspace",(0,-100))
    screen.draw.text(message,(700,0))
    alien.draw()

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        alien.x=random.randint(100,700)
        alien.y=random.randint(100,400)
        message="Good Shot!:)"
    else:
        message="Bad Shot!:("

pgzrun.go()