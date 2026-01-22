def on_received_string(receivedString):
    serial.write_string(receivedString)
    led.toggle(0, 0)
radio.on_received_string(on_received_string)

buttonVal = 0
item = 0
def button():
    global buttonVal, item
    buttonVal = pins.analog_read_pin(AnalogReadWritePin.P2)
    if buttonVal < 256:
        item = 1
    elif buttonVal < 597:
        item = 2
    elif buttonVal < 725:
        item = 3
    elif buttonVal < 793:
        item = 4
    elif buttonVal < 836:
        item = 5
    elif buttonVal < 938:
        item = 6
    else:
        item = 0

res = ""
radio.set_group(1)
serial.redirect_to_usb()
serial.set_tx_buffer_size(1000)
serial.set_rx_buffer_size(1000)
serial.set_baud_rate(BaudRate.BAUD_RATE4800)
images.create_image("""
    . . . . .
    . . . . .
    . . . . .
    # . . . #
    . # # # .
    """).show_image(0)

def on_forever():
    global res
    res = serial.read_string()
    if res.is_empty():
        pass
    else:
        radio.send_string(res)
        led.toggle(4, 0)

    button()
    if item:
        basic.show_number(item)
    elif pins.analog_read_pin(AnalogReadWritePin.P0) < 400:
        basic.show_string("-X")
    elif pins.analog_read_pin(AnalogReadWritePin.P0) > 600:
        basic.show_string("+X")
    elif pins.analog_read_pin(AnalogReadWritePin.P1) < 400:
        basic.show_string("-Y")
    elif pins.analog_read_pin(AnalogReadWritePin.P1) > 600:
        basic.show_string("+Y")
    else:
        basic.clear_screen()

basic.forever(on_forever)
