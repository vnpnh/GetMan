
VERSION = (0, 0, 0, '', 1)

if VERSION[3] and VERSION[4]:
	VERSION_TEXT = '{0}.{1}.{2}{3}{4}'.format(*VERSION)
else:
	VERSION_TEXT = '{0}.{1}.{2}'.format(*VERSION[0:3])

VERSION_EXTRA = ''
LICENSE = 'MIT License'