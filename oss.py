from pathlib import Path
import os

print(Path(__file__).as_uri(), "\n")

print(Path("../saved").absolute().as_uri(), "\n")


print("P1",  os.path.join(Path(__file__).resolve().parent.parent , "saved"))



print("P2", os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"saved"))

import pathlib

print(pathlib.__file__)

# print(os.path.getsize(__file__))