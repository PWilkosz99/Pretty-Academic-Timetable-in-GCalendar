import openpyxl

tt = 'timetable.xlsx'
wb = openpyxl.load_workbook(tt)
sheet = wb.active

groups = ["GW01", "GA02", "GĆP02","GĆL03"]


GW=[]
GA=[]
GP=[]
GL=[]
defs = [GW,GA,GP,GL]

for i in range(4):
    for row in sheet.rows:
        if(row[9].value==groups[i]):
            defs[i].append(row)


GWF = open("GW.csv", "w")

if GWF.writable():
    GWF.write("Subject,Start Date,Start Time,End Date,End Time,Description,Location,,,,\n")
    for row in GW:
        #row[2].value=row[2].value[:10]
        GWF.write(row[0].value + "," + row[2].value[:10] + "," + str(row[3].value) + "," + row[2].value[:10] + "," + str(row[4].value) + "," + row[1].value + "," + row[5].value + ",,,,\n")

GWF.close()

GAF = open("GA.csv", "w")

if GAF.writable():
    GAF.write("Subject,Start Date,Start Time,End Date,End Time,Description,Location,,,,\n")
    for row in GA:
        GAF.write(row[0].value + "," + row[2].value[:10] + "," + str(row[3].value) + "," + row[2].value[:10] + "," + str(row[4].value) + "," + row[1].value + "," + row[5].value + ",,,,\n")

GAF.close()

GPF = open("GP.csv", "w")

if GPF.writable():
    GPF.write("Subject,Start Date,Start Time,End Date,End Time,Description,Location,,,,\n")
    for row in GP:
        GPF.write(row[0].value + "," + row[2].value[:10] + "," + str(row[3].value) + "," + row[2].value[:10] + "," + str(row[4].value) + "," + row[1].value + "," + row[5].value + ",,,,\n")

GPF.close()

GLF = open("GL.csv", "w")

if GLF.writable():
    GLF.write("Subject,Start Date,Start Time,End Date,End Time,Description,Location,,,,\n")
    for row in GL:
        GLF.write(row[0].value + "," + row[2].value[:10] + "," + str(row[3].value) + "," + row[2].value[:10] + "," + str(row[4].value) + "," + row[1].value + "," + row[5].value + ",,,,\n")

GLF.close()
