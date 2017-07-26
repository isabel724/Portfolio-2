int photocellPin = A0;
int photocellReading;
int LEDbrightness;
 

void setup() {
  for (int i = 2; i<=8 ; i++){
    pinMode(i, OUTPUT);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  photocellReading = analogRead(photocellPin);
  LEDbrightness = map(photocellReading, 0, 1023, 0, 255);

  if (LEDbrightness < 7){
    for (int i = 2; i<=8; i++) {
      digitalWrite (i, HIGH);
      delay(30);
      digitalWrite (i, LOW);
    }
    for (int i = 7; i>=3; i--) {
      digitalWrite (i, HIGH);
      delay(30);
      digitalWrite (i, LOW);
    }
  }
}
