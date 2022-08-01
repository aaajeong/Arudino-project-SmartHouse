# Smart House

### Description

스마트하우스는 음성인식을 이용한 아두이노 프로젝트입니다.
사용자는 음성으로 다음과 같은 기능을 말하면 스마트 하우스는 해당 기능을 작동합니다.

'''
Serial.println( "-----------------" );  
Serial.println( "available command:" );  
Serial.println( "turn on all" ); 
Serial.println( "turn off all" ); 
Serial.println( "turn on the green light" );  
Serial.println( "turn off the green light" );  
Serial.println( "turn on the redn light" );  
Serial.println( "turn off the red light" );  
Serial.println( "turn on the yellow light" );  
Serial.println( "turn off the yellow light" );  
Serial.println( "-----------------" );
'''


### File

1. mario_buzzer: arduino file
2. oled_test: arduino file
3. Smart House.ipynb: python file for jupyter notebook
4. Smart_House.py: python file 

### Execute

First, Install the python package.
pip install speechrecognition : speech to text
pip install pyaudio 

python Smart_House.py
또는
Smart_House.ipynb 실행