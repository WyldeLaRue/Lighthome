# homepage
Messing around with React and Pyramid.








##Setting up the Pyramid server locally:

First we need to setup our virtual environment environment.
```
python3.7 -m venv ./venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install --upgrade setuptools
```

Now we install the dependencies:
```
pip3 install "pyramid==1.9.2" waitress
pip3 install pyramid_debugtoolbar
```

And now to add our Pyramid server to our virtual environment:
```
pip3 install -e .
```

and we can start it in development mode with 
```
pserve development.ini
```