from setuptools import setup, find_packages

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='create-next-app', 
    version='0.0.1', 
    packages=find_packages(), 
    author='Arbaaz Shaikh', 
    author_email='sarbaaz050@gmail.com', 
    description='Initialize NextJS Project', 
    long_description=long_description, 
    long_description_content_type='text/markdown', 
    url='https://github.com/sarbaaz0303/create-next-app',  # URL of the project
    license='NoHarm-draft', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'License :: NoHarm-draft License',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', 
    py_modules=['create-next-app'], 
    package_dir={'':'create-next-app/src'}, 
    install_requires=['requests', 'termcolor'] 
)
