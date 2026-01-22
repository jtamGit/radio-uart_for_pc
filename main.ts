radio.onReceivedString(function (receivedString) {
    serial.writeString(receivedString)
    led.toggle(0, 0)
})
let res = ""
radio.setGroup(1)
radio.setTransmitPower(7)
serial.redirectToUSB()
serial.setTxBufferSize(1000)
serial.setRxBufferSize(1000)
serial.setBaudRate(BaudRate.BaudRate4800)
basic.forever(function () {
    res = serial.readString()
    if (res.isEmpty()) {
    	
    } else {
        radio.sendString(res)
        led.toggle(4, 0)
    }
})
