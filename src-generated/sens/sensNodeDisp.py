import openseespy.opensees as ops

def nodeTag(nodeTag, dof, paramTag):
    """
   Returns the current displacement sensitivity to a parameter at a specified node.



   ========================   ===========================================================================

   ``nodeTag`` |int|          node tag

   ``dof`` |int|              specific dof at the node (1 through ndf)

   ``paramTag`` |int|         parameter tag

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.sensNodeDisp(nodeTag, dof, paramTag, *uniqueArgs)

