import xxe_builder
import sys

if __name__ == "__main__":


    builder = xxe_builder.xxe_builder(sys.argv[1],sys.argv[2])
    builder.generate_injections()