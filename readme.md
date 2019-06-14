## Camera skill
In principle this should be a skill that allows the Mycroft Home AI to take a photo on command. How successful we are in making that happen remains to be seen...

From original readme:

## Description
Take pictures with webcam, share image objects with other processes, send image file path in messagebus

You should make this a priority skill, it is meant to be used by other skills


## Examples

* "take a picture"


## Using webcam in other skills

If you want to get a file path for the latest picture you can use the
messagebus to get a file path


    def initialize(self):
        self.add_event("webcam.picture", self.get_the_feed)
        self.emitter.emit(Message("webcam.request"))


    def get_the_feed(self, message):
        file_path = message.data.get("path")


you can also get the latest webcam frame as a numpy array by using the
Camera class, ensure webcam is a priority skill!

    from shared_camera import Camera

    c = Camera()
    frame = c.get()

## email and privacy

there is an option to send taken pictures by mail in addition to storing them

your emails can be read by Mycroft Home, for privacy reasons this is not
used and you need to edit your configuration file

        ~/.mycroft/mycroft.conf

if it does not exist create it, this file must be valid json, add the
following to it

        "email": {
            "email": "send_from@gmail.com",
            "password": "SECRET",
            "destinatary": "send_to@gmail.com"
        }

email will now be sent from here, the destinatary is the same email if not
provided

skill settings were not used or your email and password would be stored in
mycroft home backend



## Credits
JarbasAI
