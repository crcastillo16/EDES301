# Coding: UTF-8
"""
----------------------------------------------------------------
Blink USR3 LED
----------------------------------------------------------------
Licnese:
Copyright 2026 Cristian Castillo

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Blinks the USR3 LED on PocketBeagle at 5 Hz (5 full on/off cycles per second) using the Adafruit BBIO library.Blinks

Press Ctrl+C to stop the program

---------------------------------------------------------------------------
"""

import time
import Adafruit_BBIO.GPIO as GPIO

LED         = "USR3"
FREQUENCY   = 5                     # Hz full on/off cycles per second
HALF_PERIOD = 1.0 / (2*FREQUENCY)   # 0.1 seconds

GPIO.setup(LED, GPIO.OUT) #Tells liibrary that USR3 is an output.

    
try:
    while True:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(HALF_PERIOD)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(HALF_PERIOD)
except KeyboardInterrupt:
    pass                        # Ctrl+C is the way to stop so we want no message
finally:
    GPIO.output(LED, GPIO.LOW)  # leave the LED off
    GPIO.cleanup()              # release the pin
