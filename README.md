# CS GSU Discord BOT

Bot used on the server used by CS students at GSU.

## Installation
### 1. Clone the GIT repository
Clone this directory `git clone https://github.com/soundzofstatic/cs_gsu_discord`

### 2. Move into cloned repository
Move into the newly cloned directory `cd cs_gsu_discord`

### 3. Setup Python
I have found that the easiest way to run the bot is while using Python 3.6 in a virtual environment (`virtualenv`). If you use other versions of Python, your mileage may vary.

#### 3.1 Setup Python Virtual Environment

Once you have Python 3.6 installed, make sure you have by running `virtualenv --version` . If you return an error, you do not have `virtualenv`. Run `pip3 install virtualenv` to install `virtualenv` for Python 3.6.

#### 3.2 Create a virtual environment for cs_gsu_discord
Once you have `virtualenv` installed, you can now create a virtual environment for the bot by running `virtualenv .` in the cs_gsu_discord directory (as cloned from git).

#### 3.3 Start the Virtual Environment
Start the virtual environemnt by running `source bin/activate` from within the cs_gsu_discord directory (as cloned from git).


### 4. Installing necessary packages
Use pip to install the packages in requirements.txt.

**Note, make sure you are running the virtual environment, otherwise you will install the packages for the global python installation**.

`pip install -r requirements.txt`

### 5. Configuration Setup
Set up a config.py file the following Dictionaries:
```python
DISCORD = {
    'token' : "YOUR_BOT_TOKEN_HERE"
}
```

### 6. Run the Bot
Run the bot by running the `index.py` file
```bash
python index.py
```

## Misc.
### Deactivating Virtualenv
If you need to deactivate an activate Python virtual env, just run `deactivate` in your cli. See more at [Python Docs - VirtualEnv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)