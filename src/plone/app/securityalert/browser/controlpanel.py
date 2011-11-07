from plone.app.registry.browser import controlpanel

from plone.app.securityalert.interfaces import ISecurityAlertSettings, _

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class SecurityAlertSettingsEditForm(controlpanel.RegistryEditForm):
    """Security Alert settings form.
    """

    schema = ISecurityAlertSettings
    label = _(u"Security Alert settings")
    id = "SecurityAlertSettingsEditForm"
    description = _(u"help_securityalert_settings_editform",
                    default=u"The Security Alert tool reports the "
                             "last time run and provides configuration options.")


class SecurityAlertSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = SecurityAlertSettingsEditForm

    index = ViewPageTemplateFile('controlpanel.pt')

    def settings(self):
        """Compose a string that contains all registry settings that are
           needed for the security alert control panel.
        """
        registry = queryUtility(IRegistry)
        settings = registry.forInterface(ISecurityAlertSettings, check=False)
        output = []

        # Globally enabled
        #if settings.last_time_run:
        #    output.append("last_time_run")

        settings.last_time_run = 'The security alert service has not yet been run.'
        output.append("last_time_run")
