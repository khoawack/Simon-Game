import random
import time
from adafruit_circuitplayground import cp

x = 0
y = 1
data = []
data_player = 0
lights_loop = 0
correct = True

#contains all functions and starts game
def start_game():
    global correct
    global y
    global t

    while True:
        if cp.button_a:
            print('start game')
            time.sleep(1.5)
            while correct == True:
                random_gen()
                game_data()
                for z in data:
                    y = z
                    set_lights()
                for x in data:
                    t = x

                    touch_light()
                    checker()

                if correct == True:
                    correct_light()
            return

# generates random int
def random_gen():
    global x
    random_number = [1,2,3,4]
    x =(random.choice(random_number))
    print ("x is", x)
    return x

# plays green correct light sequence
def correct_light ():
        cp.pixels.brightness = 0.05
        cp.pixels.fill((0, 255, 0))
        cp.play_tone(415, 1)
        time.sleep(2)
        cp.pixels.fill((0, 0, 0))

#add to array and prints array out
def game_data():
    data.append(x)
    print (data)

# the light sequence that plays
def set_lights():

    #green
    if y == 1:
        cp.pixels.brightness = 0.05
        cp.pixels[0] = (0, 255, 0)
        cp.pixels[1] = (0, 255, 0)
        cp.pixels[2] = (0, 255, 0)
        cp.play_tone(415, .5)
        time.sleep(.5)
        cp.pixels[0] = (0, 0, 0)
        cp.pixels[1] = (0, 0, 0)
        cp.pixels[2] = (0, 0, 0)
        time.sleep(.5)
        return


    #yellow
    if y == 2:
        cp.pixels.brightness = 0.05
        cp.pixels[2] = (255, 255, 0)
        cp.pixels[3] = (255, 255, 0)
        cp.pixels[4] = (255, 255, 0)
        cp.play_tone(252, .5)
        time.sleep(.5)
        cp.pixels[2] = (0, 0, 0)
        cp.pixels[3] = (0, 0, 0)
        cp.pixels[4] = (0, 0, 0)
        time.sleep(.5)
        return


    #red
    if y == 3:
        cp.pixels.brightness = 0.05
        cp.pixels[7] = (255, 0, 0)
        cp.pixels[8] = (255, 0, 0)
        cp.pixels[9] = (255, 0, 0)
        cp.play_tone(310, .5)
        time.sleep(.5)
        cp.pixels[7] = (0, 0, 0)
        cp.pixels[8] = (0, 0, 0)
        cp.pixels[9] = (0, 0, 0)
        time.sleep(.5)
        return



    #blue
    if y == 4:
        cp.pixels.brightness = 0.05
        cp.pixels[5] = (0,0,255)
        cp.pixels[6] = (0,0,255)
        cp.pixels[7] = (0,0,255)
        cp.play_tone(209, .5)
        time.sleep(.5)
        cp.pixels[5] = (0, 0, 0)
        cp.pixels[6] = (0, 0, 0)
        cp.pixels[7] = (0, 0, 0)
        time.sleep(.5)
        return

#light sensor on taps
def touch_light():
    global data_player

    while True:
         if cp.touch_A4 or cp.touch_A5:
            print("Green")
            data_player += 1
            print(data_player)
            cp.pixels.brightness = 0.05
            cp.pixels[0] = (0, 255, 0)
            cp.pixels[1] = (0, 255, 0)
            cp.pixels[2] = (0, 255, 0)
            cp.play_tone(415, .5)
            time.sleep(.5)
            cp.pixels[0] = (0, 0, 0)
            cp.pixels[1] = (0, 0, 0)
            cp.pixels[2] = (0, 0, 0)
            return


            #Yellow
         if cp.touch_A6:
            print("Yellow")
            data_player += 2
            print(data_player)
            cp.pixels.brightness = 0.05
            cp.pixels[2] = (255, 255, 0)
            cp.pixels[3] = (255, 255, 0)
            cp.pixels[4] = (255, 255, 0)
            cp.play_tone(252, .5)
            time.sleep(.5)
            cp.pixels[2] = (0, 0, 0)
            cp.pixels[3] = (0, 0, 0)
            cp.pixels[4] = (0, 0, 0)
            return



            #Red
         if cp.touch_A3 or cp.touch_A2:
            print("Red")
            data_player += 3
            print(data_player)
            cp.pixels.brightness = 0.05
            cp.pixels[7] = (255, 0, 0)
            cp.pixels[8] = (255, 0, 0)
            cp.pixels[9] = (255, 0, 0)
            cp.play_tone(310, .5)
            time.sleep(.5)
            cp.pixels[7] = (0, 0, 0)
            cp.pixels[8] = (0, 0, 0)
            cp.pixels[9] = (0, 0, 0)
            return



        #blue
         if cp.touch_A1:
            print("Blue")
            data_player += 4
            print(data_player)
            cp.pixels.brightness = 0.05
            cp.pixels[5] = (0, 0, 255)
            cp.pixels[6] = (0, 0, 255)
            cp.pixels[7] = (0, 0, 255)
            cp.play_tone(209, .5)
            time.sleep(.5)
            cp.pixels[5] = (0, 0, 0)
            cp.pixels[6] = (0, 0, 0)
            cp.pixels[7] = (0, 0, 0)
            return


#checks to see if right or wrong
def checker():
    global data_player
    global t


    if t == data_player:
        data_player = 0
        t = 0
        print ('correct')
        return
    else:
        global correct
        print('wrong')
        correct = False
        cp.pixels.brightness = 0.05
        cp.pixels.fill((255, 0, 0))
        cp.play_tone(100, 1)
        time.sleep(2)
        cp.pixels.fill((0, 0, 0))
        t = 0
        return



start_game()
