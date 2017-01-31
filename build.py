from distutils.core import setup
import py2exe
setup(windows = ["amuletapp.py"], options={"py2exe": {"includes": ["wx._xml"]}}, zipfile = None)
