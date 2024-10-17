import sys

from src.core import main
from src.deeplchain import log, mrh

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print()
            log(mrh + f"Successfully logged out of the bot\n")
            sys.exit()
