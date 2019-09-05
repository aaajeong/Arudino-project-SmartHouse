import serial
import speech_recognition as sr

arduino = serial.Serial('COM10',9600)

while(1):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Speak Anything:')
        audio = r.listen(source, timeout=1, phrase_time_limit=10)

    try:
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))
        c=text
        if c =='q':
            break
        else:
            c=c.encode('utf-8')
            arduino.write(c)
    except:
        print('Sorry could not recognize your voice')

#     Serial.println( "-----------------" );  
#     Serial.println( "available command:" );  
#     Serial.println( "turn on all" ); 
#     Serial.println( "turn off all" ); 
#     Serial.println( "turn on the green light" );  
#     Serial.println( "turn off the green light" );  
#     Serial.println( "turn on the redn light" );  
#     Serial.println( "turn off the red light" );  
#     Serial.println( "turn on the yellow light" );  
#     Serial.println( "turn off the yellow light" );  
#     Serial.println( "-----------------" );
