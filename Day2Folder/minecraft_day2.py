# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER


def teleport():
    agent.teleport_to_player()
player.on_chat("tp", teleport)

def turnleft():
    agent.turn(LEFT)
player.on_chat("tl", turnleft)

def turnright():
    agent.turn(RIGHT)
player.on_chat("tr", turnright)

def moveUp(steps):
    agent.move(UP, steps)
player.on_chat("up", moveUp)

def mvdown(steps):
    agent.move(DOWN, steps)
player.on_chat("down", mvdown)

def moveFw(steps):
    agent.move(FORWARD, steps)
player.on_chat("fwd", moveFw)

def moveBk(steps):
    agent.move(BACK, steps)
player.on_chat("bk", moveBk)

def move1():
    agent.move(FORWARD, 4)
    agent.move(LEFT, 4)
    agent.move(FORWARD, 3)

player.on_chat("obby1", move1)


def chop(height):
    for count in range(height):
        agent.destroy(UP)
        agent.destroy(FORWARD)
        agent.move(UP, 1)
        agent.collect_all()
player.on_chat("chop", chop)