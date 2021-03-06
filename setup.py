from setuptools import setup, find_packages
import os

version = '0.3.dev0'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='ploneintranet.simplesharing',
      version=version,
      description="In-line sharing/collaboration controls whilst editing content",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='',
      author='plone intranet consortium',
      author_email='',
      url='https://github.com/ploneintranet/ploneintranet.simplesharing/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['ploneintranet', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.behavior',
          'plone.directives.form',
          'zope.schema',
          'zope.interface',
          'zope.component',
          'plone.api>=1.2.1',
          'collective.workspace',
          'collective.z3cform.chosen',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              'plone.app.contenttypes',
          ],
          'develop': [
              'Sphinx',
              'zest.releaser',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
