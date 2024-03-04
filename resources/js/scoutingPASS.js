// ScoutingPASS.js
//
// The guts of the ScountingPASS application
// Written by Team 2451 - PWNAGE

document.addEventListener("touchstart", startTouch, false);
document.addEventListener("touchend", moveTouch, false);

// Swipe Up / Down / Left / Right
var initialX = null;
var xThreshold = 0.3;
var slide = 0;
var enableGoogleSheets = false;
var pitScouting = false;
var checkboxAs = 'YN';

// Options
var options = {
  correctLevel: QRCode.CorrectLevel.L,
  quietZone: 15,
  quietZoneColor: '#FFFFFF'
};

// Must be filled in: e=event, m=match#, l=level(q,qf,sf,f), t=team#, r=robot(r1,r2,b1..), s=scouter
//var requiredFields = ["e", "m", "l", "t", "r", "s", "as"];
var requiredFields = ["e", "m", "l", "r", "s", "as"];

function configure() {
  try {
    var mydata = JSON.parse(config_data);
  } catch (err) {
    console.log(`Error parsing configuration file`)
    console.log(err.message)
    console.log('Use a tool like http://jsonlint.com/ to help you debug your config file')
    var table = document.getElementById("prematch_table")
    var row = table.insertRow(0);
    var cell1 = row.insertCell(0);
    cell1.innerHTML = `Error parsing configuration file: ${err.message}<br><br>Use a tool like <a href="http://jsonlint.com/">http://jsonlint.com/</a> to help you debug your config file`
    return -1
  }

  if(mydata.hasOwnProperty('dataFormat')) {
    dataFormat = mydata.dataFormat;
  }
  
  if (mydata.hasOwnProperty('title')) {
    document.title = mydata.title;
  }

  if (mydata.hasOwnProperty('page_title')) {
    for (pgtitle of document.getElementsByClassName("page_title")) {
      pgtitle.innerHTML = mydata.page_title;
    }
  }

  if (mydata.hasOwnProperty('enable_google_sheets')) {
    if (mydata.enable_google_sheets.toUpperCase() == 'TRUE') {
      enableGoogleSheets = true;
    }
  }

  if (mydata.hasOwnProperty('pitConfig')) {
    if (mydata.pitConfig.toUpperCase() == 'TRUE') {
      pitScouting = true;
    }
  }

  function configQR() {
    
    
    const con_img = new Image()

    con_img.src = 'resources/images/carter_pog.png'
    con_img.alt = 'Congrats Image'
    con_img.id = 'congrats_img'
    con_img.height = 500
    document.getElementById('congrats').appendChild(con_img)
    let scale = 0.5
    let growing = true
    var startTime
    //Change these to last page if needed
    document.getElementById('nextButton1').addEventListener('click', onNextClick)
    document.getElementById('nextButton2').addEventListener('click', onNextClick)
    document.getElementById('nextButton9').addEventListener('click', onNextClick)
    document.getElementById('nextButton10').addEventListener('click', onNextClick)
    function onNextClick() {
      scale = 0.5
      startTime = Date.now()
      changeImageAfterDelay()
    }
  
  
    function changeImageAfterDelay() {

      con_img.style.display = ""
      let qrElement = document.getElementById('qrcode')
      
      qrElement.style.display = 'none'
      pulseImage()
      
      setTimeout(() => {
        con_img.style.display = 'none'
        qrElement.style.display = 'block'
      }, 2000)
    }
    
  
    function pulseImage() {
      if (growing) {
        scale += 0.005
      } else {
        scale -= 0.005
      }
  
      if (scale >= 1.2) {
        growing = false
      } else if (scale <= 0.8) {
        growing = true
      }
  
      con_img.style.transform = `scale(${scale})`
      if (Date.now() - startTime < 2000){
        requestAnimationFrame(pulseImage)
      }
    }
  
  }

  if (mydata.hasOwnProperty('checkboxAs')) {
    // Supported modes
    // YN - Y or N
    // TF - T or F
    // 10 - 1 or 0
    if (['YN','TF','10'].includes(mydata.checkboxAs)) {
      console.log("Setting checkboxAs to " + mydata.checkboxAs);
      checkboxAs = mydata.checkboxAs;
    } else {
      console.log("unrecognized checkboxAs setting.  Defaulting to YN.")
      checkboxAs = 'YN';
    }
  }

  // Configure prematch screen
  var pmc = mydata.prematch;
  var pmt = document.getElementById("prematch_table");
  var idx = 0;
  pmc.forEach(element => {
    idx = addElement(pmt, idx, element);
  });

  // Configure auton screen
  var ac = mydata.auton;
  var at = document.getElementById("auton_table");
  idx = 0;
  ac.forEach(element => {
    idx = addElement(at, idx, element);
  });

  // Configure teleop screen
  var tc = mydata.teleop;
  var tt = document.getElementById("teleop_table");
  idx = 0;
  tc.forEach(element => {
    idx = addElement(tt, idx, element);
  });

  // Configure endgame screen
  var egc = mydata.endgame;
  var egt = document.getElementById("endgame_table");
  idx = 0;
  egc.forEach(element => {
    idx = addElement(egt, idx, element);
  });

  // Configure postmatch screen
  pmc = mydata.postmatch;
  pmt = document.getElementById("postmatch_table");
  var idx = 0;
  pmc.forEach(element => {
    idx = addElement(pmt, idx, element);
  });

  // Configure qr screen
  configQR()

  //qr = new QRCode(document.getElementById("qrcode"), options)

  if (!enableGoogleSheets) {
    document.getElementById("submit").style.display = "none";
  }

  return 0
}

