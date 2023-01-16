# FACE ANTI SPOOFING PROJECT

## TABLE OF CONTENTS
- [PROJECT-STRUCTURE](#project-structure)
- [PYTHON-VERSION](#python-version)
- [PYTHON VIRTUAL ENVIRONMENT](#heading-2)
- [GIT](#git)
- [VS-CODE SHORTCUTS](#heading-4)

## PROJECT-STRUCTURE
- model
- lib
- trainig
- testing
- main.py

## PYTHON-VERSION
- command - python --version
- Python 3.10.8

## PYTHON VIRTUAL ENVIRONMENT
- Install venv  
> pip install virtualenv

- Create 
> python -m venv virtual-environment-name
- Activate -
> source env/bin/activate
- Deactivate 
> deactivate

## GIT
- Run deactivate to stop the virtual environment
- Project initialize 
> git init

- to include the env folder in the .gitignore file so the virtual environment is ignored in source control
> echo ‘env' > .gitignore 

- to place the dependencies in a text file to be committed. Freezing reads all the installed dependencies and then produces a text file with the name of the dependency and the installed version number.
> pip freeze > requirements.txt 

- to check the file into source control.
> git add requirements.txt 

- Commit the files and push to a repo.
> git commit -m "Message"       
> git push origin branch






## VS CODE SHORTCUTS

- ctrl + shift + v - preview readme files
- ctrl + J - terminal


