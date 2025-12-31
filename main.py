def on_received_string(receivedString):
    serial.write_string(receivedString)
radio.on_received_string(on_received_string)

res = ""
radio.set_group(1)
serial.redirect_to_usb()
serial.set_tx_buffer_size(1000)
serial.set_rx_buffer_size(1000)
serial.set_baud_rate(BaudRate.BAUD_RATE9600)
images.create_image("""
    . . . . .
    . . . . .
    # . . . #
    . # # # .
    . . . . .
    """).show_image(0)

def on_forever():
    global res
    res = serial.read_string()
    if res.is_empty():
        pass
    else:
        radio.send_string(res)
basic.forever(on_forever)