function getRobot(){
  return document.forms.scoutingForm.r.value;
}


function resetRobot() {
for ( rb of document.getElementsByName('r')) { rb.checked = false };
}


function getLevel(){
  return document.forms.scoutingForm.l.value
}


function validateData() {
  var ret = true;
  var errStr = "";
  for (rf of requiredFields) {
    var thisRF = document.forms.scoutingForm[rf];
    if (thisRF.value == "[]" || thisRF.value.length == 0) {
      if (rf == "as") {
        rftitle = "Auto Start Position"
      }
      else if (rf == "sp"){
        rftitle = "Shooting Positions"
      } else {
        thisInputEl = thisRF instanceof RadioNodeList ? thisRF[0] : thisRF;
        rftitle = thisInputEl.parentElement.parentElement.children[0].innerHTML.replace("&nbsp;","");
      }
      errStr += rf + ": " + rftitle + "\n";
      ret = false;
    }
  }
  if (ret == false) {
    alert("Enter all required values\n" + errStr);
  }
  return ret
}

function getData(dataFormat) {
  var Form = document.forms.scoutingForm;
  var UniqueFieldNames = [];
  var fd = new FormData();
  var str = [];

  switch(checkboxAs) {
    case 'TF':
      checkedChar = 'T';
      uncheckedChar = 'F';
      break;
    case '10':
      checkedChar = '1';
      uncheckedChar = '0';
      break;
    default:
      var checkedChar = 'Y';
      var uncheckedChar = 'N';
  }

  // collect the names of all the elements in the form
  var fieldnames = Array.from(Form.elements, formElmt => formElmt.name);

  // make sure to add the name attribute only to elements from which you want to collect values.  Radio button groups all share the same name
  // so those element names need to be de-duplicated here as well.
  fieldnames.forEach((fieldname) => { if (fieldname != "" && !UniqueFieldNames.includes(fieldname)) { UniqueFieldNames.push(fieldname) } });

  UniqueFieldNames.forEach((fieldname) => {
    var thisField = Form[fieldname];

    if (thisField.type == 'checkbox') {
      var thisFieldValue = thisField.checked ? checkedChar : uncheckedChar;
    } else {
      var thisFieldValue = thisField.value ? thisField.value.replace(/"/g, '').replace(/;/g,"-") : "";
    }
    fd.append(fieldname, thisFieldValue)
  })

  if (dataFormat == "kvs") {
    Array.from(fd.keys()).forEach(thisKey => {
      str.push(thisKey + "=" + fd.get(thisKey))
    });
    return str.join(";")
  } else if (dataFormat == "tsv") {
    Array.from(fd.keys()).forEach(thisKey => {
      str.push(fd.get(thisKey))
    });
    return str.join("\t")
  } else {
    return "unsupported dataFormat"
  }
}

function updateQRHeader() {
  let str = 'Event: !EVENT! Match: !MATCH! Robot: !ROBOT! Team: !TEAM!';

  if (!pitScouting) {
    str = str
      .replace('!EVENT!', document.getElementById("input_e").value)
      .replace('!MATCH!', document.getElementById("input_m").value)
      .replace('!ROBOT!', document.getElementById("display_r").value)
      .replace('!TEAM!', document.getElementById("input_t").value);
  } else {
    str = 'Pit Scouting - Team !TEAM!'
      .replace('!TEAM!', document.getElementById("input_t").value);
  }

  document.getElementById("display_qr-info").textContent = str;
}


function qr_regenerate() {
  // Validate required pre-match date (event, match, level, robot, scouter)
  if (!pitScouting) {  
    if (validateData() == false) {
      // Don't allow a swipe until all required data is filled in
      return false
    }
  }

  // Get data
  data = getData(dataFormat)

  // Regenerate QR Code
  qr.makeCode(data)

  updateQRHeader()
  return true
}

function qr_clear() {
  qr.clear()
}

function clearForm() {
  var match = 0;
  var e = 0;

  if (pitScouting) {
    swipePage(-1);
  } else {
    swipePage(-5);

    // Increment match
    match = parseInt(document.getElementById("input_m").value)
    if (match == NaN) {
      document.getElementById("input_m").value = ""
    } else {
      document.getElementById("input_m").value = match + 1
    }

    // Robot
    resetRobot()
  }

  // Clear XY coordinates
  inputs = document.querySelectorAll("[id*='XY_']");
  for (e of inputs) {
    code = e.id.substring(3)
    e.value = "[]"
  }

  inputs = document.querySelectorAll("[id*='input_']");
  for (e of inputs) {
    code = e.id.substring(6)

    // Don't clear key fields
    if (code == "m") continue
    if (code.substring(0, 2) == "r_") continue
    if (code.substring(0, 2) == "l_") continue
    if (code == "e") continue
    if (code == "s") continue

    if (e.className == "clickableImage") {
      e.value = "[]";
      continue;
    }

    radio = code.indexOf("_")
    if (radio > -1) {
      var baseCode = code.substr(0, radio)
      if (e.checked) {
        e.checked = false
        document.getElementById("display_" + baseCode).value = ""
      }
      var defaultValue = document.getElementById("default_" + baseCode).value
      if (defaultValue != "") {
        if (defaultValue == e.value) {
          e.checked = true
          document.getElementById("display_" + baseCode).value = defaultValue
        }
      }
    } else {
      if (e.type == "number" || e.type == "text" || e.type == "hidden") {
        if ((e.className == "counter") ||
          (e.className == "timer") ||
          (e.className == "cycle")) {
          e.value = 0
          if (e.className == "timer" || e.className == "cycle") {
            // Stop interval
            timerStatus = document.getElementById("status_" + code);
            startButton = document.getElementById("start_" + code);
            intervalIdField = document.getElementById("intervalId_" + code);
            var intervalId = intervalIdField.value;
            timerStatus.value = 'stopped';
            startButton.innerHTML = "Start";
            if (intervalId != '') {
              clearInterval(intervalId);
            }
            intervalIdField.value = '';
            if (e.className == "cycle") {
              document.getElementById("cycletime_" + code).value = "[]"
              document.getElementById("display_" + code).value = ""
            }
          }
        } else {
          e.value = ""
        }
      } else if (e.type == "checkbox") {
        if (e.checked == true) {
          e.checked = false
        }
      } else {
        console.log("unsupported input type")
      }
    }
  }
  drawFields()
}

function startTouch(e) {
  initialX = e.touches[0].screenX;
};

function moveTouch(e) {
  if (initialX === null) {
    return;
  }

  var currentX = e.changedTouches[0].screenX;
  var diffX = initialX - currentX;

  // sliding horizontally
  if (diffX / screen.width > xThreshold) {
    // swiped left
    swipePage(1);
  } else if (diffX / screen.width < -xThreshold) {
    // swiped right
    swipePage(-1);
  }
  initialX = null;
};

function swipePage(increment) {
  if (qr_regenerate() == true) {
    slides = document.getElementById("main-panel-holder").children
    if (slide + increment < slides.length && slide + increment >= 0) {
      slides[slide].style.display = "none";
      slide += increment;
      window.scrollTo(0, 0);
      slides[slide].style.display = "table";
      document.getElementById('data').innerHTML = "";
      document.getElementById('copyButton').setAttribute('value','Copy Data');
    }
  }
}

function drawFields(name) {

  var fields = document.querySelectorAll("[id*='canvas_']");
  const startTime = Date.now();
  for (f of fields) {
    // if(f.id == "canvas_sp"){
    //   f.setAttribute("height", "150px")
    //   f.setAttribute("width", "300px")
    // }
    if(f.id == "canvas_ci"){
      f.setAttribute("height", "500px")
      f.setAttribute("width", "500px")
    }
    
    code = f.id.substring(7);
    var img = document.getElementById("img_" + code);
    var shape = document.getElementById("shape_" + code);
    let shapeArr = shape.value.split(' ');
    var ctx = f.getContext("2d");
    ctx.clearRect(0, 0, f.width, f.height);
    ctx.drawImage(img, 0, 0, f.width, f.height);
    if(f.id == "canvas_as" || f.id == "canvas_sp"){
      var xyStr = document.getElementById("XY_" + code).value
      if (JSON.stringify(xyStr).length > 2) {
        pts = Array.from(JSON.parse(xyStr))
        for (p of pts) {
          var coord = p.split(",")
          var centerX = coord[0];
          var centerY = coord[1];
          var radius = 5;
          ctx.beginPath();
          if (shapeArr[0].toLowerCase() == 'circle') {
            ctx.arc(centerX, centerY, shapeArr[1], 0, 2 * Math.PI, false);
          } else {
            ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI, false);
          }
          ctx.lineWidth = 2;
          if (shapeArr[2] != "") {
            ctx.strokeStyle = shapeArr[2];
          } else {
            ctx.strokeStyle = '#FFFFFF';
          }
          if (shapeArr[4].toLowerCase() == 'true') {
            ctx.fillStyle = shapeArr[3];
          }
          ctx.stroke();
          if (shapeArr[4].toLowerCase() == 'true') {
            ctx.fill();
          }
        }
      }
    }
    if(f.id == "canvas_ci"){
      let scale = 1
      let growing = true
      
      function pulseImage() {
        if (growing) {
          scale += 0.02
        } else {
          scale -= 0.02
        }
        if(scale >= 1.2) {
          growing = false
        } else if (scale <= 1) {
          growing = true
        }

        img.style.transform = `scale(${scale})`

        if (Date.now() - startTime < 5000) {
          requestAnimationFrame(pulseImage)
        }
        console.log(startTime)
      }
      
      pulseImage()
      qr = new QRCode(img, options)
      console.log(qr)
    }
    
  }
}

