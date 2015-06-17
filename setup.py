from distutils.core import setup

setup(
    name='pyhammer',
    # Compliant with https://pypa.io/en/latest/peps/#pep440s
    version='0.1.dev1',
    packages=['pyhammer', 'pyhammer.lib', 'pyhammer.test'],
    url='https://github.com/my0373/pyhammer',
    license='GPLv2',
    author='Matt York',
    author_email='myork@redhat.com',
    description='A python wrapper around the Red hat satellite 6 API methods.',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: System Administrators',
        'Topic :: System :: Software Distribution',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='satellite6 hammer python',
)
