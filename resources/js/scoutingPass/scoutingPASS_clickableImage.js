
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
        flipImg.style.transform = 'scaleX(-1)';
    } else {
        flipImg.style.transform = '';
    }
    drawFields();
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
  