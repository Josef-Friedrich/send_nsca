from setuptools import setup, find_packages


setup(
    name="send_nsca",
    version="0.1.4.1-yelp1",
    author="Yelp",
    author_email="yelplabs@yelp.com",
    url="http://github.com/Roguelazer/send_nsca",
    description='pure-python nsca sender',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",  # noqa: E501
        "Topic :: System :: Monitoring",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
    ],
    packages=find_packages(),
    scripts=["bin/py_send_nsca"],
    install_requires=['six'],
    long_description="""send_nsca -- a pure-python nsca sender

NSCA is the remote passive acceptance daemon used with many Nagios installs. It
ships with a (C-language) executable called send_nsca for submitting checks.
This is a mostly-clean re-implementation of send_nsca in pure-python. It
supports 10 of the 26 crypto functions used by upstream NSCA, sending to
multiple hosts with one invocation, and timeouts.
"""
)
