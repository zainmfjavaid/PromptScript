:description: How to use loops in PromptScript

Loops
=====

.. rst-class:: lead

    Writing ``for`` and ``while`` loops in PromptScript.

----

Loops in PromptScript function the same as in Python:

For Loops
---------

.. code-block:: promptscript

    for i in range(1, 11):
        show i

You can also use ``len``:

.. code-block:: promptscript

    string = "word"
    for i in range(len(string)):
        show i

Or iterate through values:

.. code-block:: promptscript

    string = "word"
    for character in string:
        show character

While Loops
-----------

.. code-block:: promptscript

    x = 10
    while x > 0:
        show x
        x -= 1