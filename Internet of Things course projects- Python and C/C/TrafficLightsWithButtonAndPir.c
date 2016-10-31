#include <stdio.h>    // Used for printf() statements
#include <wiringPi.h> // Include WiringPi library!

// Pin number declarations. We're using the Broadcom chip pin numbers.
const int butPin = 16; // Active-low button - Broadcom pin 17, P1 pin 11

const int liike = 21; 
const int nappi = 16; 



const int vihrea1 = 5; 
const int keltainen1 = 27; 
const int punainen1 = 17; 

const int vihrea2 = 18; 
const int keltainen2 = 24; 
const int punainen2 = 20; 




int main(void)
{
    // Setup stuff:
    wiringPiSetupGpio(); // Initialize wiringPi -- using Broadcom pin numbers
    
    pinMode(vihrea1, OUTPUT);     // Set regular LED as output
    pinMode(keltainen1, OUTPUT);     // Set regular LED as output
    pinMode(punainen1, OUTPUT);     // Set regular LED as output
    pinMode(vihrea2, OUTPUT);     // Set regular LED as output
    pinMode(keltainen2, OUTPUT);     // Set regular LED as output
    pinMode(punainen2, OUTPUT);     // Set regular LED as output
    
    pinMode(butPin, INPUT);      // Set button as INPUT
    pullUpDnControl(butPin, PUD_UP); // Enable pull-up resistor on button

    printf("Blinker is running! Press CTRL+C to quit.\n");
    
    digitalWrite(vihrea2, HIGH);
    digitalWrite(punainen1, HIGH);


    // Loop (while(1)):
    while(1)
    {
         
        if (0==digitalRead(nappi)) 
        {
    	    digitalWrite(keltainen1, HIGH);
       	    printf("Nappia painettu.\n");

    	    int i = 0;
    	    while (i < 200) {
				delay(10);
				if (1==digitalRead(liike))
				{
					delay(60); //jos liiketta havaitaan, kaksinkertaistetaan viive
					printf("Auto tulee.\n");
				}
			i++;
			} 
			printf("vaihdetaan valoja.\n");
    	    digitalWrite(vihrea2, LOW);
    	    digitalWrite(keltainen2, HIGH);
    	    delay(700); 
    	    digitalWrite(keltainen2, LOW);
    	    digitalWrite(punainen2, HIGH);
    	    digitalWrite(keltainen1, LOW);
    	    delay(700); 
    	    digitalWrite(punainen1, LOW);
    	    digitalWrite(vihrea1, HIGH);
    	     
    	    delay(5000); 
    	    
    	    //vaihdetaan takaisin
    	    printf("vaihdetaan valoja.\n");
    	    digitalWrite(vihrea1, LOW);
       	    delay(700); 

            digitalWrite(punainen1, HIGH);
    	    delay(700); 
            
    	    digitalWrite(punainen2, LOW);
    	    digitalWrite(keltainen2, HIGH);
    	    delay(700); 
    	    digitalWrite(keltainen2, LOW);
    	    digitalWrite(vihrea2, HIGH);    	     
    	    
    	    
    	    
    	    //poista lopussa
    	    
            
        }
        delay(75); 
    }

    return 0;
}
