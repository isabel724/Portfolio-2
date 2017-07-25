void setup() {
  for (int i = 2; i<=8 ; i++){
    pinMode(i, OUTPUT);
  }
}

void loop() {
  for (int i = 2; i<=8; i++) {
    for(int fadeValue = 0 ; fadeValue <= 255; fadeValue +=5) {
      analogWrite(i, fadeValue);
      delay(30);
    }
    for(int fadeValue = 255 ; fadeValue >= 0; fadeValue -=5) { 
      analogWrite(i, fadeValue);
      delay(30);
    } 
  }
  for (int i = 7; i>=3; i--) {
    for(int fadeValue = 0 ; fadeValue <= 255; fadeValue +=5) {
      analogWrite(i, fadeValue);
      delay(30);
    }
    for(int fadeValue = 255 ; fadeValue >= 0; fadeValue -=5) { 
      analogWrite(i, fadeValue);
      delay(30);
    } 
  }
}
