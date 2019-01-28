from mongoengine import *

db_db = "MeetingRoom"
db_host = "47.106.8.44"
db_user = "MeetingRoomAdmin"
db_password = "Pzy19980526"
db_authentication_source = "MeetingRoom"
connect(db=db_db, host=db_host, password=db_password, username=db_user, authentication_source=db_authentication_source)

class Meeting(Document):
    _class = StringField(required=False)
    heading = StringField(required=True)
    description = StringField(required=True)
    roomId = StringField(required=True)
    date = StringField(required=True)
    location = StringField(required=False)
    hostId = StringField(required=True)
    attendantNum = StringField(required=True)
    startTime = IntField(required=True)
    endTime = IntField(required=True)
    attendants = MapField(field=StringField(), required = False)
    needSignIn = BooleanField(required=True)
    status = StringField(required=False)
    type = StringField(required=False)
    #tags = ListField(required=False)