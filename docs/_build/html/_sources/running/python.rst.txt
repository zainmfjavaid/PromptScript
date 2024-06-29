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

You can also pass parameters into the executor:

.. code-block:: python
    :linenos:
    :caption: main.py

    file_executor.run('file.prompt', user_prompt='What is 2+2?')

Then access them directly from your PromptScript file.

.. code-block:: promptscript
    :linenos:
    :caption: file.prompt

    chat_response = chat user_prompt, "gpt-4o", "API_KEY"

Running Commands
----------------

.. code-block:: python
    :linenos:
    :caption: main.py

    from promptscript.executor import CommandExecutor


    command_executor = CommandExecutor()
    command_executor.run('show "Hello, World!"')

The CommandExecutor also supports passing in parameters.

.. code-block:: python
    :linenos:
    :caption: main.py

    command_executor.run('show msg', msg='Hello, World!')

Getting Output from PromptScript
--------------------------------

To make output from PromptScript files avaliable in Python, you can use the ``yield`` command. The first argument to ``yield`` is
the key to make the value avaliable through, while the second argument is the value itself.

.. important:: ``yield`` **does not** operate like return in Python. Code after a ``yield`` statement **will be executed**.

.. code-block:: promptscript
    :linenos:
    :caption: file.prompt
    :emphasize-lines: 2

    chat_response = chat user_prompt, "gpt-4o", "API_KEY"
    yield "chat_response", chat_response

We can then access the value of chat_response:


.. container:: demo

    .. code-block:: python
        :linenos:
        :caption: main.py

        from promptscript.executor import FileExecutor


        file_executor = FileExecutor()
        output = file_executor.run('file.prompt', user_prompt='What is 2+2?')

        print(output)

    .. code-block:: python
        :class: demo-result

        {'chat_response': '2+2 equals 4.'}

.. note:: ``yield`` also works the same way in the ``CommandExecutor`` and ``PersistentCommandExecutor``.