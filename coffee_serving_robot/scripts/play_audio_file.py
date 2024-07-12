#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from gtts import gTTS
from playsound import playsound
import tempfile

def text_to_speech_callback(data):
    text = data.data

    # Create a temporary audio file with the speech
    tts = gTTS(text=text, lang='en')
    audio_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
    tts.save(audio_file.name)
    
    # Play the audio file
    playsound(audio_file.name, block=True)

if __name__ == '__main__':
    rospy.init_node('sound_player_node')
    
    rospy.Subscriber('/notification_command', String, text_to_speech_callback)

    rospy.spin()
