from requests_html import HTMLSession


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
    response = get_html(url="https://www.pylight.org")
    meetup_details = check_date_and_address(response)
    talks = get_talks(response)
    print(meetup_details)
    print("\n")
    for talk in talks:
        print(talk.text)
        print("\n")
