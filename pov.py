import time
import random
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import board
import neopixel
from colorpallette import colors

pixel_pin = board.D12
hall_sensor = digitalio.DigitalInOut(board.D5)
hall_sensor.direction = digitalio.Direction.INPUT
hall_sensor.pull = Pull.UP


num_pixels = 8

ORDER = neopixel.GRBW

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.3, auto_write=False, pixel_order=ORDER
)
# ---- Pallete import ----#
col = [
    colors.CYAN,
    colors.PEACH,
    colors.CYBER,
    colors.MAGENTA,
    colors.MINT,
    colors.GREEN,
    colors.RED,
    colors.YELLOW,
]



current_mills = 0
previous_mills = 0



y = 0

# ---- Delay between characters ----#
space = 0.4
delayTime = 0.000002
blink = 0.01
dlay = random.randint(1,20)




state = 0
lastState = 0
one_rot_time = 0
previous_mills = 0


elapse = 0
elapsed_counter = 0
previous_mills = 0
counter_1 = 0
one_rot_time = 0
time_per_deg = 0

l = 3
k = 0
rainbow = random.randint(0,7)
k = rainbow
x = col[4]


while True:

    letter_a = [ x,x,x,x,0,
                 x,0,x,0,0,
                 x,0,x,0,0,
                 0,x,x,x,x,
                 0,0,0,0,0,
             ]
    letter_b = [x,x,x,x,x,
                x,0,x,0,x,
                0,x,0,x,0,
                0,0,0,0,0
            ]
    letter_c = [0,x,x,x,0,
                x,0,0,0,x,
                x,0,0,0,x,
            ]
    letter_d = [x,x,x,x,x,
            x,0,0,0,x,
            0,x,x,x,0,
            ]
    letter_e = [x,x,x,x,x,
                x,0,x,0,x,
                x,0,x,0,x,
                x,0,x,0,x,
                0,0,0,0,0,
            ]
    letter_f = [x,x,x,x,x,
            0,0,x,0,x,
            0,0,x,0,x,
            ]
    letter_g = [0,x,x,x,0,
            x,0,0,0,x,
            x,x,x,0,x,
            ]
    letter_h = [x,x,x,x,x,
            0,0,x,0,0,
            x,x,x,x,x,
            ]
    letter_i = [0,0,0,0,0,
                0,0,0,0,0,
                x,x,x,x,x,
                0,0,0,0,0,
                0,0,0,0,0,
            ]
    letter_j = [0,x,0,0,x,
            x,0,0,0,x,
            0,x,x,x,x,
            ]
    letter_k = [0,0,0,0,0,
                x,x,x,x,x,
                0,0,x,0,0,
                0,x,0,x,0,
                x,0,0,0,x
            ]
    letter_l = [x,x,x,x,x,
                0,0,0,0,x,
                0,0,0,0,x,
                0,0,0,0,x,
                0,0,0,0,0,
            ]
    letter_m = [x,x,x,x,x,
                0,0,x,x,0,
                x,x,x,x,x,
            ]
    letter_n = [x,x,x,x,x,
                0,x,0,0,0,
                0,0,x,0,0,
                0,0,0,x,0,
                x,x,x,x,x

            ]
    letter_o = [0,x,x,x,0,
            x,0,0,0,x,
            x,0,0,0,x,
            0,x,x,x,0,
            ]
    letter_p = [x,x,x,x,x,
            0,0,x,0,x,
            0,0,0,x,0,
            ]
    letter_q = [0,0,x,x,0,
            0,0,x,0,x,
            0,x,x,x,x,
            ]
    letter_r = [x,x,x,x,x,
                x,0,x,0,0,
                x,0,x,x,0,
                0,x,0,0,x,
                0,0,0,0,0
            ]
    letter_s = [x,0,x,x,0,
            x,0,x,0,x,
            0,x,x,0,x,
            ]
    letter_t = [0,0,0,0,x,
            x,x,x,x,x,
            0,0,0,0,x,
            ]
    letter_u=  [x,x,x,x,x,
            x,0,0,0,0,
            x,x,x,x,x,
            ]
    letter_v = [0,x,x,x,0,
            x,0,0,0,0,
            0,x,x,x,0,
            ]
    letter_w = [x,x,x,x,0,
            0,x,0,0,0,
            x,x,x,x,0,
            ]
    letter_x = [0,x,0,x,0,
            0,0,x,0,0,
            0,x,0,x,0,
            ]
    letter_y = [x,0,0,0,0,
                0,x,0,0,0,
                0,0,x,x,0,
                0,x,0,0,0,
                x,0,0,0,0,
            ]
    letter_z = [x,x,x,0,x,
            x,0,x,0,x,
            x,0,0,x,x,
            ]
    number_0 = [x,x,x,x,x,
            x,0,0,0,x,
            x,x,x,x,x,
            ]
    number_1 = [x,0,0,x,0,
            x,x,x,x,x,
            x,0,0,0,0,
            ]
    number_2 = [x,x,x,0,0,
            x,0,x,0,x,
            x,0,x,x,0,
            ]
    number_3 = [0,x,0,x,0,
            x,0,x,0,x,
            x,x,0,x,x,
            ]
    number_4 = [0,0,x,0,0,
            0,0,x,x,0,
            x,x,x,x,x,
            ]
    number_5 = [x,0,x,x,x,
            x,0,x,0,x,
            x,x,x,0,x,
            ]
    number_6= [x,x,x,x,x,
            x,0,x,0,x,
            x,x,x,0,x,
            ]
    number_7 = [0,0,0,0,x,
            x,x,x,0,x,
            0,0,0,x,x,
            ]
    number_8 = [x,x,x,x,x,
            x,0,x,0,x,
            x,x,x,x,x,
            ]
    number_9 = [0,0,x,x,x,
            x,0,x,0,x,
            x,x,x,x,x,
            ]
    heart = [0,x,x,0,0,
             x,0,0,x,0,
             0,x,0,0,x,
             x,0,0,x,0,
             0,x,x,0,0
             ]


    l = 3
    k = 0
    rainbow = random.randint(0,7)
    k = rainbow
    x = col[4]
    line = (delayTime * 2)

    def print_Letter(list):
        for i in range(5):
            pixels[i] = list[i]

        pixels.show()
        pixels.fill(0)
        time.sleep(d)
        pixels.show()

        for i in range(5):
            pixels[i] = list[i+5]

        pixels.show()
        pixels.fill(0)
        time.sleep(d)
        pixels.show()

        for i in range(5):
            pixels[i] = list[i+10]

        pixels.show()
        pixels.fill(0)
        time.sleep(d)
        pixels.show()

        for i in range(5):
            pixels[i] = list[i+15]

        pixels.show()
        pixels.fill(0)
        time.sleep(d)
        pixels.show()

        for i in range(5):
            pixels[i] = list[i+20]

        pixels.show()
        pixels.fill(0)
        time.sleep(d)
        pixels.show()
        #time.sleep(space)
    def dino():
        pixels[0] = 0
        pixels[1] = colors.GREEN
        pixels[2] = colors.GREEN
        pixels[3] = 0
        pixels[4] = 0
        pixels[5] = 0
        pixels[6] = 0
        pixels[7] = 0
        pixels.show()
        #time.sleep(d)
        pixels[0] = 0
        pixels[1] = colors.GREEN
        pixels[2] = colors.GREEN
        pixels[3] = 0
        pixels[4] = colors.GREEN
        pixels[5] = 0
        pixels[6] = 0
        pixels[7] = 0
        pixels.show()
        #time.sleep(d)
        pixels[0] = colors.GREEN
        pixels[1] = colors.GREEN
        pixels[2] = colors.GREEN
        pixels[3] = colors.WHITE
        pixels[4] = colors.WHITE
        pixels[5] = colors.WHITE
        pixels[6] = colors.WHITE
        pixels[7] = colors.GREEN
        pixels.show()
        #time.sleep(d)
        pixels[0] = colors.GREEN
        pixels[1] = 0
        pixels[2] = colors.GREEN
        pixels[3] = colors.WHITE
        pixels[4] = colors.GREEN
        pixels[5] = colors.WHITE
        pixels[6] = colors.WHITE
        pixels[7] = 0
        pixels.show()
        #time.sleep(d)
        pixels[0] = colors.GREEN
        pixels[1] = colors.GREEN
        pixels[2] = colors.GREEN
        pixels[3] = colors.GREEN
        pixels[4] = colors.GREEN
        pixels[5] = colors.GREEN
        pixels[6] = colors.GREEN
        pixels[7] = colors.GREEN
        pixels.show()
        #time.sleep(d)
        pixels[0] = colors.RED
        pixels[1] = 0
        pixels[2] = colors.RED
        pixels[3] = 0
        pixels[4] = colors.RED
        pixels[5] = 0
        pixels[6] = colors.GREEN
        pixels[7] = 0
        pixels.show()
        #time.sleep(d)
        pixels[0] = 0
        pixels[1] = 0
        pixels[2] = 0
        pixels[3] = 0
        pixels[5] = colors.GREEN
        pixels[6] = 0
        pixels[7] = 0
        pixels.show()
        #time.sleep(d)
        pixels[0] = 0
        pixels[1] = colors.GREEN
        pixels[2] = colors.GREEN
        pixels[3] = 0
        pixels[5] = 0
        pixels[6] = 0
        pixels[7] = 0
        pixels.show()
        #time.sleep(d)
        pixels.fill(0)
        pixels.show()



    #print(hall_sensor.value)
    tm = time.monotonic()
    current_mills = tm

    elasped_counter = current_mills - previous_mills
    delayTime = time_per_deg * 3.5
    d = (delayTime * 4)
    if((elasped_counter >= time_per_deg * (180)) and (elasped_counter < time_per_deg * (181))):

        print("hello")
        """print_Letter(letter_r)
        #time.sleep(d)
        print_Letter(letter_i)
        #time.sleep(d)
        print_Letter(letter_l)
        #time.sleep(d)
        print_Letter(letter_e)
        #time.sleep(d)
        print_Letter(letter_y)
        #time.sleep(d)"""

        dino()



    current_count = tm
    if hall_sensor.value is True:
        counter_1 = current_count

    if hall_sensor.value is False:

        one_rot_time = current_count - counter_1
        time_per_deg = one_rot_time / 360
        previous_mills = tm
        k += 1
        if k > 7:
            k =0





# Write your code here :-)
