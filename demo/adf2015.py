#!/usr/bin/env python
# -*- coding: utf-8 -*-

from py4slide import Slide, Page, SlideStyle


s = Slide.Slide()
s.setStyle(Slide.SlideStyle.NATURAL)

p0 = Page.Page(
        title="Setting",
        contents=["This is setting"])

p1 = Page.Page(
        title="Introduction",
        contents=["by @Mizuki_Sonoko"])

p2 = Page.Page(title="Hello, world!",
        contents=[
            "I'm from University of Aizu.",
            "My name is Taisei Igarashi",
            "twitter: @Mizuki_Sonoko"
            "github: https://github.com/MizukiSonoko"])

p3 = Page.Page(title="Favorite",
        contents=[
            "Android(Kotlin, Java?), iOS(Swift,Objective-C)",
            "AWS( EC2, DynamoDB, S3)",
            "Docker",
            "Hardware( Edison, Raspberry-pi)"
        ])

p4 = Page.Page(title="Favorite",
        contents=[
            "#Anime & Game",
            "Is order a rabbit?",
            "Kiniro mosaic",
            "Sakura Trick",
            "LoveLive!",
            "LoveLive school idol festival",
            "Minecraft"
            "team teamMizuki / spiritualDB",
    ])

p5 = Page.Page(title="Other",
        contents = [
            "#Religion",
            "Vim",
            "zsh",
            "#Language +",
            "C/C++/C++11",
            "Java Java(ART)",
            "react.js",
            "Python2.x / 3.x",
            "Kotlin"
    ])

pages = []
pages.append(Page.Page(title="About this application",
        contents=[
            "This is py4slide beta. ",
            "simple presentation application",
            "only ascii code",
            "https://github.com/MizukiSonoko/py4slide",
            "bug! bug! bug! Progress is not very good!!"
    ]))

pages.append(Page.Page(title="Point",
    contents=[
        "You can use remote! (this app is in Tokyo region)",
        "terminal!!",
        "Colorful!"
    ]))

pages.append(Page.Page(title="(6)Extras",
    contents=[
        "#License",
        "Copyright Sonoko Mizuki 2015.",
        "BSD 3-Clause license, see LICENSE.txt.",
        "#Dependencies",
        "colorama url(https://pypi.python.org/pypi/colorama)",
        "Python 2.7",
    ]))

pages.append(Page.Page(contents=[]))

s.add(p0)
s.add(p1)
s.add(p2)
s.add(p3)
s.add(p4)

s.addList(pages)

s.start()

