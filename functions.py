import random, pygame



class Block:
    def __init__(self, size,state,pos,color):
        self.state = state
        self.size = size
        self.pos = pos
        self.color = color


def rand(block):
    availble = []
    list = [2,4]
    flag = 0
    for i in range(len(block)):
        if block[i].state == 0:
            availble.append(i)
            flag = 1
    if flag == 1:
        i = random.choice(availble)
        block[i].size = random.choice(list)
        block[i].state = 1


def txtToScreen(txt, pos, size, display, color=(0, 0, 0), centered=True, limiter=0):
    font = pygame.font.SysFont(None, size)
    if limiter != 0:
        newtxt = txt[0: limiter]
    else:
        newtxt = txt
    show = font.render(newtxt, True, color)
    if centered:
        new_pos = [pos[0] - show.get_width() // 2, pos[1] - show.get_height() / 2]
    else:
        new_pos = pos
    display.blit(show, new_pos)



def up(block,score):
    old_block = []
    new_block = []
    for i in range(len(block)):
        old_block.append(block[i].size)
    move_up(block)
    score = merge_up(block,score)
    move_up(block)
    for i in range(len(block)):
        new_block.append(block[i].size)
    if new_block != old_block:
        rand(block)
    return block,score
def move_up(block):
    for j in range(3):
        for i in range(len(block)):
            if i not in {0,1,2,3}:
                if block[i-4].state == 0 and block[i].state == 1 and block[i-4].size == 0:
                    block[i-4].state = 1
                    block[i-4].size = block[i].size
                    block[i].size = 0
                    block[i].state = 0
def merge_up(block,score):
        for i in range(len(block)):
            if i not in {0,1,2,3}:
                if block[i-4].size == block[i].size and block[i-4].state == 1:
                    block[i].size = 0
                    block[i].state = 0
                    block[i-4].size *= 2
                    score += block[i-4].size
        return score


def down(block,score):
    old_block = []
    new_block = []
    for i in range(len(block)):
        old_block.append(block[i].size)
    move_down(block)
    score = merge_down(block,score)
    move_down(block)
    for i in range(len(block)):
        new_block.append(block[i].size)
    if new_block != old_block:
        rand(block)
    return block,score
def move_down(block):
    for j in range(3):
        for i in reversed(range(len(block))):
            if i not in {12,13,14,15}:
                if block[i+4].state == 0 and block[i].state == 1:
                    block[i+4].state = 1
                    block[i+4].size = block[i].size
                    block[i].size = 0
                    block[i].state = 0 
def merge_down(block,score):
    for i in reversed(range(len(block))):
        if i not in {12,13,14,15}:
            if block[i+4].size == block[i].size and block[i+4].state == 1:
                block[i].size = 0
                block[i].state = 0
                block[i+4].size *= 2
                score += block[i+4].size
    return score


def right(block,score):
    old_block = []
    new_block = []
    for i in range(len(block)):
        old_block.append(block[i].size)
    move_right(block)
    score = merge_right(block,score)
    move_right(block)
    for i in range(len(block)):
        new_block.append(block[i].size)
    if new_block != old_block:
        rand(block)
    return block,score
def move_right(block):
    for _ in range(4):
        for i in reversed(range(len(block))):
            if i not in {3,7,11,15}:
                if block[i+1].state == 0 and block[i].state == 1:
                    block[i+1].state = 1
                    block[i+1].size = block[i].size
                    block[i].size = 0
                    block[i].state = 0
def merge_right(block,score):
    for i in reversed(range(len(block))):
        if i not in {3,7,11,15}:
            if block[i+1].size == block[i].size:
                block[i].size = 0
                block[i].state = 0
                block[i+1].size *= 2
                score += block[i+1].size
    return score

def left(block,score):
    old_block = []
    new_block = []
    for i in range(len(block)):
        old_block.append(block[i].size)
    move_left(block)
    score = merge_left(block,score)
    move_left(block)
    for i in range(len(block)):
         new_block.append(block[i].size)
    if new_block != old_block:
        rand(block)
    return block,score
def move_left(block):
    for _ in range(4):
        for i in range(len(block)):
            if i not in {0,4,8,12}:
                if block[i-1].state == 0 and block[i].state == 1:
                    block[i-1].state = 1
                    block[i-1].size = block[i].size
                    block[i].size = 0
                    block[i].state = 0                   
def merge_left(block,score):
    for i in range(len(block)):
        if i not in {0,4,8,12}:
            if block[i-1].size == block[i].size:
                block[i].size = 0
                block[i].state = 0
                block[i-1].size *= 2
                score += block[i-1].size
    return score
    

def set_pos(block):
     block[0].pos[0] = 105
     block[0].pos[1] = 109
     block[1].pos[0] = 203
     block[1].pos[1] = 109
     block[2].pos[0] = 302
     block[2].pos[1] = 109
     block[3].pos[0] = 401
     block[3].pos[1] = 109
     block[4].pos[0] = 105
     block[4].pos[1] = 208
     block[5].pos[0] = 203
     block[5].pos[1] = 208
     block[6].pos[0] = 302
     block[6].pos[1] = 208
     block[7].pos[0] = 401
     block[7].pos[1] = 208
     block[8].pos[0] = 105
     block[8].pos[1] = 306
     block[9].pos[0] = 203
     block[9].pos[1] = 306
     block[10].pos[0] = 302
     block[10].pos[1] = 306
     block[11].pos[0] = 401
     block[11].pos[1] = 306
     block[12].pos[0] = 105
     block[12].pos[1] = 405
     block[13].pos[0] = 203
     block[13].pos[1] = 405
     block[14].pos[0] = 302
     block[14].pos[1] = 405
     block[15].pos[0] = 401
     block[15].pos[1] = 405
     return block