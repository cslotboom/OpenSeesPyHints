import openseespy.opensees as ops

def nodeTag(nodeTag, eigenvector, dof):
    """
   Returns the eigenvector at a specified node.



   ========================   ===========================================================================

   ``nodeTag`` |int|          node tag.

   ``eigenvector`` |int|      mode number of eigenvector to be returned

   ``dof`` |int|              specific dof at the node (1 through ndf), (optional), if no ``dof`` is

                              provided, a list of values for all dofs is returned.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.nodeEigenvector(nodeTag, eigenvector, dof, *uniqueArgs)

