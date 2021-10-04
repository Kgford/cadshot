import math
import os, requests
from django.http import request

class API:
    def __init__ (self, url):
        self.url = url
        print('self.url=',self.url)
        
    def request_json(self):
        response = requests.get(self.url)
        return response
        
    def request_text(self):
        response = requests.get(self.url)
        return response.text
        
    def request_status(self):
        response = requests.get(self.url)
        '''
        200 OK	Your request was successful!
        201 Created	Your request was accepted and the resource was created.
        400 Bad Request	Your request is either wrong or missing some information.
        401 Unauthorized	Your request requires some additional permissions.
        404 Not Found	The requested resource does not exist.
        405 Method Not Allowed	The endpoint does not allow for that specific HTTP method.
        500 Internal Server Error	Your request wasn’t expected and probably broke something on the server side.
        '''
        return response.status_code
        
    def request_reason(self):
        response = requests.get(self.url)
        return response.reason
        
    def request_header(self):
        response = requests.get(self.url)
        return response.headers
        
    def request_request_header(self):
        response = requests.get(self.url)
        return response.request.headers

    def request_GET(self):
        response = requests.get(self.url)
        return response.request
    
    
        
    
    
    
    
class SMS:    
    def __init__ (self, number, message,):
        self.number = number
        self.message, = message,
        print('In security')
        print('self.message,=',self.message,)
        print('self.request=',self.request)
    
    def send_sms(self):
        till_username = settings.TILL_USERNAME
        till_api_key = settings.TILL_API_KEY
                        
        requests.post(
            "https://platform.tillmobile.com/api/send?username=%s&api_key=%s" % (
                till_username,
                till_api_key
            ), 
            json={
                "phone": self.number,
                "text" : self.message,
                "tag": "New User Alert"
            }
        )
    def send_sms_question(self):
        till_username = settings.TILL_USERNAME
        till_api_key = settings.TILL_API_KEY

        requests.post(
            "https://platform.tillmobile.com/api/send?username=%s&api_key=%s" % (
                till_username,
                till_api_key
            ), 
            json={
                "phone": [self.number],
                "introduction": "Hello from Till.",
                "questions" : [{
                    "text": "Do you have a few moments to answer a question or two?",
                    "tag": "have_a_few_moments",
                    "responses": ["Yes", "No"],
                    "conclude_on": "No",
                    "webhook": "https://yourapp.com/have_a_few_moments_results/"
                },
                {
                    "text": "What is your favorite color?",
                    "tag": "favorite_color",
                    "responses": ["Red", "Green", "Yellow"],
                    "webhook": "https://yourapp.com/favorite_color_results/"
                },
                {
                    "text": "Who is you favorite Star Wars character?",
                    "tag": "favorite_star_wars_character",
                    "webhook": "https://yourapp.com/favorite_star_wars_character_results/"
                }],
                "conclusion": "Thank you for your time"
            }
        )
        
    
    def visitor_monitor(self):