from .hash import cmd_map as hash_cmd_map
from .storage import cmd_map as storage_cmd_map


default_cmd_map = {}
default_cmd_map.update(hash_cmd_map)
default_cmd_map.update(storage_cmd_map)
