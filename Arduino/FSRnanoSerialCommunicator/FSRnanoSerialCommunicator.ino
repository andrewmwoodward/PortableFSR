

int sensorPin1 = A1;
int sensorPin2 = A2;
int sensorPin3 = A3;

int buttonPin = 2;
int buttonState = 0;

void setup(){
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
}

void loop(){

  buttonState = digitalRead(buttonPin);

  if(buttonState == HIGH){

    delay(2000);
     
    int i;

    for(i=0; i<120; i++){
    
      int sensorValue1, sensorValue2, sensorValue3;

      sensorValue1 = analogRead(sensorPin1);
      sensorValue2 = analogRead(sensorPin2);
      sensorValue3 = analogRead(sensorPin3);

      Serial.println(sensorValue1);
      Serial.println(sensorValue2);
      Serial.println(sensorValue3);
      Serial.println("---");
  
      delay(500);

    }

    Serial.println("End");
  
  }
}
