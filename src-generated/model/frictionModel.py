import openseespy.opensees as ops

def Coulomb(frnTag, mu):
    """


   This command is used to construct a `Coulomb friction <http://en.wikipedia.org/wiki/Friction>`_ model object. Coulomb's Law of Friction states that kinetic friction is independent of the sliding velocity.



   ================================   ===========================================================================

   ``frnTag`` |int|                   unique friction model tag

   ``mu`` |float|                     coefficient of friction

   ================================   ===========================================================================

    """
    uniqueArgs = []
    ops.frictionModel('Coulomb', frnTag, mu, *uniqueArgs)

def VelDependent(frnTag, muSlow, muFast, transRate):
    """


   This command is used to construct a VelDependent friction model object. It is useful for modeling the behavior of `PTFE <http://en.wikipedia.org/wiki/Polytetrafluoroethylene>`_ or PTFE-like materials sliding on a stainless steel surface. For a detailed presentation on the velocity dependence of such interfaces please refer to Constantinou et al. (1999).



   ================================   ===========================================================================

   ``frnTag`` |int|                   unique friction model tag

   ``muSlow`` |float|                 coefficient of friction at low velocity

   ``muFast`` |float|                 coefficient of friction at high velocity

   ``transRate`` |float|              transition rate from low to high velocity

   ================================   ===========================================================================



.. math::



   \mu = {\mu _{fast}} - \left( {{\mu _{fast}} - {\mu _{slow}}} \right) \cdot {e^{ - transRate\, \cdot \,\left| v \right|}}



REFERENCE:



Constantinou, M.C., Tsopelas, P., Kasalanati, A., and Wolff, E.D. (1999). "Property modification factors for seismic isolation bearings". Report MCEER-99-0012, Multidisciplinary Center for Earthquake Engineering Research, State University of New York.

    """
    uniqueArgs = []
    ops.frictionModel('VelDependent', frnTag, muSlow, muFast, transRate, *uniqueArgs)

def VelNormalFrcDep(frnTag, aSlow, nSlow, aFast, nFast, alpha0, alpha1, alpha2, maxMuFact):
    """


   This command is used to construct a VelNormalFrcDep friction model object.



   ================================   ===========================================================================

   ``frnTag`` |int|                   unique friction model tag

   ``aSlow`` |float|                  constant for coefficient of friction at low velocity

   ``nSlow`` |float|                  exponent for coefficient of friction at low velocity

   ``aFast`` |float|                  constant for coefficient of friction at high velocity

   ``nFast`` |float|                  exponent for coefficient of friction at high velocity

   ``alpha0`` |float|                 constant rate parameter coefficient

   ``alpha1`` |float|                 linear rate parameter coefficient

   ``alpha2`` |float|                 quadratic rate parameter coefficient

   ``maxMuFact`` |float|              factor for determining the maximum coefficient of friction. This value prevents the friction coefficient from exceeding an unrealistic maximum value when the normal force becomes very small. The maximum friction coefficient is determined from μFast, for example :math:`\mu \leq maxMuFac*μFast`.

   ================================   ===========================================================================

    """
    uniqueArgs = []
    ops.frictionModel('VelNormalFrcDep', frnTag, aSlow, nSlow, aFast, nFast, alpha0, alpha1, alpha2, maxMuFact, *uniqueArgs)

def VelPressureDep(frnTag, muSlow, muFast0, A, deltaMu, alpha, transRate):
    """


   This command is used to construct a VelPressureDep friction model object.



   ================================   ===========================================================================

   ``frnTag`` |int|                   unique friction model tag

   ``muSlow`` |float|                 coefficient of friction at low velocity

   ``muFast0`` |float|                initial coefficient of friction at high velocity

   ``A`` |float|                      nominal contact area

   ``deltaMu`` |float|                pressure parameter calibrated from experimental data

   ``alpha`` |float|                  pressure parameter calibrated from experimental data

   ``transRate`` |float|              transition rate from low to high velocity

   ================================   ===========================================================================

    """
    uniqueArgs = []
    ops.frictionModel('VelPressureDep', frnTag, muSlow, muFast0, A, deltaMu, alpha, transRate, *uniqueArgs)

def VelDepMultiLinear(frnTag, velPoints=None, frnPoints=None):
    """


   This command is used to construct a VelDepMultiLinear friction model object. The friction-velocity relationship is given by a multi-linear curve that is define by a set of points. The slope given by the last two specified points on the positive velocity axis is extrapolated to infinite positive velocities. Velocity and friction points need to be equal or larger than zero (no negative values should be defined). The number of provided velocity points needs to be equal to the number of provided friction points.



   ================================   ===========================================================================

   ``frnTag`` |int|                   unique friction model tag

   ``velPoints`` |listf|              list of velocity points along friction-velocity curve

   ``frnPoints`` |listf|              list of friction points along friction-velocity curve

   ================================   ===========================================================================

    """
    uniqueArgs = []
    if velPoints:
        uniqueArgs.append('-vel')
        uniqueArgs.append(velPoints)
    if frnPoints:
        uniqueArgs.append('-frn')
        uniqueArgs.append(frnPoints)
    ops.frictionModel('VelDepMultiLinear', frnTag, *uniqueArgs)

