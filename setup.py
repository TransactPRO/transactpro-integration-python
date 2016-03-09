import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
        name='transactpro-integration-python',
        description='TransactPRO Python integration',
        long_description=read('README.md'),
        author='Olga Zdanchuk',
        author_email='zdanchuk@gmail.com',
        packages=['transactpro_integration'],
        version='0.1',
        url='https://github.com/TransactPRO/transactpro-integration-python',
        keywords=[],
        license='BSD',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Topic :: Internet :: WWW/HTTP :: WSGI',
            'Framework :: Django',
        ],
)
