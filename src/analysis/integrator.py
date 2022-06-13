import openseespy.opensees as ops

def LoadControl(incr, numIter, minIncr, maxIncr):
    """


   Create a OpenSees LoadControl integrator object.



   ========================   =============================================================

   ``incr`` |float|           Load factor increment :math:`\lambda`.

   ``numIter`` |int|          Number of iterations the user would

                              like to occur in the solution algorithm. (optional)

   ``minIncr`` |float|        Min stepsize the user will allow :math:`\lambda_{min}`.

                              (optional)

   ``maxIncr`` |float|        Max stepsize the user will allow :math:`\lambda_{max}`.

                              (optional)

   ========================   =============================================================



   #. The change in applied loads that this causes depends on the active load pattern (those load pattern not set constant) and the loads in the load pattern. If the only active load acting on the Domain are in load pattern with a Linear time series with a factor of 1.0, this integrator is the same as the classical load control method.

   #. The optional arguments are supplied to speed up the step size in cases where convergence is too fast and slow down the step size in cases where convergence is too slow.

    """
    uniqueArgs = []
    ops.integrator('LoadControl', incr, numIter, minIncr, maxIncr, *uniqueArgs)

def DisplacementControl(nodeTag, dof, incr, numIter, dUmin, dUmax):
    """


   Create a DisplacementControl integrator.  In an analysis step with Displacement Control we seek to determine the time step that will result in a displacement increment for a particular degree-of-freedom at a node to be a prescribed value.



   ========================   =============================================================

   ``nodeTag`` |int|               tag of node whose response controls solution

   ``dof`` |int|              Degree of freedom at the node,

                              1 through ndf.

   ``incr`` |float|           First displacement increment :math:`\Delta U_{dof}`.

   ``numIter`` |int|          Number of iterations the user would

                              like to occur in the solution algorithm. (optional)

   ``minIncr`` |float|        Min stepsize the user will allow :math:`\Delta U_{min}`.

                              (optional)

   ``maxIncr`` |float|        Max stepsize the user will allow :math:`\Delta U_{max}`.

                              (optional)

   ========================   =============================================================

    """
    uniqueArgs = []
    ops.integrator('DisplacementControl', nodeTag, dof, incr, numIter, dUmin, dUmax, *uniqueArgs)

def ParallelDisplacementControl(nodeTag, dof, incr, numIter, dUmin, dUmax):
    """


   Create a Parallel version of DisplacementControl integrator.  In an analysis step with Displacement Control we seek to determine the time step that will result in a displacement increment for a particular degree-of-freedom at a node to be a prescribed value.



   ========================   =============================================================

   ``nodeTag`` |int|               tag of node whose response controls solution

   ``dof`` |int|              Degree of freedom at the node,

                              1 through ndf.

   ``incr`` |float|           First displacement increment :math:`\Delta U_{dof}`.

   ``numIter`` |int|          Number of iterations the user would

                              like to occur in the solution algorithm. (optional)

   ``minIncr`` |float|        Min stepsize the user will allow :math:`\Delta U_{min}`.

                              (optional)

   ``maxIncr`` |float|        Max stepsize the user will allow :math:`\Delta U_{max}`.

                              (optional)

   ========================   =============================================================





   Use this command only for parallel model.



.. warning::



   Don't use this command if model is not parallel, for example,

   parametric study.

    """
    uniqueArgs = []
    ops.integrator('ParallelDisplacementControl', nodeTag, dof, incr, numIter, dUmin, dUmax, *uniqueArgs)

def MinUnbalDispNorm(dlambda1, Jd, minLambda, maxLambda, det):
    """


   Create a MinUnbalDispNorm integrator.



   ========================   ================================================================

   ``dlambda1`` |float|       First load increment (pseudo-time step) at the first

                              iteration in the next invocation of the analysis command.

   ``Jd`` |int|               Factor relating first load increment at subsequent

                              time steps. (optional)

   ``minLambda`` |float|      Min load increment. (optional)

   ``maxLambda`` |float|      Max load increment. (optional)

   ========================   ================================================================

    """
    uniqueArgs = []
    ops.integrator('MinUnbalDispNorm', dlambda1, Jd, minLambda, maxLambda, det, *uniqueArgs)

def ArcLength(s, alpha):
    """


   Create a ArcLength integrator. In an analysis step with ArcLength we seek to determine the time step that will result in our constraint equation being satisfied.



   ========================   ================================================================

   ``s`` |float|              The arcLength.

   ``alpha`` |float|          :math:`\alpha` a scaling factor on the reference loads.

   ========================   ================================================================

    """
    uniqueArgs = []
    ops.integrator('ArcLength', s, alpha, *uniqueArgs)

def CentralDifference():
    """


   Create a centralDifference integrator.



   #. The calculation of :math:`U_t + \Delta t`, is based on using the equilibrium equation at time t. For this reason the method is called an explicit integration method.

   #. If there is no rayleigh damping and the C matrix is 0, for a diagonal mass matrix a diagonal solver may and should be used.

   #. For stability, :math:`\frac{\Delta t}{T_n} < \frac{1}{\pi}`

    """
    uniqueArgs = []
    ops.integrator('CentralDifference', *uniqueArgs)

