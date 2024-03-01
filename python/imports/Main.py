from package import main

# In python there are 2 types of import : relative and absolute 
# Relative is used in packages and it is some annoying problems when you try to use it not in package 
# (module cant be run directly and when you use relative import python thinks this file is a module)
# Absolute import is a standard import (shown right here) which can be use in all python files including modules
# https://realpython.com/absolute-vs-relative-python-imports/

# relative imports are used when ur importing something from imported module that is deep relative to main file
# in this case if u will use absolute import ull need to write long string the whole path to the second import, 
# but using relative import gives u an ability to wrap it up writing path relatively.
