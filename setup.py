# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(

    name = "rt-api",
    version = "1.0",
    keywords = ("pdf2html", "xxx"),
    description = "api-SDK",
    long_description = "rt sdk for python",
    license = "MIT Licence",

    url = "http://pdf2html.com",
    author = "qiancheng.xiao",
    author_email = "qiancheng.xiao@weitaige.com",
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    #依赖包
    install_requires = [],
    #依赖的文件
    data_files= [('pdf2html',['./pdf2html/pdf2phtml/pdf2htmlEX/README.md','poppler-global.cpp'])],

    scripts = [],
    entry_points = {
    }
)