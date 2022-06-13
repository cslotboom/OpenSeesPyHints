import openseespy.opensees as ops

def PFEM(dtmax, dtmin, gravity, ratio):
    """


   Create a OpenSees PFEMAnalysis object. 



   ===============================   ======================================================================================

   ``dtmax`` |float|                 Maximum time steps.

   ``dtmin`` |float|                 Mimimum time steps.

   ``gravity`` |float|               Gravity acceleration used to move isolated particles.

   ``ratio`` |float|                 The ratio to reduce time steps if it was not converged. (optional)

   ===============================   ======================================================================================

    """
    uniqueArgs = []
    ops.analysis('PFEM', dtmax, dtmin, gravity, ratio, *uniqueArgs)

