from setuptools import setup, find_packages

setup(
    name='promptscript',
    version='0.2.0',
    author='Zain Javaid',
    author_email='zainmfj@gmail.com',
    description='A simple scripting language for interacting with AI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/zainmfjavaid/PromptScript',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'promptscript=promptscript.__main__:main',
        ],
    },
    install_requires=[
        'openai==1.35.1',
        'Pygments==2.8.1',
        'shibuya==2024.6.23',
        'sphinx-tabs==3.4.5',
        'sphinx_design==0.5.0',
        'twine==5.1.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
    ],
    python_requires='>=3.6',
)