import time

# Default values
a1 = '#'
a2 = '#'
a3 = '#'
a4 = '#'
b1 = '#'
b2 = '#'
b3 = '#'
b4 = '#'
c1 = '#'
c2 = '#'
c3 = '#'
c4 = '#'
d1 = '#'
d2 = '#'
d3 = '#'
d4 = '#'
e1 = '#'
e2 = '#'
e3 = '#'
e4 = '#'
f1 = '#'
f2 = '#'
f3 = '#'
f4 = '#'
g1 = '#'
g2 = 'F'
g3 = '#'
g4 = '#'
h1 = 'A'
h2 = 'A'
h3 = 'A'
h4 = 'A'
fugitive = ''


# Players array to make movement easier
movable_slots = [
        [a1,a2,a3,a4],
        [b1,b2,b3,b4],
        [c1,c2,c3,c4],
        [d1,d2,d3,d4],
        [e1,e2,e3,e4],
        [f1,f2,f3,f4],
        [g1,g2,g3,g4],
        [h1,h2,h3,h4]
    ]

# Reset board
def resetBoard():
    global movable_slots

    a1 = '#'
    a2 = '#'
    a3 = '#'
    a4 = '#'
    b1 = '#'
    b2 = '#'
    b3 = '#'
    b4 = '#'
    c1 = '#'
    c2 = '#'
    c3 = '#'
    c4 = '#'
    d1 = '#'
    d2 = '#'
    d3 = '#'
    d4 = '#'
    e1 = '#'
    e2 = '#'
    e3 = '#'
    e4 = '#'
    f1 = '#'
    f2 = '#'
    f3 = '#'
    f4 = '#'
    g1 = '#'
    g2 = 'F'
    g3 = '#'
    g4 = '#'
    h1 = 'A'
    h2 = 'A'
    h3 = 'A'
    h4 = 'A'

    movable_slots = [
        [a1,a2,a3,a4],
        [b1,b2,b3,b4],
        [c1,c2,c3,c4],
        [d1,d2,d3,d4],
        [e1,e2,e3,e4],
        [f1,f2,f3,f4],
        [g1,g2,g3,g4],
        [h1,h2,h3,h4]
    ]



# Keep track of fugitive / agent
def return_var_name(variable):
 for name in globals():
     if eval(name) == variable:
        return name


# Get fugitive variable
def get_fugitive_position():
    global fugitive
    global movable_slots
    for row in movable_slots:
        for item in row:
            if item == 'F':
                fugitive = return_var_name(item)
    return fugitive



# Fugitive move left forward
def move_fugitive_forward_left():
    global movable_slots
    for r in range(len(movable_slots)):
        for c in range(len(movable_slots[r])):
            # print(movable_slots[r][c])
            if movable_slots[r][c] == 'F':
                fugitive = return_var_name(movable_slots[r][c])
                # row = r
                # col = c
    if fugitive in ('a1', 'a2', 'a3', 'a4'):
        return None
    elif fugitive in ('b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'):
        return None
    else:
        # Assigning fugitive value as variable and changing it to #
        vars()[fugitive] = "#"
        # exec("%s = '%s'" % (fugitive,'#'))
        left = fugitive[0]
        right = fugitive[1]
        # Decrease variable letter by 1 i.e: a + 1 = b
        new_fugitive = chr(ord(left) - 1) + right
        vars()[new_fugitive] = "F"
        # exec("%s = '%s'" % (new_fugitive,'F'))

        print(fugitive)
        print(vars()[fugitive])
        print(vars())
        print(g2)
        

        # print(new_fugitive)
        # print(f2)
        # print(left)
        # print(right)
        
        # movable_slots[row][col] = '#'
        # movable_slots[new_row][new_col] = 'F'

        # draw_board()


# To generate the board after every move
def draw_board():
    global movable_slots

    bp = {}

    varl = 'a'
    varn = '1'
    for i in movable_slots:
        for t in i:
            # print(varl+varn)
            # print(t)
            bp[varl+varn] = t
            varn = str(int(varn) + 1)
        # Increase variable letter by 1 i.e: a + 1 = b
        varl = chr(ord(varl) + 1)
        varn = '1'

    board = [
        ['_',bp['a1'],'_',bp['a2'],'_',bp['a3'],'_',bp['a4']],
        [bp['b1'],'_',bp['b2'],'_',bp['b3'],'_',bp['b4'],'_'],
        ['_',bp['c1'],'_',bp['c2'],'_',bp['c3'],'_',bp['c4']],
        [bp['d1'],'_',bp['d2'],'_',bp['d3'],'_',bp['d4'],'_'],
        ['_',bp['e1'],'_',bp['e2'],'_',bp['e3'],'_',bp['e4']],
        [bp['f1'],'_',bp['f2'],'_',bp['f3'],'_',bp['f4'],'_'],
        ['_',bp['g1'],'_',bp['g2'],'_',bp['g3'],'_',bp['g4']],
        [bp['h1'],'_',bp['h2'],'_',bp['h3'],'_',bp['h4'],'_']
    ]
    for row in board:
        for item in row:
            print('|', item, end=' ')
        print('|', end=' ')
        print()





# Main code

# draw_board()
# move_fugitive_forward_left()
# time.sleep(4)
# print('\n')
# draw_board()

# print(get_fugitive_position())
move_fugitive_forward_left()
# resetBoard()
draw_board()

# food = 'bread'

# vars()[food] = 123123

# print(bread) 