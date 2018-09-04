import re
import StringIO
from html_extractor import *

class cleaner:
    def __init__(self, htmlrequested):
        self.html = htmlrequested


    def virtual_html(self):
        i = 1
        html_content = self.html.content
        # create a virtual file for html content
        # reading--> self.write_file.read/readline/readlines()

        write_file = StringIO.StringIO(html_content)

        # TEST SECTION
        #f = open("html.txt","w")
        #f.write(self.html.content)
        added_newline_file = StringIO.StringIO()

        # first cleaning---> adding new lines/ shortening lines
        for line in write_file.readlines():
            # strip line with trailing and leading whitespaces

            #strip_line = re.sub(r"(<.+?>)([\w\d\W]+?)(</.+?>)", r"\1\2\3\n", line).strip()

            ex_line = re.sub(">",">\n",line).strip()

            # checking.... uncomment next line to see effect
            # subbed_line = re.sub("id","sexxxxxxxxx",strip_line)
            # print str(i) + "\t" + ex_line


            added_newline_file.write(ex_line)
            i+=1




        #print added_newline_file.getvalue()
        # TEST SECTION
        #g = open("new.txt", "w")
        #g.write(added_newline_file.getvalue())

        # end of first cleaner >

        return extract(added_newline_file).extractor()