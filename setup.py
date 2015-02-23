from distutils.core import setup
setup(
  name = 'emailvalidator',
  packages = ['emailvalidator'], # this must be the same as the name above
  version = '0.3',
  description = 'A python package for validating email',
  author = 'Amit Jaiswal, Rohit Sonawane',
  author_email = 'amitjaiswal396@gmail.com, rohitsonawane.genie@gmail.com',
  url = 'https://github.com/amitjaiswal396/emailvalidator', # use the URL to the github repo
  download_url = 'https://github.com/amitjaiswal396/emailvalidator/tarball/0.3', # I'll explain this in a second
  keywords = ['email', 'email validation', 'email validator', 'python package for email validation', 'python email validator'], # arbitrary keywords
  classifiers = ['Natural Language :: English','License :: Freeware', 'Programming Language :: Python :: 2.7'],
)