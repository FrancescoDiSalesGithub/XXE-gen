import xxe_builder
import sys
import graphics

if __name__ == "__main__":

    if(sys.argv[1] == "help" or sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        graph = graphics.graphics()
        
        graph.banner()
        graph.help()
        
        sys.exit(1)

    builder = xxe_builder.xxe_builder(sys.argv[1],sys.argv[2])
    builder.generate_injections()