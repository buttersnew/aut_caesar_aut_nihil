from os.path import dirname, basename, isfile, join
import glob
path = ".\\" + join(basename(dirname(__file__)), "*.py")
modules = glob.glob(path)
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')] # add all 'py' files except '__init__.py'

# Alternatively you can add modules to list '__all__' manually (comment out all previous lines)
#__all__ = ['module_1', 'module_2', 'module_3']