radio.onReceivedString(function (receivedString) {
    serial.writeString(receivedString)
    led.toggle(0, 0)
})
let buttonVal = 0
let y_bar = 0
let x_bar = 0
let res = ""
radio.setGroup(1)
radio.setTransmitPower(7)
serial.redirectToUSB()
serial.setTxBufferSize(1000)
serial.setRxBufferSize(1000)
serial.setBaudRate(BaudRate.BaudRate4800)
// serial.write_value("x=", x_bar)
// serial.write_value("y=", y_bar)
// serial.write_value("b=", buttonVal)
basic.forever(function () {
    res = serial.readString()
    if (res.isEmpty()) {
        x_bar = pins.analogReadPin(AnalogReadWritePin.P0)
        y_bar = pins.analogReadPin(AnalogReadWritePin.P1)
        buttonVal = pins.analogReadPin(AnalogReadWritePin.P2)
        radio.sendValue("x", x_bar)
        radio.sendValue("y", y_bar)
        radio.sendValue("button", buttonVal)
    } else {
        radio.sendString(res)
        led.toggle(4, 0)
    }
})
