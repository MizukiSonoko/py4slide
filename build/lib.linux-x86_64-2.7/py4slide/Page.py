#!/usr/bin/python
#!coding:utf-8

from colorama import Fore

class Page:

    def __init__(self):
        self.title = ""
        self.content = []
        self.intex = []
        self.title_color = Fore.BLACK
        self.content_color = Fore.BLACK

    def __init__(self, **contents):
        flag = True
        if "title" in contents:
            self.title   = contents["title"]
            flag = False
        if "contents" in contents:
            self.content = contents["contents"]
            flag = False

        if flag:
            raise ValueError, 'No contents!'
