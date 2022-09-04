import setuptools
with open ( "README.md" , "r", encoding="utf-8") as fh:
    long_description = fh.read ( )

setuptools.setup (
    name = "ivansabogal_780" , # Replace with your own username
    version = "0.0.1" ,
    author = "Ivan Sabogal" ,
    author_email = "isabogal780@gmail.com " ,
    description = "A small example package" ,
    long_description = long_description ,
    long_description_content_type = "text/markdown" ,
    url = "https://github.com/pypa/sampleproject" ,
    classifiers=[
        "Programming Languege :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = setuptools.find_packages ( ) ,
    python_requires='>=3.6' ,
)
