#include <Stepper.h>

const int stepsPerRevolution = 12800; 
Stepper myStepper(stepsPerRevolution,7,8);

void setup() {
  // set the speed at  rpm:
  myStepper.setSpeed(15);
  
}

void loop() {
  
  myStepper.step(stepsPerRevolution);
  
  myStepper.step(-stepsPerRevolution);
}
