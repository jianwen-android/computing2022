/* Arduino master left hand */

#include <Arduino.h>

int data1[5];

int pinkie;
int ring;
int middle;
int index;
int thumb;
// static const uint8_t analog_pins[] = {A0,A1,A2,A3,A4}

void setup() {
  Serial.begin(38400);

}

void loop() {
  pinkie = analogRead(A0);
  ring   = analogRead(A1);
  middle = analogRead(A2);
  index  = analogRead(A3);
  thumb  = analogRead(A4);
  for (byte i = 0; i < 6; i = i + 1) {
    data1[i] = analogRead(i)
  }
  Serial.write(data1);
  delay(10); // delay for performance
}
