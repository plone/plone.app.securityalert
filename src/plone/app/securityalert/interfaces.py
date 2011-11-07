from z3c.form import interfaces

from zope import schema
from zope.interface import Interface

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('plone.app.securityalert')


class ISecurityAlertTool(Interface):
    pass

class ISecurityAlertSettings(Interface):
    """Global Security Alert settings. This describes records stored in the
    configuration registry and obtainable via plone.registry.
    """

    last_time_run = schema.TextLine(title=_(u"Last Time Run"),
                                  description=_(u"help_last_time_run",
                                                default=u"The last time the security alert service "
                                                         "checked plone.org for vulnerabilities"),
                                  required=False,
                                  default=u'',)