function onFieldClick(event) {
  let target = event.target;
  let base = getIdBase(target.id);
  //console.log(target.height)
  //Resolution height and width (e.g. 52x26)
  var resX = 15
  var resY = 15
  var dimensions
  var arr

  if (target.id == "canvas_as" || target.id == "canvas_sp"){
    resX = 12;
    resY = 6;

    dimensions = document.getElementById("dimensions" + base);
    if (dimensions.value != "") {
      arr = dimensions.value.split(' ');
      resX = arr[0];
      resY = arr[1];
    }
  }
  else if (target.id == "canvas_pi"){
    resX = 20;
    resY = 25;
    
    dimensions = document.getElementById("dimensions" + base);
    if (dimensions.value != "") {
      arr = dimensions.value.split(' ');
      resX = arr[0];
      resY = arr[1];
    }
  }

  //Turns coordinates into a numeric box
  let box = ((Math.ceil(event.offsetY / target.height * resY) - 1) * resX) + Math.ceil(event.offsetX / target.width * resX);
  let coords = event.offsetX + "," + event.offsetY;

  let allowableResponses = document.getElementById("allowableResponses" + base).value;

  if(allowableResponses != "none"){
    allowableResponsesList = allowableResponses.split(',').map(Number);
    if (allowableResponsesList.indexOf(box)==-1){
      return;
    }
  }

  //Cumulating values
  let changingXY = document.getElementById("XY" + base);
  let changingInput = document.getElementById("input" + base);
  let clickRestriction = document.getElementById("clickRestriction" + base).value;
  let toggleClick = document.getElementById("toggleClick" + base).value;
  let cycleTimer = document.getElementById("cycleTimer" + base);
  let boxArr = Array.from(JSON.parse(changingInput.value));
  let xyArr = Array.from(JSON.parse(changingXY.value));

  if ((toggleClick.toLowerCase() == 'true') &&
    (boxArr.includes(box))) {
    // Remove it
    let idx = boxArr.indexOf(box);
    boxArr.splice(idx, 1);
    xyArr.splice(idx, 1);
    changingInput.value = JSON.stringify(boxArr);
    changingXY.value = JSON.stringify(xyArr);
  } else {
    if (JSON.stringify(changingXY.value).length <= 2) {
      changingXY.value = JSON.stringify([coords]);
      changingInput.value = JSON.stringify([box]);
    } else if (clickRestriction == "one") {
      // Replace box and coords
      changingXY.value = JSON.stringify([coords]);
      changingInput.value = JSON.stringify([box]);
    } else if (clickRestriction == "onePerBox") {
      // Add if box already not in box list/Array
      if (!boxArr.includes(box)) {
        boxArr.push(box);
        changingInput.value = JSON.stringify(boxArr);

        coords = findMiddleOfBox(box, target.width, target.height, resX, resY);
        xyArr.push(coords);
        changingXY.value = JSON.stringify(xyArr);
      }
    } else {
      // No restrictions - add to array
      xyArr.push(coords);
      changingXY.value = JSON.stringify(xyArr);

      boxArr.push(box);
      changingInput.value = JSON.stringify(boxArr);
    }
    // If associated with cycleTimer - send New Cycle EVENT
    if (cycleTimer != null) {
      document.getElementById("cycle_" + cycleTimer.value).click();
    }
  }

  drawFields()
}

