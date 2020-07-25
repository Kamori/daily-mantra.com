import os
from datetime import datetime

cur_dir = os.path.dirname(__file__)

with open(f"{cur_dir}/../docs/index.html", "w+") as f:
    f.write(f"Test {datetime.now()}")


print("fin")
