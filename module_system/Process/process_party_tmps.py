from module_info import *
from module_party_templates import *
#from process_operations import *

from process_common import *


def save_party_template_troop(file, troop):
  if troop:
    # Ensure all elements in `troop` are integers before writing
    try:
      troop_values = [int(value) for value in troop[:3]]  # Convert first three elements to integers
    except ValueError:
      raise ValueError("Invalid data in troop: {}. Expected all numeric values for the first three elements.".format(troop))

    file.write("%d %d %d " % (troop_values[0], troop_values[1], troop_values[2]))

    if len(troop) > 3:
      try:
        additional_value = int(troop[3])
      except ValueError:
        raise ValueError("Invalid data in troop[3]: {}. Expected a numeric value.".format(troop[3]))
      file.write("%d " % additional_value)
    else:
      file.write("0 ")
  else:
    file.write("-1 ")


def save_party_templates():
  file = open(export_dir + "party_templates.txt","w")
  file.write("partytemplatesfile version 1\n")
  file.write("%d\n"%(len(party_templates)))
  for party_template in party_templates:
#    add_tag_use(tag_uses,tag_faction,party_template[4])
    file.write("pt_%s %s %d %d %d %d "%(convert_to_identifier(party_template[0]),replace_spaces(party_template[1]),party_template[2],party_template[3], party_template[4], party_template[5]))
    members = party_template[6]
    if (len(members) > 6):
      print "Error! NUMBER OF TEMPLATE MEMBERS EXCEEDS 6 " + party_template[0]
      members = members[0:6]
    for party_template_member in members:
      save_party_template_troop(file,party_template_member)
    for i in xrange(6 - len(members)):
      save_party_template_troop(file,0)
    file.write("\n")
  file.close()

def save_python_header():
  file = open("./ID_party_templates.py","w")
  for i_party_template in xrange(len(party_templates)):
    file.write("pt_%s = %d\n"%(convert_to_identifier(party_templates[i_party_template][0]),i_party_template))
  file.close()

print "Exporting party_template data..."
#tag_uses = load_tag_uses(export_dir)
save_python_header()
save_party_templates()
#save_tag_uses(export_dir, tag_uses)
