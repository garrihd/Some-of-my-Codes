# implementation of card game - Memory

import simplegui
import random


#Assign Globals
num = ''
list_a = list(range(8))
list_b = list(range(8))
list_c = list_a + list_b
pos_of_card = [0, 0]
matches = []
non_matches = []
state = 0
turns = 0
pos_of_click = [0,0]


# helper function to initialize globals
def new_game():
    random.shuffle(list_c)
    print (list_c)
    global state, matches, turns
    global exposed
    exposed = [False for x in range(16)]
    matches = []
    state = 0
    turns = 0
    label.set_text(str(turns))
    

# define event handlers
def mouseclick(pos):
    global chances
    global state, turns
    label.set_text(str(turns))
    if state == 0:
        matches.append(pos[0]//50)
        exposed[pos[0] // 50] = True
        state = 1
        turns += 1
        
    elif state == 1:
        if not(pos[0] // 50 in matches):
            matches.append(pos[0] // 50)
            state = 2
        exposed[pos[0] // 50] = True
        turns += 1
            
    else:	
         if not (pos[0] // 50 in matches):
            if list_c[matches[-1]]!=list_c[matches[-2]]:
                exposed[matches[-1]] = False
                exposed[matches[-2]] = False
                matches.pop(), matches.pop()
                turns += 0
                
            state = 1
    
            exposed[pos[0] // 50] = True
            matches.append(pos[0] // 50)

                                    

# cards are logically 50x100 pixels in size    
def draw(canvas):
    global num, pos_of_click 
    for card_index in range(16):
        card_pos = 50 * card_index + 15
        pos_of_card = [card_pos, 70]
        canvas.draw_text(str(list_c[card_index]), pos_of_card, 40, 'White')
    for j in range(16):
        canvas.draw_polygon([[50 * j, 0], [50 * j, 0], [50 * j, 100], [50 * j, 100]], 100, 'Green')
    for x in range(16): 
        canvas.draw_line([50 * x, 100], [50 * x, 0], 1, "white")
        for c in matches:
            canvas.draw_text(str(list_c[c]), [15+50*c, 70], 40, 'White')
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label(str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric