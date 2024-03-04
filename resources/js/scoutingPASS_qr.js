
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

//TODO:Find a better name for this 
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

  