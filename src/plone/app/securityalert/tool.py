from OFS.SimpleItem import SimpleItem
from AccessControl import ClassSecurityInfo
from Globals import InitializeClass
from zope.interface import implements

from interfaces import ISecurityAlertTool

class SecurityAlertTool(SimpleItem):
    implements(ISecurityAlertTool)
    security = ClassSecurityInfo()


    def __init__ (self, id, title=None):
        super (SecurityAlertTool, self).__init__ (id, title)

    

InitializeClass(SecurityAlertTool)







