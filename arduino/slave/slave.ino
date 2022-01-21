#include <SoftwareSerial.h> 
SoftwareSerial left(2, 3); // RX | TX left hand
SoftwareSerial right(4, 5); // RX | TX right hand

void setup() {
  
  Serial.begin(9600);
  left.begin(9600);
  right.begin(9600);

}

void loop() {
  if (left.available()) {
    data1 = left.read();
  }
  if (right.available()) {
    data2 = right.read();
  }
  if (sizeof(data1) == 5) 

}
