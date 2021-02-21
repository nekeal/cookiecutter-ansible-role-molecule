#!/usr/bin/env python
import os
import shutil
import subprocess


def subprocess_cmd(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout)


if '{{ cookiecutter.add_github_actions_config }}' == 'n':
    shutil.rmtree(".github/workflows")

subprocess_cmd('git init')
subprocess_cmd('git add .')
subprocess_cmd('pre-commit install')

print(f"Path to your new role is {os.getcwd()}")
