import json
import os
from datetime import datetime
from random import choice

cur_dir = os.path.dirname(__file__)

MANTRA_LIST = json.load(f"{cur_dir}/../assets/mantras.json")["mantras"]

todays_mantra = choice(MANTRA_LIST)

with open(f"{cur_dir}/../docs/index.html", "w+") as f:
    f.write(f"Today's Mantra is {todays_mantra}")


print("fin")
