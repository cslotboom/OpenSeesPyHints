import openseespy.opensees as ops

def basic(ndm, ndf):
    """
    Set the default model dimensions and number of dofs.
     
     
     
    ========================   ===========================================================================
     
    ``ndm`` |int|              number of dimensions (1,2,3)
     
    ``ndf`` |int|              number of dofs (optional)
     
    ========================   ===========================================================================
     
     
    OpenSeesPyHint:
        Checked

    """
    uniqueArgs = []
    if ndm:
        uniqueArgs.append('-ndm')
        uniqueArgs.append(ndm)
    if ndf:
        uniqueArgs.append('-ndf')
        uniqueArgs.append(ndf)
    ops.model('basic', *uniqueArgs)

