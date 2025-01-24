Ensure you're good to go by typing 

```zsh
python3 --version
```

You're looking for something like `3.9.6` - i think it should already be installed by default?

Upgrade pip (pythons npm)

```zsh
python3 -m pip install --upgrade pip
```

Open vscode and create a file with the `.py` extension - eg `helloworld.py`

VSCODE should pop up with an offer to install extensions for you. Accept the offer. 

Hit `cmd + shift + p` and search `Python, run python file in terminal` and hit enter to run.

If you wanna be shouted at to learn more about python install the `Pylint` extension by Microsoft. 

If you want to have a go at making a request from API, make sure to install `requests`

```
pip3 install requests
```

tim knows more about the environment stuff idk

You might read about 'the standard library' - in JS, we kinda just have all its features available. In python, the standard library is maintained by the python devs, but we have to import specific methods if we want them.