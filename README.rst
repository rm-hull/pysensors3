PySensors3
----------
Python3 bindings to libsensors (via ctypes)

.. image:: https://img.shields.io/pypi/pyversions/pysensors3.svg
   :target: https://pypi.python.org/pypi/pysensors3

.. image:: https://img.shields.io/pypi/v/pysensors3.svg
   :target: https://pypi.python.org/pypi/pysensors3

.. image:: https://img.shields.io/maintenance/yes/2019.svg?maxAge=2592000

Hard fork of `pysensors <https://bitbucket.org/blackjack/pysensors/>`_. See `<doc/OLD_README.rst>`_ for original documentation.


Usage
-----

.. code-block:: python

   import sensors

   sensors.init()
   try:
       for chip in sensors.iter_detected_chips():
           print(f'{chip} at {chip.adapter_name}')
           for feature in chip:
               print(f'  {feature.label}: {feature.get_value()}')
   finally:
       sensors.cleanup()



Copyright
---------

Original license (LGPL 2+) retained for this derivative work.
