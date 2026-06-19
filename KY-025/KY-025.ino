const int LED_PIN  = 13;
const int REED_PIN = 2;

int digitalVal;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  pinMode(REED_PIN, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  digitalVal = !digitalRead(REED_PIN);  // invert: LOW=closed=1, HIGH=open=0

  digitalWrite(LED_PIN, digitalVal);
  Serial.println(digitalVal);  // prints 0 or 1
  delay(100);
}
