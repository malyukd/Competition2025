
float toMv(float val){
  return (val*5*10)/1024;
}

void setup() {
  Serial.begin(115200);

}

void loop() {
  float ekg = toMv(analogRead(A5));
  float emg = toMv(analogRead(A0));
  Serial.print(ekg);
  Serial.print(" ");
  Serial.println(emg);


  delay(50);

}

