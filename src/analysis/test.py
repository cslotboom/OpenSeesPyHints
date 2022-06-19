import openseespy.opensees as ops

def NormUnbalance(tol, iter, pFlag=0, nType=None, maxIncr=None):
    """

    Create a NormUnbalance test, which uses the norm of the right hand side of 
    the matrix equation to determine if convergence has been reached.
    
    ======================   =============================================================
    
    ``tol`` |float|          Tolerance criteria used to check for convergence.
    ``iter`` |int|           Max number of iterations to check
    ``pFlag`` |int|          Print flag (optional):
                             * 0 print nothing.
                             * 1 print information on norms each time ``test()`` is invoked.
                             * 2 print information on norms and number of iterations at end of successful test.
                             * 4 at each step it will print the norms and also the :math:`\Delta U` and :math:`R(U)` vectors.
                             * 5 if it fails to converge at end of ``numIter`` it will print an error message **but return a successfull test**.
    
    ``nType`` |int|          Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional)
    ``maxIncr`` |int|        Maximum times of error increasing. (optional)
    ======================   =============================================================
    
    When using the Penalty method additional large forces to enforce the 
    penalty functions exist on the right hand side, making convergence using 
    this test usually impossible (even though solution might have converged).

    """
    uniqueArgs = []
    
    if nType:
        uniqueArgs.append(nType)
    
    if maxIncr:
        uniqueArgs.append(maxIncr)        
    ops.test('NormUnbalance', tol, iter, pFlag, *uniqueArgs)

def NormDispIncr(tol, iter, pFlag=0, nType=None):
    """

    Create a NormDispIncr test, which uses the norm of the left hand side 
    solution vector of the matrix equation to determine if convergence has 
    been reached.
    
    ======================   =============================================================
    
    ``tol`` |float|          Tolerance criteria used to check for convergence.
    ``iter`` |int|           Max number of iterations to check
    ``pFlag`` |int|          Print flag (optional):
                             * 0 print nothing.
                             * 1 print information on norms each time ``test()`` is invoked.
                             * 2 print information on norms and number of iterations at end of successful test.
                             * 4 at each step it will print the norms and also the :math:`\Delta U` and :math:`R(U)` vectors.
                             * 5 if it fails to converge at end of ``numIter`` it will print an error message **but return a successfull test**.
    
    ``nType`` |int|          Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional)
    
    ======================   =============================================================

    When using the Lagrange method to enforce the constraints, the Lagrange 
    multipliers appear in the solution vector.

    Hints:
        untested

    """
    uniqueArgs = []
    
    if nType:
        uniqueArgs.append(nType)
        
    ops.test('NormDispIncr', tol, iter, pFlag, *uniqueArgs)

def EnergyIncr(tol, iter, pFlag=0, nType=None):
    """

    Create a EnergyIncr test, which uses the dot product of the solution vector
    and norm of the right hand side of the matrix equation to determine if 
    convergence has been reached.
    
    ======================   =============================================================
    
    ``tol`` |float|          Tolerance criteria used to check for convergence.
    ``iter`` |int|           Max number of iterations to check
    ``pFlag`` |int|          Print flag (optional):
                             * 0 print nothing.
                             * 1 print information on norms each time ``test()`` is invoked.
                             * 2 print information on norms and number of iterations at end of successful test.
                             * 4 at each step it will print the norms and also the :math:`\Delta U` and :math:`R(U)` vectors.
                             * 5 if it fails to converge at end of ``numIter`` it will print an error message **but return a successfull test**.
    
    ``nType`` |int|          Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional)
    
    ======================   =============================================================
    
    * When using the Penalty method additional large forces to enforce the penalty functions exist on the right hand side, making convergence using this test usually impossible (even though solution might have converged).
    * When using the Lagrange method to enforce the constraints, the Lagrange multipliers appear in the solution vector.

    Hints:
        untested

    """
    uniqueArgs = []
    
    if nType:
        uniqueArgs.append(nType)            
    ops.test('EnergyIncr', tol, iter, pFlag,  *uniqueArgs)

