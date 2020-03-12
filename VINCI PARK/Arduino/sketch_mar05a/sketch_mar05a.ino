/* Constantes pour les broches */
const byte TRIGGER_PIN1 = 2; // Broche TRIGGER
const byte ECHO_PIN1 = 3; // Broche ECHO
 
/* Constantes pour le timeout */
const unsigned long MEASURE_TIMEOUT1 = 25000UL; // 25ms = ~8m à 340m/s

/* Vitesse du son dans l'air en mm/us */
const float SOUND_SPEED1 = 340.0 / 1000;

const float distance_min1 = 200 ;// distance minimale en mm 


void setup() {
/* Initialise le port série */
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  Serial.begin(115200);
   
  /* Initialise les broches */
  
  pinMode(TRIGGER_PIN1, OUTPUT);
  digitalWrite(TRIGGER_PIN1, LOW); // La broche TRIGGER doit être à LOW au repos
  pinMode(ECHO_PIN1, INPUT);  
}

void loop() {
  /* 1. Lance une mesure de distance en envoyant une impulsion HIGH de 10µs sur la broche TRIGGER */
  digitalWrite(TRIGGER_PIN1, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER_PIN1, LOW);


  
  /* 2. Mesure le temps entre l'envoi de l'impulsion ultrasonique et son écho (si il existe) */
  long measure1 = pulseIn(ECHO_PIN1, HIGH, MEASURE_TIMEOUT1);
     
  /* 3. Calcul la distance à partir du temps mesuré */
  float distance_mm1 = measure1 / 2.0 * SOUND_SPEED1;

  if(distance_mm1 < distance_min1) {
   
    /* Affiche les résultats en mm, cm et m */
    Serial.print(F("Distance: "));
    Serial.print(distance_mm1);
    Serial.print(F("mm ("));
    Serial.print(distance_mm1 / 10.0, 2);
    Serial.print(F("cm, "));
    Serial.print(distance_mm1 / 1000.0, 2);
    Serial.println(F("m)"));
    
    digitalWrite(10, HIGH);   // turn the LED on (HIGH is the voltage level)
    digitalWrite(11, LOW);
     
    /* Délai d'attente pour éviter d'afficher trop de résultats à la seconde */
    delay(500);
  }else{
    digitalWrite(10, LOW);
    digitalWrite(11, HIGH);  
  }                    
}
