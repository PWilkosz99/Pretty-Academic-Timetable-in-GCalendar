import openpyxl
import datetime

tt = 'timetable.xlsx'
wb = openpyxl.load_workbook(tt)
sheet = wb.active

groups = ["GW01", "GA02", "GĆP02","GĆL03","GCL_Now_04"]


GW=[]
GA=[]
GP=[]
GL=[]
GSL=[]
defs = [GW,GA,GP,GL,GSL]


elrn= {"ABC ABC": "TEAMS", "DCE DCE": "UPEL"}

for i in range(5):
    for row in sheet.rows:
        if(row[9].value==groups[i]):
            defs[i].append(row)


def room(place, teacher):
    if(place=="WIMiIP on-line"):
        for prsn in elrn:
            if prsn == teacher:
                return elrn[prsn]
    return place
        


GWF = open("GW.csv", "w")

if GWF.writable():
    GWF.write("Subject,Start Date,Start Time,End Date,End Time,Description,Location,,,,\n")
    for row in GW:
        GWF.write(row[0].value + "," + row[2].value[:10] + "," + str(row[3].value) + "," + row[2].value[:10] + "," + str(row[4].value) + "," + row[1].value + "," + room(row[5].value, row[1].value) + ",,,,\n")

GWF.close()

GAF = open("GA.csv", "w")

if GAF.writable():
    GAF.write("Subject,Start Date,Start Time,End Date,End Time,Description,Location,,,,\n")
    for row in GA:
        GAF.write(row[0].value + "," + row[2].value[:10] + "," + str(row[3].value) + "," + row[2].value[:10] + "," + str(row[4].value) + "," + row[1].value + "," + room(row[5].value, row[1].value) + ",,,,\n")

GAF.close()

GPF = open("GP.csv", "w")

if GPF.writable():
    GPF.write("Subject,Start Date,Start Time,End Date,End Time,Description,Location,,,,\n")
    for row in GP:
        GPF.write(row[0].value + "," + row[2].value[:10] + "," + str(row[3].value) + "," + row[2].value[:10] + "," + str(row[4].value) + "," + row[1].value + "," + room(row[5].value, row[1].value) + ",,,,\n")

GPF.close()

GLF = open("GL.csv", "w")

if GLF.writable():
    GLF.write("Subject,Start Date,Start Time,End Date,End Time,Description,Location,,,,\n")
    for row in GL:
        GLF.write(row[0].value + "," + row[2].value[:10] + "," + str(row[3].value) + "," + row[2].value[:10] + "," + str(row[4].value) + "," + row[1].value + "," + room(row[5].value, row[1].value) + ",,,,\n")
    for row in GSL:
        GLF.write(row[0].value + "," + row[2].value[:10] + "," + str(row[3].value) + "," + row[2].value[:10] + "," + str(row[4].value) + "," + row[1].value + "," + room(row[5].value, row[1].value) + ",,,,\n")

GLF.close()


#other activities generator

# GE = open("GE.csv", "w")
# GEcounter = 15
# deltadays=datetime.timedelta(0)
# startdate=datetime.date(2021, 3, 1)
# if GE.writable():
#     GE.write("Subject,Start Date,Start Time,End Date,End Time,Description,Location,,,,\n")
#     while GEcounter>0:
#         GE.write("EXAMPLE SUBJECT,"+(str)(startdate+deltadays)+","+"16:00:00"+","+(str)(startdate+deltadays)+","+"17:30:00"+","+"EXAMPLE TEACHER"+","+"ONLINE"+",,,,\n")
#         deltadays=deltadays+datetime.timedelta(7)
#         GEcounter=GEcounter-1

#async version

GE = open("GE.csv", "w")
GEcounter = 30
deltadays=datetime.timedelta(0)
startdate=datetime.date(2021, 3, 1)
if GE.writable():
    GE.write("Subject,Start Date,Start Time,End Date,End Time,Description,Location,,,,\n")
    while GEcounter>0:
        GE.write("EXAMPLE SUBJECT,"+(str)(startdate+deltadays)+","+"16:00:00"+","+(str)(startdate+deltadays)+","+"17:30:00"+","+"EXAMPLE TEACHER"+","+"ONLINE"+",,,,\n")
        if(GEcounter%2==0):
            deltadays=deltadays+datetime.timedelta(2)
        else:
            deltadays=deltadays+datetime.timedelta(5)
        GEcounter=GEcounter-1
