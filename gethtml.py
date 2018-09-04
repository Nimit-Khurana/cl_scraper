"""
get the url page source
to do ......
.. check encodings   *done
..http/s
..create dictionary of tags and their contents   *done



"""


import requests
from cleaner import *

class get_content():
    def __init__(self,url):
        self.url = url

    def request(self):
        page_request = requests.get(self.url)

        #check encoding
        print "Page Encoding: " + "\"" + page_request.encoding + "\"" + "\n"

        # cleaner module <
        clean_html = cleaner(page_request)
        clean_html.virtual_html()
        # cleaner module >