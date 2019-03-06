from mongoengine import *

db_db = "MeetingRoom"
db_host = "pipipan.cn"
connect(db=db_db, host=db_host)

STATUS = ('Pending', 'Running', 'Cancelled', 'Stopped')
TYPE = ('COMMON', 'URGENCY')
NOTETYPE = ('HTML', 'VOICE')

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
    attendants = MapField(field=StringField(), required=False)
    needSignIn = BooleanField(required=True)
    status = StringField(required=False, choices=STATUS)
    type = StringField(required=False, choices=TYPE)
    tags = ListField(required=False)
    foreignGuestList = ListField(required=False)
    timestamp = StringField(required=False)
    meta = {'collection': 'meeting'}

class MeetingNote(Document):
    _class = StringField(required=False)
    meetingNoteType = StringField(required=True, choices=NOTETYPE)
    voiceFileName = StringField(required=False)
    title = StringField(required=True)
    note = StringField(required=False)
    meetingId = StringField(required=True)
    ownerId = StringField(required=True)
    collectorIds = ListField(required=False)
    meta = {'collection': 'meetingNote'}