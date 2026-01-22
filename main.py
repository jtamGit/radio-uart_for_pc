def on_received_string(receivedString):
    serial.write_string(receivedString)
    led.toggle(0, 0)
radio.on_received_string(on_received_string)

buttonVal = 0
y_bar = 0
x_bar = 0
res = ""
radio.set_group(1)
radio.set_transmit_power(7)
serial.redirect_to_usb()
serial.set_tx_buffer_size(1000)
serial.set_rx_buffer_size(1000)
serial.set_baud_rate(BaudRate.BAUD_RATE4800)
# serial.write_value("x=", x_bar)
# serial.write_value("y=", y_bar)
# serial.write_value("b=", buttonVal)

def on_forever():
    global res, x_bar, y_bar, buttonVal
    res = serial.read_string()
    if res.is_empty():
        pass
    else:
        radio.send_string(res)
        led.toggle(4, 0)
    x_bar = pins.analog_read_pin(AnalogReadWritePin.P0)
    y_bar = pins.analog_read_pin(AnalogReadWritePin.P1)
    buttonVal = pins.analog_read_pin(AnalogReadWritePin.P2)
    radio.send_value("x", x_bar)
basic.forever(on_forever)
