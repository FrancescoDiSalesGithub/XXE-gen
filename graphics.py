class graphics:

    def banner(self):
        print("###################################")
        print("XXE-GEN")
        print("###################################")

    def help(self):
        print("")
        print("HELP ")
        print("python3 xxe-gen.py [operation] [entity]")
        print("")
        print("[operation] = what do you want to do with the XXE vulnerability")
        print("[entity] = the name of the xml entity")
        print("")
        print("possible operations: ")
        print("- injection -> does a classic xxe")
        print("- dos -> does a dos xxe")
        print("")
        print("example usage:")
        print("")
        print("python3 xxe-gen.py injection banana")
        print("python3 xxe-gen.py dos banana")