// Define model and input pin:
#define IRPin A0
#define model 20150

// Create variable to store the distance:
int IR_data;

#define sensor A0 // Sharp IR GP2Y0A02YF


const uint16_t SERVO_PERIOD = 20;       // Period of servo position control signals in milliseconds
const uint16_t SERVO_MIN_WIDTH = 900;   // Minimum servo control signal pulse width in microseconds
const uint16_t SERVO_MAX_WIDTH = 2100;  // Maximum servo control signal pulse width in microseconds
const uint8_t SERVO1 = 6;               // Servo1 control signal is connected to D9
const uint8_t SERVO2 = 7;              // Servo2 control signal is connected to D10

uint32_t servo_time;                    // Global variable to store the time of the last servo update

/*
** Returns a boolean value that indicates whether the current time, t, is later than some prior 
** time, t0, plus a given interval, dt.  The condition accounts for timer overflow / wraparound.
*/
bool it_is_time(uint32_t t, uint32_t t0, uint16_t dt) {
  return ((t >= t0) && (t - t0 >= dt)) ||         // The first disjunct handles the normal case
            ((t < t0) && (t + (~t0) + 1 >= dt));  //   while the second handles the overflow case
}

void setup() {
  // Begin serial communication at a baud rate of 9600:
  Serial.begin(9600);
  pinMode(SERVO1, OUTPUT);
  digitalWrite(SERVO1, LOW);
  pinMode(SERVO2, OUTPUT);
  digitalWrite(SERVO2, LOW);
  servo_time = millis();
}

void loop() {
  uint32_t t;
  uint16_t servo1_pos, servo2_pos;

  t = millis();
  if (it_is_time(t, servo_time, SERVO_PERIOD)) { 
    servo1_pos = 100;
    servo2_pos = 100;
    digitalWrite(SERVO1, HIGH);
    delayMicroseconds(servo1_pos);
    digitalWrite(SERVO1, LOW);
    digitalWrite(SERVO2, HIGH);
    delayMicroseconds(servo2_pos);
    digitalWrite(SERVO2, LOW);
    servo_time = t;

    // Get a IR data
  IR_data = analogRead(sensor);
  }
  
  // Print the measured distance to the serial monitor:
  Serial.println(IR_data);
  
  delay(400);
}