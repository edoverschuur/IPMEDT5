const int BUTTON = 10;
bool pressed = false;

void setup(){
    pinMode(BUTTON, INPUT_PULLUP);
    Serial.begin(9600);

}

void loop(){
    if(!digitalRead(BUTTON)){
        delay(10);
        if (!digitalRead(BUTTON)){
            if(!pressed){
                pressed = true;
                Serial.println('b');
            }

        }
    }else{
        pressed = false;
    }
}