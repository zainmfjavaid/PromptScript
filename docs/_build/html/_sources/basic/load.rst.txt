:description: How to read environment variables in PromptScript?

Environment Variables
=====================

.. rst-class:: lead

    Using ``load`` to access PromptScript environment files.

----

PromptScript has its own environment management system.

Creating an Environment File
----------------------------

You can create a PromptScript environment file be creating a file with the name ``.env.prompt``.

.. code-block:: promptscript
    :linenos:
    :caption: .env.prompt
    
    API_KEY="SUPER_SECRET"
    CHAT_MODEL="LLM-01"

You can also run PromptScript code in your ``.env.prompt`` file:

.. code-block:: promptscript
    :linenos:
    :caption: .env.prompt

    prod = True
    
    if prod:
        API_KEY="PROD_KEY"
    else:
        API_KEY="TESTING_KEY"
    CHAT_MODEL="LLM-01"

Accessing Environment Variables
-------------------------------

To access environment variables from a PromptScript file, you can use the ``load`` keyword

----

.. code-block:: promptscript
    
    load variable_name

**Parameters**

    **variable_name** (str: required): Name of the variable to load from the ``.env.prompt`` file.

**Output**

    **Any**: The variable's value.

----

So, for this example, we could access the ``API_KEY`` and ``CHAT_MODEL`` fields like this:

.. code-block:: promptscript
    :linenos:
    :caption: file.prompt

    api_key = load "API_KEY"
    chat_model = load "CHAT_MODEL"

.. important:: Make sure your PromptScript file and environment file are in the same directory!