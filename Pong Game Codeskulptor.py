import simplegui
import random

v = [0, 0]
time = 0
cs_key = " "
sp = [0, 0]
bal_vel = [2, 2]
key_pressed = " "
r = 20
x = 600 
y = 400
bal_pos_init = [x/2, y/2]
left_line_x = [4, y/2]
left_line_y = [4, y/2 + 100]
right_line_x = [596, y/2]
right_line_y = [596, y/2 + 100]
score_left = 0
score_right = 0
LEFT = False
RIGHT = True
random_num = random.randrange(0, 2)



#Define Key_Down

def keydown(key):
    global left_line_x, v, cs_key, left_line_y, key_pressed, sp
    cs_key = key
    
    if key == simplegui.KEY_MAP["up"]: 
        v[1] = -7
        key_pressed = "up"
            
    if key == simplegui.KEY_MAP["down"]:
        v[1] = 7
        key_pressed = "down"
        
    if key == simplegui.KEY_MAP["w"]:
        sp[1] = -7
        cs_key = "w"
    
    if key == simplegui.KEY_MAP["s"]:
        sp[1] = 7
        cs_key = "s"

        
#Define Draw Functions
        
def draw_circle(canvas):
    global bal_pos_init, bal_vel, score_right, score_left
    bal_pos_init[0] -= bal_vel[0]
    bal_pos_init[1] += bal_vel[1]    
    
    if bal_pos_init[1] >= y - r:
        bal_vel[1] = -bal_vel[1]        
    
    if bal_pos_init[1] <= r:
        bal_vel[1] = -bal_vel[1]  
    
    if bal_pos_init[0] < (left_line_x[0] + r) and bal_pos_init[1] in range(left_line_x[1], left_line_y[1]) :
        bal_vel[0] = -bal_vel[0]
    
    if bal_pos_init[0] > (right_line_x[0] - r) and bal_pos_init[1] in range(right_line_x[1], right_line_y[1]) :
        bal_vel[0] = -bal_vel[0]
    
    if bal_pos_init[0] < 0 and bal_pos_init[1] not in range(left_line_x[1], left_line_y[1]):
        bal_vel[0] = 0
        bal_vel[1] = 0
    
    if bal_pos_init[0] > x and bal_pos_init[1] not in range(right_line_x[1], right_line_y[1]) :
        bal_vel[0] = 0
        bal_vel[1] = 0
    
    if bal_pos_init[0] < 1:
        score_right += 1
        print score_right       
    
    if bal_pos_init[0] > x:
        score_left += 1
        print score_left     
    new_game()               
    canvas.draw_circle(bal_pos_init, r, 6, 'White')

#Draw Left Paddle    
def left_line(canvas):
    global left_line_x,left_line_y
    if left_line_x[1] >= 0 and key_pressed == "up": 
        left_line_x[1] = left_line_x[1] + v[1]
        left_line_y[1] = left_line_y[1] + v[1]
    if left_line_y[1] <= 400 and key_pressed == "down": 
        left_line_x[1] = left_line_x[1] + v[1]
        left_line_y[1] = left_line_y[1] + v[1]            
    canvas.draw_line(left_line_x, left_line_y, 8, 'White')

# Draw Right Paddle
def right_line(canvas):
    global right_line_x,right_line_y
    if right_line_x[1] >= 0 and cs_key == "w": 
        right_line_x[1] = right_line_x[1] + sp[1]
        right_line_y[1] = right_line_y[1] + sp[1]
    if right_line_y[1] <= 400 and cs_key == "s": 
        right_line_x[1] = right_line_x[1] + sp[1]
        right_line_y[1] = right_line_y[1] + sp[1]  
    canvas.draw_line(right_line_x, right_line_y, 8, 'White')

#Draw Middle Line
def middle_line(canvas):
    canvas.draw_line([x/2, 0], [x/2, y], 2, 'White')

#Draw Left Score Line
def gutter_left_line(canvas):
    canvas.draw_line([12, 0], [4, 400], 1, "White")

#Draw Right Score Line   
def gutter_right_line(canvas):
    canvas.draw_line([588, 0], [596, 400], 1, "White")

#Draw Score Board - Right Side        
def right_score(canvas):
    canvas.draw_text(str(score_right), (530, 50), 50, "White")

#Draw Score Board - Left Side       
def left_score(canvas):
    canvas.draw_text(str(score_left), (70, 50), 50, "White")

#Combine All Draw Handlers    
def draw_it(canvas):
    draw_circle(canvas)
    left_line(canvas)
    middle_line(canvas)
    right_line(canvas)
    gutter_left_line(canvas)
    gutter_right_line(canvas)
    right_score(canvas)
    left_score(canvas)

#Define New Game
def new_game():
    global bal_pos_init, bal_vel, score_right, score_left, left_line_x, left_line_y
    global right_line_x, right_line_y, LEFT, random_num
    if bal_pos_init[0] < 1:
        bal_pos_init[0] = x/2
        bal_pos_init[1] = random.randrange(20, 350)
        bal_vel[0] = -(random.randint(4, 15))
        bal_vel[1] = -(random.randint(1, 3))
        left_line_x = [4, y/2]
        left_line_y = [4, y/2 + 100]
        right_line_x = [596, y/2]
        right_line_y = [596, y/2 + 100]
    if bal_pos_init[0] > x:
        left_line_x = [4, y/2]
        left_line_y = [4, y/2 + 100]
        right_line_x = [596, y/2]
        right_line_y = [596, y/2 + 100]
        bal_pos_init[0] = x/2
        bal_pos_init[1] = random.randrange(20, 350)
        bal_vel[0] = (random.randint(4, 15))
        bal_vel[1] = (random.randint(1, 3))
    goal()        

#Define Scoring Function            
def goal():
    global score_right, score_left
    if bal_pos_init[0] < 1:
        score_right += 1
        print score_right
        
    if bal_pos_init[0] > x:
        score_left += 1
        print score_left

#Define Key UP Events            
def keyup(key):
    global cs_key, v
    v[1] = 0
    sp[1] = 0

    
#Timer Function
def tick():
    global time, bal_vel
    if bal_vel[1] > 0:
        bal_vel[1] += 0.5
    if bal_vel[1] < 0:
        bal_vel[1] -= 0.5
    if bal_vel[0] > 0:
        bal_vel[0] += 0.5
    if bal_vel[0] < 0:
        bal_vel[0] -= 0.5
    print bal_vel

#Reset Function
def reset():
    global score_right, bal_vel, score_left, left_line_x, left_line_y
    global right_line_x, right_line_y
    left_line_x = [4, y/2]
    left_line_y = [4, y/2 + 100]
    right_line_x = [596, y/2]
    right_line_y = [596, y/2 + 100]
    bal_pos_init[0] = x/2
    bal_pos_init[1] = random.randrange(20, 350)
    bal_vel[0] = random.randrange(1, 10)
    bal_vel[1] = random.randrange(1, 10)
    score_right = 0
    score_left = 0

    
    
timer = simplegui.create_timer(1000, tick)    
frame = simplegui.create_frame("Testing", x, y)
frame.set_draw_handler(draw_it)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", reset, 200)




frame.start()
timer.start()

