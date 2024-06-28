:description: How to write conditionals in PromptScript

Conditionals
============

.. rst-class:: lead

    Using conditionals in PromptScript.

----

Conditionals in PromptScript function the same as in python:

.. code-block:: promptscript
    :linenos:
    
    number = 8
    guess = 5

    if guess > number:
        show "your guess is too high."
    elif guess < number:
        show "your guess is too low."
    else:
        show "you guessed correctly!"