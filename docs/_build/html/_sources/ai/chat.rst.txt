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


Keyword Arguments
------------------

For more advanced LLM calls, you can pass in additional arguments. To use these, you must include 
the name of the parameter you're setting.

.. code-block:: promptscript

    chat prompt, model, api_key, max_tokens=100, system_prompt="you are a pirate."

**Keyword Arguments**

    **max_tokens** (int, optional): Max LLM response length in tokens. If not set, the default is 4096.

    **system_prompt** (str, optional): Instructions to tell LLM how to respond to queries. If not set,
    the default system prompt is ``you are a helpful chat assistant``.

Supported Models
----------------

.. tabs::

    .. tab:: OpenAI

        ``gpt-3.5-turbo``, ``gpt-4``, ``gpt-4-turbo``, ``gpt-4-turbo-preview``, ``gpt-4o``

    .. tab:: Anthropic

        ``claude-3-5-sonnet``, ``claude-3-opus``, ``claude-3-sonnet``, ``claude-3-haiku``

        .. note:: These are aliases for the latest versions of each of these models. You can also specify a specific
            release (e.g. ``claude-3-5-sonnet-20240620``).