import os

from dotenv import load_dotenv

load_dotenv()

NUMBER = os.environ.get("NUMBER")

if __name__ == "__main__":
    num = int(NUMBER)
    for i in range(3):
        num += i

    print(num)
