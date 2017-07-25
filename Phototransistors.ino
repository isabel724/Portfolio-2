//Define the photoresistor PIN (A0)
int photocellPin = A0;
 
//This variable will contain the raw value read from photoresistor
int photocellReading;
 
//Define the LED PIN 10 (PWM)
int LEDpin = 10;
 
//This variable contains the brightness of the LED
int LEDbrightness;
 
void setup(void) {
}
 
void loop(void) {
    //Read the value from ptohoresistor
    photocellReading = analogRead(photocellPin);
 
    //Map the ptohoresistor reading to 0,255
    //to set correctly the LED brightness
    LEDbrightness = map(photocellReading, 0, 1023, 0, 255);
 
    //Set the LED brightness
    analogWrite(LEDpin, LEDbrightness*6);
 
    delay(50);
}
