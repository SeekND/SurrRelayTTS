# This repository contains game code for Surrogate SDK in operating a game with relays (or a virtual keyboard) and TTS.



What do you need:

- Raspberry pi 3b (minimum)
- Capture card and HDMI cable to connect to your PC(eg: https://www.amazon.co.uk/gp/product/B08FCFRRQT )
- Surrogate SDK imaged
- Speaker (optional) (eg: https://www.amazon.co.uk/gp/product/B07QYFFNK5 )
- Understanding on how programming works (specifically python)
- Relay (eg: https://www.amazon.co.uk/ELEGOO-Optocoupler-Compatible-Official-Raspberry/dp/B06XKQQXKW )
- Two push switches to end the game or give a win


The code:

- The code available allows for 6 relays signals (or 6 contacts on a arduino beetle which you can use as a virtual keyboard) connected to Raspi pins: 19, 13, 6, 20, 16, 12
- The code available also allows for two trigger buttons that will give win ( pin 26) or lose (pin 5)
- Also available is code for the arduino beetle in order to trigger keypresses in your keyboard

How does it work:

- Once configured and the game is available in Surrogate.tv when a player hits a predefined key in the game that will trigger your raspberry pi to action the command it's configured for, being that triggering a relay or pressing a key in your keyboard.
- The capture card connected to your pc will relay the video and sound (if configured) present on your screen directly to the gane page.


A full step by step video explanation on how to apply the code is available for my patreons in https://www.patreon.com/carlitouniverse
