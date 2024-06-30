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

    **model** (str: required): The model to use for image generation.

    **api_key** (str: required): API key for the image generation service.

    **destination_file** (str: required): File path to save generated image to.

**Output**
    
    **None** (output saved to destination_file).

Supported Models
----------------

.. tabs::

    .. tab:: OpenAI

        ``dall-e-3``, ``dall-e-2``

    .. tab:: Stability AI

        ``ultra``, ``core``, ``sd3``