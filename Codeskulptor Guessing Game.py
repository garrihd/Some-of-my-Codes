
import random
import simplegui

number = 0
num = 0
num1 = 0
count = 0
max_count = 0

def range1000():
    global num, max_count
    max_count = 10
    num = random.randint(0, 1000)
    print "Range is (0, 1000)"
    print ""
    return num


def range100():
    global num1
    num1 = random.randint(0, 100)
    print "Range is (0, 100)"
    print ""
    return num1
 
def new_game():
    global count, max_count
    max_count = 7
    count = 0
    range100()
    
    
    

def compare100(inp):
    global number, num1, count, max_count
    
    number = int(inp)
    print "Player chose: ", number
    print "_____________"
    
    
    while count < max_count:
        if number > num1:
            print "Too big"
            count += 1
            print "Attempts left", max_count - count
            print "_____________"
            if max_count - count  == 1:
                print "Last try"
            if max_count - count == 0:
                break
            return
       
        if number < num1:
            print "Too low"
            count += 1
            print "Attempts left", max_count - count
            print "_____________"
            if max_count - count == 1:
                print "Last try"
            if max_count - count == 0:
                break
            return
        if number == num1:
            print "Correct!"
            print "It took you ", count ,"attempts !"
            new_game()
            return count
        
    if max_count - count == 0:
        print "Better luck next time ! Try again !"
        new_game()
           
    
        
        

        



frame = simplegui.create_frame("Guess the Number !", 300, 300)
frame.add_button("Range100", range100, 200)
frame.add_button("Range1000", range1000, 200)
frame.add_input('Input', compare100, 150)


frame.start()
new_game()
