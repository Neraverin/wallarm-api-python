from distutils.core import setup

setup(
    name='wallarm_api',
    packages=['wallarm_api'],
    version='0.1',
    license='Apache license 2.0',
    description='Wallarm API client',
    author='Vladimir Salykin',
    author_email='neraverin@gmail.com',
    url='https://github.com/Neraverin/wallarm-api-python',
    download_url='https://github.com/Neraverin/wallarm-api-python/archive/v0.1-alpha.tar.gz',
    keywords=['Wallarm', 'API client'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
    ],
)
