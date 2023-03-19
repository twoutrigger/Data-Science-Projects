Had issues for "pip install ChatterBot".

Pre-reqs to get chatterbot working:
1. created virtualenv venv_chat for standalone dependencies
2. Install Microsoft Visual C++ 14.0 or greater
    - https://github.com/gunthercox/ChatterBot/issues/2036
    - https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst
3. Install and upgrade LLVM
    - https://github.com/gunthercox/ChatterBot/issues/2009#issuecomment-678737176

Issue:
- Current version of chatterbot dependencies are not compatible with Python 3.8.
 - Returns error "AttributeError: module 'time' has no attribute 'clock'"

Solution:
- Install Python version 3.7. Specify venv to use 3.7 via "virtualenv venv_chat -p python3.7"
- Install previous chatterbot version via "python -m pip install chatterbot==1.0.4 pytz"
- More details here: https://realpython.com/build-a-chatbot-python-chatterbot/#:~:text=Step%201%3A%20Create%20a%20Chatbot,Custom%20Data%20and%20Start%20Chatting
