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
    { "name": "Robot Info",
      "type": "header"
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
        "f": "Falcon/Kraken<br>",
        "c": "CIM<br>",
        "x": "Other<br>"
      },
      "defaultValue":"x"
    },


    { "name": "General Game Info",
      "type": "header"
    },
    { "name": "Defense/Offense focused",
      "code": "do",
      "type":"radio",
      "choices": {
        "d": "Defense<br>",
        "o": "Offense<br>",
        "x": "Doesn't Matter<br>"
      },
      "defaultValue": "c"
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
    { "name": "Cycle Times(s) (Time to grab note)",
    "code": "cyt",
    "type": "text",
    "defaultValue": "x"
    },
    { "name": "Reliable Shooting Distance(ft)",
      "code": "rsd",
      "type": "number",
      "defaultValue": "0"
    },
    { "name": "Shooting Positions",
    "code": "sp",
    "type": "clickable_image",
    "filename": "2024/field_image_half.png",
    "shape": "circle 5 black red true"
    },



    { "name": "Auto",
      "type": "header"
    },
    { "name": "What Do They Do In Auto?",
      "code": "autoco",
      "type": "text",
      "size": 20,
      "maxSize": 250
    },
    { "name": "Auto: Can Leave Starting Zone",
    "code": "lst",
    "type": "bool"
    },
    { "name": "Auto Amp Score",
      "code": "aas",
      "type": "counter"
    },
    { "name": "Auto Speaker Score",
      "code": "ass",
      "type": "counter"
    },
    { "name": "Auto Start Position",
    "code": "as",
    "type": "clickable_image",
    "filename": "2024/field_image_half.png",

    "allowableResponses": "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24",
    "shape": "circle 5 black red true"
    },



    { "name": "Teleop",
      "type": "header"
    },
    { "name": "Teleop Amp Score",
    "code": "tas",
    "type": "counter"
    },
    { "name": "Teleop Speaker Score",
      "code": "tss",
      "type": "counter"
    },



    { "name": "Endgame",
      "type": "header"
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
    { "name": "Climb Time(s)",
    "code": "cbt",
    "type": "text",
    "defaultValue": "x"
    },
    { "name": "Can Score Note in Trap",
      "code": "nit",
      "type": "bool"
    },
    { "name": "Designated Human Player?",
    "code": "hp",
    "type": "bool"
    },



    { "name": "Misc.",
      "type": "header"
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
    { "name": "Final Comments",
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
