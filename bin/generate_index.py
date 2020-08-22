import json
import os
from datetime import datetime
from random import choice

cur_dir = os.path.dirname(__file__)

with open(f"{cur_dir}/../assets/mantras.json") as mantras:
    MANTRA_LIST = json.load(mantras)["mantras"]

todays_mantra = choice(MANTRA_LIST)

with open(f"{cur_dir}/../docs/index.html", "w+") as f:

    f.write(
        f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Daily Mantra</title>
    <link rel="stylesheet" href="blue_relax.css" />
    <link rel="stylesheet" href="foundation-icons/foundation-icons.css" />
    <link
      rel="stylesheet"
      type="text/css"
      href="//fonts.googleapis.com/css?family=Josefin+Sans"
    />
  </head>
  <body>
    <div class="circle circle1"></div>
    <div class="circle circle2"></div>
    <div class="circle circle3"></div>
    <div class="circle circle4"></div>
    <div class="circle circle5"></div>
    <div class="circle circle6"></div>
    <div class="circle circle7"></div>
    <div class="circle circle8"></div>
    <div class="mantra">
      {todays_mantra['quote']}
    </div>
        <a
      href="https://github.com/kamori/daily-mantra.com"
      class="socials"
      target="_blank"
      ><i class="fi-social-github"></i> GitHub Project</a
    >
  </body>
</html>
            """
    )

print("fin")