function findMiddleOfBox(boxNum, width, height, resX, resY) {
  let boxHeight = height / resY;
  let boxWidth = width / resX;
  let boxX = (boxNum % resX) - 1;
  if (boxX == -1) { boxX = resX - 1 }
  let boxY = Math.floor((boxNum - boxX + 1) / resX);
  let x = Math.round((boxWidth * boxX) + (Math.floor(boxWidth / 2)));
  let y = Math.round((boxHeight * boxY) + (Math.floor(boxHeight / 2)));
  return x+","+y
}

function getIdBase(name) {
  return name.slice(name.indexOf("_"), name.length)
}

function getTeamName(teamNumber) {
  if (teamNumber !== undefined) {
    if (teams) {
      var teamKey = "frc" + teamNumber;
      var ret = "";
      Array.from(teams).forEach(team => ret = team.key == teamKey ? team.nickname : ret);
      return ret;
    }
  }
  return "";
}

function getMatch(matchKey) {
  //This needs to be different than getTeamName() because of how JS stores their data
  if (matchKey !== undefined) {
    if (schedule) {
      var ret = "";
      Array.from(schedule).forEach(match => ret = match.key == matchKey ? match.alliances : ret);
      return ret;
    }
  }
  return "";
}

function getCurrentTeamNumberFromRobot() {
  if (getRobot() != "" && typeof getRobot() !== 'undefined' && getCurrentMatch() != "") {
    if (getRobot().charAt(0) == "r") {
      return getCurrentMatch().red.team_keys[parseInt(getRobot().charAt(1)) - 1]
    } else if (getRobot().charAt(0) == "b") {
      return getCurrentMatch().blue.team_keys[parseInt(getRobot().charAt(1)) - 1]
    }
  }
}

