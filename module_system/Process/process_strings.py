from __future__ import absolute_import
from __future__ import print_function
import string
from header_common import *
from module_info import *
from module_strings import *

from .process_common import *
from six.moves import range

def save_strings(strings):
  ofile = open(export_dir + "strings.txt","w")
  ofile.write("stringsfile version 1\n")
  ofile.write("%d\n"%len(strings))
  for i_string in range(len(strings)):
    str = strings[i_string]
    ofile.write("str_%s %s\n"%(convert_to_identifier(str[0]),replace_spaces(str[1])))
  ofile.close()

def save_python_header():
  ofile = open("./ID_strings.py","w")
  for i_string in range(len(strings)):
    ofile.write("str_%s = %d\n"%(convert_to_identifier(strings[i_string][0]),i_string))
  ofile.write("\n\n")
  ofile.close()

print("Exporting strings...")
save_python_header()
save_strings(strings)
  
