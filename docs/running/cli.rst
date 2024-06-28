:description: Running PromptScript from the CLI.

CLI
===

.. rst-class:: lead

    Using the CLI to run PromptScript.

----

Using the ``promptscript`` alias, you can execute scripts or run individual commands.

Running PromptScript Files
--------------------------

.. code-block:: shell

    $ promptscript file.prompt

Or, if you'd like to run the file with parameters:

.. code-block:: shell

    $ promptscript file.prompt param1="Hello" param2="World"

These values can then be accessed directly in the file:

.. container:: demo

    .. code-block:: promptscript
        :linenos:
        :caption: file.prompt

        show "{}, {}!".format(param1, param2)

    .. code-block::
        :class: demo-result

        Output: Hello, World!

Running Commands
----------------

.. code-block:: shell

    $ promptscript

This will enter into the CLI. To exit, press :kbd:`^+d`.