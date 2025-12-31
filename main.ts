radio.onReceivedString(function (receivedString) {
    serial.writeString(receivedString)
})
let res = ""
radio.setGroup(1)
serial.redirectToUSB()
serial.setTxBufferSize(1000)
serial.setRxBufferSize(1000)
serial.setBaudRate(BaudRate.BaudRate9600)
images.createImage(`
    . . . . .
    . . . . .
    # . . . #
    . # # # .
    . . . . .
    `).showImage(0)
basic.forever(function () {
    res = serial.readString()
    if (res.isEmpty()) {
    	
    } else {
        radio.sendString(res)
    }
})
