from html_template import *

class HTMLGenerator:
    def __init__(self):
        self.HEADERTEMPLATE = '<html><body>{}<form method="POST"><div> '
        self.FOOTER = '</div></form></body></html>'
        self.BUTTONTEMPLATE = '<button type="button" name="submit" class="btn btn-info btn-1g active" value="{}" onclick="{}">{}</button>&nbsp;'
        self.LINKTEMPLATE = '<a href="{}" target="_blank">{}</a>'

    def generateHTML(self,theResponse):
        finalResponse = self.HEADERTEMPLATE.format(theResponse.summaryText)
        for entry in theResponse.entries:
            if(entry.type == ResponseType.BUTTON):
                finalResponse+=self.BUTTONTEMPLATE.format(entry.link,theResponse.submitAction,entry.linkText)
            if(entry.type == ResponseType.LINK):
                finalResponse+=self.LINKTEMPLATE.format(entry.link,entry.linkText)
        finalResponse+=self.FOOTER
        return finalResponse
