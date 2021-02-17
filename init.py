import os

# Get path of this init file
dot_nuke_path = os.path.dirname(__file__) 

# Append custom plugin paths to nuke
nuke.pluginAddPath(os.path.join(dot_nuke_path, "jp_nukeToolkit"))
nuke.pluginAddPath(os.path.join(dot_nuke_path, "External_Plugins"))