def RelativeNormUnbalance(tol, iter, pFlag=0, nType=None):
    """

    Create a RelativeNormUnbalance test, which uses the relative norm of the right hand side of the matrix equation to determine if convergence has been reached.
    
    ======================   =============================================================
    
    ``tol`` |float|          Tolerance criteria used to check for convergence.
    ``iter`` |int|           Max number of iterations to check
    ``pFlag`` |int|          Print flag (optional):
                             * 0 print nothing.
                             * 1 print information on norms each time ``test()`` is invoked.
                             * 2 print information on norms and number of iterations at end of successful test.
                             * 4 at each step it will print the norms and also the :math:`\Delta U` and :math:`R(U)` vectors.
                             * 5 if it fails to converge at end of ``numIter`` it will print an error message **but return a successfull test**.
    
    ``nType`` |int|          Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional)
    
    ======================   =============================================================
    
    
    * When using the Penalty method additional large forces to enforce the penalty functions exist on the right hand side, making convergence using this test usually impossible (even though solution might have converged).

    Hints:
        untested

    """
    uniqueArgs = []
    
    if nType:
        uniqueArgs.append(nType)
        
    ops.test('RelativeNormUnbalance', tol, iter, pFlag, *uniqueArgs)

def RelativeNormDispIncr(tol, iter, pFlag=0, nType=None):
    """

    Create a RelativeNormDispIncr test, which uses the relative of the 
    solution vector of the matrix equation to determine if convergence has been reached.
    
    ======================   =============================================================
    
    ``tol`` |float|          Tolerance criteria used to check for convergence.
    ``iter`` |int|           Max number of iterations to check
    ``pFlag`` |int|          Print flag (optional):
                             * 0 print nothing.
                             * 1 print information on norms each time ``test()`` is invoked.
                             * 2 print information on norms and number of iterations at end of successful test.
                             * 4 at each step it will print the norms and also the :math:`\Delta U` and :math:`R(U)` vectors.
                             * 5 if it fails to converge at end of ``numIter`` it will print an error message **but return a successfull test**.
    
    ``nType`` |int|          Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional)
    
    ======================   =============================================================

    Hints:
        untested

    """
    uniqueArgs = []
    
    if nType:
        uniqueArgs.append(nType)    
    
    ops.test('RelativeNormDispIncr', tol, iter, pFlag, *uniqueArgs)

def RelativeTotalNormDispIncr(tol, iter, pFlag=0, nType=None):
    """

    Create a RelativeTotalNormDispIncr test, which uses the ratio of the 
    current norm to the total norm (the sum of all the norms since last 
    convergence) of the solution vector.
    
    ======================   =============================================================
    
    ``tol`` |float|          Tolerance criteria used to check for convergence.
    ``iter`` |int|           Max number of iterations to check
    ``pFlag`` |int|          Print flag (optional):
                             * 0 print nothing.
                             * 1 print information on norms each time ``test()`` is invoked.
                             * 2 print information on norms and number of iterations at end of successful test.
                             * 4 at each step it will print the norms and also the :math:`\Delta U` and :math:`R(U)` vectors.
                             * 5 if it fails to converge at end of ``numIter`` it will print an error message **but return a successfull test**.
    
    ``nType`` |int|          Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional)
    
    ======================   =============================================================

    Hints:
        untested

    """
    uniqueArgs = []
    
    if nType:
        uniqueArgs.append(nType)    
    
    ops.test('RelativeTotalNormDispIncr', tol, iter, pFlag, *uniqueArgs)

def RelativeEnergyIncr(tol, iter, pFlag=0, nType=None):
    """
    
    Create a RelativeEnergyIncr test, which uses the relative dot product of 
    the solution vector and norm of the right hand side of the matrix equation 
    to determine if convergence has been reached.
    
    ======================   =============================================================
    
    ``tol`` |float|          Tolerance criteria used to check for convergence.
    ``iter`` |int|           Max number of iterations to check
    ``pFlag`` |int|          Print flag (optional):
                             * 0 print nothing.
                             * 1 print information on norms each time ``test()`` is invoked.
                             * 2 print information on norms and number of iterations at end of successful test.
                             * 4 at each step it will print the norms and also the :math:`\Delta U` and :math:`R(U)` vectors.
                             * 5 if it fails to converge at end of ``numIter`` it will print an error message **but return a successfull test**.
    
    ``nType`` |int|          Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional)
    
    ======================   =============================================================

    Hints:
        untested

    """
    uniqueArgs = []
    
    if nType:
        uniqueArgs.append(nType)    
    
    ops.test('RelativeEnergyIncr', tol, iter, pFlag, nType, *uniqueArgs)

