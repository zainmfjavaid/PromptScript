Image Generation
================

.. rst-class:: lead

    Using ``draw`` to generate and edit images

----

PromptScript supports image generation through the ``draw`` keyword.

Syntax
------

.. code-block:: promptscript

    draw prompt, model, api_key, destination_file

**Parameters**

    **prompt** (str: required): Prompt to generate image based on.

    **model** (str: required): What image generation model to send the prompt to.

    **api_key** (str: required): The API key for whatever service you're sending the chat to.

    **destination_file** (str: optional): File path to save generated image to

**Output**

    If ``destination_file`` is specified:

        **None**.

    If no ``destination_file`` is specified:

        **str**: Link to generated image.