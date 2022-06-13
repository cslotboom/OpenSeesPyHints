import openseespy.opensees as ops

def commitTag(commitTag):
    """
   Save current state to database, which should be created through :func:`database`.



   ===========================   =====================================================================================================================================================

   ``commitTag`` |int|           a tag identify the commit

   ===========================   =====================================================================================================================================================

    """
    uniqueArgs = []
    ops.save(commitTag, *uniqueArgs)

