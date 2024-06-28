:description: How to read and write files in PromptScript?

File I/O
========

.. rst-class:: lead

    Using ``read`` and ``save`` to perform basic file I/O operations in PromptScript.

----

PromptScript currently only supports basic file I/O operations on non-binary files.

Reading Files
-------------

To read the content of files, use the ``read`` command

.. code-block:: promptscript

    read file_path


**Parameters**
    
    **file_path** (str: required): File path to read from.

**Output**

    **str**: The file's text content.

Writing Files
-------------

To write to files, use the ``save`` command

.. code-block:: promptscript

    save content, file_path

**Parameters**

    **content** (str: required): Text to write to file.

    **file_path** (str: required): File path to read from.

**Output**

    **None**.

Example Usage
-------------


.. container:: demo

    .. code-block:: promptscript
        :linenos:
        :emphasize-lines: 3, 4

        message = "File Content"

        save message, "file.txt"
        show [read "file.txt"]

    .. code-block::
        :class: demo-result

        Output: File Content
