import openseespy.opensees as ops

def size(size):
    """
   This command is used to set the displaying node size

   in cloud viewer.



   ========================   ===========================================================================

   ``size`` |float|           display size > 0, < 10.

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.nodeSizeForViewer(size, *uniqueArgs)

