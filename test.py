import sys
import random

class Game():
    def __init__(self):
        # Default values
        self.fugitive = {'row' : 6, 'col' : 1}
        self.agent1 = {'row' : 7, 'col' : 0}
        self.agent2 = {'row' : 7, 'col' : 1}
        self.agent3 = {'row' : 7, 'col' : 2}
        self.agent4 = {'row' : 7, 'col' : 3}
        self.current_agent = '1'
        self.posible_fugitive_moves = []
        self.posible_agent_moves = []

        # Players array to make movement easier
        self.movable_slots = [
                ['#','#','#','#'],
                ['#','#','#','#'],
                ['#','#','#','#'],
                ['#','#','#','#'],
                ['#','#','#','#'],
                ['#','#','#','#'],
                ['#','F','#','#'],
                ['A','A','A','A']
            ]

    # Reset board
    def resetBoard(self):
        self.movable_slots

        self.movable_slots = [
            ['#','#','#','#'],
            ['#','#','#','#'],
            ['#','#','#','#'],
            ['#','#','#','#'],
            ['#','#','#','#'],
            ['#','#','#','#'],
            ['#','F','#','#'],
            ['A','A','A','A']
        ]

    # To generate the board after every move
    def draw_board(self):
        self.movable_slots

        bp = {}

        varl = 'a'
        varn = '1'
        for i in self.movable_slots:
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
        print('\n')

    # Function to check if an array contains only one element type
    def uniqueElement(self, arr, n):   
        # Create a set
        s = set(arr)
        # Compare and print the result
        if(len(s) == 1):
            return True
        else:
            return False

    # *********************** FUGITIVE FUNCTIONS **************************

    # Get fugitive variable
    def get_fugitive_position(self):
        self.movable_slots
        position = {}
        for row in range(len(self.movable_slots)):
            for item in range(len(self.movable_slots[row])):
                if self.movable_slots[row][item] == 'F':
                    position['row'] = row
                    position['col'] = item
        return position

    # Fugitive move left forward
    def move_fugitive_forward_left(self):
        
        # Get fugitive position
        position = self.get_fugitive_position()
        self.fugitive = position

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        b1 = {'row' : 1, 'col' : 0}
        # c1 = {'row' : 2, 'col' : 0}
        d1 = {'row' : 3, 'col' : 0}
        # e1 = {'row' : 4, 'col' : 0}
        f1 = {'row' : 5, 'col' : 0}
        # g1 = {'row' : 6, 'col' : 0}


        # Checking if the next step has an agent
        check_position = {}
        if self.fugitive['row'] % 2 == 0:
            check_position['row'] = self.fugitive['row'] - 1
            check_position['col'] = self.fugitive['col']
        else:
            check_position['row'] = self.fugitive['row'] - 1
            check_position['col'] = self.fugitive['col'] - 1


        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,b1,d1,f1):
            return None
        elif check_position in (self.agent1,self.agent2,self.agent3,self.agent4):
            return None
        else:
            # Creating temporary variable to hold current fugitive position
            temp = {}
            temp['row'] = self.fugitive['row']
            temp['col'] = self.fugitive['col']

            # Shifting fugitive to forward left (New fugitive position)
            if self.fugitive['row'] % 2 == 0:
                self.fugitive['row'] = self.fugitive['row'] - 1
                self.fugitive['col'] = self.fugitive['col']
            else:
                self.fugitive['row'] = self.fugitive['row'] - 1
                self.fugitive['col'] = self.fugitive['col'] - 1

            # Replace fugitive position with '#' and new position with fugitive 'F'
            self.movable_slots[temp['row']][temp['col']] = '#'
            self.movable_slots[self.fugitive['row']][self.fugitive['col']] = 'F'

    # Fugitive move right forward
    def move_fugitive_forward_right(self):
        
        # Get fugitive position
        position = self.get_fugitive_position()
        self.fugitive = position

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        # b4 = {'row' : 1, 'col' : 3}
        c4 = {'row' : 2, 'col' : 3}
        # d4 = {'row' : 3, 'col' : 3}
        e4 = {'row' : 4, 'col' : 3}
        # f4 = {'row' : 5, 'col' : 3}
        g4 = {'row' : 6, 'col' : 3}
        # h4 = {'row' : 7, 'col' : 3}

        # Checking if the next step has an agent
        check_position = {}
        if self.fugitive['row'] % 2 == 0:
            check_position['row'] = self.fugitive['row'] - 1
            check_position['col'] = self.fugitive['col'] + 1
        else:
            check_position['row'] = self.fugitive['row'] - 1
            check_position['col'] = self.fugitive['col']

        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,c4,e4,g4):
            return None
        elif check_position in (self.agent1,self.agent2,self.agent3,self.agent4):
            return None
        else:
            # Creating temporary variable to hold current fugitive position
            temp = {}
            temp['row'] = self.fugitive['row']
            temp['col'] = self.fugitive['col']


            # Shifting fugitive to forward left (New fugitive position)
            if self.fugitive['row'] % 2 == 0:
                self.fugitive['row'] = self.fugitive['row'] - 1
                self.fugitive['col'] = self.fugitive['col'] + 1
            else:
                self.fugitive['row'] = self.fugitive['row'] - 1
                self.fugitive['col'] = self.fugitive['col']


            # Replace fugitive position with '#' and new position with fugitive 'F'
            self.movable_slots[temp['row']][temp['col']] = '#'
            self.movable_slots[self.fugitive['row']][self.fugitive['col']] = 'F'

    # Fugitive move left backward
    def move_fugitive_backward_left(self):

        # Get fugitive position
        position = self.get_fugitive_position()
        self.fugitive = position

        # Slots that can't move forward left (forbidden slots)
        h1 = {'row' : 7, 'col' : 0}
        h2 = {'row' : 7, 'col' : 1}
        h3 = {'row' : 7, 'col' : 2}
        h4 = {'row' : 7, 'col' : 3}
        b1 = {'row' : 1, 'col' : 0}
        # c1 = {'row' : 2, 'col' : 0}
        d1 = {'row' : 3, 'col' : 0}
        # e1 = {'row' : 4, 'col' : 0}
        f1 = {'row' : 5, 'col' : 0}
        # g1 = {'row' : 6, 'col' : 0}
        # a1 = {'row' : 0, 'col' : 0}

        # Checking if the next step has an agent
        check_position = {}
        if self.fugitive['row'] % 2 == 0:
            check_position['row'] = self.fugitive['row'] + 1
            check_position['col'] = self.fugitive['col']
        else:
            check_position['row'] = self.fugitive['row'] + 1
            check_position['col'] = self.fugitive['col'] - 1


        # Check if position is in forbidden slots
        if position in (h1,h2,h3,h4,b1,d1,f1):
            return None
        elif check_position in (self.agent1,self.agent2,self.agent3,self.agent4):
            return None
        else:
            # Creating temporary variable to hold current fugitive position
            temp = {}
            temp['row'] = self.fugitive['row']
            temp['col'] = self.fugitive['col']

            # Shifting fugitive to forward left (New fugitive position)
            if self.fugitive['row'] % 2 == 0:
                self.fugitive['row'] = self.fugitive['row'] + 1
                self.fugitive['col'] = self.fugitive['col']
            else:
                self.fugitive['row'] = self.fugitive['row'] + 1
                self.fugitive['col'] = self.fugitive['col'] - 1


            # Replace fugitive position with '#' and new position with fugitive 'F'
            self.movable_slots[temp['row']][temp['col']] = '#'
            self.movable_slots[self.fugitive['row']][self.fugitive['col']] = 'F'

    # Fugitive move right backward
    def move_fugitive_backward_right(self):
        
        # Get fugitive position
        position = self.get_fugitive_position()
        self.fugitive = position

        # Slots that can't move forward left (forbidden slots)
        h1 = {'row' : 7, 'col' : 0}
        h2 = {'row' : 7, 'col' : 1}
        h3 = {'row' : 7, 'col' : 2}
        h4 = {'row' : 7, 'col' : 3}
        # b1 = {'row' : 1, 'col' : 0}
        c4 = {'row' : 2, 'col' : 3}
        # d1 = {'row' : 3, 'col' : 0}
        e4 = {'row' : 4, 'col' : 3}
        # f1 = {'row' : 5, 'col' : 0}
        g4 = {'row' : 6, 'col' : 3}
        a4 = {'row' : 0, 'col' : 3}


        # Checking if the next step has an agent
        check_position = {}
        if self.fugitive['row'] % 2 == 0:
            check_position['row'] = self.fugitive['row'] + 1
            check_position['col'] = self.fugitive['col'] + 1
        else:
            check_position['row'] = self.fugitive['row'] + 1
            check_position['col'] = self.fugitive['col']


        # Check if position is in forbidden slots
        if position in (h1,h2,h3,h4,c4,e4,g4,a4):
            return None
        elif check_position in (self.agent1,self.agent2,self.agent3,self.agent4):
            return None
        else:
            # Creating temporary variable to hold current fugitive position
            temp = {}
            temp['row'] = self.fugitive['row']
            temp['col'] = self.fugitive['col']

            # Shifting fugitive to forward left (New fugitive position)
            if self.fugitive['row'] % 2 == 0:
                self.fugitive['row'] = self.fugitive['row'] + 1
                self.fugitive['col'] = self.fugitive['col'] + 1
            else:
                self.fugitive['row'] = self.fugitive['row'] + 1
                self.fugitive['col'] = self.fugitive['col']

            # Replace fugitive position with '#' and new position with fugitive 'F'
            self.movable_slots[temp['row']][temp['col']] = '#'
            self.movable_slots[self.fugitive['row']][self.fugitive['col']] = 'F'

    # If fugitive moves forward left
    def assume_fugitive_moved_forward_left(self):
        position = self.fugitive

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        b1 = {'row' : 1, 'col' : 0}
        d1 = {'row' : 3, 'col' : 0}
        f1 = {'row' : 5, 'col' : 0}
        h1 = {'row' : 7, 'col' : 0}

        # Checking if the next step has an agent
        check_position = {}
        if self.fugitive['row'] % 2 == 0:
            check_position['row'] = self.fugitive['row'] - 1
            check_position['col'] = self.fugitive['col']
        else:
            check_position['row'] = self.fugitive['row'] - 1
            check_position['col'] = self.fugitive['col'] - 1


        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,b1,d1,f1,h1):
            return 0
        elif check_position in (self.agent1,self.agent2,self.agent3,self.agent4):
            return 0
        # Let's say the fugitive has moved forward left, how many slots are free
        else:
            slots = self._free_fugitive_slots(check_position)
            return slots         

    # If fugitive moves forward right
    def assume_fugitive_moved_forward_right(self):
        position = self.fugitive

        # Slots that can't move forward right (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        c4 = {'row' : 2, 'col' : 3}
        e4 = {'row' : 4, 'col' : 3}
        g4 = {'row' : 6, 'col' : 3}

        # Checking if the next step has an agent
        check_position = {}
        if self.fugitive['row'] % 2 == 0:
            check_position['row'] = self.fugitive['row'] - 1
            check_position['col'] = self.fugitive['col'] + 1
        else:
            check_position['row'] = self.fugitive['row'] - 1
            check_position['col'] = self.fugitive['col']


        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,c4,e4,g4):
            return 0
        elif check_position in (self.agent1,self.agent2,self.agent3,self.agent4):
            return 0
        # Let's say the fugitive has moved forward left, how many slots are free
        else:
            slots = self._free_fugitive_slots(check_position)
            return slots         

    # If fugitive moves backward left
    def assume_fugitive_moved_backward_left(self):
        position = self.fugitive

        # Slots that can't move backward left (forbidden slots)
        h1 = {'row' : 7, 'col' : 0}
        h2 = {'row' : 7, 'col' : 1}
        h3 = {'row' : 7, 'col' : 2}
        h4 = {'row' : 7, 'col' : 3}
        b1 = {'row' : 1, 'col' : 0}
        d1 = {'row' : 3, 'col' : 0}
        f1 = {'row' : 5, 'col' : 0}

        # Checking if the next step has an agent
        check_position = {}
        if self.fugitive['row'] % 2 == 0:
            check_position['row'] = self.fugitive['row'] + 1
            check_position['col'] = self.fugitive['col']
        else:
            check_position['row'] = self.fugitive['row'] + 1
            check_position['col'] = self.fugitive['col'] - 1


        # Check if position is in forbidden slots
        if position in (h1,h2,h3,h4,b1,d1,f1):
            return 0
        elif check_position in (self.agent1,self.agent2,self.agent3,self.agent4):
            return 0
        # Let's say the fugitive has moved forward left, how many slots are free
        else:
            slots = self._free_fugitive_slots(check_position)
            return slots         

    # If fugitive moves backward right
    def assume_fugitive_moved_backward_right(self):
        position = self.fugitive

        # Slots that can't move backward right (forbidden slots)
        h1 = {'row' : 7, 'col' : 0}
        h2 = {'row' : 7, 'col' : 1}
        h3 = {'row' : 7, 'col' : 2}
        h4 = {'row' : 7, 'col' : 3}
        c4 = {'row' : 2, 'col' : 3}
        e4 = {'row' : 4, 'col' : 3}
        g4 = {'row' : 6, 'col' : 3}
        a4 = {'row' : 0, 'col' : 3}

        # Checking if the next step has an agent
        check_position = {}
        if self.fugitive['row'] % 2 == 0:
            check_position['row'] = self.fugitive['row'] + 1
            check_position['col'] = self.fugitive['col'] + 1
        else:
            check_position['row'] = self.fugitive['row'] + 1
            check_position['col'] = self.fugitive['col']


        # Check if position is in forbidden slots
        if position in (h1,h2,h3,h4,c4,e4,g4,a4):
            return 0
        elif check_position in (self.agent1,self.agent2,self.agent3,self.agent4):
            return 0
        # Let's say the fugitive has moved forward left, how many slots are free
        else:
            slots = self._free_fugitive_slots(check_position)
            return slots         

    # Heuristic for the fugitive movement i.e: direction to move
    def fugitive_next_move(self):
        
        # Current fugitive position
        previous_fugitive_position = self.fugitive

        # If fugitive moves forward left
        forwardLeft = self.assume_fugitive_moved_forward_left()
        # If fugitive moves forward right
        forwardRight = self.assume_fugitive_moved_forward_right()
        # If fugitive moves backward left
        backwardLeft = self.assume_fugitive_moved_backward_left()
        # If fugitive moves backward right
        backwardRight = self.assume_fugitive_moved_backward_right()
        
        # Putting direction and values in the posible moves dictionary
        self.posible_fugitive_moves.append(forwardLeft) # Index 0 is forward left
        self.posible_fugitive_moves.append(forwardRight) # Index 1 is forward right
        self.posible_fugitive_moves.append(backwardLeft) # Index 2 is backward left
        self.posible_fugitive_moves.append(backwardRight) # Index 3 is backward right

        best_option = self.posible_fugitive_moves[0]
        move_direction = 0
        for index in range(len(self.posible_fugitive_moves)):
            if self.posible_fugitive_moves[index] > best_option:
                best_option = self.posible_fugitive_moves[index]
                move_direction = index

        # Try moving down
        if backwardLeft > backwardRight:
            self.move_fugitive_backward_left()
            print("Fugitive moved backward left!")
        elif backwardRight > backwardLeft:
            self.move_fugitive_backward_right()
            print("Fugitive moved backward right!")
        else:
            pass
       
        # Check if fugitive has moved down. if not move to an up position
        if previous_fugitive_position != self.fugitive:
            pass
        else:
            if move_direction == 0:
                self.move_fugitive_forward_left()
                print("Fugitive moved forward left!")
            elif move_direction == 1:
                self.move_fugitive_forward_right()
                print("Fugitive moved forward right!")
            elif move_direction == 2:
                self.move_fugitive_backward_left()
                print("Fugitive moved backward left!")
            elif move_direction == 3:
                self.move_fugitive_backward_right()
                print("Fugitive moved backward right!")

        self.posible_fugitive_moves = []

    # Goal for the fugitive; returns True if goal is reached
    def fugitive_goal_reached(self):
        h1 = {'row' : 7, 'col' : 0}
        h2 = {'row' : 7, 'col' : 1}
        h3 = {'row' : 7, 'col' : 2}
        h4 = {'row' : 7, 'col' : 3}

        if self.fugitive in (h1,h2,h3,h4):
            return True
        else:
            return False
 
    # Fugitive caught. MUST BE PRINTED
    def caught_fugitive(self):
        
        # **** Checking forward left ****
        # Checking if the next step has an agent
        check_positionFl = {}
        if self.fugitive['row'] % 2 == 0:
            check_positionFl['row'] = self.fugitive['row'] - 1
            check_positionFl['col'] = self.fugitive['col']
        else:
            check_positionFl['row'] = self.fugitive['row'] - 1
            check_positionFl['col'] = self.fugitive['col'] - 1
        
        # **** Checking forward right ****
        # Checking if the next step has an agent
        check_positionFr = {}
        if self.fugitive['row'] % 2 == 0:
            check_positionFr['row'] = self.fugitive['row'] - 1
            check_positionFr['col'] = self.fugitive['col'] + 1
        else:
            check_positionFr['row'] = self.fugitive['row'] - 1
            check_positionFr['col'] = self.fugitive['col']

        # **** Checking backward left ****
        # Checking if the next step has an agent
        check_positionBl = {}
        if self.fugitive['row'] % 2 == 0:
            check_positionBl['row'] = self.fugitive['row'] + 1
            check_positionBl['col'] = self.fugitive['col']
        else:
            check_positionBl['row'] = self.fugitive['row'] + 1
            check_positionBl['col'] = self.fugitive['col'] - 1
        
        # **** Checking backward right ****
        # Checking if the next step has an agent
        check_positionBr = {}
        if self.fugitive['row'] % 2 == 0:
            check_positionBr['row'] = self.fugitive['row'] + 1
            check_positionBr['col'] = self.fugitive['col'] + 1
        else:
            check_positionBr['row'] = self.fugitive['row'] + 1
            check_positionBr['col'] = self.fugitive['col']
        
        # Defining boundaries
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        b1 = {'row' : 1, 'col' : 0}
        b1 = {'row' : 1, 'col' : 0}
        d1 = {'row' : 3, 'col' : 0}
        f1 = {'row' : 5, 'col' : 0}
        c4 = {'row' : 2, 'col' : 3}
        e4 = {'row' : 4, 'col' : 3}
        g4 = {'row' : 6, 'col' : 3}

        # If fugitive is at the top, check if it is surrounded by agents
        if self.fugitive in (a1, a2, a3, a4) and check_positionBl in (self.agent1, self.agent2, self.agent3, self.agent4) and check_positionBr in (self.agent1, self.agent2, self.agent3, self.agent4):
            message = "Fugitive has been caught at", self.fugitive
            return message
        # If fugitive is at the left, check if it is surrounded by agents
        elif self.fugitive in (b1, d1, f1) and check_positionFr in (self.agent1, self.agent2, self.agent3, self.agent4) and check_positionBr in (self.agent1, self.agent2, self.agent3, self.agent4):
            message = "Fugitive has been caught at", self.fugitive
            return message
        # If fugitive is at the right, check if it is surrounded by agents
        elif self.fugitive in (c4, e4, g4) and check_positionFl in (self.agent1, self.agent2, self.agent3, self.agent4) and check_positionBl in (self.agent1, self.agent2, self.agent3, self.agent4):
            message = "Fugitive has been caught at", self.fugitive
            return message
        # Check generally
        elif check_positionFl in (self.agent1, self.agent2, self.agent3, self.agent4) and check_positionFr in (self.agent1, self.agent2, self.agent3, self.agent4) and check_positionBl in (self.agent1, self.agent2, self.agent4, self.agent4) and check_positionBl in (self.agent1, self.agent2, self.agent4, self.agent4):
            message = "Fugitive has been caught at", self.fugitive
            return "Fugitive has been caught at", self.fugitive
        # Fugitive is not surrounded
        else:
            return None

    # Check for available slots around fugitive postion
    def _free_fugitive_slots(self, position):
        count = 0   # Free slots count

        # Checking left forward position
        check_position = {}
        if position['row'] % 2 == 0:
            check_position['row'] = position['row'] - 1
            check_position['col'] = position['col']
        else:
            check_position['row'] = position['row'] - 1
            check_position['col'] = position['col'] - 1

        # Forbidden slots
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        b1 = {'row' : 1, 'col' : 0}
        d1 = {'row' : 3, 'col' : 0}
        f1 = {'row' : 5, 'col' : 0}

        if position in (a1,a2,a3,a4,b1,d1,f1):
            pass
        elif check_position in (self.agent1,self.agent2,self.agent3,self.agent4):
            pass
        else:
            count += 1
        
        # Checking right forward position
        check_position = {}
        if position['row'] % 2 == 0:
            check_position['row'] = position['row'] - 1
            check_position['col'] = position['col'] + 1
        else:
            check_position['row'] = position['row'] - 1
            check_position['col'] = position['col']

        # Forbidden slots
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        c4 = {'row' : 2, 'col' : 3}
        e4 = {'row' : 4, 'col' : 3}
        g4 = {'row' : 6, 'col' : 3}

        if position in (a1,a2,a3,a4,c4,e4,g4):
            pass
        elif check_position in (self.agent1,self.agent2,self.agent3,self.agent4):
            pass
        else:
            count += 1

        # Checking left backward position
        check_position = {}
        if position['row'] % 2 == 0:
            check_position['row'] = position['row'] + 1
            check_position['col'] = position['col']
        else:
            check_position['row'] = position['row'] + 1
            check_position['col'] = position['col'] - 1

        # Forbidden slots
        h1 = {'row' : 7, 'col' : 0}
        h2 = {'row' : 7, 'col' : 1}
        h3 = {'row' : 7, 'col' : 2}
        h4 = {'row' : 7, 'col' : 3}
        b1 = {'row' : 1, 'col' : 0}
        d1 = {'row' : 3, 'col' : 0}
        f1 = {'row' : 5, 'col' : 0}

        if position in (h1,h2,h3,h4,b1,d1,f1):
            pass
        elif check_position in (self.agent1,self.agent2,self.agent3,self.agent4):
            pass
        else:
            count += 1

        # Checking right backward position
        check_position = {}
        if position['row'] % 2 == 0:
            check_position['row'] = position['row'] + 1
            check_position['col'] = position['col'] + 1
        else:
            check_position['row'] = position['row'] + 1
            check_position['col'] = position['col']

        # Forbidden slots
        h1 = {'row' : 7, 'col' : 0}
        h2 = {'row' : 7, 'col' : 1}
        h3 = {'row' : 7, 'col' : 2}
        h4 = {'row' : 7, 'col' : 3}
        c4 = {'row' : 2, 'col' : 3}
        e4 = {'row' : 4, 'col' : 3}
        g4 = {'row' : 6, 'col' : 3}
        a4 = {'row' : 0, 'col' : 3}

        if position in (h1,h2,h3,h4,c4,e4,g4,a4):
            pass
        elif check_position in (self.agent1,self.agent2,self.agent3,self.agent4):
            pass
        else:
            count += 1
        return count

    # move fugitive; controlled by USER
    def move_fugitive(self):

        print("Move fugitive forward left('fl'), forward right('fr'), backward left('bl') or backward right('br')")
        direction = input("Select direction, either 'fl', 'fr', 'bl' or 'br': ")

        # Error checking
        while direction not in ('fl', 'fr', 'bl', 'br'):
            print("Only 'fl', 'fr', 'bl' or 'br' can be selected!")
            direction = input("Select direction, either 'fl', 'fr', 'bl' or 'br': ")
        
        if direction == 'fl':
            self.move_fugitive_forward_left()
            print("Moving fugitive forward left.")
        elif direction == 'fr':
            self.move_fugitive_forward_right()
            print("Moving fugitive forward right.")
        elif direction == 'bl':
            self.move_fugitive_backward_left()
            print("Moving fugitive backward left.")
        elif direction == 'br':
            self.move_fugitive_backward_right()
            print("Moving fugitive backward right.")

        


    # *********************** AGENTS FUNCTIONS **************************

    # ***** Move agent 1 *****
    # Move forward left
    def move_first_agent_forward_left(self):
        self.agent1

        position = self.agent1

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        b1 = {'row' : 1, 'col' : 0}
        # c1 = {'row' : 2, 'col' : 0}
        d1 = {'row' : 3, 'col' : 0}
        # e1 = {'row' : 4, 'col' : 0}
        f1 = {'row' : 5, 'col' : 0}
        # g1 = {'row' : 6, 'col' : 0}
        h1 = {'row' : 7, 'col' : 0}


        # Checking if the next step has an agent
        check_position = {}
        if self.agent1['row'] % 2 == 0:
            check_position['row'] = self.agent1['row'] - 1
            check_position['col'] = self.agent1['col']
        else:
            check_position['row'] = self.agent1['row'] - 1
            check_position['col'] = self.agent1['col'] - 1
        
        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,b1,d1,f1,h1):
            return None
        elif check_position in (self.agent2,self.agent3,self.agent4, self.fugitive):
            return None
        else:
            # Creating temporary variable to hold current agent1 position
            temp = {}
            temp['row'] = self.agent1['row']
            temp['col'] = self.agent1['col']

            # Shifting agent1 to forward left (New agent1 position)
            if self.agent1['row'] % 2 == 0:
                self.agent1['row'] = self.agent1['row'] - 1
                self.agent1['col'] = self.agent1['col']
            else:
                self.agent1['row'] = self.agent1['row'] - 1
                self.agent1['col'] = self.agent1['col'] - 1

            # Replace agent1 position with '#' and new position with agent1 'A'
            self.movable_slots[temp['row']][temp['col']] = '#'
            self.movable_slots[self.agent1['row']][self.agent1['col']] = 'A'

    # Move forward right
    def move_first_agent_forward_right(self):
        self.agent1

        position = self.agent1

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        # b4 = {'row' : 1, 'col' : 3}
        c4 = {'row' : 2, 'col' : 3}
        # d4 = {'row' : 3, 'col' : 3}
        e4 = {'row' : 4, 'col' : 3}
        # f4 = {'row' : 5, 'col' : 3}
        g4 = {'row' : 6, 'col' : 3}
        # h4 = {'row' : 7, 'col' : 3}

        # Checking if the next step has an agent
        check_position = {}
        if self.agent1['row'] % 2 == 0:
            check_position['row'] = self.agent1['row'] - 1
            check_position['col'] = self.agent1['col'] + 1
        else:
            check_position['row'] = self.agent1['row'] - 1
            check_position['col'] = self.agent1['col']

        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,c4,e4,g4):
            return None
        elif check_position in (self.agent2,self.agent3,self.agent4,self.fugitive):
            return None
        else:
            # Creating temporary variable to hold current agent1 position
            temp = {}
            temp['row'] = self.agent1['row']
            temp['col'] = self.agent1['col']


            # Shifting agent1 to forward left (New agent1 position)
            if self.agent1['row'] % 2 == 0:
                self.agent1['row'] = self.agent1['row'] - 1
                self.agent1['col'] = self.agent1['col'] + 1
            else:
                self.agent1['row'] = self.agent1['row'] - 1
                self.agent1['col'] = self.agent1['col']


            # Replace agent1 position with '#' and new position with agent1 'A'
            self.movable_slots[temp['row']][temp['col']] = '#'
            self.movable_slots[self.agent1['row']][self.agent1['col']] = 'A'

    # ***** Move agent 2 *****
    # Move forward left
    def move_second_agent_forward_left(self):
        self.agent2

        position = self.agent2

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        b1 = {'row' : 1, 'col' : 0}
        # c1 = {'row' : 2, 'col' : 0}
        d1 = {'row' : 3, 'col' : 0}
        # e1 = {'row' : 4, 'col' : 0}
        f1 = {'row' : 5, 'col' : 0}
        # g1 = {'row' : 6, 'col' : 0}
        h1 = {'row' : 7, 'col' : 0}


        # Checking if the next step has an agent
        check_position = {}
        if self.agent2['row'] % 2 == 0:
            check_position['row'] = self.agent2['row'] - 1
            check_position['col'] = self.agent2['col']
        else:
            check_position['row'] = self.agent2['row'] - 1
            check_position['col'] = self.agent2['col'] - 1
        
        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,b1,d1,f1,h1):
            return None
        elif check_position in (self.agent1,self.agent3,self.agent4, self.fugitive):
            return None
        else:
            # Creating temporary variable to hold current agent2 position
            temp = {}
            temp['row'] = self.agent2['row']
            temp['col'] = self.agent2['col']

            # Shifting agent2 to forward left (New agent2 position)
            if self.agent2['row'] % 2 == 0:
                self.agent2['row'] = self.agent2['row'] - 1
                self.agent2['col'] = self.agent2['col']
            else:
                self.agent2['row'] = self.agent2['row'] - 1
                self.agent2['col'] = self.agent2['col'] - 1

            # Replace agent2 position with '#' and new position with agent2 'A'
            self.movable_slots[temp['row']][temp['col']] = '#'
            self.movable_slots[self.agent2['row']][self.agent2['col']] = 'A'

    # Move forward right
    def move_second_agent_forward_right(self):
        self.agent2

        position = self.agent2

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        # b4 = {'row' : 1, 'col' : 3}
        c4 = {'row' : 2, 'col' : 3}
        # d4 = {'row' : 3, 'col' : 3}
        e4 = {'row' : 4, 'col' : 3}
        # f4 = {'row' : 5, 'col' : 3}
        g4 = {'row' : 6, 'col' : 3}
        # h4 = {'row' : 7, 'col' : 3}

        # Checking if the next step has an agent
        check_position = {}
        if self.agent2['row'] % 2 == 0:
            check_position['row'] = self.agent2['row'] - 1
            check_position['col'] = self.agent2['col'] + 1
        else:
            check_position['row'] = self.agent2['row'] - 1
            check_position['col'] = self.agent2['col']

        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,c4,e4,g4):
            return None
        elif check_position in (self.agent1,self.agent3,self.agent4,self.fugitive):
            return None
        else:
            # Creating temporary variable to hold current agent2 position
            temp = {}
            temp['row'] = self.agent2['row']
            temp['col'] = self.agent2['col']


            # Shifting agent2 to forward left (New agent2 position)
            if self.agent2['row'] % 2 == 0:
                self.agent2['row'] = self.agent2['row'] - 1
                self.agent2['col'] = self.agent2['col'] + 1
            else:
                self.agent2['row'] = self.agent2['row'] - 1
                self.agent2['col'] = self.agent2['col']


            # Replace agent2 position with '#' and new position with agent2 'A'
            self.movable_slots[temp['row']][temp['col']] = '#'
            self.movable_slots[self.agent2['row']][self.agent2['col']] = 'A'

    # ***** Move agent 3 *****
    # Move forward left
    def move_third_agent_forward_left(self):
        self.agent3

        position = self.agent3

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        b1 = {'row' : 1, 'col' : 0}
        # c1 = {'row' : 2, 'col' : 0}
        d1 = {'row' : 3, 'col' : 0}
        # e1 = {'row' : 4, 'col' : 0}
        f1 = {'row' : 5, 'col' : 0}
        # g1 = {'row' : 6, 'col' : 0}
        h1 = {'row' : 7, 'col' : 0}


        # Checking if the next step has an agent
        check_position = {}
        if self.agent3['row'] % 2 == 0:
            check_position['row'] = self.agent3['row'] - 1
            check_position['col'] = self.agent3['col']
        else:
            check_position['row'] = self.agent3['row'] - 1
            check_position['col'] = self.agent3['col'] - 1
        
        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,b1,d1,f1,h1):
            return None
        elif check_position in (self.agent1,self.agent2,self.agent4, self.fugitive):
            return None
        else:
            # Creating temporary variable to hold current agent3 position
            temp = {}
            temp['row'] = self.agent3['row']
            temp['col'] = self.agent3['col']

            # Shifting agent3 to forward left (New agent3 position)
            if self.agent3['row'] % 2 == 0:
                self.agent3['row'] = self.agent3['row'] - 1
                self.agent3['col'] = self.agent3['col']
            else:
                self.agent3['row'] = self.agent3['row'] - 1
                self.agent3['col'] = self.agent3['col'] - 1

            # Replace agent3 position with '#' and new position with agent3 'A'
            self.movable_slots[temp['row']][temp['col']] = '#'
            self.movable_slots[self.agent3['row']][self.agent3['col']] = 'A'

    # Move forward right
    def move_third_agent_forward_right(self):
        self.agent3

        position = self.agent3

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        # b4 = {'row' : 1, 'col' : 3}
        c4 = {'row' : 2, 'col' : 3}
        # d4 = {'row' : 3, 'col' : 3}
        e4 = {'row' : 4, 'col' : 3}
        # f4 = {'row' : 5, 'col' : 3}
        g4 = {'row' : 6, 'col' : 3}
        # h4 = {'row' : 7, 'col' : 3}

        # Checking if the next step has an agent
        check_position = {}
        if self.agent3['row'] % 2 == 0:
            check_position['row'] = self.agent3['row'] - 1
            check_position['col'] = self.agent3['col'] + 1
        else:
            check_position['row'] = self.agent3['row'] - 1
            check_position['col'] = self.agent3['col']

        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,c4,e4,g4):
            return None
        elif check_position in (self.agent1,self.agent2,self.agent4,self.fugitive):
            return None
        else:
            # Creating temporary variable to hold current agent3 position
            temp = {}
            temp['row'] = self.agent3['row']
            temp['col'] = self.agent3['col']


            # Shifting agent3 to forward left (New agent3 position)
            if self.agent3['row'] % 2 == 0:
                self.agent3['row'] = self.agent3['row'] - 1
                self.agent3['col'] = self.agent3['col'] + 1
            else:
                self.agent3['row'] = self.agent3['row'] - 1
                self.agent3['col'] = self.agent3['col']


            # Replace agent3 position with '#' and new position with agent3 'A'
            self.movable_slots[temp['row']][temp['col']] = '#'
            self.movable_slots[self.agent3['row']][self.agent3['col']] = 'A'

    # ***** Move agent 4 *****
    # Move forward left
    def move_fourth_agent_forward_left(self):
        self.agent4

        position = self.agent4

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        b1 = {'row' : 1, 'col' : 0}
        # c1 = {'row' : 2, 'col' : 0}
        d1 = {'row' : 3, 'col' : 0}
        # e1 = {'row' : 4, 'col' : 0}
        f1 = {'row' : 5, 'col' : 0}
        # g1 = {'row' : 6, 'col' : 0}
        h1 = {'row' : 7, 'col' : 0}


        # Checking if the next step has an agent
        check_position = {}
        if self.agent4['row'] % 2 == 0:
            check_position['row'] = self.agent4['row'] - 1
            check_position['col'] = self.agent4['col']
        else:
            check_position['row'] = self.agent4['row'] - 1
            check_position['col'] = self.agent4['col'] - 1
        
        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,b1,d1,f1,h1):
            return None
        elif check_position in (self.agent1,self.agent2,self.agent3,self.fugitive):
            return None
        else:
            # Creating temporary variable to hold current agent4 position
            temp = {}
            temp['row'] = self.agent4['row']
            temp['col'] = self.agent4['col']

            # Shifting agent4 to forward left (New agent4 position)
            if self.agent4['row'] % 2 == 0:
                self.agent4['row'] = self.agent4['row'] - 1
                self.agent4['col'] = self.agent4['col']
            else:
                self.agent4['row'] = self.agent4['row'] - 1
                self.agent4['col'] = self.agent4['col'] - 1

            # Replace agent4 position with '#' and new position with agent4 'A'
            self.movable_slots[temp['row']][temp['col']] = '#'
            self.movable_slots[self.agent4['row']][self.agent4['col']] = 'A'

    # Move forward right
    def move_fourth_agent_forward_right(self):
        self.agent4

        position = self.agent4

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        # b4 = {'row' : 1, 'col' : 3}
        c4 = {'row' : 2, 'col' : 3}
        # d4 = {'row' : 3, 'col' : 3}
        e4 = {'row' : 4, 'col' : 3}
        # f4 = {'row' : 5, 'col' : 3}
        g4 = {'row' : 6, 'col' : 3}
        # h4 = {'row' : 7, 'col' : 3}

        # Checking if the next step has an agent
        check_position = {}
        if self.agent4['row'] % 2 == 0:
            check_position['row'] = self.agent4['row'] - 1
            check_position['col'] = self.agent4['col'] + 1
        else:
            check_position['row'] = self.agent4['row'] - 1
            check_position['col'] = self.agent4['col']

        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,c4,e4,g4):
            return None
        elif check_position in (self.agent1,self.agent2,self.agent3,self.fugitive):
            return None
        else:
            # Creating temporary variable to hold current agent4 position
            temp = {}
            temp['row'] = self.agent4['row']
            temp['col'] = self.agent4['col']


            # Shifting agent4 to forward left (New agent4 position)
            if self.agent4['row'] % 2 == 0:
                self.agent4['row'] = self.agent4['row'] - 1
                self.agent4['col'] = self.agent4['col'] + 1
            else:
                self.agent4['row'] = self.agent4['row'] - 1
                self.agent4['col'] = self.agent4['col']


            # Replace agent4 position with '#' and new position with agent4 'A'
            self.movable_slots[temp['row']][temp['col']] = '#'
            self.movable_slots[self.agent4['row']][self.agent4['col']] = 'A'

    # Select agent to move
    def _select_agent(self):
        self.current_agent

        # Displaying prompt to the user
        print("Agents: 1, 2, 3, 4")
        agent = input("Please select the agent to move: ")

        # Error checking
        while agent not in ('1', '2', '3', '4'):
            print("Agent must either be '1', '2', '3' or '4' only!!!")
            agent = input("Please select the agent to move: ")

        self.current_agent = agent
        print("Agent", agent, "selected!")

    # Move agents; controlled by USER
    def move_agent(self):
        # Selecting the agent to move
        self._select_agent()

        # Deciding where to move
        if self.current_agent == '1':
            # Display prompt to the user
            print("l = left; r = right")
            # Get direction to move
            direction = input("Move agent left (l) or right (r): ")
            # Error checking
            while direction not in ('l', 'r'):
                print("Direction can either be 'l' or 'r' only!!!")
                direction = input("Move agent left (l) or right (r): ")

            # left or right
            direct = ''
            if direction == 'l':
                direct = 'left'
            else:
                direct = 'right'

            print("Moving agent", self.current_agent, "to the", direct)
            # Moving agent
            if direction == 'l':
                self.move_first_agent_forward_left()
            else:
                self.move_first_agent_forward_right()
        elif self.current_agent == '2':
            # Display prompt to the user
            print("l = left; r = right")
            # Get direction to move
            direction = input("Move agent left (l) or right (r): ")
            # Error checking
            while direction not in ('l', 'r'):
                print("Direction can either be 'l' or 'r' only!!!")
                direction = input("Move agent left (l) or right (r): ")

            # left or right
            direct = ''
            if direction == 'l':
                direct = 'left'
            else:
                direct = 'right'

            print("Moving agent", self.current_agent, "to the", direct)
            # Moving agent
            if direction == 'l':
                self.move_second_agent_forward_left()
            else:
                self.move_second_agent_forward_right()
        elif self.current_agent == '3':
            # Display prompt to the user
            print("l = left; r = right")
            # Get direction to move
            direction = input("Move agent left (l) or right (r): ")
            # Error checking
            while direction not in ('l', 'r'):
                print("Direction can either be 'l' or 'r' only!!!")
                direction = input("Move agent left (l) or right (r): ")

            # left or right
            direct = ''
            if direction == 'l':
                direct = 'left'
            else:
                direct = 'right'

            print("Moving agent", self.current_agent, "to the", direct)
            # Moving agent
            if direction == 'l':
                self.move_third_agent_forward_left()
            else:
                self.move_third_agent_forward_right()
        elif self.current_agent == '4':
            # Display prompt to the user
            print("l = left; r = right")
            # Get direction to move
            direction = input("Move agent left (l) or right (r): ")
            # Error checking
            while direction not in ('l', 'r'):
                print("Direction can either be 'l' or 'r' only!!!")
                direction = input("Move agent left (l) or right (r): ")

            # left or right
            direct = ''
            if direction == 'l':
                direct = 'left'
            else:
                direct = 'right'

            print("Moving agent", self.current_agent, "to the", direct)
            # Moving agent
            if direction == 'l':
                self.move_fourth_agent_forward_left()
            else:
                self.move_fourth_agent_forward_right()
    
    # Check for available slots around agent1 postion
    def _agent_close_to_fugitive(self, position):
        count = 0   # Free slots count

        # Checking left forward position
        check_position = {}
        if position['row'] % 2 == 0:
            check_position['row'] = position['row'] - 1
            check_position['col'] = position['col']
        else:
            check_position['row'] = position['row'] - 1
            check_position['col'] = position['col'] - 1

        # Forbidden slots
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        b1 = {'row' : 1, 'col' : 0}
        d1 = {'row' : 3, 'col' : 0}
        f1 = {'row' : 5, 'col' : 0}

        if position in (a1,a2,a3,a4,b1,d1,f1):
            pass
        elif check_position in (self.agent1,self.agent2,self.agent3,self.agent4):
            pass
        elif check_position == self.fugitive:
            count += 1
        else:
            pass
        
        # Checking right forward position
        check_position = {}
        if position['row'] % 2 == 0:
            check_position['row'] = position['row'] - 1
            check_position['col'] = position['col'] + 1
        else:
            check_position['row'] = position['row'] - 1
            check_position['col'] = position['col']

        # Forbidden slots
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        c4 = {'row' : 2, 'col' : 3}
        e4 = {'row' : 4, 'col' : 3}
        g4 = {'row' : 6, 'col' : 3}

        if position in (a1,a2,a3,a4,c4,e4,g4):
            pass
        elif check_position in (self.agent1,self.agent2,self.agent3,self.agent4):
            pass
        elif check_position == self.fugitive:
            count += 1
        else:
            pass

        # Checking left backward position
        check_position = {}
        if position['row'] % 2 == 0:
            check_position['row'] = position['row'] + 1
            check_position['col'] = position['col']
        else:
            check_position['row'] = position['row'] + 1
            check_position['col'] = position['col'] - 1

        # Forbidden slots
        h1 = {'row' : 7, 'col' : 0}
        h2 = {'row' : 7, 'col' : 1}
        h3 = {'row' : 7, 'col' : 2}
        h4 = {'row' : 7, 'col' : 3}
        b1 = {'row' : 1, 'col' : 0}
        d1 = {'row' : 3, 'col' : 0}
        f1 = {'row' : 5, 'col' : 0}

        if position in (h1,h2,h3,h4,b1,d1,f1):
            pass
        elif check_position in (self.agent1,self.agent2,self.agent3,self.agent4):
            pass
        elif check_position == self.fugitive:
            count += 1
        else:
            pass

        # Checking right backward position
        check_position = {}
        if position['row'] % 2 == 0:
            check_position['row'] = position['row'] + 1
            check_position['col'] = position['col'] + 1
        else:
            check_position['row'] = position['row'] + 1
            check_position['col'] = position['col']

        # Forbidden slots
        h1 = {'row' : 7, 'col' : 0}
        h2 = {'row' : 7, 'col' : 1}
        h3 = {'row' : 7, 'col' : 2}
        h4 = {'row' : 7, 'col' : 3}
        c4 = {'row' : 2, 'col' : 3}
        e4 = {'row' : 4, 'col' : 3}
        g4 = {'row' : 6, 'col' : 3}
        a4 = {'row' : 0, 'col' : 3}

        if position in (h1,h2,h3,h4,c4,e4,g4,a4):
            pass
        elif check_position in (self.agent1,self.agent2,self.agent3,self.agent4):
            pass
        elif check_position == self.fugitive:
            count += 1
        else:
            pass
        return count

    # ************ AGENT HEURISTICS *************
    # If agent 1 moves forward left; MUST BE PRINTED
    def assume_agent1_moved_forward_left(self):
        position = self.agent1

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        b1 = {'row' : 1, 'col' : 0}
        d1 = {'row' : 3, 'col' : 0}
        f1 = {'row' : 5, 'col' : 0}
        h1 = {'row' : 7, 'col' : 0}

        # Checking if the next step has an agent
        check_position = {}
        if self.agent1['row'] % 2 == 0:
            check_position['row'] = self.agent1['row'] - 1
            check_position['col'] = self.agent1['col']
        else:
            check_position['row'] = self.agent1['row'] - 1
            check_position['col'] = self.agent1['col'] - 1


        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,b1,d1,f1,h1):
            return 0
        elif check_position in (self.agent2,self.agent3,self.agent4,self.fugitive):
            return 0
        # Let's say the agent1 has moved forward left, how many slots are free
        else:
            heuristic = self._agent_close_to_fugitive(check_position)
            return heuristic

    # If agent 1 moves forward right; MUST BE PRINTED
    def assume_agent1_moved_forward_right(self):
        position = self.agent1

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        c4 = {'row' : 2, 'col' : 3}
        e4 = {'row' : 4, 'col' : 3}
        g4 = {'row' : 6, 'col' : 3}

        # Checking if the next step has an agent
        check_position = {}
        if self.agent1['row'] % 2 == 0:
            check_position['row'] = self.agent1['row'] - 1
            check_position['col'] = self.agent1['col'] + 1
        else:
            check_position['row'] = self.agent1['row'] - 1
            check_position['col'] = self.agent1['col']


        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,c4,e4,g4):
            return 0
        elif check_position in (self.agent2,self.agent3,self.agent4,self.fugitive):
            return 0
        # Let's say the agent1 has moved forward left, how many slots are free
        else:
            heuristic = self._agent_close_to_fugitive(check_position)
            return heuristic

    # If agent 2 moves forward left; MUST BE PRINTED
    def assume_agent2_moved_forward_left(self):
        position = self.agent2

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        b1 = {'row' : 1, 'col' : 0}
        d1 = {'row' : 3, 'col' : 0}
        f1 = {'row' : 5, 'col' : 0}
        h1 = {'row' : 7, 'col' : 0}

        # Checking if the next step has an agent
        check_position = {}
        if self.agent2['row'] % 2 == 0:
            check_position['row'] = self.agent2['row'] - 1
            check_position['col'] = self.agent2['col']
        else:
            check_position['row'] = self.agent2['row'] - 1
            check_position['col'] = self.agent2['col'] - 1


        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,b1,d1,f1,h1):
            return 0
        elif check_position in (self.agent1,self.agent3,self.agent4,self.fugitive):
            return 0
        # Let's say the agent1 has moved forward left, how many slots are free
        else:
            heuristic = self._agent_close_to_fugitive(check_position)
            return heuristic
    
    # If agent 2 moves forward right; MUST BE PRINTED
    def assume_agent2_moved_forward_right(self):
        position = self.agent2

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        c4 = {'row' : 2, 'col' : 3}
        e4 = {'row' : 4, 'col' : 3}
        g4 = {'row' : 6, 'col' : 3}

        # Checking if the next step has an agent
        check_position = {}
        if self.agent2['row'] % 2 == 0:
            check_position['row'] = self.agent2['row'] - 1
            check_position['col'] = self.agent2['col'] + 1
        else:
            check_position['row'] = self.agent2['row'] - 1
            check_position['col'] = self.agent2['col']


        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,c4,e4,g4):
            return 0
        elif check_position in (self.agent1,self.agent3,self.agent4,self.fugitive):
            return 0
        # Let's say the agent1 has moved forward left, how many slots are free
        else:
            heuristic = self._agent_close_to_fugitive(check_position)
            return heuristic

    # If agent 3 moves forward left; MUST BE PRINTED
    def assume_agent3_moved_forward_left(self):
        position = self.agent3

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        b1 = {'row' : 1, 'col' : 0}
        d1 = {'row' : 3, 'col' : 0}
        f1 = {'row' : 5, 'col' : 0}
        h1 = {'row' : 7, 'col' : 0}

        # Checking if the next step has an agent
        check_position = {}
        if self.agent3['row'] % 2 == 0:
            check_position['row'] = self.agent3['row'] - 1
            check_position['col'] = self.agent3['col']
        else:
            check_position['row'] = self.agent3['row'] - 1
            check_position['col'] = self.agent3['col'] - 1


        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,b1,d1,f1,h1):
            return 0
        elif check_position in (self.agent1,self.agent2,self.agent4,self.fugitive):
            return 0
        # Let's say the agent1 has moved forward left, how many slots are free
        else:
            heuristic = self._agent_close_to_fugitive(check_position)
            return heuristic
    
    # If agent 3 moves forward right; MUST BE PRINTED
    def assume_agent3_moved_forward_right(self):
        position = self.agent3

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        c4 = {'row' : 2, 'col' : 3}
        e4 = {'row' : 4, 'col' : 3}
        g4 = {'row' : 6, 'col' : 3}

        # Checking if the next step has an agent
        check_position = {}
        if self.agent3['row'] % 2 == 0:
            check_position['row'] = self.agent3['row'] - 1
            check_position['col'] = self.agent3['col'] + 1
        else:
            check_position['row'] = self.agent3['row'] - 1
            check_position['col'] = self.agent3['col']


        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,c4,e4,g4):
            return 0
        elif check_position in (self.agent1,self.agent2,self.agent4,self.fugitive):
            return 0
        # Let's say the agent1 has moved forward left, how many slots are free
        else:
            heuristic = self._agent_close_to_fugitive(check_position)
            return heuristic

    # If agent 4 moves forward left; MUST BE PRINTED
    def assume_agent4_moved_forward_left(self):
        position = self.agent4

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        b1 = {'row' : 1, 'col' : 0}
        d1 = {'row' : 3, 'col' : 0}
        f1 = {'row' : 5, 'col' : 0}
        h1 = {'row' : 7, 'col' : 0}

        # Checking if the next step has an agent
        check_position = {}
        if self.agent4['row'] % 2 == 0:
            check_position['row'] = self.agent4['row'] - 1
            check_position['col'] = self.agent4['col']
        else:
            check_position['row'] = self.agent4['row'] - 1
            check_position['col'] = self.agent4['col'] - 1


        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,b1,d1,f1,h1):
            return 0
        elif check_position in (self.agent1,self.agent3,self.agent2,self.fugitive):
            return 0
        # Let's say the agent1 has moved forward left, how many slots are free
        else:
            heuristic = self._agent_close_to_fugitive(check_position)
            return heuristic
    
    # If agent 4 moves forward right; MUST BE PRINTED
    def assume_agent4_moved_forward_right(self):
        position = self.agent4

        # Slots that can't move forward left (forbidden slots)
        a1 = {'row' : 0, 'col' : 0}
        a2 = {'row' : 0, 'col' : 1}
        a3 = {'row' : 0, 'col' : 2}
        a4 = {'row' : 0, 'col' : 3}
        c4 = {'row' : 2, 'col' : 3}
        e4 = {'row' : 4, 'col' : 3}
        g4 = {'row' : 6, 'col' : 3}

        # Checking if the next step has an agent
        check_position = {}
        if self.agent4['row'] % 2 == 0:
            check_position['row'] = self.agent4['row'] - 1
            check_position['col'] = self.agent4['col'] + 1
        else:
            check_position['row'] = self.agent4['row'] - 1
            check_position['col'] = self.agent4['col']


        # Check if position is in forbidden slots
        if position in (a1,a2,a3,a4,c4,e4,g4):
            return 0
        elif check_position in (self.agent1,self.agent3,self.agent2,self.fugitive):
            return 0
        # Let's say the agent1 has moved forward left, how many slots are free
        else:
            heuristic = self._agent_close_to_fugitive(check_position)
            return heuristic

    # Heuristic for the agents movement i.e: direction and agent to move
    def agent_next_move(self):

        # If agent1 moved forward left
        agent1_left = self.assume_agent1_moved_forward_left()
        # If agent1 moved forward right
        agent1_right = self.assume_agent1_moved_forward_right()
        # If agent2 moved forward left
        agent2_left = self.assume_agent2_moved_forward_left()
        # If agent2 moved forward right
        agent2_right = self.assume_agent2_moved_forward_right()
        # If agent3 moved forward left
        agent3_left = self.assume_agent3_moved_forward_left()
        # If agent3 moved forward right
        agent3_right = self.assume_agent3_moved_forward_right()
        # If agent4 moved forward left
        agent4_left = self.assume_agent4_moved_forward_left()
        # If agent4 moved forward right
        agent4_right = self.assume_agent4_moved_forward_right()

        # Adding the heuristics to the posible agent moves
        self.posible_agent_moves.append(agent1_left) # Index 0 is agent 1 moving left
        self.posible_agent_moves.append(agent1_right) # Index 1 is agent 1 moving right
        self.posible_agent_moves.append(agent2_left) # Index 2 is agent 2 moving left
        self.posible_agent_moves.append(agent2_right) # Index 3 is agent 2 moving right
        self.posible_agent_moves.append(agent3_left) # Index 4 is agent 3 moving left
        self.posible_agent_moves.append(agent3_right) # Index 5 is agent 3 moving right
        self.posible_agent_moves.append(agent4_left) # Index 6 is agent 4 moving left
        self.posible_agent_moves.append(agent4_right) # Index 7 is agent 4 moving left

        # Variable to hold index of best fit
        move_direction = 0
        
        # Going through the array to fing the best movement for the agents
        best_option = self.posible_agent_moves[0]
        for index in range(len(self.posible_agent_moves)):
            if self.posible_agent_moves[index] > best_option:
                best_option = self.posible_agent_moves[index]
                move_direction = index

        # If none of the agents can get near the fugitive, move agent 1 forward right
        if self.uniqueElement(self.posible_agent_moves, 0):
            print("0s")         
            move_direction += random.choice((1, 4))
        
        print(move_direction)

        # Check the index and make the move
        if move_direction == 0: # Agent 1 left movement has best heuristic and moves left
            self.move_first_agent_forward_left()
            print("Agent 1 moved forward left!")
        elif move_direction == 1: # Agent 1 right movement has the best heuristic and moves right
            self.move_first_agent_forward_right()
            print("Agent 1 moved forward right!")
        elif move_direction == 2: # Agent 2 left movement has the best heuristic and moves left
            self.move_second_agent_forward_left()
            print("Agent 2 moved forward left!")
        elif move_direction == 3: # Agent 2 right movement has the best heuristic and moves right
            self.move_second_agent_forward_right()
            print("Agent 2 moved forward right!")
        elif move_direction == 4: # Agent 3 left movement has the best heuristic and moves left
            self.move_third_agent_forward_left()
            print("Agent 3 moved forward left!")
        elif move_direction == 5: # Agent 3 right movement has the best heuristic and moves right
            self.move_third_agent_forward_right()
            print("Agent 3 moved forward right!")
        elif move_direction == 6: # Agent 4 left movement has the best heuristic and moves left
            self.move_fourth_agent_forward_left()
            print("Agent 4 moved forward left!")
        elif move_direction == 7: # Agent 4 right movement has the best heuristic and moves right
            self.move_fourth_agent_forward_right()
            print("Agent 4 moved forward right!")

        self.posible_agent_moves = []
    

# Main code
