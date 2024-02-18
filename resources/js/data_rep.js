var data,temp
var xlsx = require("xlsx")
var fs = require("fs")
var excelFile = "../../Excel/TestSheet.xlsx"
var wb = xlsx.readFile(excelFile)
var sheetNames = wb.sheetNames
console.log(sheetNames)