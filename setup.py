from setuptools import setup, find_packages

setup(
    name='promptscript',
    version='0.1.0',
    author='Zain Javaid',
    author_email='zainmfj@gmail.com',
    description='A simple scripting language for interacting with AI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/zainmfjavaid/PromptScript',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'promptscript=project.__main__:main',
        ],
    },
    install_requires=[
        'annotated-types>=0.7.0',
        'anyio>=4.4.0',
        'certifi>=2024.6.2',
        'distro>=1.9.0',
        'exceptiongroup>=1.2.1',
        'h11>=0.14.0',
        'httpcore>=1.0.5',
        'httpx>=0.27.0',
        'idna>=3.7',
        'openai>=1.35.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
    ],
    python_requires='>=3.6',
)