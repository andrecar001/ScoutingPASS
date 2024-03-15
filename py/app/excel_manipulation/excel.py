from openpyxl import load_workbook
import os
import information
def isDouble(value):
    try:
        float_value = float(value)
        return True
    except ValueError:
        return False

# print(wb.sheetnames)
def populateSheet(workbookPath):
    path = 'py/app/data/Test.xlsx'
    workbookPath = os.path.abspath(workbookPath)
    wb = load_workbook(workbookPath)

    filePath = 'py/app/data/match_scouting_data.txt'

    match_sheet_name = 'ScoutingInfo'
    # pit_sheet_name = 'PitScoutingInfo'
    match_sheet = wb[match_sheet_name]
    # pit_sheet = wb[pit_sheet_name]
    all_lines = []

    # with open(filePath, 'r') as file:
    #     lines = file.readlines()
    #     for line in lines:
            
    #         line_array = line.split('\t')
    #         if line_array[0].isdigit() or line_array[0] == '':
    #             continue
    #         line_array[len(line_array)-1] = line_array[len(line_array)-1].rstrip('\n')
    #         all_lines.append(line_array)
    # # print(all_lines)   
    all_lines = information.getAllMatchInfoList(filePath)
    for row_idx, row in enumerate(all_lines, start=1):
        if row[0].isdigit() == True:
            continue
        for col_idx, value in enumerate(row, start=1):
            cell = match_sheet.cell(row=row_idx+1,column=col_idx)
            if isDouble(value):
                cell.value = float(value)
                if '.' in value:
                    cell.number_format = '0.0'
                else:
                    cell.number_format = '0'
            else:
                cell.value = value
    wb.save(workbookPath)

    wb.close()

