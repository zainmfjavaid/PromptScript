:description: How to read chain together commands in PromptScript?

Chaining
========

.. rst-class:: lead

    Chaning multiple PromptScript commands together.

----

.. _chaining:

To pass the output of one process as the parameter of another, surround it in square brackets (``[]``). Example:

.. code-block:: promptscript

    save [chat "<prompt>", "<model>", "<api_key>"], "file.txt"

.. note:: Chaining isn't required for passing the output of one process into a method that only takes one parameter 
    (e.g. ``show``). It's still recommended for readability.