import functools
import pkg_resources

from setuptools import setup, find_packages

from pip.req import parse_requirements as parse_reqs


# Compatibility with older versions of pip
pip_dist = pkg_resources.get_distribution('pip')
pip_version = tuple(map(int, pip_dist.version.split('.')))

# Use a base partial that will be updated depending on the version of pip
parse_requirements = functools.partial(parse_reqs, options=None)

if pip_version < (1, 2):
    # pip versions before 1.2 require an options keyword for using it outside
    # of invoking a pip shell command
    from pip.baseparser import parser
    parse_requirements.keywords['options'] = parser.parse_args()[0]

if pip_version >= (1, 5):
    # pip 1.5 introduced a session kwarg that is required in later versions
    from pip.download import PipSession
    parse_requirements.keywords['session'] = PipSession()


setup(
    name='helga-giphy',
    version='0.1.0',
    description="A command plugin to search giphy for an anmiated gif.",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'Framework :: Twisted',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='helga giphy',
    author="Shaun Duncan",
    author_email="shaun.duncan@gmail.com",
    url="https://github.com/shaunduncan/helga-giphy",
    packages=find_packages(),
    py_modules=['helga_giphy'],
    include_package_data=True,
    install_requires=[
        str(req.req) for req in parse_requirements('requirements.txt')
    ],
    zip_safe=True,
    entry_points=dict(
        helga_plugins=[
            'giphy = helga_giphy:giphy',
        ],
    ),
)
