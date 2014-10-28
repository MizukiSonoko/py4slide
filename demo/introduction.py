#!/usr/bin/env python
# -*- coding: utf-8 -*-

from py4slide import Slide, Page, SlideStyle


s = Slide.Slide()
s.setStyle(Slide.SlideStyle.NATURAL)
p1 = Page.Page(
        title="Introduction Slide",
        contents=["This slide is tutorial.", "by @Mizuki_Sonoko"])

p2 = Page.Page(title="Introduction",
        contents=[
            "This library shows slide.",
            "beta varsion."])

p3 = Page.Page(title="(1)Import",
        contents=[
            "You import slide, Page from pyslide and",
            "SlideStyle from SlideStyle"
        ])

p4 = Page.Page(title="(2)Create slide",
        contents=[
            "You create slide.",
            "#case 1",
            "page1 = Page(title=\"Title!\",contents=[\"CONTENTS\"])",
            "#case 2",
            "page2 = Page(title=\"Title only\")",
            "#case 3",
            "page3 = Page(contents=[\"Contents\".\"Only\"])",
    ])

p5 = Page.Page(title="(3)Register slide",
        contents = [
            "You register slide",
            "slide.add(page1)",
            "slide.add(page2)",
            "slide.add(page3)",
    ])

pages = []
pages.append(Page.Page(title="(4)Also ...",
        contents=[
            "You can insert page in slide using list",
            "pages = []",
            "pages.append(Page(contents=[\"sample1\"]))",
            "pages.append(Page(contents=[\"sample2\"]))",
            "slide.addList(pages)"
    ]))

pages.append(Page.Page(title="(5)start",
    contents=[
        "You only start",
        "slide.start()"
    ]))

pages.append(Page.Page(title="(6)Extras",
    contents=[
        "#License",
        "Copyright Sonoko Mizuki 2014. BSD 3-Clause license, see LICENSE.txt.",
        "#Dependencies",
        "colorama url(https://pypi.python.org/pypi/colorama)",
        "Python 2.7",
    ]))

pages.append(Page.Page(contents=[]))

s.add(p1)
s.add(p2)
s.add(p3)
s.add(p4)

s.addList(pages)

s.start()

