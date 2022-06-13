import openseespy.opensees as ops

def nodeTag(nodeTag, dof):
    """
   Returns the current displacement at a specified node.



   ========================   ===========================================================================

   ``nodeTag`` |int|          node tag.

   ``dof`` |int|              specific dof at the node (1 through ndf), (optional), if no ``dof`` is

                              provided, a list of values for all dofs is returned.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.nodeDisp(nodeTag, dof, *uniqueArgs)

