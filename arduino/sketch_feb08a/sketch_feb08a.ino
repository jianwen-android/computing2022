float thumb;
int index;
int middle;
int ring;
int pinkie;

int fat;

void setup() {
  Serial.begin(9600);
}

void loop() {
  //thumb = map(analogRead(A0), 313, 866, 0, 553);
  fat = analogRead(A0);
  thumb = processFunc(analogRead(A0), 313, 866);
  //index = map(analogRead(A1), 0, 1023, 492, 9 92);
  //middle = map(analogRead(A2), 0, 1023, 521, 988);
  //ring = map(analogRead(A3), 0, 1023, 498, 920);
  //pinkie = map(analogRead(A4), 0, 1023, 285, 606);
  Serial.println(thumb);
  Serial.println(fat);
  //Serial.print(", ");
  //Serial.print(index);
  //Serial.print(", ");
  //Serial.print(middle);
  //Serial.print(", ");
  //Serial.print(ring);
  //Serial.print(", ");
  //Serial.println(pinkie);
  //Serial.print(", ");
}

float processFunc(float current, float minimun, float maximun) {
  float result = (current-minimun) / (maximun-minimun);
  return result;
}

//313,492,521,498,285 r
// 866,992,988,920,606
