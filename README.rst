===============================
bash.org quote viewer
===============================

.. image:: https://badge.fury.io/py/bash_quote.png
    :target: http://badge.fury.io/py/bash_quote
    
.. image:: https://travis-ci.org/ruairif/bash_quote.png?branch=master
        :target: https://travis-ci.org/ruairif/bash_quote

.. image:: https://pypip.in/d/bash_quote/badge.png
        :target: https://crate.io/packages/bash_quote?version=latest


Browse quotes on bash.org from the comfort of your shell.

* License: BSD 3-Clause License
* Documentation: http://bash_quote.rtfd.org.

Installation
------------
If you have pip installed all you have to do is::

    pip install bash_quote

Usage
-----
If you have bash_quote installed in your environment you can view quotes 
by running the command::

    bashquote [-h] [-n [NUM_QUOTES]] [-t [{random,r,top,t,latest,l}]]

To use bash quote viewer in a project::

    import bash_quote

    # get a list of 10 random quotes with rating > 0
    bash_quote.get_quotes(option='r', num_quotes=10)

    # get the latest quote
    bash_quote.get_quotes(option='l', num_quotes=1)

    # get the top 100 quotes
    bash_quote.get_quotes(option='t', num_quotes=100)



Features
--------

* View the latest, top or random quotes on bash.org from the comfort of your
  shell
* Return a single quote or return up to 100 quotes if you really need to
  procrastinate
