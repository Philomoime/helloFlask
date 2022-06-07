# helloFlask

## install Python 3.8.6
pyenv install 3.8.6

## Poetry installation and use
poetry new cow-counts # create new folder with Poetry arborescence  
poetry add cowsay # add dependencies  
poetry install # install dependencies and create the .lock file with the list of dependencies  
poetry build # enable to share an installable package with a wheel .whl folder  
poetry init --no-interaction # initialize a poetry project with existing folder: you have to build your own arborescence  

## Example of arborescence
$ tree ~/Documents/cow-counts  
cow-counts  
  ├── cow_counts  
  │   ├── __init__.py  
  │   └── mycow.py  
  ├── poetry.lock  
  ├── pyproject.toml  
  ├── README.rst  
  └── tests  
       ├── __init__.py  
       └── test_cow_counts.py  