def FixedNumIter(iter, pFlag=0, nType=None):
    """
    
    Create a FixedNumIter test, that performs a fixed number of iterations 
    without testing for convergence.

    ======================   =============================================================
    
    ``tol`` |float|          Tolerance criteria used to check for convergence.
    ``iter`` |int|           Max number of iterations to check  
    ``pFlag`` |int|          Print flag (optional):    
                             * 0 print nothing.
                             * 1 print information on norms each time ``test()`` is invoked.
                             * 2 print information on norms and number of iterations at end of successful test.
                             * 4 at each step it will print the norms and also the :math:`\Delta U` and :math:`R(U)` vectors.
                             * 5 if it fails to converge at end of ``numIter`` it will print an error message **but return a successfull test**.
    
    ``nType`` |int|          Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional)
    
    ======================   =============================================================

    Hints:
        untested

    """
    uniqueArgs = []
    
    if nType:
        uniqueArgs.append(nType)    
    
    ops.test('FixedNumIter', iter, pFlag, *uniqueArgs)

def NormDispAndUnbalance(tolIncr, tolR, iter, pFlag=0, nType=None, maxincr=None):
    """

    Create a NormDispAndUnbalance test, which check if both   ``'NormUnbalance'`` and ``'NormDispIncr'`` are converged.
    
    ======================   =============================================================
    
    ``tolIncr`` |float|      Tolerance for left hand solution increments
    ``tolIncr`` |float|      Tolerance for right hand residual
    ``iter`` |int|           Max number of iterations to check
    ``pFlag`` |int|          Print flag (optional):
                             * 0 print nothing.
                             * 1 print information on norms each time ``test()`` is invoked.
                             * 2 print information on norms and number of iterations at end of successful test.
                             * 4 at each step it will print the norms and also the :math:`\Delta U` and :math:`R(U)` vectors.
                             * 5 if it fails to converge at end of ``numIter`` it will print an error message **but return a successfull test**.
    ``nType`` |int|          Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional)
    ``maxincr`` |int|        Maximum times of error increasing. (optional)
    
    ======================   =============================================================

    Hints:
        untested

    """
    uniqueArgs = []
    
    if nType:
        uniqueArgs.append(nType)
    
    if maxincr:
        uniqueArgs.append(maxincr)        
        
    ops.test('NormDispAndUnbalance', tolIncr, tolR, iter, *uniqueArgs)

def NormDispOrUnbalance(tolIncr, tolR, iter, pFlag=0, nType=None, maxincr=None):
    """
    
    Create a NormDispOrUnbalance test, which check if both
    ``'NormUnbalance'`` and ``'normDispIncr'`` are converged.
    
    ======================   =============================================================
    
    ``tolIncr`` |float|      Tolerance for left hand solution increments
    ``tolR`` |float|         Tolerance for right hand residual
    ``iter`` |int|           Max number of iterations to check
    ``pFlag`` |int|          Print flag (optional):
                             * 0 print nothing.
                             * 1 print information on norms each time ``test()`` is invoked.
                             * 2 print information on norms and number of iterations at end of successful test.
                             * 4 at each step it will print the norms and also the :math:`\Delta U` and :math:`R(U)` vectors.
                             * 5 if it fails to converge at end of ``numIter`` it will print an error message **but return a successfull test**.
    
    ``nType`` |int|          Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional)
    ``maxincr`` |int|        Maximum times of error increasing. (optional)
    
    ======================   =============================================================

    Hints:
        untested

    """
    uniqueArgs = []
    
    if nType:
        uniqueArgs.append(nType)
    
    if maxincr:
        uniqueArgs.append(maxincr)        
        
    ops.test('NormDispOrUnbalance', tolIncr, tolR, iter, pFlag, *uniqueArgs)

