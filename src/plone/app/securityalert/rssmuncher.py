from lxml import etree


XMLNS = {
        "rss": "http://purl.org/rss/1.0/",
        "alert": "http://namespaces.plone.org/securityalert" }


def fetch(url=None, stream=None):
    """Returns a list of lxml etree's from an rss at url""" 


    if stream is None:
        raise Exception ("No stream to read rss data from")

    rssdoc = etree.parse(stream)
    items = rssdoc.findall("//rss:content/rss:item", namespace=XMLNS)

    import pdb; pdb.set_trace()
    
    announcements = []
    for item in items:
        
        alert_e = item.xpath("//alert:alert", namespace=XMLNS)

        alert = {}

        # below is old
        announcement = {"link": item.link}
        content = item.content
        tree = etree.fromstring(content)
        announcement["payload"] = tree.find("{%s}announcement" % NAMESPACE)


    return announcements


        



        

        






