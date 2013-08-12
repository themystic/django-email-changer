#!/usr/bin/env python

from distutils.core import setup

setup(name="django-email-changer",
      version="0.0.1",
      description="A Django App to let users securely change the email associated with their account.",
      author="Tom Aratyn",
      author_email="tom@aratyn.name",
      url='http://github.com/themystic/djang_email_changer',
      license="MIT",
      install_requires=["django<1.5"],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "Framework :: Django",
          "Environment :: Web Environment",
      ])
