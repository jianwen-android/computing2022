#define thumb A4
#define index A3
#define middle A2
#define ring A1
#define pinkie A0

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.print(analogRead(pinkie));
  Serial.print(", ");
  Serial.print(analogRead(ring));
  Serial.print(", ");
  Serial.print(analogRead(middle));
  Serial.print(", ");
  Serial.print(analogRead(index));
  Serial.print(", ");
  Serial.print(analogRead(thumb));
  delay(1000);
}
