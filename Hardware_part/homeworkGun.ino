#include <SoftwareSerial.h>
#include <Wire.h>

#define CLOCK 2 // blue
#define VSYNC 3 // green
#define PIN_START 4
#define PIN_END 11
// D0-YELLOW,,D1-BROWN,,D2-ORANGE,,D3-WHITE,,D4-GREY,,D5-PURPLE,,D6-WHITE,,D7-BROWN
#define BAUD_RATE 9600
#define BUTTON 12

void setup() {
  pinMode(BUTTON, INPUT_PULLUP);
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  if (digitalRead(BUTTON) == LOW) {
    // Serial.println("Button pressed!");
    Serial.print(0, DEC);
    delay(1000);
    }

  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
}