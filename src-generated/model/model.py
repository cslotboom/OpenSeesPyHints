import openseespy.opensees as ops

def basic(ndm=None, ndf):
    """
   Set the default model dimensions and number of dofs.



   ========================   ===========================================================================

   ``ndm`` |int|              number of dimensions (1,2,3)

   ``ndf`` |int|              number of dofs (optional)

   ========================   ===========================================================================



    """
    uniqueArgs = []
    if ndm:
        uniqueArgs.append('-ndm')
        uniqueArgs.append(ndm)
    if ndf=ndm:
        uniqueArgs.append('-ndf')
    ops.model('basic', ndf, *uniqueArgs)

