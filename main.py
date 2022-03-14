# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
from haralyzer import HarParser, HarPage

with open('nu.nl.har', 'r') as f:
    har_parser = HarParser(json.loads(f.read()))

data = har_parser.har_data
counter = 0
request_cookie_counter = 0
response_cookie_counter = 0

results = {
    "num_reqs": counter,
    "num_requests_w_cookies": request_cookie_counter,
    "num_responses_w_cookies": response_cookie_counter,
    "third_party_domains": [],
    "domains_w_cookies": [],
    "server_countries": [],
    "xorigin_cookie_domains": [],
    "requests": {"request_domain": "String",
                 "server_country": "String",
                 "server_in_eu": True,
                 "num_request_cookies": 0,
                 "num_response_cookies": 0,
                 "is_tracker": True,
                 "url_first_128_char": "String"
                 }
}

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for page in har_parser.pages:
        for entry in page.entries:
            counter = counter + 1
            #print(entry.url)
            print(entry['request']['headers'])
            #if(entry.request.host != None):
                #print(entry.request.host)
            if(len(entry.request.cookies) != 0):
                #print(entry.request.cookies)
                request_cookie_counter = request_cookie_counter + 1
            if(len(entry['response']['cookies']) != 0):
                #print(entry['response']['cookies'])
                response_cookie_counter = response_cookie_counter + 1
#print(counter)
#print(request_cookie_counter)
#print(response_cookie_counter)