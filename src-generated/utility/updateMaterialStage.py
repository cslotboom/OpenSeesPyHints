import openseespy.opensees as ops

def material(matTag, value=None, paramTag=None):
    """


   This function is used in geotechnical modeling to maintain elastic nDMaterial response during the application of gravity loads. The material is then updated to allow for plastic strains during additional static loads or earthquakes.



   ========================   =============================================================

   ``matTag`` |int|           tag of nDMaterial

   ``value`` |int|            stage value

   ``paramTag`` |int|         tag of parameter (optional)

   ========================   =============================================================



    """
    uniqueArgs = []
    if value:
        uniqueArgs.append('-stage')
        uniqueArgs.append(value)
    if paramTag:
        uniqueArgs.append('-parameter')
        uniqueArgs.append(paramTag)
    ops.updateMaterialStage('-material', matTag, *uniqueArgs)

