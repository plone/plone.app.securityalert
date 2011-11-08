import feedparser
from lxml import etree


NAMESPACE = "http://namespaceses.plone.org/securityalert"


def fetch(url):
    """Returns a list of lxml etree's from an rss at url""" 

    rss = feedparser.parse (url)

    announcements = []
    for item in rss.entries:
        announcement = {"link": item.link}

        content = item.content
        tree = etree.fromstring(content)
        announcement["payload"] = tree.find("{%s}announcement" % NAMESPACE)

        announcements.append(announcement)

    return announcements


        



        

        






    return None


