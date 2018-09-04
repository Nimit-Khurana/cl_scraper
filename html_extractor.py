'''define and extract html tags
 a contains hyperlink or links to another page
 h contains headers
 p contains paragraph
 '''

import re
import collections

important_tags = ("<a>",
                  "<h1>","<h2>","<h3>","<h4>"
                  "<html>",
                  "<image>",
                  "<p>",
                  "<main>",
                  "<link>")


FIND_TAG_DICT= { "TAG_A" : "<a.+?<.+?/a>",
            "TAG_HTML" : "<html.+?",
            "TAG_IMAGE" : "<(img.+?)>",
            "TAG_MAIN" : "<main.+?>.+?",
            "TAG_LINK" : "<(link.+?)>",
            "TAG_P" : "<p.+?/p>"
            }

TO_REMOVE_TAGS = {"TAG_SPAN" : "(<span.+?>[\w\d\S\s]+?)",
                  "TAG_DIV" : "<div.+?>[\S]+?" ,
                  "TAG_STYLE" : "(<style.+?>.+?)"
}

elem_dict = {}
'''
youtube only
'''
YOUTUBE_VID = "(watch\?v=.+?)"

class extract():
    def __init__(self,file):
        self.file = file


    def extractor(self):
        # collections module defaultdict.. check link*
        # https://docs.python.org/2/library/collections.html#collections.defaultdict
        for tag in FIND_TAG_DICT.keys():
            print tag
            for tag_content in re.compile(FIND_TAG_DICT[tag]).findall(self.file.getvalue()):
                if elem_dict.has_key(tag):
                    elem_dict.setdefault(tuple(FIND_TAG_DICT.keys()), []).append(tag_content)
                    # setdefault takes tuple/parenthesis
                else:
                    elem_dict[tag] = tag_content
        print elem_dict[tag]

    def purge_tags(self):
        for tag in TO_REMOVE_TAGS.keys():
            for content in re.compile(TO_REMOVE_TAGS[tag]).findall(self.file.getvalue()):
                improved_line = re.sub(content,"sexxxxxxxx",content)
                print improved_line



    def parser(self):
        for element in elem_dict.keys():
            print elem_dict[element]