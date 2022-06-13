import openseespy.opensees as ops

def mesh(mtag):
    """
   Get all nodes in the domain or in a mesh.



   ========================   ===========================================================================

   ``mtag`` |int|             mesh tag. (optional)

   ========================   ===========================================================================



    """
    uniqueArgs = []
    ops.getNodeTags('-mesh', mtag, *uniqueArgs)

