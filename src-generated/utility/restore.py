import openseespy.opensees as ops

def commitTag(commitTag):
    """
   Restore data from database, which should be created through :func:`database`.



   ===========================   =====================================================================================================================================================

   ``commitTag`` |int|           a tag identify the commit

   ===========================   =====================================================================================================================================================

    """
    uniqueArgs = []
    ops.restore(commitTag, *uniqueArgs)

