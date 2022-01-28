#define pinkie A0
#define ring A1
#define middle A2
#define index A3
#define thumb A4

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.print(analogRead(pinkie));
  Serial.print('\t');
  Serial.print(analogRead(ring));
  Serial.print('\t');
  Serial.print(analogRead(middle));
  Serial.print('\t');
  Serial.print(analogRead(index));
  Serial.print('\t');
  Serial.print(analogRead(thumb));
  delay(1000);
}
