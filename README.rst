Sphinx tutorial
===============

This is a simple tutorial showing how to use sphinx to document your code.
In this folder there is some very simple code, and we want to create some nice
looking documentation.

Before you start let us create a virtual environment where we will install all our stuff

.. code::

   pip install virtualenv
   virtualenv --python python3 venv
   source venv/bin/activate

Let us also install the dummy package

.. code::
   
   python setup.py install


Install sphinx
##############
First thing we need to do in order to use sphinx is to install it

.. code::

   pip install sphinx

Create the doc directory
########################

Next we will create a the directory where we will put the documentation

.. code::

   mkdir doc
   cd doc

Now we run the `sphinx-quickstart` which is the first step in generating documentation.
This will ask you some questions, and I will reply as follows

.. code::


    (venv) Henriks-MacBook-Pro:doc henriknf$ sphinx-quickstart 
    Welcome to the Sphinx 1.7.6 quickstart utility.

    Please enter values for the following settings (just press Enter to
    accept a default value, if one is given in brackets).

    Selected root path: .

    You have two options for placing the build directory for Sphinx output.
    Either, you use a directory "_build" within the root path, or you separate
    "source" and "build" directories within the root path.
    > Separate source and build directories (y/n) [n]: y

    Inside the root directory, two more directories will be created; "_templates"
    for custom HTML templates and "_static" for custom stylesheets and other static
    files. You can enter another prefix (such as ".") to replace the underscore.
    > Name prefix for templates and static dir [_]: 

    The project name will occur in several places in the built documentation.
    > Project name: Mypackage
    > Author name(s): Henrik Finsberg
    > Project release []: 1.0

    If the documents are to be written in a language other than English,
    you can select a language here by its language code. Sphinx will then
    translate text that it generates into that language.

    For a list of supported codes, see
    http://sphinx-doc.org/config.html#confval-language.
    > Project language [en]: 

    The file name suffix for source files. Commonly, this is either ".txt"
    or ".rst".  Only files with this suffix are considered documents.
    > Source file suffix [.rst]: 

    One document is special in that it is considered the top node of the
    "contents tree", that is, it is the root of the hierarchical structure
    of the documents. Normally, this is "index", but if your "index"
    document is a custom template, you can also set this to another filename.
    > Name of your master document (without suffix) [index]: 

    Sphinx can also add configuration for epub output:
    > Do you want to use the epub builder (y/n) [n]: 
    Indicate which of the following Sphinx extensions should be enabled:
    > autodoc: automatically insert docstrings from modules (y/n) [n]: y
    > doctest: automatically test code snippets in doctest blocks (y/n) [n]: 
    > intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
    > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: 
    > coverage: checks for documentation coverage (y/n) [n]: 
    > imgmath: include math, rendered as PNG or SVG images (y/n) [n]: 
    > mathjax: include math, rendered in the browser by MathJax (y/n) [n]: y
    > ifconfig: conditional inclusion of content based on config values (y/n) [n]: 
    > viewcode: include links to the source code of documented Python objects (y/n) [n]: y
    > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]:

    A Makefile and a Windows command file can be generated for you so that you
    only have to run e.g. `make html' instead of invoking sphinx-build
    directly.
    > Create Makefile? (y/n) [y]: 
    > Create Windows command file? (y/n) [y]: n

    Creating file ./source/conf.py.
    Creating file ./source/index.rst.
    Creating file ./Makefile.

    Finished: An initial directory structure has been created.

    You should now populate your master file ./source/index.rst and create other documentation
    source files. Use the Makefile to build the docs, like so:
       make builder
    where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

You can look at your documentation by running

.. code::

   make html
   python -m http.server

Then open a webbrowser and go to `localhost:8000`, and navigate to `build/html`.

Creating the API documentation
##############################

Now we will make the documentation for our python package

.. code::

   sphinx-apidoc -o source/ ../myproject/


If you run `make html` now you will get a warnin saying `Unexpected section title`,
and this is because I have documented the code using the numpy style, which
is not default. Open `source/conf.py` and add `'sphinx.ext.napoleon'` to the list
called `extensions`. Let us also change the html theme.
Scroll down and set `html_theme = 'sphinx_rtd_theme'`, and run `pip install sphinx-rtd-theme`.

Now you can run `make html`.



Adding the README to the docs
#############################
Let us add this README file to the docs. Copy this README file to the source directory

.. code::

   cp ../README.rst source/.
   
Next, open `source/index.rst` and put in the following command in there

.. code::

   .. toctree::
      README
      myproject
      modules

   
Now let use have a look at the documentation.

Create pdf documentation
########################

Just do

.. code::

   make latexpdf
   open build/latex/Mypackage.pdf