function getCurrentMatchKey() {
  return document.getElementById("input_e").value + "_" + getLevel() + document.getElementById("input_m").value;
}

function getCurrentMatch() {
  return getMatch(getCurrentMatchKey());
}

function updateMatchStart(event) {
  if ((getCurrentMatch() == "") ||
    (!teams)) {
    console.log("No match or team data.");
    return;
  }
  if (event.target.id.startsWith("input_r")) {
    document.getElementById("input_t").value = getCurrentTeamNumberFromRobot().replace("frc", "");
    onTeamnameChange();
  }
  if (event.target.id == "input_m") {
    if (getRobot() != "" && typeof getRobot()) {
      document.getElementById("input_t").value = getCurrentTeamNumberFromRobot().replace("frc", "");
      onTeamnameChange();
    }
  }
}

function onTeamnameChange(event) {
  var newNumber = document.getElementById("input_t").value;
  var teamLabel = document.getElementById("teamname-label");
  if (newNumber != "") {
    teamLabel.innerText = getTeamName(newNumber) != "" ? "You are scouting " + getTeamName(newNumber) : "That team isn't playing this match, please double check to verify correct number";
  } else {
    teamLabel.innerText = "";
  }
}

function newCycle(event)
{
  let timerID = event.firstChild;
  let base = getIdBase(timerID.id);
  let inp = document.getElementById("input" + base)
  let cycleTime = inp.value
  inp.value = 0

  if (cycleTime > 0) {
    let cycleInput = document.getElementById("cycletime" + base);
    var tempValue = Array.from(JSON.parse(cycleInput.value));
    tempValue.push(cycleTime);
    cycleInput.value = JSON.stringify(tempValue);
    let d = document.getElementById("display" + base);
    d.value = cycleInput.value.replace(/\"/g,'').replace(/\[/g, '').replace(/\]/g, '').replace(/,/g, ', ');
  }
}

function undoCycle(event) {
  let undoID = event.firstChild;
  let uId = getIdBase(undoID.id);
  //Getting rid of last value
  let cycleInput = document.getElementById("cycletime" + uId);
  var tempValue = Array.from(JSON.parse(cycleInput.value));
  tempValue.pop();
  cycleInput.value = JSON.stringify(tempValue);
  let d = document.getElementById("display" + uId);
  d.value = cycleInput.value.replace(/\"/g,'').replace(/\[/g, '').replace(/\]/g, '').replace(/,/g, ', ');
}

function resetTimer(event) {
  let timerID = event.firstChild;
  let tId = getIdBase(timerID.id);
  let inp = document.getElementById("input" + tId)
  inp.value = 0

  // stop timer
  timerStatus = document.getElementById("status" + tId);
  startButton = document.getElementById("start" + tId);
  intervalIdField = document.getElementById("intervalId" + tId);
  var intervalId = intervalIdField.value;
  timerStatus.value = 'stopped';
  startButton.setAttribute("value", "Start");
  if (intervalId != '') {
    clearInterval(intervalId);
  }
  intervalIdField.value = '';
}

function timer(event) {
  let timerID = event.firstChild;
  let tId = getIdBase(timerID.id)
  timerStatus = document.getElementById("status" + tId);
  startButton = document.getElementById("start" + tId);
  intervalIdField = document.getElementById("intervalId" + tId);
  var statusValue = timerStatus.value;
  var intervalId = intervalIdField.value;
  if (statusValue == 'stopped') {
    timerStatus.value = 'started';
    startButton.setAttribute("value", "Stop");

    var intId = setInterval(() => {
      if (document.getElementById("status" + tId).value == 'started') {
        inp = document.getElementById("input" + tId);
        var t = parseFloat(inp.value);
        t += 0.1;
        tTrunc = t.toFixed(1)
        inp.value = tTrunc;
      }
    }, 100);
    intervalIdField.value = intId;
  } else {
    timerStatus.value = 'stopped';
    startButton.setAttribute("value", "Start");

    clearInterval(intervalId);
    intervalIdField.value = '';
  }
  drawFields();
}

function undo(event) {
  let undoID = event.firstChild;
  //Getting rid of last value
  changingXY = document.getElementById("XY" + getIdBase(undoID.id));
  changingInput = document.getElementById("input" + getIdBase(undoID.id));
  var tempValue = Array.from(JSON.parse(changingXY.value));
  tempValue.pop();
  changingXY.value = JSON.stringify(tempValue);

  tempValue = Array.from(JSON.parse(changingInput.value));
  tempValue.pop();
  changingInput.value = JSON.stringify(tempValue);
  drawFields();
  direction_radio = document.getElementsByName('dir');
  //console.log(direction_radio)
  document.getElementById("input_dir_l").checked = false;
  document.getElementById("input_dir_r").checked = false;
}

function flip(event) {
  let flipID = event.firstChild;
  var flipImg = document.getElementById("canvas" + getIdBase(flipID.id));
  if (flipImg.style.transform == "") {
    flipImg.style.transform = 'rotate(180deg)';
  } else {
    flipImg.style.transform = '';
  }
  drawFields();
}

function left(event){
  let leftButton = event.querySelector('input[type="button"]');
  //var leftButton = document.getElementById("input" + getIdBase(leftID.id))
  if (leftButton.style.backgroundColor == 'black' || leftButton.style.backgroundColor == ''){
    leftButton.style.backgroundColor = 'green'
  } else{
    leftButton.style.backgroundColor = 'black'
  }
}

function right(event){
  let rightButton = event.querySelector('input[type="button"]');
  //var leftButton = document.getElementById("input" + getIdBase(leftID.id))
  if (rightButton.style.backgroundColor == 'black' 
      || rightButton.style.backgroundColor == ''
      && leftButton.style.backgroundColor != 'green'){
    rightButton.style.backgroundColor = 'green'
  } else{
    rightButton.style.backgroundColor = 'black'
  }
}

function displayData(){
  document.getElementById('data').innerHTML = getData(dataFormat);
}

function copyData(){
  navigator.clipboard.writeText(getData(dataFormat));
  document.getElementById('copyButton').setAttribute('value','Copied');
}

window.onload = function () {
  let ret = configure();
  if (ret != -1) {
    let ece = document.getElementById("input_e");
    let ec = null;
    if (ece != null) {
      ec = ece.value;
    }
    if (ec != null) {
      getTeams(ec);
      getSchedule(ec);
    }
    this.drawFields();
    if (enableGoogleSheets) {
      console.log("Enabling Google Sheets.");
      setUpGoogleSheets();
    }
  }
};
