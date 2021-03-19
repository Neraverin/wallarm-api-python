# Setup file
from setuptools import setup

setup(
    packages=['wallarm_api'],
    name='wallarm_api',
    version='0.6',
    license='Apache license 2.0',
    description='Wallarm API client',
    author='Vladimir Salykin',
    author_email='neraverin@gmail.com',
    url='https://github.com/Neraverin/wallarm-api-python',
    download_url='https://github.com/Neraverin/wallarm-api-python/archive/v0.6.tar.gz',
    keywords=['Wallarm', 'API client'],
    install_requires=[
        'requests',
        'pydantic',
        'urllib3'
    ],
    setup_requires=['wheel'],
    python_requires='>=3.6, <4',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
    ],
)
