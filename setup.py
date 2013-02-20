from setuptools import setup, find_packages
import os

version = '1.5.1.dev0'

setup(name='rt.purge',
      version=version,
      description="Product for Plone for invalidate (purge) documents "
                  "cached in Varnish",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 3.3",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone varnish purge cache',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='http://www.redturtle.it/',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['rt'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.interface',
          'zope.component',
          'zope.event',
          'zope.annotation',
          'zope.lifecycleevent',
          'zope.i18nmessageid',
          'plone.app.registry',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
