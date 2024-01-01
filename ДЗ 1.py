from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder=clean_folder.clean:main'
        ]
    },
    install_requires=[
        'click'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for cleaning up folders',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/clean_folder',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)