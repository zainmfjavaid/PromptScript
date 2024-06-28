:description: Guide on running PromptScript embedded in Python.

Python
======

.. rst-class:: lead

    Using the ``promptscript`` package to run PromptScript embedded in Python.

----

There are two main ways to run PromptScript in Python using the ``promptscript`` package: running files or commands.

Running PromptScript Files
--------------------------

.. code-block:: python
    :linenos:
    :caption: main.py

    from promptscript.executor import FileExecutor


    file_executor = FileExecutor()
    file_executor.run('file.prompt')


Running Commands
----------------

.. code-block:: python
    :linenos:
    :caption: main.py

    from promptscript.executor import CommandExecutor


    command_executor = CommandExecutor()
    command_executor.run('show "Hello, World!"')