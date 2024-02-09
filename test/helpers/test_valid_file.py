import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../promptscript')))

from utils.is_valid_file import is_promptscript_file


assert is_promptscript_file('/dir1/dir2/dir3/file.prompt')
assert is_promptscript_file('dir1/file.prompt')
assert is_promptscript_file('file.prompt')
assert is_promptscript_file('/file.prompt')

assert is_promptscript_file('/dir1/dir2/dir3/file')
assert is_promptscript_file('dir1/file')
assert is_promptscript_file('file')
assert is_promptscript_file('/file')

assert not is_promptscript_file('/dir1/dir2/dir3/file.py')
assert not is_promptscript_file('/dir1/dir2/dir3/fi.le')
assert not is_promptscript_file('dir1/fi.le')
assert not is_promptscript_file('fi.le')
assert not is_promptscript_file('prompt.file')