from gethtml import get_content
import requests
import sys


def url_fix(url):
    if not url.startswith("https"):
        url = "https://" + url

    try:
        if not url.endswith(".com"):
            URL = url + ".com"
        if requests.get(URL).status_code != requests.codes.ok:
            pass
    except:
        URL = url + ".org"

    return URL


def main():
    while True:
        try:
            user_input_url = raw_input("['e' to exit] URL>> ")

            if user_input_url == "e":
                sys.exit()
            if not user_input_url:
                continue

            #fixing url
            user_input_url = url_fix(user_input_url)

# module gethtml <
            scraper = get_content(user_input_url)
            print scraper.request()
# module gethtml >
        except EOFError:
            break


if __name__ == "__main__":
    main()