                   ]#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <ArduinoJson.h>
#include <HTTPClient.h>
#include <Servo.h>

#define SSID "embeddo_ext"
#define PASSWD "72230F4F4A"

#define N1 14
#define N2 27

#define N3 26
#define N4 25

Servo servo1;
Servo servo2;

int x = 70;
int y = 140;

String msg;

HTTPClient http;

void setup(){
  Serial.begin(9600);

  pinMode(N1, OUTPUT);
  pinMode(N2, OUTPUT);
  pinMode(N3, OUTPUT);
  pinMode(N4, OUTPUT);

  WiFi.begin(SSID,PASSWD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println(".");
  }
  Serial.println("Conectado!");

  servo1.attach(13);
  servo2.attach(12);

  servo1.write(x);
  servo2.write(y);
}

void loop() {
    WiFiClientSecure client;
    HTTPClient http;
    client.setInsecure();

    http.useHTTP10(true);
    http.begin(client, "https://test7.lucasteixeira23.repl.co/r");
    int httpCode = http.GET();

    if (httpCode > 0) {

        DynamicJsonDocument doc(2048);
        deserializeJson(doc, http.getStream());
        msg = doc.as<String>();
        if (msg != ""){
          Serial.println(msg);

if(msg == "andar para frente"){
  Serial.println("ligando o hot wheels");
     digitalWrite(N1, LOW);
     digitalWrite(N2, HIGH);
     digitalWrite(N3, LOW);
     digitalWrite(N4, HIGH);
     delay(1000);
     digitalWrite(N1, LOW);
     digitalWrite(N2, LOW);
     digitalWrite(N3, LOW);
     digitalWrite(N4, LOW);
     }

if(msg == "parar"){
  Serial.println("parando o hot wheels");
     digitalWrite(N1, LOW);
     digitalWrite(N2, LOW);
     digitalWrite(N3, LOW);
     digitalWrite(N4, LOW);
     }

if(msg == "andar para tras"){
  Serial.println("hot wheels dando ré");
     digitalWrite(N1, HIGH);
     digitalWrite(N2, LOW);
     digitalWrite(N3, HIGH);
     digitalWrite(N4, LOW);
     delay(1000);
     digitalWrite(N1, LOW);
     digitalWrite(N2, LOW);
     digitalWrite(N3, LOW);
     digitalWrite(N4, LOW);
}


if (msg == "descer garra"){
  while (y >= 45){
    servo2.write(y);
    y--;
    delay(20);
  }

  while (x <= 150){
    servo1.write(x);
    x++;
    delay(20);
  }
}


if (msg == "subir garra"){
   while (x >= 70){
    servo1.write(x);
    x--;
    delay(20);
  }

  while (y <= 140){
    servo2.write(y);
    y++;
    delay(20);
   }

}

        }

      }

    else {
        Serial.println("Falha na requisição");
    }
}