#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from urllib import urlopen

# url = "http://www.gutenberg.org/files/2554/2554.txt"
# raw = urlopen(url).read()
# print type(raw) #<type 'str'>
# print len(raw) #1176896
# print raw[:75]
# print raw[:2000]
#
# tokens = nltk.word_tokenize(raw)
# print type(tokens)#<type 'list'>
# print len(tokens)#254352
# print tokens[:10]
#
# text = nltk.Text(tokens)
# print type(text) #<type 'nltk.text.Text'>
# print "1",text[1020:1060]
# print "2"; text.collocations()
#
# print raw.find("PART I")#5338
# print raw.rfind("End of Project Gutenberg's Crime")#1157746
# raw = raw[5303:1157681]
# print raw.find("PART I")


# import re
# def clean_url(url):
#     html = compat.urlopen(url).read()
#     return clean_html(html)
# def clean_html(html):
#     """
#     Copied from NLTK package.
#     Remove HTML markup from the given string.
#
#     :param html: the HTML string to be cleaned
#     :type html: str
#     :rtype: str
#     """
#
#     # First we remove inline JavaScript/CSS:
#     cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
#     # Then we remove html comments. This has to be done before removing regular
#     # tags since comments can contain '>' characters.
#     cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
#     # Next we can remove the remaining tags:
#     cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
#     # Finally, we deal with whitespace
#     cleaned = re.sub(r"&nbsp;", " ", cleaned)
#     cleaned = re.sub(r"  ", " ", cleaned)
#     cleaned = re.sub(r"  ", " ", cleaned)
#     return cleaned.strip()
#
# url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
# html = urlopen(url).read()
# print html[:60]
# raw = clean_html(html)
# tokens = nltk.word_tokenize(raw)
# print tokens


# path = nltk.data.find('corpora/gutenberg/melville-moby_dick.txt')
# raw = open(path, 'rU').read()
# print raw[:20]







