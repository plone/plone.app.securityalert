import unittest2 as unittest

from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login

from plone.app.securityalert.tests import SECURITYALERT_INTEGRATION_TESTING

class ToolInstallation(unittest.TestCase):

    layer = SECURITYALERT_INTEGRATION_TESTING

    def test_tool_is_installed(self):
        portal = self.layer['portal']
        self.assertTrue('portal_security_alerts' in portal.objectIds())
