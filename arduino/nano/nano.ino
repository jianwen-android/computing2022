#define thumb A0
#define index A1
#define middle A2
#define ring A3
#define pinkie A4

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.print(analogRead(pinkie));
  Serial.print(",");
  Serial.print(analogRead(ring));
  Serial.print(",");
  Serial.print(analogRead(middle));
  Serial.print(",");
  Serial.print(analogRead(index));
  Serial.print(",");
  Serial.print(analogRead(thumb));
}
