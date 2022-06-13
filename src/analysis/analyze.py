import openseespy.opensees as ops

def numIncr=1(numIncr, dt, dtMin, dtMax, Jd):
    """
   Perform the analysis. Return ``0`` if successful, ``<0`` if **NOT** successful



   ===============================   ======================================================================================

   ``numIncr`` |int|                 Number of analysis steps to perform. (required except for :ref:`PFEM-Analysis`)

   ``dt`` |float|                    Time-step increment. (required for Transient analysis and VariableTransient analysis.`)

   ``dtMin`` |float|                 Minimum time steps. (required for VariableTransient analysis)

   ``dtMax`` |float|                 Maximum time steps (required for VariableTransient analysis)

   ``Jd`` |float|                    Number of iterations user would like performed at each step. The variable transient analysis will change current time step if last analysis step took more or less iterations than this to converge (required for VariableTransient analysis)

   ===============================   ======================================================================================





    """
    uniqueArgs = []
    ops.analyze(numIncr, dt, dtMin, dtMax, Jd, *uniqueArgs)

