#include "Ultrasonic.h"
#define SENSEPIN 13

Ultrasonic ultrasonic(SENSEPIN);
int dist;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(1000);
  dist = ultrasonic.MeasureInCentimeters();
  Serial.print("The distance is\t");
  Serial.print(dist, DEC);
  Serial.print("\n");
  delay(1000);
}
