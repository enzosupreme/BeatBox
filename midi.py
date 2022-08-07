
import time
import board
import terminalio
import rotaryio
import busio
import digitalio
import neopixel
from colorpallette import colors
from adafruit_debouncer import Debouncer
import usb_midi
import adafruit_midi
from adafruit_midi.note_on          import NoteOn
from adafruit_midi.note_off         import NoteOff

pixel_pin = board.GP16
#  MIDI setup as MIDI out device
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)


# ----- Rotary Encoder ---- #
encoder = rotaryio.IncrementalEncoder(board.GP20, board.GP19)
last_position = None
button = digitalio.DigitalInOut(board.GP18)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_state = None

#  array for LEDs
leds = []
led_pins = [board.GP2,board.GP1,board.GP0,board.GP5,board.GP4,board.GP3]
#  setup to create the AW9523 outputs for LEDs
for pin in led_pins:
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    leds.append(led)



#  button pins, all pins in order skipping GP15
note_pins = [board.GP6,board.GP7,board.GP8,board.GP11,board.GP10,board.GP9]

note_buttons = []

for pin in note_pins:
    note_pin = digitalio.DigitalInOut(pin)
    note_pin.direction = digitalio.Direction.INPUT
    note_pin.pull = digitalio.Pull.UP
    note_buttons.append(note_pin)

#  note states
note0_pressed = False
note1_pressed = False
note2_pressed = False
note3_pressed = False
note4_pressed = False
note5_pressed = False

#  array of note states
note_states = [note0_pressed, note1_pressed, note2_pressed, note3_pressed,
               note4_pressed, note5_pressed]


sub_state = False
#  default midi number
midi_num = 60
#  default MIDI button
button_num = 0
#  default MIDI button position
button_pos = 0
#  check for blinking LED
led_check = None
#  time.monotonic() device
clock = time.monotonic()


#  array of default MIDI notes


num_pixels = 8

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.3, auto_write=False, pixel_order=ORDER
)

#midi_notes = [60, 61, 62, 63, 64, 65]

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





while True:

    position = (encoder.position)
    while position >= 8:
        position = 0
    while position < 0:
        position +=8

    if last_position is None or position != last_position:
        last_position = position


    if position is 0:
        midi_notes = [79,80,81,76,77,78]
    if position is 1:
        midi_notes = [75,74,73,70,71,72]
    if position is 2:
        midi_notes = [67,68,69,64,65,66]
    if position is 3:
        midi_notes = [61,62,63,58,59,60]
    if position is 4:
        midi_notes = [55,56,57,52,53,54]
    if position is 5:
        midi_notes = [49,50,51,46,47,48]
    if position is 6:
        midi_notes = [43,44,45,40,41,42]
    if position is 7:
        midi_notes = [37,38,39,34,35,36]

    pixels.fill(0)
    pixels.show()
    time.sleep(0.001)
    pixels[position] = col[position]
    pixels.show()

    #  MIDI input
    for i in range(6):
        buttons = note_buttons[i]
        #  if button is pressed...
        if not buttons.value and note_states[i] is False:
            #  send the MIDI note and light up the LED
            midi.send(NoteOn(midi_notes[i], 120))
            note_states[i] = True
            leds[i].value = True
        #  if the button is released...
        if buttons.value and note_states[i] is True:
            #  stop sending the MIDI note and turn off the LED
            midi.send(NoteOff(midi_notes[i], 120))
            note_states[i] = False
            leds[i].value = False



