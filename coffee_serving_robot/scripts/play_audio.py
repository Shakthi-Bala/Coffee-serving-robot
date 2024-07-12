#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from gtts import gTTS
from playsound import playsound
from rospkg import RosPack
import os
import tempfile

# Get the path to the package using RosPack
rospack = RosPack()
package_path = rospack.get_path("coffee_serving_robot")

audio_folder = os.path.join(package_path, "audio")

def text_to_speech_callback(data):

    command = data.data

    sentence_mapping = {
        "1":"Ready to serve delicious coffee",
        "2":"Heading to the coffee making space",
        "3":"Please press the button after loading the coffee",
        "4":"Heading to the Customer",
        "5":"Please press the button after picking the coffee",
        "6":"Returning to the home position"
    }

    audio_filename = command + ".mp3"
    audio_path = os.path.join(audio_folder, audio_filename)
    
    # Check if an audio file exists for the received string
    if command in sentence_mapping and os.path.isfile(audio_path):
        pass
        
    else:
        # If not, use gTTS to generate and save the audio file
        speech_text = sentence_mapping[command]
        tts = gTTS(text=speech_text, lang='en')
        audio_path = os.path.join(audio_folder, audio_filename)
        tts.save(audio_path)

    # Play the audio file
    playsound(audio_path, block=True)

if __name__ == '__main__':
    rospy.init_node('sound_player_node')
    
    rospy.Subscriber('/notification_command', String, text_to_speech_callback)

    rospy.spin()
