from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.util import play_wav, play_mp3
from sultan.api import Sultan

from mycroft.util import play_wav

__author__ = 'Flamekebab'

# Logger: used for debug lines, like "LOGGER.debug(xyz)". These
# statements will show up in the command line when running Mycroft.
LOGGER = getLogger(__name__)

# The logic of each skill is contained within its own class, which inherits
# base methods from the MycroftSkill class with the syntax you can see below:
# "class ____Skill(MycroftSkill)"
class WebcamSkill(MycroftSkill):

    # The constructor of the skill, which calls Mycroft Skill's constructor
    def __init__(self):
        super(WebcamSkill, self).__init__(name="WebcamSkill")

    def initialize(self):
        take_picture_intent = IntentBuilder("TakePictureIntent"). \
            require("take_picture").build()
        self.register_intent(take_picture_intent, self.take_picture_intent)

    def take_picture_intent(self, message):
        self.speak_dialog("picture")
        sultan = Sultan()
        sultan.fswebcam("-r 640x480 ~/webcam/image.jpg").run()
        play_wav("camera.wav")

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, the method just contains the keyword "pass", which
    # does nothing.
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return WebcamSkill()

