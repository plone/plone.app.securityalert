import pkg_resources
import unittest2 as unittest

from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login

from plone.app.securityalert.tests import SECURITYALERT_INTEGRATION_TESTING

from plone.app.securityalert.rssmuncher import fetch

class TesterMuncher(unittest.TestCase):

    layer = SECURITYALERT_INTEGRATION_TESTING

    def test_tool_is_installed(self):
        testannouncementfile = pkg_resources.resource_filename("plone.app.securityalert.tests", "testannouncement.rss")

        fin = open(testannouncementfile, "r")
        result = fetch(stream=fin)
        self.assertTrue(len(result))
