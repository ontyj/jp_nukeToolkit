import nuke

def deselect_all():
    """Deselect all selected nodes
    """
    for node in nuke.selectedNodes():
        node["selected"].setValue(False)

def get_top_selected_node(n):
    """Return the node at the top of the pipe based on the current selection.
    """
    top_node = None
    for node in n:
        if node.dependencies(): # Check if there is actually node(s) above this one. 
            for dep in node.dependencies():
                if dep not in n:
                    top_node = node
        else: # There is no node above this one.
            top_node = node
    return top_node
                
def get_bottom_selected_node(n):
    """Return the node at the bottom of the pipe based on the current selection.
    """
    bottom_node = None
    for node in n:
        if node.dependent(): # Check if there is actually node(s) below this one.
            for dep in node.dependent():
                if dep not in n:
                    bottom_node = node
        else: # There is no node below this one.
            bottom_node = node

    return bottom_node

def create_mult_sandwich():
    """Creates unpremult and premult nodes around the currently selected node.
    """
    selection = nuke.selectedNodes()

    if not selection:
        # Nothing selected.
        nuke.message("No nodes selected.")
    else:
       top_node = get_top_selected_node(selection)
       bottom_node = get_bottom_selected_node(selection)

       if top_node and bottom_node:

        # Create unpremult
        unpremult = nuke.nodes.Unpremult()
        unpremult.setInput(0, top_node.input(0))
        top_node.setInput(0, unpremult)
        if unpremult.dependencies() == []: #Check if there is no node above.
            unpremult.setXpos(top_node.xpos())
            unpremult.setYpos(top_node.ypos() - top_node.screenHeight() - 10)
        # selection.append(unpremult)

        #Create premult
        premult = nuke.nodes.Premult()
        premult.setInput(0, bottom_node)
        if bottom_node.dependent():
            for dep in bottom_node.dependent():
                dep.setInput(0, premult)
        # selection.append(premult)

        #Restore original selection
        deselect_all()
        for node in selection:
            node["selected"].setValue(True)

       else:
            nuke.message("Something went wrong.")
