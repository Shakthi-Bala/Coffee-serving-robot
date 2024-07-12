#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from pocketsphinx import LiveSpeech

class VoiceController(object):

    def __init__(self):
        rospy.init_node('voice_controller')
        self.pub = rospy.Publisher('/cmd_vel', String, queue_size=1)

    def start(self):
        speech = LiveSpeech(
            verbose=False,
            sampling_rate=16000,
            buffer_size=2048,
            no_search=False,
            full_utt=False,
            lm=False
        )

        for phrase in speech:
            rospy.loginfo(str(phrase))
            if "forward" in str(phrase):
                self.pub.publish("forward")
            elif "backward" in str(phrase):
                self.pub.publish("backward")
            elif "left" in str(phrase):
                self.pub.publish("left")
            elif "right" in str(phrase):
                self.pub.publish("right")
            elif "stop" in str(phrase):
                self.pub.publish("stop")

if __name__ == '__main__':
    vc = VoiceController()
    vc.start()
