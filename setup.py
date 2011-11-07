from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='plone.app.securityalert',
      version=version,
      description="""Provides feedback on Plone site setup and warns against 
          unacceptable settings found.""",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "Topic :: System :: Systems Administration",
        ],
      keywords='plone security headsup',
      author='Matthew Wilkes',
      author_email='wilkes@jarn.com',
      url='http://svn.plone.org/svn/plone/plone.app.securityalert',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir = {'':'src'},
      namespace_packages=['plone', 'plone.app'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.testing',
          'plone.app.registry',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
          ],
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
