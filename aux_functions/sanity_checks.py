import os
import ast

# --- CONFIGURATION ---

# Add the string names of the operations you want to scan for to this list.
OPERATIONS_TO_CHECK = [
    "troop_slot_eq",
    "party_slot_eq",
    "faction_slot_eq",
    "troop_slot_ge",
    "faction_slot_ge",
    "party_slot_ge",
    "scene_slot_ge",
    "scene_slot_eq",
    "item_slot_eq",
    "item_slot_ge",
    "neg|item_slot_eq",
    "neg|item_slot_ge",
    "neg|troop_slot_eq",
    "neg|party_slot_eq",
    "neg|faction_slot_eq",
    "neg|troop_slot_ge",
    "neg|faction_slot_ge",
    "neg|party_slot_ge",
    "neg|scene_slot_ge",
    "neg|scene_slot_eq",
    "troop_get_slot",
    "faction_get_slot",
    "party_get_slot",
    "scene_get_slot",
    "item_get_slot",
    "scene_prop_get_slot",
]

# Add the names of the files you want to scan to this list.
FILES_TO_SCAN = [
    r"module_system\module_scripts.py",
    r"module_system\module_dialogs.py",
    r"module_system\module_game_menus.py",
    r"module_system\module_mission_templates.py",
    r"module_system\module_simple_triggers.py",
]

# --- THE SCANNER ---

