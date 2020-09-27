ICE Portal
==========

Python Client for getting the data from the `ICE portal <https://iceportal.de>`_
on ICE connections in Germany and partially in Switzerland.

This module is not official, developed, supported or endorsed by
`Deutsche Bahn <https://deutsche-bahn.de/>`_.

Installation
------------

The module is available from the `Python Package Index <https://pypi.python.org/pypi>`_.

.. code:: bash

    $ pip3 install iceportal

Usage
-----

The file ``example.py`` contains an example about how to use this module.

Currently available information:

- ID of the train
- The next stop
- The arrival track in the next station
- The arrival time for the next station


Development
-----------

For development is recommended to use a ``venv``.

.. code:: bash

    $ python3 -m venv .
    $ source bin/activate
    $ python3 setup.py develop

License
-------

``iceportal`` is licensed under MIT, for more details check LICENSE.
