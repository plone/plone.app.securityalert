from plone.app.registry.browser import controlpanel

from plone.app.securityalert.interfaces import ISecurityAlertSettings, _

from Acquisition import aq_base, aq_inner
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter, queryUtility
from plone.registry.interfaces import IRegistry
from plone.registry.interfaces import IRecordModifiedEvent

class SecurityAlertSettingsEditForm(controlpanel.RegistryEditForm):
    """Security Alert settings form.
    """

    schema = ISecurityAlertSettings
    label = _(u"Security Alert settings")
    id = "SecurityAlertSettingsEditForm"
    description = _(u"help_securityalert_settings_editform",
                    default=u"The Security Alert tool reports the "
                             "last time run and provides configuration options.")

    def updateFields(self):
        super(SecurityAlertSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(SecurityAlertSettingsEditForm, self).updateWidgets()


class SecurityAlertSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = SecurityAlertSettingsEditForm
    index = ViewPageTemplateFile('controlpanel.pt')
    last_time_run = 'This service has not yet run.'

    def settings(self):
        """Compose a string that contains all registry settings that are
           needed for the discussion control panel.
        """
        registry = queryUtility(IRegistry)
        settings = registry.forInterface(ISecurityAlertSettings, check=False)
        output = []

        # Globally enabled
        if settings.last_time_run:
            output.append("last_time_run")


    def mailhost_warning(self):
        """Returns true if mailhost is not configured properly.
        """
        # Copied from plone.app.controlpanel/plone/app/controlpanel/overview.py
        mailhost = getToolByName(aq_inner(self.context), 'MailHost', None)
        if mailhost is None:
            return True
        mailhost = getattr(aq_base(mailhost), 'smtp_host', None)
        email = getattr(aq_inner(self.context), 'email_from_address', None)
        if mailhost and email:
            return False
        return True