class OperationScanner(ast.NodeVisitor):
    """
    This class walks through the Python code's structure (AST)
    and validates specific M&B operations based on a configured list.
    """
    def __init__(self, filename, operations_to_check):
        self.filename = filename
        self.error_count = 0

        # Build a dictionary of validation rules for the operations we care about.
        all_rules = self._get_all_rules()
        self.validation_rules = {}
        for op_name in operations_to_check:
            if op_name in all_rules:
                self.validation_rules[op_name] = all_rules[op_name]
            else:
                print("WARNING: No validation rule defined for '{}'. It will be skipped.".format(op_name))

    def _get_all_rules(self):
        """A master dictionary of all available validation functions."""
        return {
            "troop_slot_eq": self.validate_generic_slot_eq,
            "party_slot_eq": self.validate_generic_slot_eq,
            "faction_slot_eq": self.validate_generic_slot_eq,
            "troop_slot_ge": self.validate_generic_slot_eq,
            "faction_slot_ge": self.validate_generic_slot_eq,
            "party_slot_ge": self.validate_generic_slot_eq,
            "scene_slot_eq": self.validate_generic_slot_eq,
            "scene_slot_ge": self.validate_generic_slot_eq,
            "item_slot_eq": self.validate_generic_slot_eq,
            "item_slot_ge": self.validate_generic_slot_eq,
            "neg|item_slot_eq": self.validate_generic_slot_eq,
            "neg|item_slot_ge": self.validate_generic_slot_eq,
            "neg|troop_slot_eq": self.validate_generic_slot_eq,
            "neg|party_slot_eq": self.validate_generic_slot_eq,
            "neg|faction_slot_eq": self.validate_generic_slot_eq,
            "neg|troop_slot_ge": self.validate_generic_slot_eq,
            "neg|faction_slot_ge": self.validate_generic_slot_eq,
            "neg|party_slot_ge": self.validate_generic_slot_eq,
            "neg|scene_slot_eq": self.validate_generic_slot_eq,
            "neg|scene_slot_ge": self.validate_generic_slot_eq,
            "troop_get_slot": self.validate_generic_get_slot,
            "faction_get_slot": self.validate_generic_get_slot,
            "party_get_slot": self.validate_generic_get_slot,
            "scene_get_slot": self.validate_generic_get_slot,
            "item_get_slot": self.validate_generic_get_slot,
            "scene_prop_get_slot": self.validate_generic_get_slot,
        }

    def visit_Tuple(self, node):
        # This function is automatically called for every tuple in the code.
        if not node.elts:
            return  # Skip empty tuples

        # Check if the first element of the tuple is an operation we need to validate.
        first_element = node.elts[0]
        if isinstance(first_element, ast.Name) and first_element.id in self.validation_rules:
            operation_name = first_element.id
            # Call the appropriate validation function from our dictionary
            validation_function = self.validation_rules[operation_name]
            validation_function(node, operation_name)

        # Continue scanning inside this tuple for nested operations
        self.generic_visit(node)

    # --- VALIDATION RULE METHODS ---
    def validate_generic_get_slot(self, node, op_name):
        """ Validates generic get_slot operations like (troop_get_slot, <destination>, <id>, <slot_no>). """
        line_num = node.lineno
        elements = node.elts

        # CHECK 1: Argument Count
        if len(elements) != 4:
            print("ERROR in {}: line {}".format(self.filename, line_num))
            print("  -> Invalid Argument Count for '{}'. Expected 4 elements, but found {}.".format(op_name, len(elements)))
            self.error_count += 1
            return

        destination_node = elements[1]

        # CHECK 2: <destination> should not be a slot
        # This is the key check for this function.
        is_error = False
        if isinstance(destination_node, ast.Name) and destination_node.id.startswith('slot_'):
            is_error = True
        elif isinstance(destination_node, ast.Constant) and isinstance(destination_node.value, str) and destination_node.value.startswith('slot_'):
            is_error = True

        if is_error:
            print("ERROR in {}: line {}".format(self.filename, line_num))
            print("  -> Invalid <destination> for '{}'. The destination (first argument) must be a variable (e.g., ':my_var' or 'reg0'), not a slot.".format(op_name))
            self.error_count += 1

    def validate_generic_slot_eq(self, node, op_name):
        """
        Validates generic slot_eq operations like (troop_slot_eq, <id>, <slot_no>, <value>).
        """
        line_num = node.lineno
        elements = node.elts
        subject_type = op_name.split('_')[0] # 'troop', 'party', etc.

        # CHECK 1: Argument Count
        if len(elements) != 4:
            print("ERROR in {}: line {}".format(self.filename, line_num))
            print("  -> Invalid Argument Count for '{}'. Expected 4 elements, but found {}.".format(op_name, len(elements)))
            self.error_count += 1
            return

        id_node = elements[1]
        value_node = elements[3]

        # CHECK 2: <id> should not be a slot
        is_error = False
        if isinstance(id_node, ast.Name) and id_node.id.startswith('slot_'):
            is_error = True
        elif isinstance(id_node, ast.Constant) and isinstance(id_node.value, str) and id_node.value.startswith('slot_'):
            is_error = True

        if is_error:
            print("ERROR in {}: line {}".format(self.filename, line_num))
            print("  -> Invalid <{}_id> for '{}'. The first argument should be a {}, not a slot.".format(subject_type, op_name, subject_type))
            self.error_count += 1

        # CHECK 3: <value> should not be a slot
        is_error = False
        if isinstance(value_node, ast.Name) and value_node.id.startswith('slot_'):
            is_error = True
        elif isinstance(value_node, ast.Constant) and isinstance(value_node.value, str) and value_node.value.startswith('slot_'):
            is_error = True

        if is_error:
            print("ERROR in {}: line {}".format(self.filename, line_num))
            print("  -> Invalid <value> for '{}'. The value to compare against should not be a slot.".format(op_name))
            print("     (If you want to compare one slot to another, use '{}_get_slot' and a temporary variable).".format(subject_type))
            self.error_count += 1


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    total_errors = 0
    print("Starting scan of module files...")
    print("Operations to check: {}".format(", ".join(OPERATIONS_TO_CHECK)))
    print("-" * 70)

    for filename in FILES_TO_SCAN:
        if not os.path.exists(filename):
            print("WARNING: Could not find file '{}'. Skipping.".format(filename))
            continue

        print("Scanning {}...".format(filename))
        with open(filename, 'r') as f:
            file_content = f.read()

        try:
            tree = ast.parse(file_content, filename=filename)
            # Pass the list of operations to the scanner
            scanner = OperationScanner(filename, OPERATIONS_TO_CHECK)
            scanner.visit(tree)
            total_errors += scanner.error_count
        except SyntaxError as e:
            print("FATAL SYNTAX ERROR in {}: line {}".format(filename, e.lineno))
            print("  -> Could not parse the file. Please fix this Python syntax error first.")
            print("     Error: {}".format(e.msg))
            total_errors += 1

    print("-" * 70)
    if total_errors == 0:
        print("Scan complete. No errors found for the specified operations.")
    else:
        print("Scan complete. Found {} error(s).".format(total_errors))