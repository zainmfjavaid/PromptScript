:orphan:

About
=====

.. rst-class:: lead

   What is PromptScript, why should you use it, and other FAQs.

----

What is PromptScript?
---------------------

PromptScript is a scripting language designed to make programmatically interacting with AI systems as easy as possible.
It's designed to be beginner-friendly, while containing powerful functionality out of the box. 

----

Why use it?
-----------

The most basic way to integrate AI into applications is through provider libraries. However, these are often difficult
to work with, and lock you in to using that company. If you ever want to switch from one provider to another, it'll 
require refactoring the entire code base.

Frameworks like `Langchain <https://langchain.com>`_ solve this issue, but introduce a number of their own: 

1. They're often over-specced, leading to confusing abstraction, bloat, and boilerplate.
2. Most only support one type of task (text generation, image generation, etc), meaning projects that work with more than one modality require multiple dependencies.

PromptScript makes it easy to integrate multiple AI systems across different modalities without major
code changes. 

With PromptScript, you can:

.. grid:: 1
    :gutter: 2
    :padding: 0
    :class-row: surface

    .. grid-item-card:: :octicon:`arrow-switch` Easily switch between AI providers
        
        Avoid vendor lock-in and choose the best provider for your needs.

    .. grid-item-card:: :octicon:`dependabot` Work with multiple AI modalities

        Integrate `text generation <ai/chat.html>`_, `image generation <ai/draw.html>`_, and other AI capabilities in a single project.

    .. grid-item-card:: :octicon:`issue-reopened` Quickly prototype and test

        Experiment with new ideas and iterate faster with minimal setup.

    .. grid-item-card:: :octicon:`plug` Run anywhere

        PromptScript can be run `on its own <running/cli.html>`_, or `embedded in Python <running/python.html>`_ applications.

----

Who made it?
------------

Howdy! I'm Zain Javaid, a 17 year-old high schooler living in Austin, Texas.

If you want to see what I'm up to, you can check out my `GitHub <https://github.com/zainmfjavaid>`_ or my `blog <https://zainj.dev>`_.

----

Can I use PromptScript for commercial projects?
-----------------------------------------------

Yes, PromptScript is liscensed under the `MIT License <https://opensource.org/license/mit>`_, which allows free use in both 
personal and commercial projects.

----

How can I contribute?
---------------------

Contributions to PromptScript are welcome and encouraged! Here are some ways you can contribute:

1. **Report Bugs**: If you encounter any issues, please report them on the `GitHub issue tracker <https://github.com/zainmfjavaid/PromptScript/issues>`_.
2. **Submit Feature Requests**: If you have ideas for new features or improvements, `open an issue <https://github.com/zainmfjavaid/PromptScript/issues/new?labels=feature>`_ with the ``feature`` label.
3. **Code Contributions**: If you're a developer, you can contribute code by forking the repository and submitting a pull request with your changes.