def Newmark(gamma, beta, form=None):
    """


   Create a Newmark integrator.



   ========================   =============================================================

   ``gamma`` |float|          :math:`\gamma` factor.

   ``beta`` |float|           :math:`\beta` factor.

   ``form`` |str|             Flag to indicate which variable to be used as primary

                              variable (optional)



                              * ``'D'`` -- displacement (default)

                              * ``'V'`` -- velocity

                              * ``'A'`` -- acceleration

   ========================   =============================================================



   #. If the accelerations are chosen as the unknowns and :math:`\beta` is chosen as 0, the formulation results in the fast but conditionally stable explicit Central Difference method. Otherwise the method is implicit and requires an iterative solution process.

   #. Two common sets of choices are



      #. Average Acceleration Method (:math:`\gamma=\tfrac{1}{2}, \beta = \tfrac{1}{4}`)

      #. Linear Acceleration Method (:math:`\gamma=\tfrac{1}{2}, \beta = \tfrac{1}{6}`)



   #. :math:`\gamma > \tfrac{1}{2}` results in numerical damping proportional to :math:`\gamma - \tfrac{1}{2}`

   #. The method is second order accurate if and only if :math:`\gamma=\tfrac{1}{2}`

   #. The method is unconditionally stable for  :math:`\beta >= \frac{\gamma}{2} >= \tfrac{1}{4}`

    """
    uniqueArgs = []
    if form:
        uniqueArgs.append('-form')
        uniqueArgs.append(form)
    ops.integrator('Newmark', gamma, beta, *uniqueArgs)

def HHT(alpha, gamma, beta):
    """


   Create a Hilber-Hughes-Taylor (HHT) integrator. This is an implicit method that allows for energy dissipation and second order accuracy (which is not possible with the regular Newmark object). Depending on choices of input parameters, the method can be unconditionally stable.



   ========================   =============================================================

   ``alpha`` |float|          :math:`\alpha` factor.

   ``gamma`` |float|          :math:`\gamma` factor. (optional)

   ``beta`` |float|           :math:`\beta` factor. (optional)

   ========================   =============================================================



   #. Like Mewmark and all the implicit schemes, the unconditional stability of this method applies to linear problems. There are no results showing stability of this method over the wide range of nonlinear problems that potentially exist. Experience indicates that the time step for implicit schemes in nonlinear situations can be much greater than those for explicit schemes.

   #. :math:`\alpha` = 1.0 corresponds to the Newmark method.

   #. :math:`\alpha` should be between 0.67 and 1.0. The smaller the :math:`\alpha` the greater the numerical damping.

   #. :math:`\gamma` and :math:`\beta` are optional. The default values ensure the method is second order accurate and unconditionally stable when :math:`\alpha` is :math:`\tfrac{2}{3} <= \alpha <= 1.0`. The defaults are:



      :math:`\beta = \frac{(2 - \alpha)^2}{4}`



      and



      :math:`\gamma = \frac{3}{2} - \alpha`

    """
    uniqueArgs = []
    ops.integrator('HHT', alpha, gamma, beta, *uniqueArgs)

def GeneralizedAlpha(alphaM, alphaF, gamma, beta):
    """


   Create a GeneralizedAlpha integrator. This is an implicit method that like the HHT method allows for high frequency energy dissipation and second order accuracy, i.e. :math:`\Delta t^2`. Depending on choices of input parameters, the method can be unconditionally stable.



   ========================   =============================================================

   ``alphaM`` |float|         :math:`\alpha_M` factor.

   ``alphaF`` |float|         :math:`\alpha_F` factor.

   ``gamma`` |float|          :math:`\gamma` factor. (optional)

   ``beta`` |float|           :math:`\beta` factor. (optional)

   ========================   =============================================================



   #. Like Newmark and all the implicit schemes, the unconditional stability of this method applies to linear problems. There are no results showing stability of this method over the wide range of nonlinear problems that potentially exist. Experience indicates that the time step for implicit schemes in nonlinear situations can be much greater than those for explicit schemes.

   #. :math:`\alpha_M` = 1.0, :math:`\alpha_F` = 1.0 produces the Newmark Method.

   #. :math:`\alpha_M` = 1.0 corresponds to the :meth:`integrator.HHT` method.

   #. The method is second-order accurate provided :math:`\gamma = \tfrac{1}{2} + \alpha_M - \alpha_F`

   #. The method is unconditionally stable provided :math:`\alpha_M >= \alpha_F >= \tfrac{1}{2}, \beta>=\tfrac{1}{4} +\tfrac{1}{2}(\gamma_M - \gamma_F)`

   #. :math:`\gamma` and :math:`\beta` are optional. The default values ensure the method is unconditionally stable, second order accurate and high frequency dissipation is maximized.



      The defaults are:



      :math:`\gamma = \tfrac{1}{2} + \alpha_M - \alpha_F`



      and



      :math:`\beta = \tfrac{1}{4}(1 + \alpha_M - \alpha_F)^2`

    """
    uniqueArgs = []
    ops.integrator('GeneralizedAlpha', alphaM, alphaF, gamma, beta, *uniqueArgs)

def TRBDF2():
    """


      Create a TRBDF2 integrator. The TRBDF2 integrator is a composite scheme that alternates between the Trapezoidal scheme and a 3 point backward Euler scheme. It does this in an attempt to conserve energy and momentum, something Newmark does not always do.



   As opposed to dividing the time-step in 2 as outlined in the `Bathe2007`_, we just switch alternate between the 2 integration strategies,i.e. the time step in our implementation is double that described in the `Bathe2007`_.

    """
    uniqueArgs = []
    ops.integrator('TRBDF2', *uniqueArgs)

def ExplicitDifference():
    """
   Create a ExplicitDifference integrator.



   #. When using Rayleigh damping, the damping ratio of high vibration modes is overrated, and the critical time step size will be much smaller. Hence Modal damping is more suitable for this method.

   #. There should be no zero element on the diagonal of the mass matrix when using this method.

   #. Diagonal solver should be used when lumped mass matrix is used because the equations are uncoupled.

   #. For stability, :math:`\Delta t \leq \left(\sqrt{\zeta^2+1}-\zeta\right)\frac{2}{\omega}`

    """
    uniqueArgs = []
    ops.integrator('ExplicitDifference', *uniqueArgs)

