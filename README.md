# flake8-contracting

Flake8 plugin that lints contracts written in python on [Xian-network](https://github.com/xian-network/)

## Prerequisite
python>=3.8, flake8>=3.7 

## Installation
You can decide to create a virtual environment for this or go ahead with the following instructions.
(Kindly google how to create a python virtual environment if you want to do so)

1. Install Flake8 if you haven't
```
pip install flake8
```
2. Clone this repo and move into flake8-contracting folder
```
git clone https://github.com/KELs7/flake8-contracting.git 
cd flake8-contracting
```
3. Install Flake8-contracting
```
pip install -e .
```
4. Check that Flake8-contracting is properly installed
```
flake --version
```
You should see something similar to this (if you installed Flake8 v7.0.0)
```
7.0.0 (flake8-contracting: 0.1.0, mccabe: 0.7.0, pycodestyle: 2.11.1, pyflakes: 3.2.0)
```
5. When you want to lint your contract code from the command line, do
```
flake8 path/to/contract.py
```

## Ignoring some errors/violations
Flake8 will flag any line of code containing any of the below as undefined with error code `F821`
* ForeignHash
* Hash
* Variable
* random
* @construct
* @export  
* ctx
* now
To avoid this add the comment `# noqa:  F821` to the line of code containing any of the above.
Example:
```python
settings = Hash(default_value=0)  # noqa:  F821
```
Ensure there is a single space between `#` and `noqa` and a double space between `:` and the error code `F821`

## TODO
- [ ] ignore as much errors that might conflict with the linter
- [ ] list all available error codes in README
- [ ] probably add tests
- [ ] ensure each reported error has the correct column offset value
