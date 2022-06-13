import openseespy.opensees as ops

def nodeTag(nodeTag, dof):
    """
   Returns the reactions at a specified node. Must call :func:`reactions` command before

   this command.



   ========================   ===========================================================================

   ``nodeTag`` |int|          node tag.

   ``dof`` |int|              specific dof at the node (1 through ndf), (optional),

                              if no ``dof`` is

                              provided, a list of values for all dofs is returned.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.nodeReaction(nodeTag, dof, *uniqueArgs)

