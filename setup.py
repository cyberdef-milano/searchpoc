from setuptools import setup, find_packages

setup(
    name='searchpoc',
    version=f'1.0',
    description='Searchpoc is a tool to extract PoCs from CVE ids',
    long_description="""
    Why manually look for a PoC in the wild, wild web? This python 
    script can query github.com, exploit-db.com, youtube.com and 
    cvebase.com to get as much PoCs as you can get. Enjoy!
    """,
    author='Valerio Casalino',
    author_email='casalinovalerio.cv@gmail.com',
    url='https://github.com/cyberdef-milano/searchpoc',
    license='GPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Security',
    ],
    keywords='searchpoc vulnerability cve poc scraping',
    packages=find_packages(),
    scripts=['install/searchpoc'],
)