int red = 2;
int yellow = 1;
int green = 0;

void setup() {
  pinMode(red, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(green, OUTPUT);
}

void loop() {
  digitalWrite(red, HIGH);
  delay (1000);
  digitalWrite(red, LOW);
  digitalWrite(yellow, HIGH);
  delay (1000);
  digitalWrite(yellow, LOW);
  digitalWrite(green, HIGH);
  delay (1000);
  digitalWrite(green, LOW);
}

