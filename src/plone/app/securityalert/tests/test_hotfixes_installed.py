import unittest2 as unittest

from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login

from plone.app.securityalert.tests import SECURITYALERT_INTEGRATION_TESTING

class NoSecurityHoles(unittest.TestCase):

    layer = SECURITYALERT_INTEGRATION_TESTING

    def test_all_hotfixes_installed_is_fine(self):
        from plone.app.securityalert.checks.security import HotfixCheckViewlet
        portal = self.layer['portal']
        viewlet = HotfixCheckViewlet(portal, None, None, manager=None)

        hotfix = ['Plone', 'HotfixCVE00000000', 'http://plone.org']
        viewlet.getInstalledHotfixes = lambda: [hotfix[1]]
        viewlet.getHotfixesForVersion = lambda version: [hotfix]
        viewlet.update()

        self.assertEqual(viewlet.severity, "None")
        self.assertEqual(viewlet.missing, [])

    def test_missing_hotfix_is_critical(self):
        from plone.app.securityalert.checks.security import HotfixCheckViewlet
        portal = self.layer['portal']
        viewlet = HotfixCheckViewlet(portal, None, None, manager=None)

        hotfix = ['Plone', 'HotfixCVE00000000', 'http://plone.org']        
        viewlet.getInstalledHotfixes = lambda: []
        viewlet.getHotfixesForVersion = lambda version: [hotfix]
        viewlet.update()

        self.assertEqual(viewlet.severity, "Critical")
        self.assertEqual(viewlet.missing, [hotfix])
        self.assertIn('HotfixCVE00000000', viewlet.text)
    
    def test_unneeded_hotfix_warns(self):
        from plone.app.securityalert.checks.security import HotfixCheckViewlet
        portal = self.layer['portal']
        viewlet = HotfixCheckViewlet(portal, None, None, manager=None)

        hotfix = ['Plone', 'HotfixCVE00000000', 'http://plone.org']
        viewlet.getInstalledHotfixes = lambda: [hotfix[1]]
        viewlet.getHotfixesForVersion = lambda version: []
        viewlet.update()

        self.assertEqual(viewlet.severity, "Warning")
        self.assertIn('HotfixCVE00000000', viewlet.text)