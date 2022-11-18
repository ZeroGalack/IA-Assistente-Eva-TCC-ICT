#define P1 13
#define P2 12
#define P3 11


#define R 3
#define G 5
#define B 6

int vl;


void setup() {
  Serial.begin(9600);
  pinMode(P1, OUTPUT);
  pinMode(P2, OUTPUT);
  pinMode(P3, OUTPUT);

  pinMode(R, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(B, OUTPUT);
}

void loop() {
 if (Serial.available() > 0) {
    vl = Serial.parseInt();

    if (vl == 77){//SetHome Lucas C
      digitalWrite(P1, 1);
      analogWrite(R, 0);
      analogWrite(G, 0);
      analogWrite(B, 255);
    }
    if (vl == 44){//SetHome Lucas F
      digitalWrite(P1, 1);
      analogWrite(R, 0);
      analogWrite(G, 255);
      analogWrite(B, 0);
    }
    if (vl == 55){//SetHome Thais
      digitalWrite(P1, 1);
      analogWrite(R, 255);
      analogWrite(G, 102);
      analogWrite(B, 0);
    }
    if (vl == 22){//SetHome William
      digitalWrite(P1, 1);
      analogWrite(R, 255);
      analogWrite(G, 0);
      analogWrite(B, 255);
    }
    if (vl == 33){//SetHome Miguel
      digitalWrite(P1, 1);
      analogWrite(R, 255);
      analogWrite(G, 0);
      analogWrite(B, 0);
    }

    if (vl == -1){
      digitalWrite(P1, 0);
      analogWrite(R, 0);
      analogWrite(G, 0);
      analogWrite(B, 0);
    }

    if (vl == 2){
      digitalWrite(P1, 1);
      delay(500);
      digitalWrite(P1, 0);
      delay(500);
      digitalWrite(P1, 1);
      delay(500);
      digitalWrite(P1, 0);
      delay(500);
      digitalWrite(P1, 1);
    }

    if (vl == 3){
      digitalWrite(P2, 1);
    }
    if (vl == -3){
      digitalWrite(P2, 0);
    }

    if (vl == 4){
      digitalWrite(P3, 1);
    }
    if (vl == -4){
      digitalWrite(P3, 0);
    }
  }

}
