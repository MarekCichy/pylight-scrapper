from requests_html import HTMLSession
import sys
import json

def get_html(url):
    session = HTMLSession()
    response = session.get(url)
    return response


def check_date_and_address(response):
    details = response.html.find(".date-and-localization", first=True)
    return details.text


def get_talks(response):
    talks = response.html.find(".talk-detail")
    return talks


if __name__ == "__main__":
    try:
        response = get_html(url="https://web.archive.org/web/20190618105438/http://www.pylight.org/")
        try:
            if sys.argv[1] == '--output-format=text':
                meetup_details = check_date_and_address(response)
                talks = get_talks(response)
                print(meetup_details)
                print("\n")
                for talk in talks:
                    print(talk.text)
                    print("\n")
        
            elif sys.argv[1] == '--output-format=json':         
                raw_details = check_date_and_address(response)
                raw_talks = get_talks(response)

                talks = []
                for talk in raw_talks:
                    talk_details = talk.text.split('\n')
                    talks.append(dict(speaker=talk_details[0], title=talk_details[1]))
                meetup_details = raw_details.split('\n')

                scrapped_info = dict(time=meetup_details[0], place=meetup_details[1],
                         talks=talks)
                scrapped_json = json.dumps(scrapped_info)

                print(scrapped_json)
        
            else:
                print('Please specify correct output format as the script argument (--output-format=text/json)')
    
        except:
            meetup_details = check_date_and_address(response)
            talks = get_talks(response)
            print(meetup_details)
            print("\n")
            for talk in talks:
                print(talk.text)
                print("\n")   
    except:
        print ('No details available yet for the next PyLight talk, please drop by in a few days!')
         