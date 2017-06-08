from optimized import detectColour
import sys
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: scriptfinal dictionaryFile imageFile\n")
        exit(1)

    detectColour(sys.argv[1], sys.argv[2])
