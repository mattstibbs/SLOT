import gspread
import config
import datetime
import uuid

class Creds(object):

    def __init__(self, access_token):
        self.access_token = access_token


print "Loading DB..."
creds = Creds(config.google_access_token)
gs = gspread.authorize(creds)
sheet = gs.open_by_key(config.google_sheet_key)
log_worksheet = sheet.worksheet("log")
student_worksheet = sheet.worksheet("students")

print "Complete"



def to_timestamp(dt):
    return (dt - datetime.datetime(1970, 1, 1)).total_seconds()

def get_all_students():
    return student_worksheet.get_all_records()

def get_all_opportunities():

    rs = log_worksheet.get_all_records()


    for r in rs:
        if r["student"]:
            r["status"] = "Accepted"
        elif to_timestamp(datetime.datetime.now()) > int(r["expiry_time"]):
            r["status"] = "Expired"
        else:
            r["status"] = "Offered"
    return rs


## Call this function with a new opportunity:
# db.add_opportunity({
#        "doctor": "Dr Thing",
#        "procedure":"do thing",
#        "location": "the ward",
#        "duration": 20
#    })
#
# Returns the GUID of the created opportunity
def add_opportunity(op):
    c = Creds(config.google_access_token)
    gs = gspread.authorize(c)
    s = gs.open_by_key(config.google_sheet_key)
    w = s.worksheet("log")

    vs = [uuid.uuid4()]

    now = to_timestamp(datetime.datetime.now())
    vs.append(op["doctor"])
    vs.append(now)
    vs.append(op["procedure"])
    vs.append(now + int(op["duration"]))
    vs.append(op["location"])
    w.append_row(vs)

    return vs[0]