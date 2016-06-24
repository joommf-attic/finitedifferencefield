from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='finitedifferencefield',
    version='0.1',
    description='A Python package for analysing and manipulating finite difference vector fields',
    long_description=readme,
    author='Computational Modelling Group',
    author_email='fangohr@soton.ac.uk',
    packages=['finitedifferencefield', 'finitedifferencefield.tests'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
