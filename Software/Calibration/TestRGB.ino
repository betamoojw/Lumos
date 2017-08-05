//Calibration code to calibrate R,G,B values for Individual Colors.

int b = 9;
int r = 10;
int g = 11;


void setup() {
  // put your setup code here, to run once:
pinMode(r,OUTPUT);
pinMode(g,OUTPUT);
pinMode(b,OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
//rgb(200,75,0);
//rgb(200,60,0);//yellow
//rgb(200,45,0);//
//rgb(200,30,0);//orange
//rgb(200,15,0);
//rgb(150,15,0);//reddish orange
//rgb(150,15,30);
//rgb(120,150,180);//bluish white
//rgb(220,220,180);//white ish
//rgb(5,5,10);//grey blue
//rgb(100,255,120);//white
//rgb(200,15,0);
//rgb(255,0,0);
//rgb(0,0,255);
rgb(0,150,150);
}

void rgb(int R, int G, int B)
{
  analogWrite(r,R);
  analogWrite(g,G);
  analogWrite(b,B);
}
