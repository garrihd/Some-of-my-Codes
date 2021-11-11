# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
a = 0
b = 0
c = 0
d = 0
win = 0
total = 0
watch = False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global a, b, c, d
    a = t // 600
    b = t % 600 / 100
    b1 = t // 10
    b2 = b1 % 60
    c = b2 % 10
    if t < 10:
        d = t
    else:
        d = t % 10
    return str(a) + ":" + str(b) + str(c) +"." + str(d)  
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def  start():
    global watch
    timer.start()
    watch = True
    return watch

def stop():
    global watch, total, win, d
    timer.stop()
    if watch == True:
        total += 1
        if d == 0:
            win += 1
    watch = False        
    return win, watch

def reset():
    global time, win, total
    win = 0
    time = 0
    total = 0

    
def clock():
    global time, loss
    time += 1
    format(time)
    print (format(time))
    return time
    
def draw_handler(canvas):
    global time, win, loss
    canvas.draw_text(format(time), (80, 150), 50, 'Red')
    canvas.draw_text((str(win) + "/" + str(total)), (200, 30),30, "Green")



    
#def score():
    #global win, loss, d

# define event handler for timer with 0.1 sec interval

   
# define draw handler
timer = simplegui.create_timer(100, clock)

    
# create frame

frame = simplegui.create_frame("Testing", 300, 300)
frame.set_draw_handler(draw_handler)
frame.start()


# register event handlers
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)

# start frame





# Please remember to review the grading rubric
