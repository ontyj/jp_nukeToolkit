from jp_nukeToolkit.jp_mult_sandwich import create_mult_sandwich

menubar=nuke.menu("Nuke")
m=menubar.addMenu("Custom")
m.addCommand("Mult Sandwich", "create_mult_sandwich()", "Shift+q")

