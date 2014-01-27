========
Usage
========

To use bash quote viewer in your shell::

    bashquote [-h] [-n [NUM_QUOTES]] [-t [{random,r,top,t,latest,l}]]


To use bash quote viewer in a project::

    import bash_quote

    # get a list of 10 random quotes with rating > 0
    bash_quote.get_quotes(option='r', num_quotes=10)

    # get the latest quote
    bash_quote.get_quotes(option='l', num_quotes=1)

    # get the top 100 quotes
    bash_quote.get_quotes(option='t', num_quotes=100)
