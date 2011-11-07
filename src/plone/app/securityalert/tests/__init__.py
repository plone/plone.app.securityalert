from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

class SecurityAlertLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import plone.app.securityalert
        self.loadZCML(package=plone.app.securityalert)

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'plone.app.securityalert:default')

SECURITYALERT_FIXTURE = SecurityAlertLayer()
SECURITYALERT_INTEGRATION_TESTING = IntegrationTesting(bases=(SECURITYALERT_FIXTURE,), name="SecurityAlert:Integration")
