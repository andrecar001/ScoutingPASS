var config_data = `
{
  "dataFormat": "tsv",
  "title": "Scouting PASS 2024",
  "page_title": "Crescendo",
  "pitConfig": "true",
  "prematch": [
    { "name": "Team Number",
      "code": "t",
      "type": "number"
    },
    { "name": "Cool Robot Name",
      "code": "crn",
      "type": "text",
      "size": 20,
      "maxSize": 50
    },
    { "name": "Width",
      "code": "wid",
      "type": "number",
      "defaultValue": "0"
    },
    { "name": "Weight",
      "code": "wei",
      "type": "number",
      "defaultValue": "0"
    },
    { "name": "Drivetrain",
      "code": "drv",
      "type": "radio",
      "choices": {
        "s": "Swerve<br>",
        "w": "West Coast/Tank<br>",
        "b": "Butterfly/Grashopper<br>",
        "m": "Mechanum<br>",
        "o": "Other"
      },
      "defaultValue": "o"
    },
    { "name": "Other Drivetrain",
      "code": "odt",
      "type": "text",
      "size": 20,
      "maxSize": 50
    },
    { "name": "Input Gear Ratio",
      "code": "sr",
      "type": "radio",
      "choices": {
        "1": "L1 (8.14:1)<br>",
        "2": "L2 (6.75:1)<br>",
        "3": "L3 (6.12:1)<br>",
        "4": "L4 (5.14:1)<br>",
        "o": "Other ratio (put in comments)<br>",
        "x": "Not Swerve"
      },
      "defaultValue":"x"
    },
    { "name": "Drivetrain Motor",
      "code": "mot",
      "type": "radio",
      "choices": {
        "n": "Neo<br>",
        "f": "Falcon<br>",
        "c": "CIM<br>",
        "x": "Other<br>"
      },
      "defaultValue":"x"
    },
    { "name": "# of Batteries",
      "code": "nob",
      "type": "number"
    },
    { "name": "Floor pickup Notes",
      "code": "fpu",
      "type": "bool"
    },
    { "name": "Score Speaker?",
      "code": "ss",
      "type": "bool"
    },
    { "name": "Score Amp",
      "code": "sa",
      "type": "bool"
    },
    { "name": "Good Defense",
      "code": "def",
      "type": "bool"
    },
    { "name": "Good Driver?",
      "code": "driv",
      "type": "bool"
    },
    { "name": "Climbing",
      "code": "clmb",
      "type": "radio",
      "choices": {
        "s": "Single Climb<br>",
        "d": "Double Climb<br>",
        "x": "No"
      },
      "defaultValue": "x"
    },
    { "name": "Autos",
      "code": "aut",
      "type": "text",
      "size": 20,
      "maxSize": 250
    },
    { "name": "Do They Scout",
      "code": "dts",
      "type": "radio",
      "choices": {
        "2": "A lot<br>",
        "1": "A little<br>",
        "x": "No"
      },
      "defaultValue":"x"
    },
    { "name": "Pit Image",
      "code": "pi",
      "type": "image",
      "filename": "2024/gn_pit_map_v3.png"
    },
    {"name": "Pit Location",
      "code": "pl",
      "type": "text",
      "size": "20",
      "maxSize": 2
    },
    { "name": "Comments",
      "code": "co",
      "type": "text",
      "size": 20,
      "maxSize": 250
    }
  ],
  "auton": [
  ],
  "teleop": [
  ],
  "endgame": [
  ],
  "postmatch": [
  ],
  "qr_page": [
    { "name": "congrats_img",
      "code": "ci",
      "type": "image",
      "filename": "resources/images/pog_test.png"
    }
  ]
}`;
