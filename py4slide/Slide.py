#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Sonoko Mizuki 2014. BSD 3-Clause license, see LICENSE file. 

from colorama import init, Fore, Back, Style
from subprocess import call, check_output
from SlideStyle import SlideStyle

#from py4slide_page import Page

class Slide:

    def __init__(self, cols=-1, lines=-1):
        init()
        self.page=1
        if lines == -1:
            self.lines = int(check_output(['tput','lines']))
        else:
            self = lines

        if cols == -1:
            self.cols = 20 #適当決めた
        else:
            self.cols = cols
        self.back_col = Back.RESET

        self.styles = {}
        self.pages = []
    
    #3.x対応したいのでprintに挟む
    def __prn(self, txt="", newline=True):
        if newline:
            print txt
        else:
            print txt,

    def __chmod(self,back):
        self.__prn(back, False)
        self.__lines()

    def __lines(self):
        for _i in range(self.lines):
            self.__prn(' ', False)
        self.__prn()

    def __space(self, num):
        for i in range(num):
            self.__prn(' ',False)

    def __block(self, num):
        for i in range(num):
            self.__lines()

    def setStyle(self, style=SlideStyle.DEFAULT):
        self.back_col = style["Back"]
        self.text_col = style["Font"]


    def __header(self):
        self.__prn(self.back_col, True)
        self.__block(3)

    def __footer(self,page_num):
        self.__prn(self.back_col+Fore.RED, True)
        self.__lines()
        for _i_ in range(self.lines/2 - len(str(page_num))/2):
            self.__prn(' ', False)
        self.__prn(page_num,False)
        for _i_ in range(self.lines/2 - len(str(page_num))/2):
            self.__prn(' ', False)
        self.__prn()
        self.__lines()

    def __splitLine(self,s):
        length = len(s)
        return [s[i:i+self.lines*2] for i in range(0, length, self.lines*2)]

    def __ListText(self, text):
        res = ""
        for _i_ in range(self.lines - len(text)*(1/4)):
            res += ' '
        res += text
        for _i_ in range(self.lines - len(text)*(3/4)):
            res += ' '
        self.__prn(self.__splitLine(res)[0])
    

    def __centerText(self, text):
        res = ""
        for _i_ in range(self.lines - len(text)/2):
            res += ' '
        res += text
        for _i_ in range(self.lines - len(text)/2):
            res += ' '
        self.__prn(self.__splitLine(res)[0])
    
    
    def __view(self, page, count):
        call("clear")
        self.__header()
        self.__prn(Back.WHITE+Fore.BLUE)
        self.__block(self.cols/2+1)
        self.__chmod(Style.BRIGHT)
        if "title" in page.__dict__.keys() and page.title != "":
            self.__centerText(page.title)
        self.__chmod(Style.DIM)
        if "content" in page.__dict__.keys():
            for c in page.content:
                if c[0] == "#":
                    self.__ListText(c)
                else:
                    self.__centerText(c)
        self.__block(self.cols/2)
        self.__footer(count)

    def add(self, page):
        self.pages.append(page)

    def addList(self, pages):
        self.pages.extend(pages)

    def start(self):
        count = 1
        while True:
            if count == len(self.pages):
                return
            if count <= 1:
                count = 1
            self.__view(self.pages[count-1], count)
            while True:
                _indata=  raw_input(Style.RESET_ALL+"previous:j next:k first:f last:l ->")
                if _indata == "j":
                    count -= 1
                    break
                if _indata == "k":
                    count += 1
                    break
                if _indata == "f":
                    count = 1
                    break
                if _indata == "l":
                    count = len(self.pages)
                    break


if __name__ == "__main__":
    s = Slide()
    s.mainColor(Back.GREEN)
    s.textColor(Fore.BLUE)
    p1 = Page(title="Test Slide",contents=["This slide is tutorial.","by @Mizuki_Sonoko"])
    p2 = Page(title="Introduction",contents=["This library shows slide.","beta varsion.","hogehoge"])
    p3 = Page(title="Title only")
    p4 = Page(contents=["No title","#Contents only","content1","content2"])
    pages = []
    pages.append(Page(contents=[
        "You can insert page in slide using list",
        "pages = []",
        "pages.append(Page(contents=[\"sample1\"]))",
        "pages.append(Page(contents=[\"sample2\"]))",
        "slide.addList(pages)"]))
    pages.append(Page(title="",contents=[
        ]))
    pages.append(Page(contents=[]))
    s.add(p1)
    s.add(p2)
    s.add(p3)
    s.add(p4)

    s.start()

