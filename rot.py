import time
import random
import rotaryio
from board import SCL, SDA
import board
import usb_hid
import busio
import digitalio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Debouncer
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import terminalio
from adafruit_display_text import label
from adafruit_hid.keycode import Keycode
import adafruit_ssd1306

# -----Weapon Generator---- #
"""from weapon import lootbox
from weapon import cost_roll
from weapon import weight_roll
from weapon import first_damage
from weapon import second_damage"""

i2c = busio.I2C(SCL,SDA)

display =adafruit_ssd1306.SSD1306_I2C(128,32,i2c)

switch_left_output = Keycode.Z
switch_right_output = Keycode.X

# ----- Rotary Encoder ---- #
encoder = rotaryio.IncrementalEncoder(board.D7, board.D9)
last_position = None
button = digitalio.DigitalInOut(board.D10)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_state = None

# ----- Key setup ----- #
switch_left_in = DigitalInOut(board.D11)
switch_right_in = DigitalInOut(board.D12)
switch_left_in.pull = Pull.UP
switch_right_in.pull = Pull.UP
switch_left = Debouncer(switch_left_in)
switch_right = Debouncer(switch_right_in)
total = 0
lev = 0
while True:
    weapon_type = [
    "LightHammer",
    "Warhammer",
    "MorningStar",
    "Club",
    "Mace",
    "Maul",
    "Sword",
    "Whip",
    "Handaxe",
    "LongSword",
    "Halberd",
    "GreatSword",
    "Scimitar",
    "Dagger",
    "Javelin",
    "Shortbow",
    "Rapier",
    "Lance",
    "Dart",
    "Trident",
    "War Pick",
    "Spear",
    "Crossbow",
    "Longbow",
    ]

    damage_type = [
    "Bludgeoning",
    "Slashing",
    "Piercing",
    ]
    def cost_roll(x):
        number = ((x % 7) + 1 )* 14
        max_num = number * 3
        rando = random.randint(number,max_num)
        return rando
    def weight_roll(x):
        rando = random.randint(1,12)
        number = (x % 7) + rando
        return number
    def first_damage(x): #takes argument of lvl
        number = ((x % 7) + 1 )+ 4
        rando = random.randint(1, number)
        return rando
    def second_damage(x): #takes argument of lvl
        dice = 0
        if x  > 0 and x < 5:
            dice = 4
        if x  > 4 and x < 9:
            dice = 8
        if x  > 8 and x < 13:
            dice = 10
        if x  > 12 and x < 17:
            dice = 12
        if x  > 16 and x < 21:
            dice = 20

        return dice
    def lootbox(x):
        d_type = damage_type[0]
        d = random.randint(0,2)
        r = random.randint(0,22)
        lvl = x
        if x is 0:
            lvl = random.randint(1,20)
        weapon = weapon_type[r]     #string
        if r > 0 and r < 6:
            d_type = damage_type[0]
        if r > 5 and r < 13:
            d_type = damage_type[1]
        if r > 12 and r < 23:
            d_type = damage_type[2]
        level = str(lvl)            #string
        damage1 = first_damage(lvl)
        damage2 = second_damage(lvl)
        price = cost_roll(lvl)
        w = weight_roll(lvl)

        first = str(damage1)        #string
        second = str(damage2)       #string
        cost = str(price)           #string
        weight = str(w)             #string

        full_damage = first + "d" + second  #string
        full_price = cost + " gp"
        full_weight = weight + " lb"
        #display can fit four y positions(0,8,16,24)

        display.text("lvl:",0,0,1)
        display.text(level,25,0,1)
        display.text(weapon,60,0,1)
        #display.text("Damage:",0,8,1)
        display.text("Cost:",0,16,1)
        display.text("Weight",0,24,1)

        display.text(full_damage,72,8,1)
        display.text(full_price,70,16,1)
        display.text(d_type,0,8,1)
        display.text(full_weight,72,24,1)
        display.show()
    num = 0

    def dice_roll(x):
        roll = 0
        roll = (random.randint(1,x))
        return roll


    switch_left.update()  # Debouncer checks for changes in switch state
    switch_right.update()
    position = (encoder.position + 1)
    while position > 11:
        position = 1
    while position < 1:
        position +=11
    post = str(position)



    if last_position is None or position != last_position:
        y=10
        display.fill(0) #clears display after position change
        print(position)
        button_state = None
    last_position = position

    if position is 1:
        title = "D4"
        display.text(title,58,y,1)
        num = 4
        display.show()
    if position is 2:
        title = "D6"
        display.text(title,58,y,1)
        num = 6
        display.show()
    if position is 3:
        title = "D8"
        display.text(title,58,y,1)
        num = 8
        display.show()
    if position is 4:
        title = "D10"
        display.text(title,58,y,1)
        num = 10
        display.show()
    if position is 5:
        title = "D12"
        display.text(title,58,y,1)
        num = 12
        display.show()
    if position is 6:
        title = "D20"
        display.text(title,58,y,1)
        num = 20
        display.show()
    if position is 7:
        title = "D100"
        display.text(title,58,y,1)
        num = 100
        display.show()
    if position is 8:
        title = "D10000"
        display.text(title,58,y,1)
        num = 10000
        display.show()
    if position is 9:
        title = "D69"
        display.text(title,58,y,1)
        num = 69
        display.show()
    if position is 10:
        title = "D420"
        display.text(title,58,y,1)
        num = 420
        display.show()
    if position is 11:
        title = " "
        if button_state is not "pressed":
            display.text("Weapon Generator",18,10,1)
        #num = 1
        display.show()

    if not button.value and button_state is None:
        button_state = "pressed"

    if switch_left.fell:
        if position is 11:
            display.fill(0)
            lev +=1
            if lev > 20:
                lev = 0
            l = str(lev)
            if lev is 0:
                l = "??"
            display.text("Level",50,8,1)
            display.text(l,60,16,1)
            display.show()
        else:
            x = 63
            display.fill(0)#"clears" display
            title = "Total"
            if total > 100 and total < 1000:
                x = 60
            elif total > 999:
                x = 55
            tost =str(total)
            display.text(title,53,24,1)
            display.text(tost,x,12,1)
            display.show()
            #time.sleep(1.3)
            total = 0

    if switch_right.fell:
        x = 63
        display.fill(0)

        if position is 11:
            button_state = "pressed"
            display.fill(0)
            lootbox(lev)
        else:
            display.fill(0)
            display.show()
            time.sleep(0.1)
            display.text(title,58,0,1)
            die = dice_roll(num)
            total += die
            dice = str(die)
            display.text(dice,x,10,1)
            if die > 100:
                x = 58

        print(total)
        display.show()
        y=0
        #time.sleep(1)

    pass# Write your code here :-)
