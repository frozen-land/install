import os

def download(pipName):
  os.system("pip install {} --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org".format(pipName)
