# PromptScript

A simple scripting language for interacting with AI built on top of Python.

## Quick Install

With pip:
```bash
pip install promptscript
```

## Why PromptScript?

**PromptScript** is designed for efficient tooling with AI systems.

PromptScript can be written and executed on its own or embedded into Python projects and allows for no-boilerplate interactions with large language models (LLMs), image generation models, and transcription.

## Running PromptScript

Once you've installed PromptScript, you can run it in one of the following ways

### Option 1: CLI

Run:

```bash
promptscript
```

### Option 2: Files

Create a file ending in **.prompt**

Example _(test.prompt)_:
```
show "Hello, World!"
```

Then, you can run the file from the terminal:

```bash
promptscript test.prompt
```

Replacing _test.prompt_ with the actual file path

### Option 3: Embedded in Python

To run PromptScript from python, you can either run it from a file or individual commands

**Running From Files**

```python
from promptscript.executor import FileExecutor

FileExecutor().run('<file_name>.prompt')
```

**Running Individual Commands**

```python
from promptscript.executor import CommandExecutor

CommandExecutor().run('show "Hello World!"')
```

## Documentation

Visit [promptscript.wiki](https://promptscript.wiki) for full documentation and usage examples