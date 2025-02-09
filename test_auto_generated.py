import pytest
import os
import subprocess

def test_file_created():
    assert os.path.exists("Hello World.py")

def test_file_content():
    with open("Hello World.py", "r") as file:
        content = file.read()
        assert "print('Hello World')" in content

def test_execution():
    result = subprocess.run(["python", "Hello World.py"], capture_output=True, text=True)
    assert result.stdout.strip() == "Hello World"
