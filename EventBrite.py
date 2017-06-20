import requests
import json
from pprint import pprint
import os
import urllib2
from bs4 import BeautifulSoup

class EventBrite:

    def __init__(self, oAuthToken):
        self.oAuthToken = oAuthToken

    def getEvents(self):
        response = requests.get(
        "https://www.eventbriteapi.com/v3/users/me/events" ,
        headers = {
            "Authorization": "Bearer {}".format(self.oAuthToken),
        },
        verify = True,  # Verify SSL certificate
        )
        events = response.json()['events']
        
       # return pprint(events)
        return events

    def eventInfo(self, eventID):
        response = requests.get(
        "https://www.eventbriteapi.com/v3/events/{}".format(eventID) ,
        headers = {
            "Authorization": "Bearer {}".format(self.oAuthToken),
        },
        verify = True,  # Verify SSL certificate
        )
        event = response.json()
        return event

    def eventVenue(self, venueID):
        response = requests.get(
            "https://www.eventbriteapi.com/v3/venues/{}".format(venueID) ,
            headers = {
                "Authorization": "Bearer {}".format(self.oAuthToken),
            },
            verify = True,  # Verify SSL certificate
            )
        venue = response.json()
        return venue

    def eventPrice(self, eventID):
        url = self.eventInfo(eventID)['url']
        url = urllib2.urlopen(url)
        soup = BeautifulSoup(url, 'html.parser')
        price = soup.find("div" ,{'class':'js-display-price'}).text.strip()
        return price


eventbrite =  EventBrite(["YOUR AUTHENTICATION TOKEN"])

events = eventbrite.getEvents()

eventID = events[0]['id']

event = eventbrite.eventInfo(eventID)
price = eventbrite.eventPrice(eventID)

venue = eventbrite.eventVenue(event['venue_id'])

print price

