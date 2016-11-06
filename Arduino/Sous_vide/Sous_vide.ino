//---------------------------------------------------------
//  Sous vide cooker
//  author: dlofstrom
//  date: 2016-11-06
//  
//  TODOS:
//  - Create user flow
//  - PID temperature regulator
//  - User serial as debug port
//      data on/off
//  - Store settings in EEPROM
//      Pump speed
//      PID coefficients
//      Temperature calibration
//      Temperature range
//  
//---------------------------------------------------------
#include <LiquidCrystal.h>

//LCD Pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

int pot = 0;
int temp = 0;

void setup() {
  //16x2 Display
  lcd.begin(16, 2);

  //Blink
  pinMode(13,OUTPUT);

  //Initial message
  lcd.print("Sous vide cooker");
  delay(5000);
}


void loop() {
  lcd.setCursor(0, 1);
  lcd.print("                ");
  
  lcd.setCursor(0, 1);
  pot = analogRead(3);
  lcd.print(pot);

  lcd.setCursor(8,1);
  temp = map(pot, 0, 1023, 25, 85);
  lcd.print(temp);
  
  digitalWrite(13,HIGH);
  delay(1000);
  digitalWrite(13,LOW);
  delay(1000);
}
