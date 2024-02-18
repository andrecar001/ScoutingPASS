//data_rep.js
//
// The data representation application
// Written by Team 2508 - Armada
// Influenced by Team 2451 - PWNAGE

document.addEventListener("touchstart",startTouch,false)
document.addEventListener("touchend",moveTouch,false)

// Swipe Up / Down / Left / Right
var initialX = null
var xThreshold = 0.3
var slide = 0
var checkboxAs = 'YN'

//Required Format for data
//var requiredScoutingFields = ["s","e","m","r","t","as","dir","al","aas","ass","tss","tta","tpu","dt","fs","nit","dr","sr","die","tie","dn","co"]
var requiredPrematchFields = ['Initials','Match Level','Match #','Team #','Position','Direction']
var requiredAutonFields = ['Leave Start','Auto Amp Score','Auto Speaker Score']
var requiredTeleopFields = ['Teleop Amp Scores','Teleop Speaker Scores','Times Amplified','Pickup From']
var requiredEndgameFields = ['Stage Time','Final Status','Note in Trap']
var requiredMiscellaneousFields = ['Driver Skill','Defense Rating','Speed Rating','Died/Immobilized','Tippy','Dropped Notes(>2)','Good Ally','Comments']
var requiredScoutingFields = [...requiredPrematchFields,...requiredAutonFields,...requiredTeleopFields,...requiredEndgameFields,...requiredMiscellaneousFields]

var requiredPitFields = ["t","crn","wid","wei","drv","odt","sr","mot","nob","fpu","ss","sa","def","driv","clmb","aut","dts","co"]



async function create2dFileArray(fileName) {
    let fileText
    try{
        var res = await fetch(fileName)
        var text = await res.text()
        fileText = text
    } catch (e) {
        console.error('Error fetching data', e)
    }
    
    
    lines = fileText.trim().split('\n')
    var splitArray = lines.map(line => {
        let splitLine = line.split('\t')
        let lastElement = splitLine[splitLine.length -1]
        let lastElementIdx = splitLine.length-1
        //let returnLine = splitLine[lastElementIdx].slice(0,-1)
        if (lastElement.charAt(lastElement.length-1) === '\r'){
            splitLine[lastElementIdx] = lastElement.slice(0,-1)
            return splitLine
        } else {
            return splitLine
        }
        return returnLine
    })
   
    return splitArray
}

async function createTable(fileName){

    data = await create2dFileArray(fileName)

    //Create div for table
    const tableContainer = document.createElement('div');
    tableContainer.setAttribute('id', 'table-container')
    tableContainer.setAttribute('class', 'all-scouting-data')
    tableContainer.style.height = '100%'
    document.getElementById('allData_table').appendChild(tableContainer);
    //Create table in div
    const table = document.createElement('table');
    table.setAttribute('class', 'all-scouting-data')
    document.getElementById('table-container').appendChild(table);
    var theader = document.createElement('tr')
    requiredScoutingFields.forEach(newHeader => {
        const currHeader = document.createElement('th')
        currHeader.textContent = newHeader
        currHeader.style.borderBottom = '1px solid black';
        currHeader.style.minWidth = '50px';
        currHeader.style.padding = '5px';
        theader.appendChild(currHeader)

    })
    table.appendChild(theader)

    // Loop through the data and create rows and cells
    data.forEach(rowData => {
        const row = document.createElement('tr');
        row.setAttribute('class', 'tableRow')
        row.style.display = 'flex';
        
        rowData.forEach(cellData => {
            const cell = document.createElement('td');
            cell.textContent = cellData;
            cell.style.borderBottom = '1px solid black';
            cell.style.minWidth = '50px';
            cell.style.padding = '5px';
            row.appendChild(cell);
        });

        table.appendChild(row);
    });
}


function addTable(table, idx, name, data) {
    var container = document.createElement('div')
    container.style.border = '1px solid black'
    container.style.padding = '10px'
    //document.getElementById('allData_table').appendChild(container)
    var row = table.insertTow(idx)
    var cell1 = row.insertCell(0)
    cell1.classList.add('title')
    var cell2 = row.insertCell(1)
    cell1.innerHTML = name + '&nbsp;'
    cell2.classList.add('field')

    data.forEach(sheetRowData => {
        var sheetRow = document.createElement('div')
        sheetRow.style.display = 'flex'

        sheetRowData.forEach(cellData => {
            var cell = document.createElement('div')
            cell.textContent = cellData
            cell.style.border = '1px solid black'
            cell.style.minWidth = '50px'
            cell.style.padding = '5px'
            sheetRow.appendChild(cell)
        })

        container.appendChild(sheetRow)
    })
    cell2.appendChild(container)
    return idx + 1
}

function addTeamNumber(table, idx, name, data) {
    var row = table.insertRow(idx)
    var cell1 = row.insertCell(0)
    cell1.classList.add('title')
    var cell2 = row.insertCell(1)
    cell1.innerHTML = name + '&nbsp;'
    cell2.classList.add('field')

    var inp = document.createElement('input')
    inp.setAttribute('id','input_team')
    inp.setAttribute('type', 'number')
    inp.setAttribute('size', 5)
    inp.setAttribute('min', 999)
    inp.setAttribute('max', 9999)
    inp.setAttribute('defaultValue', 2508)
    inp.setAttribute('required',"")
    cell2.appendChild(inp)
    return idx +1
}

function addElement(table,idx,data) {
    var type = null
    var name = 'Default Name'
    if (data.hasOwnProperty('name')) {
        name = data.name
      }
    if (data.hasOwnProperty('type')) {
    type = data.type
    } else {
    console.log("No type specified");
    console.log("Data: ")
    console.log(data);
    err = { code: "err", defaultValue: "No type specified: " + data };
    idx = addText(table, idx, name, err);
    return
    }
    if (data.type == 'text'){idx = addTeamText(table, idx, name, data)}
    else if (data.type == 'table'){idx = addTable(table, idx, name, data)}
    else {console.log(`Unrecongnized type: ${data.type}`)}
    return idx
}

function startTouch(e) {
    initialX = e.touches[0].screenX;
}

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
}
function getIdBase(name) {
    return name.slice(name.indexOf("_"), name.length)
}
// Sample data for the spreadsheet

window.onload = function() {
    console.log(requiredScoutingFields)
    createTable('../../data/scoutingData.txt')
    
}
