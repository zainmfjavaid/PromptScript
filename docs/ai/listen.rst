Transcription
=============

.. rst-class:: lead

    Using ``listen`` to perform speech-to-text tasks

----

PromptScript currently supports audio transcription using `OpenAI's Whisper <https://openai.com/index/whisper/>`_
through the ``listen`` keyword.

Syntax
------

.. code-block:: promptscript

    listen file_path, api_key

**Parameters**

    **file_path** (str: required): File to transcribe.

    **api_key** (str: required): OpenAI API key.

**Output**

    **str**: Transcribed text.

.. note:: The following file formats are supported: ``.mp3``, ``.mp4``, ``.wav``, ``.mpeg``, ``.mpga``, ``.webm``