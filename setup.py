import setuptools

setuptools.setup(
    include_package_data=True,
    name='hkshiteshpkg',
    version='0.0.1',
    description='limeguru python module',
    url='https://github.com/hkshitesh/hkshiteshpkg',
    author='hkshitesh',
    author_email='hkshitesh@gmail.com',
    packages=setuptools.find_packages(),
    install_requires=['pandas', 'pytest'],
    long_description='limeguru python module',
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
    ],
)