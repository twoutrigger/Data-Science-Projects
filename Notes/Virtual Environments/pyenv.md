Notes on how to use pyenv for managing virtual environments:

1. For Windows, install pyenv via this link: https://pyenv-win.github.io/pyenv-win/#installation
2. Ensure that Path variable is updated. Restart VS Code if necessary
3. Verify pyenv installation via "pyenv --version"
4. Download Python version from options available via "pyenv install -l"
5. Specify global version of Python via "pyenv global <version>"

6. Create pyenv virtual env via "pyenv exec python -m venv <env name>"
7. Activate virtual env via "<env name>/Scripts/activate"