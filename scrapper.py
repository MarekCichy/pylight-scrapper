from requests_html import HTMLSession


def get_html(url="https://www.pylight.org"):
    session = HTMLSession()
    response = session.get(url)
    return response


def check_date_and_address(response):
    details = response.html.find(".date-and-localization", first=True)
    return details.text


def get_talks(response):
    talks = response.html.find('.talk-title')
    authors = response.html.find('.talk-speaker')
    return authors, talks


def format_output(authors, talks):
    # Expected output format:
    # Speaker: Talk topic
    talks = "\n".join(
        [
            "{}: {}".format(author.text, talk.text)
            for author, talk in zip(authors, talks)
        ]
    )
    return talks


if __name__ == "__main__":
    pylight_response = get_html()
    pylight_authors, pylight_talks = get_talks(pylight_response)
    meetup_details = check_date_and_address(pylight_response)
    meetup_description = format_output(pylight_authors, pylight_talks)
    print(meetup_details)
    print(meetup_description)
