import openseespy.opensees as ops

def mesh(mtag):
    """
   Get all elements in the domain or in a mesh.



   ========================   ===========================================================================

   ``mtag`` |int|             mesh tag. (optional)

   ========================   ===========================================================================



    """
    uniqueArgs = []
    ops.getEleTags('-mesh', mtag, *uniqueArgs)

