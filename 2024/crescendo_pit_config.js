var config_data = `
{
  "dataFormat": "tsv",
  "title": "Scouting PASS 2024",
  "page_title": "Crescendo",
  "pitConfig": "true",
  "prematch": [
    { "name": "Robot",
      "type": "header"
    },
    { "name": "Team Number",
      "code": "t",
      "type": "number"
    },
    { "name": "Cool Robot Name",
      "code": "crn",
      "type": "text"
    },
    { "name": "Width(in)",
      "code": "wid",
      "type": "number",
      "defaultValue": "0"
    },
    { "name": "Length(in)",
      "code": "len",
      "type": "number",
      "defaultValue": "0"
    },
    { "name": "Weight(lbs)",
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
    { "name": "Gear Ratio",
      "code": "gr",
      "type": "text",
      "size": 20,
      "maxSize": 50
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
    { "name": "Points",
      "type": "header"
    },
    { "name": "Can Leave Starting Zone",
    "code": "lst",
    "type": "bool"
    },
    { "name": "Pickup From",
      "code": "tpu",
      "type": "radio",
      "choices": {
        "s": "Source<br>",
        "f": "Floor<br>",
        "b": "Both<br>",
        "x": "Neither"
      },
      "defaultValue": "x"
    },
    { "name": "Cycle Time(s)",
    "code": "cyt",
    "type": "text",
    "defaultValue": "x"
    },
    { "name": "Auto Amp Score",
      "code": "aas",
      "type": "counter"
    },
    { "name": "Auto Speaker Score",
      "code": "ass",
      "type": "counter"
    },
    { "name": "Teleop Amp Score",
    "code": "tas",
    "type": "counter"
    },
    { "name": "Teleop Speaker Score",
      "code": "tss",
      "type": "counter"
    },
    { "name": "Reliable Shooting Distance(ft)",
      "code": "rsd",
      "type": "number",
      "defaultValue": "0"
    },
    { "name": "Designated Human Player?",
    "code": "hp",
    "type": "bool"
    },
    { "name": "Climb Time(s)",
    "code": "cbt",
    "type": "text",
    "defaultValue": "x"
    },
    { "name": "Climb Status",
      "code": "fs",
      "type":"radio",
      "choices": {
        "c": "Can't Climb<br>",
        "s": "Single Climb<br>",
        "d": "Double Climb<br>"
      },
      "defaultValue": "c"
    },
    { "name": "Can Score Note in Trap",
      "code": "nit",
      "type": "bool"
    },
    { "name": "Positions",
      "type": "header"
    },
    { "name": "Auto Start Position",
    "code": "as",
    "type": "clickable_image",
    "filename": "2024/field_image.png",
    "clickRestriction": "one",
    "allowableResponses": "1 12 13 24 25 36 37 48 49 60 61 72",
    "shape": "circle 5 black red true"
  },
    { "name": "Shooting Positions",
    "code": "sp",
    "type": "clickable_image",
    "filename": "2024/field_image_half.png",
    "shape": "circle 5 black red true"
    },
    { "name": "Misc.",
      "type": "header"
    },
    { "name": "Defense/Offense",
      "code": "do",
      "type":"radio",
      "choices": {
        "d": "Defense<br>",
        "o": "Offense<br>",
        "x": "Doesn't Matter<br>"
      },
      "defaultValue": "c"
    },
    { "name": "Scouting Amount",			
      "code": "sa",
      "type": "radio",
      "choices": {
        "l": "Alot<br>",
        "f": "Few<br>",
        "n": "None<br>",
        "o": "Other<br>"
      },
      "defaultValue": "o"
    },
    { "name": "What Do They Do In Auto?",
      "code": "autoco",
      "type": "text",
      "size": 20,
      "maxSize": 250
    },
    { "name": "Comments",
      "code": "co",
      "type": "text",
      "size": 20,
      "maxSize": 250
    },
    { "name": "Coolness😎(1-10)",
      "code": "cn",
      "type": "counter"
    }
  ],
  "auton": [
  ],
  "teleop": [
  ],
  "endgame": [
  ],
  "postmatch": [
  ]
}`;
