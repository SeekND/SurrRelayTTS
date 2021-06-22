/*
  KeyboardAndMouseControl

  Controls the mouse from five pushbuttons on an Arduino Leonardo, Micro or Due.

  Hardware:
  - five pushbuttons attached to D2, D3, D4, D5, D6

  The mouse movement is always relative. This sketch reads four pushbuttons, and
  uses them to set the movement of the mouse.

  WARNING: When you use the Mouse.move() command, the Arduino takes over your
  mouse! Make sure you have control before you use the mouse commands.

  created 15 Mar 2012
  modified 27 Mar 2012
  by Tom Igoe

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/KeyboardAndMouseControl
*/

#include "Keyboard.h"

// review raspberry pi pins here: https://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/

// start by connecting a ground pin from beetle to raspi

const int upButton = 11; // D11 > connect to raspi GPIO 20
const int downButton = 10; // D10 > connect to raspi GPIO 6

const int leftButton = 9; // D9 > connect to raspi GPIO 12
const int rightButton = 3; // SCL > connect to raspi GPIO 16

const int attackButton = 2; // SDA > connect to raspi GPIO 13
const int defendButton = 0; // rx > connect to raspi GPIO 19

void setup() { // initialize the buttons' inputs:
  pinMode(upButton, INPUT);
  pinMode(downButton, INPUT);
  pinMode(leftButton, INPUT);
  pinMode(rightButton, INPUT);
  pinMode(attackButton, INPUT);
  pinMode(defendButton, INPUT);

  Serial.begin(9600);
  Keyboard.begin();
}

void loop() {

  // use the pushbuttons to control the keyboard, if you want to use another letter in the keyboard simply change the letter after keyboard.write
  if (digitalRead(upButton) == HIGH) {
    Keyboard.write('w');
  }
  if (digitalRead(downButton) == HIGH) {
    Keyboard.write('s');
  }
  if (digitalRead(leftButton) == HIGH) {
    Keyboard.write('a');
  }
  if (digitalRead(rightButton) == HIGH) {
    Keyboard.write('d');
  }
  if (digitalRead(attackButton) == HIGH) {
    Keyboard.write('q');
  }
  if (digitalRead(defendButton) == HIGH) {
    Keyboard.write('e');
  }

}
