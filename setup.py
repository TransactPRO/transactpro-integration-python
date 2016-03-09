import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
        name='transactpro',
        description='TransactPRO Python integration',
        long_description=read('README.md'),
        author='Olga Zdanchuk',
        author_email='zdanchuk@gmail.com',
        packages=['transactpro'],
        version='0.1',
        url='https://github.com/TransactPRO/transactpro-integration-python',
        keywords=[],
        license='BSD',
        install_requires=[
            'mock==1.0.1',
            'nose==1.3.0',
            'coverage==3.7.1',
            'pycurl==7.19.3.1',
            'wsgiref==0.1.2',
        ],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Topic :: Internet :: WWW/HTTP :: WSGI',
            'Framework :: Django',
        ],
)
