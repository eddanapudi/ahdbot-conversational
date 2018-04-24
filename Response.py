from enum import Enum
ResponseType = Enum('ResponseType','BUTTON LINK')

class Entry:
    def __init__(self):
        self.type = ResponseType.BUTTON
        self.link = 'LINK'
        self.linkText = 'LINKTEXT'
    def __init__(self,type,link,linkText):
        self.type = type
        self.link = link
        self.linkText = linkText

class Response:
    def __init__(self):
        self.summaryText = "TEXT"
        self.submitAction = 'http://hostname:port/endpoint'
        self.entries = []

