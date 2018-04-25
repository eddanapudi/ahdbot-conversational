
import random
from html_template import *
from HTMLGenerator import *

hg = HTMLGenerator()

##dict of response for each type of intent
intent_response_dict = {
    "intro": ["This is a EDPI FAQ bot. One stop-shop to all your EDPI related queries"],
    "greet":["Hey, how can i help you?","Hello,How can i help you?","Hi,How can i help you?"],
    "goodbye":["Bye","It was nice talking to you","See you","ttyl"],
    "affirm":["Cool","I know you would like it"],
    "edpi_intro": "<html><body>EDPI is an Enterprise Data Platform Interface. Once onboarded consumers can access AM/WM Data from predefined Data towers. Choose one from below <br/><input type=\"button\" name=\"submit\" class=\"btn btn-info btn-lg active\" value=\"AM EDPI\" onclick=\"javascript:window.open('http://edpiamui')\">&nbsp;<input type=\"button\" name=\"submit\" class=\"btn btn-info btn-lg active\" value=\"WM EDPI\" onclick=\"javascript:window.open('http://edpiwmui')\"> </form></body></html>",
    "edpi_faq": "EDPI is an Enterprise Data Platform Interface. Once onboarded consumers can access AM/WM Data from predefined Data towers.",
    "edpi_offer": "EDPI Offers below feautures. <br>Metadata Driven Interface.<br>Single point of Control<br>High Performance<br>Business Definition link<br>Robus and Scalable<br>Cross Domain queries",
    "onboard_edpi": "You need to have Janus entitlements to onboard application and create queries. More details <a target='_blank' href='http://edpihelppage'>here</a>",
    "edpi_consume": "EDPI allows you to construct GraphQL from its UI and expose the same as a rest endpoint which streams out the data ",
    "create_query": "Click on the me@edpi on the top menu. Click on Build queries, and write GraphQL",
    "edpi_gql": "Stored queries are defined in a format based on <a target='_blank' href='https://reactjs.org/blog/2015/05/01/graphql-introduction.html'>GraphQL.</a>. Stored queries are team specific and owned/managed by them ",
    "benefits": "EDPI is a data distribution layer for AWM which acts as golden source",
    "faq_link": "You can check all the answers here AM EDPI: <a target='_blank' href=\"go/edpi\"</a>, WM EDPI:\"<a target='_blank' href=\"go/edpiwm\"</a>",
    "data_entitlement": "Which LOB?Options:AM#WM",
    "AM_data_entitlement": "You need to have an EDPI parent Query Entitlement and also we have data sourced from below towers. Which tower are you interested in?Options:Reference#Securities & Pricing#Funds",
    "WM_data_entitlement": "You need to have an EDPI parent Query Entitlement and also we have data sourced from below towers. Which tower are you interested in?Options:Reference#Transaction & Holdings#Morningstar",
    "Reference_AM_data_entitlement": "Please find the Link:www.entitlement.com/am/Reference",
    "Securities & Pricing_AM_data_entitlement": "Please find the Link:www.entitlement.com/am/s&p",
    "Funds_AM_data_entitlement": "Please find the Link:www.entitlement.com/am/funds",
    "Reference_WM_data_entitlement": "Please find the Link:www.entitlement.com/wm/Reference",
    "Transaction & Holdings_WM_data_entitlement": "Please find the Link:www.entitlement.com/WM/t&h",
    "Morningstar_WM_data_entitlement": "Please find the Link:www.entitlement.com/wm/morningstar",
    "entitlements_info":"EDPI uses janus entitlements to authorize user, Which one you look for?Options:Self Service#Data",
    "Self Service_entitlements_info":"For Individual Users accessing Self Service or EDPI UI, please raise EDPI Consumer entitlement",
    "Data_entitlements_info":"Raise the Janus data entitlement specific to data tower, Reference/Instrument/Funds etc.",
    "ui_entitlement": "Which LOB?Options:AM#WM",
    "AM_ui_entitlement":"Please raise EDPI Consumer entitlement for AM in RMT Prod. Visit Link:http://RMT",
    "WM_ui_entitlement":"Please raise EDPI Consumer entitlement for WM in RMT Prod. Visit Link:http://RMT,RMT"
    
}

edpifaq_response_dict = {    
    "edpi": "EDPI is an Enterprise Data Platform Interface. Once onboarded consumers can access AM/WM Data from predefined Data towers.",
    "benefits":"EDPI is a data distribution layer for AWM which acts as golden source",
    "faq_link":'You can check all the answers here AM EDPI: <a href=\"go/edpi\"</a>, WM EDPI:\"<a href=\"go/edpiwm\"</a>',
    "reference": "Which LOB?Options:AM#WM",
    "AM_reference": "Which Version do you want to see?Options:v0#v1#v2",
    "WM_reference": "Which Version do you want to see?Options:v3#v4#v5",
    "v0_AM_reference": "Please find the Link:www.google.com"
}

def button_generator(buttons,append_text):
    button_template = []
    for b in buttons:
        entry = Entry(ResponseType.BUTTON,b+"_"+append_text,b)
        button_template.append(entry)
    return button_template

def link_generator(links):
    link_template=[]
    for l in links:
        link_link_text=l.split(',')
        if(len(link_link_text)>1):
            entry = Entry(ResponseType.LINK,link_link_text[0],link_link_text[1])
        else:
            entry = Entry(ResponseType.LINK,link_link_text[0],link_link_text[0])
        link_template.append(entry)
    return link_template

def define_html_template(response_text,append_text):
    entry = []
    
    if response_text.find("Options")!= -1:
        a=response_text.find("Options")
        text=response_text[0:a]
        button_text=response_text[a+8:len(response_text)]
        buttons=button_text.split("#")
        entry = button_generator(buttons,append_text)
                    
    elif response_text.find("Link")!= -1:
        a=response_text.find("Link")
        text=response_text[0:a+5]
        link_text=response_text[a+5:len(response_text)]
        links=link_text.split("#")
        entry= link_generator(links)
    else:
        text = response_text

    h_t=Response()
    print (str(h_t))
    h_t.summaryText = text
    h_t.submitAction = "javascript:sendToServer(value)"
    h_t.entries = entry
    return h_t

get_random_response = lambda intent:random.choice(intent_response_dict[intent])

def getBotResponse(intent,entities):

    if intent == "intro":
        response_text = get_random_response(intent)
    elif intent == "greet":
        response_text = get_random_response(intent)
        print(response_text)
    elif intent == "goodbye":
        response_text = get_random_response(intent)
    elif intent == "affirm":
        response_text = get_random_response(intent)
    elif intent in intent_response_dict:
        response_text=intent_response_dict[intent]
        h_t=define_html_template(response_text,intent)
        response_text= hg.generateHTML(h_t)
    elif intent == "edpi_faq":
        print (intent)
        response_text = edpi_faq(entities)
        append_text=''
        if len(entities)>0:
            ent=entities[0]
            append_text=ent["entity"]
        h_t=define_html_template(response_text,append_text)
        response_text= hg.generateHTML(h_t)

    else:
        response_text = "Sorry I am not trained to do that yet..." 

    return response_text

def edpi_faq(entities):
    print("----------")
    print(entities)
    if len(entities) == 0:
        return intent_response_dict["edpi_intro"]
    if len(entities) == 1:
        print(" ************** ")
        ent = entities[0]
        return edpifaq_response_dict[ent["entity"]]
    return "Sorry.." + edpifaq_response_dict["faq_link"]