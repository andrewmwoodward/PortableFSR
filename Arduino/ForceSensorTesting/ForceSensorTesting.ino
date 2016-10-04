
#include <SoftwareSerial.h>
#include <LiquidCrystal.h>

LiquidCrystal lcd(8,9,4,5,6,7);

int sensorPin1 = A8;
int sensorPin2 = A9;
int sensorPin3 = A10;




void setup() {
 
  lcd.begin(16, 2);
  lcd.setCursor(0, 0);
  lcd.print("Force Sensors");
  delay(500); // wait for display to boot up
  
}

void loop() {
  // put your main code here, to run repeatedly:
  
  int sensorValue1, sensorValue2, sensorValue3;
  
  sensorValue1 = analogRead(sensorPin1);
  sensorValue2 = analogRead(sensorPin2);
  sensorValue3 = analogRead(sensorPin3);
  
  lcd.setCursor(0,1);
  lcd.print(sensorValue1);

  lcd.setCursor(6,1);
  lcd.print(sensorValue2);
  
  lcd.setCursor(11,1);
  lcd.print(sensorValue3);

  delay(500);
}
