Chat
====

.. rst-class:: lead

    Using ``chat`` to interact with LLMs

----

PromptScript supports chatting with LLMs through the ``chat`` keyword.

Syntax
------

.. code-block:: promptscript

    chat prompt, model, api_key

**Parameters**

    **prompt** (str: required): Prompt to send to LLM.

    **model** (str: required): What LLM to send the prompt to.

    **api_key** (str: required): The API key for whatever service you're sending the chat to.

**Output**

    **str**: Text response from the LLM.