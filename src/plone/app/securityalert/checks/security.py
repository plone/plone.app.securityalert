import sys
import urllib
import urllib2

from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName

HOTFIX_URL = "http://plone.org/getHotfixes"

class HotfixCheckViewlet(ViewletBase):
    
    title = "Security Hotfixes"
    
    def getHotfixesForVersion(self, version):
        version = urllib.urlencode(version)
        for line in urllib2.urlopen(HOTFIX_URL, data=version).readlines():
            # Releaser, name, url
            yield line.split(" ")
    
    def getInstalledHotfixes(self):
        modules = sys.modules.keys()
        modules = map(str.lower, modules)
        hotfix_modules = [mod for mod in modules if 'hotfix' in mod]
        for hotfix in hotfix_modules:
            for part in hotfix.split("."):
                if 'hotfix' in part:
                    yield part
    
    def update(self):
        migration = getToolByName(self.context, 'portal_migration')
        plone_version = migration.coreVersions()
        self.available = list(self.getHotfixesForVersion(plone_version))
        self.installed = list(self.getInstalledHotfixes())
        self.missing = []
        for hotfix in self.available:
            if hotfix[1] not in self.installed:
                self.missing.append(hotfix)
            else:
                self.installed.remove(hotfix[1])
        if len(self.missing) > 0:
            self.severity = "Critical"
            self.text = "Some security fixes have not been installed."
            self.text += "Missing: " + ", ".join(cve[1] for cve in self.missing)
        elif len(self.installed) > 0:
            self.severity = "Warning"
            self.text = "Some unneeded security fixes are installed. This may cause some features to be unavailable."
            self.text = "Unneeded: " + ", ".join(self.installed)        
        else:
            self.severity = "None"
            self.text = "No missing hotfixes found."
        
        

