:description: How to print in PromptScript

Printing
========

.. rst-class:: lead

    Using ``show`` to print values in PromptScript.

----

.. code-block:: promptscript
    :linenos:

    show "Hello, World!"
    show "{} - {}".format("Slot 1", "Slot 2")

.. note:: Strings can also be created with single quotes

You can also print variables:

.. code-block:: promptscript

    message = "Hello, World!"
    show message

Or the output from another process:

.. code-block:: promptscript

    show [read "file.txt"]

.. tip:: The square brackets (``[]``) are for chaining. Learn more about :ref:`operation chaining <chaining>` here.