import openseespy.opensees as ops

def ElasticIsotropic(matTag, E, nu, rho):
    """


   This command is used to construct an ElasticIsotropic material object.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``E`` |float|                      elastic modulus

   ``nu`` |float|                     Poisson's ratio

   ``rho`` |float|                    mass density (optional)

   ================================   ===========================================================================



The material formulations for the ElasticIsotropic object are:



* ``'ThreeDimensional'``

* ``'PlaneStrain'``

* ``'Plane Stress'``

* ``'AxiSymmetric'``

* ``'PlateFiber'``

    """
    uniqueArgs = []
    ops.nDMaterial('ElasticIsotropic', matTag, E, nu, rho, *uniqueArgs)

def ElasticOrthotropic(matTag, Ex, Ey, Ez, nu_xy, nu_yz, nu_zx, Gxy, Gyz, Gzx, rho):
    """


   This command is used to construct an ElasticOrthotropic material object.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``Ex`` |float|                     elastic modulus in x direction

   ``Ey`` |float|                     elastic modulus in y direction

   ``Ez`` |float|                     elastic modulus in z direction

   ``nu_xy`` |float|                  Poisson's ratios in x and y plane

   ``nu_yz`` |float|                  Poisson's ratios in y and z plane

   ``nu_zx`` |float|                  Poisson's ratios in z and x plane

   ``Gxy`` |float|                    shear modulii in x and y plane

   ``Gyz`` |float|                    shear modulii in y and z plane

   ``Gzx`` |float|                    shear modulii in z and x plane

   ``rho`` |float|                    mass density (optional)

   ================================   ===========================================================================



The material formulations for the ElasticOrthotropic object are:



* ``'ThreeDimensional'``

* ``'PlaneStrain'``

* ``'Plane Stress'``

* ``'AxiSymmetric'``

* ``'BeamFiber'``

* ``'PlateFiber'``

    """
    uniqueArgs = []
    ops.nDMaterial('ElasticOrthotropic', matTag, Ex, Ey, Ez, nu_xy, nu_yz, nu_zx, Gxy, Gyz, Gzx, rho, *uniqueArgs)

def J2Plasticity(matTag, K, G, sig0, sigInf, delta, H):
    """


   This command is used to construct an multi dimensional material object that has a von Mises (J2) yield criterium and isotropic hardening.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``K`` |float|                      bulk modulus

   ``G`` |float|                      shear modulus

   ``sig0`` |float|                   initial yield stress

   ``sigInf`` |float|                 final saturation yield stress

   ``delta`` |float|                  exponential hardening parameter

   ``H`` |float|                      linear hardening parameter

   ================================   ===========================================================================



The material formulations for the J2Plasticity object are:



* ``'ThreeDimensional'``

* ``'PlaneStrain'``

* ``'Plane Stress'``

* ``'AxiSymmetric'``

* ``'PlateFiber'``



J2 isotropic hardening material class



Elastic Model



.. math::



   \sigma = K * trace(\epsilon_e) + (2 * G) * dev(\epsilon_e)



Yield Function



.. math::



   \phi(\sigma,q) = || dev(\sigma) ||  - \sqrt(\tfrac{2}{3}*q(x_i))



Saturation Isotropic Hardening with linear term



.. math::



 q(x_i) = \sigma_0 + (\sigma_\infty - \sigma_0)*exp(-delta*\xi) + H*\xi



Flow Rules



.. math::



 \dot {\epsilon_p} =  \gamma * \frac{\partial \phi}{\partial \sigma}



 \dot \xi  = -\gamma * \frac{\partial \phi}{\partial q}



Linear Viscosity



.. math::

   \gamma = \frac{\phi}{\eta}  ( if   \phi > 0 )



Backward Euler Integration Routine Yield condition enforced at time n+1



set :math:`\eta` = 0 for rate independent case

    """
    uniqueArgs = []
    ops.nDMaterial('J2Plasticity', matTag, K, G, sig0, sigInf, delta, H, *uniqueArgs)

def DruckerPrager(matTag, K, G, sigmaY, rho, rhoBar, Kinf, Ko, delta1, delta2, H, theta, density, atmPressure):
    """


   This command is used to construct an multi dimensional material object that has a Drucker-Prager yield criterium.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``K`` |float|                      bulk modulus

   ``G`` |float|                      shear modulus

   ``sigmaY`` |float|                 yield stress

   ``rho`` |float|                    frictional strength parameter

   ``rhoBar`` |float|                 controls evolution of plastic volume change, :math:`0\le rhoBar \le rho`.

   ``Kinf`` |float|                   nonlinear isotropic strain hardening parameter, :math:`Kinf \ge 0`.

   ``Ko`` |float|                     nonlinear isotropic strain hardening parameter, :math:`Ko \ge 0`.

   ``delta1`` |float|                 nonlinear isotropic strain hardening parameter, :math:`delta1\ge 0`.

   ``delta2`` |float|                 tension softening parameter, :math:`delta2\ge 0`.

   ``H`` |float|                      linear hardening parameter, :math:`H \ge 0`.

   ``theta`` |float|                  controls relative proportions of isotropic and kinematic

                                      hardening, :math:`0 \le theta \le 1`.

   ``density`` |float|                mass density of the material

   ``atmPressure`` |float|            optional atmospheric pressure for update of elastic bulk and shear moduli

   ================================   ===========================================================================



The material formulations for the DrukerPrager object are:



* ``'ThreeDimensional'``

* ``'PlaneStrain'``



See `theory <http://opensees.berkeley.edu/wiki/index.php/Drucker_Prager>`_.

    """
    uniqueArgs = []
    ops.nDMaterial('DruckerPrager', matTag, K, G, sigmaY, rho, rhoBar, Kinf, Ko, delta1, delta2, H, theta, density, atmPressure, *uniqueArgs)

def Damage2p(matTag, fcc, fct=None, E=None, ni=None, Gt=None, Gc=None, rho_bar=None, H=None, theta=None, tangent=None):
    """


   This command is used to construct a three-dimensional material object that has a Drucker-Prager plasticity model coupled with a two-parameter damage model.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``fcc`` |float|                    concrete compressive strength,

                                      negative real value (positive input is changed in sign automatically)

   ``fct`` |float|                    optional concrete tensile strength,

                                      positive real value (for concrete like materials is less than fcc),

                                      :math:`0.1*abs(fcc)` =

                                      :math:`4750*sqrt(abs(fcc))\text{ }if\text{ }abs(fcc)<2000`

                                      because fcc is assumed in MPa (see ACI 318)

   ``E`` |float|                      optional Young modulus,

                                      :math:`57000*sqrt(abs(fcc))` if :math:`abs(fcc)>2000`

                                      because fcc is assumed in psi (see ACI 318)

   ``ni`` |float|                     optional Poisson coefficient,

                                      0.15 (from comparison with tests by Kupfer Hilsdorf Rusch 1969)

   ``Gt`` |float|                     optional tension fracture energy density,

                                      positive real value (integral of the stress-strain envelope in tension),

                                      :math:`1840*fct*fct/E`

                                      (from comparison with tests by Gopalaratnam and Shah 1985)

   ``Gc`` |float|                     optional compression fracture energy density,

                                      positive real value (integral of the stress-strain

                                      envelope after the peak in compression),

                                      :math:6250*fcc*fcc/E`

                                      (from comparison with tests by Karsan and Jirsa 1969)

   ``rho_bar`` |float|                optional parameter of plastic volume change,

                                      positive real value :math:`0=rhoBar< sqrt(2/3)`,

                                      0.2 (from comparison with tests by Kupfer Hilsdorf Rusch 1969)

   ``H`` |float|                      optional linear hardening parameter for plasticity,

                                      positive real value (usually less than E),

                                      :math:`0.25*E`

                                      (from comparison with tests by Karsan and Jirsa 1969 and

                                      Gopalaratnam and Shah 1985)

   ``theta`` |float|                  optional ratio between isotropic and kinematic hardening,

                                      positive real value :math:`0=theta=1` (with: 0 hardening kinematic

                                      only and 1 hardening isotropic only,

                                      0.5 (from comparison with tests by Karsan and Jirsa 1969

                                      and Gopalaratnam and Shah 1985)

   ``tangent`` |float|                optional integer to choose the computational stiffness matrix,

                                      0: computational tangent; 1: damaged secant stiffness

                                      (hint: in case of strong nonlinearities use it with

                                      Krylov-Newton algorithm)

   ================================   ===========================================================================



The material formulations for the Damage2p object are:



* ``'ThreeDimensional'``

* ``'PlaneStrain'``

* ``'Plane Stress'``

* ``'AxiSymmetric'``

* ``'PlateFiber'``



See also `here <http://opensees.berkeley.edu/wiki/index.php/Damage2p>`_

    """
    uniqueArgs = []
    if fct:
        uniqueArgs.append('-fct')
        uniqueArgs.append(fct)
    if E:
        uniqueArgs.append('-E')
        uniqueArgs.append(E)
    if ni:
        uniqueArgs.append('-ni')
        uniqueArgs.append(ni)
    if Gt:
        uniqueArgs.append('-Gt')
        uniqueArgs.append(Gt)
    if Gc:
        uniqueArgs.append('-Gc')
        uniqueArgs.append(Gc)
    if rho_bar:
        uniqueArgs.append('-rho_bar')
        uniqueArgs.append(rho_bar)
    if H:
        uniqueArgs.append('-H')
        uniqueArgs.append(H)
    if theta:
        uniqueArgs.append('-theta')
        uniqueArgs.append(theta)
    if tangent:
        uniqueArgs.append('-tangent')
        uniqueArgs.append(tangent)
    ops.nDMaterial('Damage2p', matTag, fcc, *uniqueArgs)

def PlaneStress(matTag, mat3DTag):
    """


   This command is used to construct a plane-stress material wrapper which converts any three-dimensional material into a plane stress material via static condensation.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``mat3DTag`` |int|                 tag of perviously defined 3d ndMaterial material

   ================================   ===========================================================================



The material formulations for the PlaneStress object are:



* ``'Plane Stress'``

    """
    uniqueArgs = []
    ops.nDMaterial('PlaneStress', matTag, mat3DTag, *uniqueArgs)

def PlaneStrain(matTag, mat3DTag):
    """


   This command is used to construct a plane-stress material wrapper which converts any three-dimensional material into a plane strain material by imposing plain strain conditions on the three-dimensional material.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``mat3DTag`` |int|                 integer tag of previously defined 3d ndMaterial material

   ================================   ===========================================================================



The material formulations for the PlaneStrain object are:



* ``'PlaneStrain'``

    """
    uniqueArgs = []
    ops.nDMaterial('PlaneStrain', matTag, mat3DTag, *uniqueArgs)

def MultiaxialCyclicPlasticity(matTag, rho, K, G, Su, Ho, h, m, beta, KCoeff):
    """


   This command is used to construct an multiaxial Cyclic Plasticity model for clays



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``rho`` |float|                    density

   ``K`` |float|                      buck modulus

   ``G`` |float|                      maximum (small strain) shear modulus

   ``Su`` |float|                     undrained shear strength, size of bounding

                                      surface :math:`R=\sqrt{8/3}*Su`

   ``Ho`` |float|                     linear kinematic hardening modulus of bounding surface

   ``h`` |float|                      hardening parameter

   ``m`` |float|                      hardening parameter

   ``beta`` |float|                   integration parameter, usually beta=0.5

   ``KCoeff`` |float|                 coefficient of earth pressure, K0

   ================================   ===========================================================================

    """
    uniqueArgs = []
    ops.nDMaterial('MultiaxialCyclicPlasticity', matTag, rho, K, G, Su, Ho, h, m, beta, KCoeff, *uniqueArgs)

def BoundingCamClay(matTag, massDensity, C, bulkMod, OCR, mu_o, alpha, lambda, h, m):
    """


   This command is used to construct a multi-dimensional bounding surface Cam Clay material object after Borja et al. (2001).



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``massDensity`` |float|            mass density

   ``C`` |float|                      ellipsoidal axis ratio (defines shape of ellipsoidal

                                      loading/bounding surfaces)

   ``bulkMod`` |float|                initial bulk modulus

   ``OCR`` |float|                    overconsolidation ratio

   ``mu_o`` |float|                   initial shear modulus

   ``alpha`` |float|                  pressure-dependency parameter for modulii (greater than or equal to zero)

   ``lambda`` |float|                 soil compressibility index for virgin loading

   ``h`` |float|                      hardening parameter for plastic response inside of bounding

                                      surface (if h = 0, no hardening)

   ``m`` |float|                      hardening parameter (exponent) for plastic response inside

                                      of bounding surface (if m = 0, only linear hardening)

   ================================   ===========================================================================



The material formulations for the BoundingCamClay object are:



* ``'ThreeDimensional'``

* ``'PlaneStrain'``



See also for `information <http://opensees.berkeley.edu/wiki/index.php/Bounding_Cam_Clay>`_

    """
    uniqueArgs = []
    ops.nDMaterial('BoundingCamClay', matTag, massDensity, C, bulkMod, OCR, mu_o, alpha, lambda, h, m, *uniqueArgs)

def PlateFiber(matTag, threeDTag):
    """


   This command is used to construct a plate-fiber material wrapper which converts any three-dimensional material into a plate fiber material (by static condensation) appropriate for shell analysis.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``threeDTag`` |float|              material tag for a previously-defined three-dimensional material

   ================================   ===========================================================================

    """
    uniqueArgs = []
    ops.nDMaterial('PlateFiber', matTag, threeDTag, *uniqueArgs)

def FSAM(matTag, rho, sXTag, sYTag, concTag, rouX, rouY, nu, alfadow):
    """


   This command is used to construct a nDMaterial FSAM (Fixed-Strut-Angle-Model, Figure 1, Kolozvari et al., 2015), which is a plane-stress constitutive model for simulating the behavior of RC panel elements under generalized, in-plane, reversed-cyclic loading conditions (Ulugtekin, 2010; Orakcal et al., 2012). In the FSAM constitutive model, the strain fields acting on concrete and reinforcing steel components of a RC panel are assumed to be equal to each other, implying perfect bond assumption between concrete and reinforcing steel bars. While the reinforcing steel bars develop uniaxial stresses under strains in their longitudinal direction, the behavior of concrete is defined using stress-strain relationships in biaxial directions, the orientation of which is governed by the state of cracking in concrete. Although the concrete stress-strain relationship used in the FSAM is fundamentally uniaxial in nature, it also incorporates biaxial softening effects including compression softening and biaxial damage. For transfer of shear stresses across the cracks, a friction-based elasto-plastic shear aggregate interlock model is adopted, together with a linear elastic model for representing dowel action on the reinforcing steel bars (Kolozvari, 2013). Note that FSAM constitutive model is implemented to be used with Shear-Flexure Interaction model for RC walls (SFI_MVLEM), but it could be also used elsewhere.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``rho`` |float|                    Material density

   ``sXTag`` |int|                    Tag of uniaxialMaterial simulating horizontal (x) reinforcement

   ``sYTag`` |int|                    Tag of uniaxialMaterial simulating vertical (y) reinforcement

   ``concTag`` |int|                  Tag of uniaxialMaterial simulating concrete,

                                      shall be used with uniaxialMaterial ConcreteCM

   ``rouX`` |float|                   Reinforcing ratio in horizontal (x) direction

                                      (:math:`rouX = _{s,x}/A_{gross,x}`)

   ``rouY`` |float|                   Reinforcing ratio in vertical (x) direction

                                      (:math:`rouY = _{s,y}/A_{gross,y}`)

   ``nu`` |float|                     Concrete friction coefficient (:math:`0.0 < \nu < 1.5`)

   ``alfadow`` |float|                Stiffness coefficient of reinforcement dowel action

                                      (:math:`0.0 < alfadow < 0.05`)

   ================================   ===========================================================================



See also `here <http://opensees.berkeley.edu/wiki/index.php/FSAM_-_2D_RC_Panel_Constitutive_Behavior>`_





References:



1) Kolozvari K., Orakcal K., and Wallace J. W. (2015). "Shear-Flexure Interaction Modeling of reinforced Concrete Structural Walls and Columns under Reversed Cyclic Loading", Pacific Earthquake Engineering Research Center, University of California, Berkeley, PEER Report No. 2015/12



2) Kolozvari K. (2013). "Analytical Modeling of Cyclic Shear-Flexure Interaction in Reinforced Concrete Structural Walls", PhD Dissertation, University of California, Los Angeles.



3) Orakcal K., Massone L.M., and Ulugtekin D. (2012). "Constitutive Modeling of Reinforced Concrete Panel Behavior under Cyclic Loading", Proceedings, 15th World Conference on Earthquake Engineering, Lisbon, Portugal.



4) Ulugtekin D. (2010). "Analytical Modeling of Reinforced Concrete Panel Elements under Reversed Cyclic Loadings", M.S. Thesis, Bogazici University, Istanbul, Turkey.

    """
    uniqueArgs = []
    ops.nDMaterial('FSAM', matTag, rho, sXTag, sYTag, concTag, rouX, rouY, nu, alfadow, *uniqueArgs)

def ManzariDafalias(matTag, G0, nu, e_init, Mc, c, lambda_c, e0, ksi, P_atm, m, h0, ch, nb, A0, nd, z_max, cz, Den):
    """


   This command is used to construct a multi-dimensional Manzari-Dafalias(2004) material.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``G0`` |float|                     shear modulus constant

   ``nu`` |float|                     poisson ratio

   ``e_init`` |float|                 initial void ratio

   ``Mc`` |float|                     critical state stress ratio

   ``c`` |float|                      ratio of critical state stress ratio in extension and compression

   ``lambda_c`` |float|               critical state line constant

   ``e0`` |float|                     critical void ratio at p = 0

   ``ksi`` |float|                    critical state line constant

   ``P_atm`` |float|                  atmospheric pressure

   ``m`` |float|                      yield surface constant (radius of yield surface in stress ratio space)

   ``h0`` |float|                     constant parameter

   ``ch`` |float|                     constant parameter

   ``nb`` |float|                     bounding surface parameter, :math:`nb \ge 0`

   ``A0`` |float|                     dilatancy parameter

   ``nd`` |float|                     dilatancy surface parameter :math:`nd \ge 0`

   ``z_max`` |float|                  fabric-dilatancy tensor parameter

   ``cz`` |float|                     fabric-dilatancy tensor parameter

   ``Den`` |float|                    mass density of the material

   ================================   ===========================================================================



The material formulations for the ManzariDafalias object are:



* ``'ThreeDimensional'``

* ``'PlaneStrain'``



See also `here <http://opensees.berkeley.edu/wiki/index.php/Manzari_Dafalias_Material>`_



References



Dafalias YF, Manzari MT. "Simple plasticity sand model accounting for fabric change effects". Journal of Engineering Mechanics 2004

    """
    uniqueArgs = []
    ops.nDMaterial('ManzariDafalias', matTag, G0, nu, e_init, Mc, c, lambda_c, e0, ksi, P_atm, m, h0, ch, nb, A0, nd, z_max, cz, Den, *uniqueArgs)

def PM4Sand(matTag, D_r, G_o, h_po, Den, P_atm, h_o, e_max, e_min, n_b, n_d, A_do, z_max, c_z, c_e, phi_cv, nu, g_degr, c_dr, c_kaf, Q_bolt, R_bolt, m_par, F_sed, p_sed):
    """


   This command is used to construct a 2-dimensional PM4Sand material.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``D_r`` |float|                    Relative density, in fraction

   ``G_o`` |float|                    Shear modulus constant

   ``h_po`` |float|                   Contraction rate parameter

   ``Den`` |float|                    Mass density of the material

   ``P_atm`` |float|                  Optional, Atmospheric pressure

   ``h_o`` |float|                    Optional, Variable that adjusts the ratio of plastic modulus

                                      to elastic modulus

   ``e_max`` |float|                  Optional, Maximum and minimum void ratios

   ``e_min`` |float|                  Optional, Maximum and minimum void ratios

   ``n_b`` |float|                    Optional, Bounding surface parameter, :math:`n_b \ge 0`

   ``n_d`` |float|                    Optional, Dilatancy surface parameter :math:`n_d \ge 0`

   ``A_do`` |float|                   Optional, Dilatancy parameter, will be computed at the time

                                      of initialization if input value is negative

   ``z_max`` |float|                  Optional, Fabric-dilatancy tensor parameter

   ``c_z`` |float|                    Optional, Fabric-dilatancy tensor parameter

   ``c_e`` |float|                    Optional, Variable that adjusts the rate of strain accumulation

                                      in cyclic loading

   ``phi_cv`` |float|                 Optional, Critical state effective friction angle

   ``nu`` |float|                     Optional, Poisson's ratio

   ``g_degr`` |float|                 Optional, Variable that adjusts degradation of elastic modulus

                                      with accumulation of fabric

   ``c_dr`` |float|                   Optional, Variable that controls the rotated dilatancy surface

   ``c_kaf`` |float|                  Optional, Variable that controls the effect that sustained

                                      static shear stresses have on plastic modulus

   ``Q_bolt`` |float|                 Optional, Critical state line parameter

   ``R_bolt`` |float|                 Optional, Critical state line parameter

   ``m_par`` |float|                  Optional, Yield surface constant (radius of yield surface

                                      in stress ratio space)

   ``F_sed`` |float|                  Optional, Variable that controls the minimum value the

                                      reduction factor of the elastic moduli can get during reconsolidation

   ``p_sed`` |float|                  Optional, Mean effective stress up to which reconsolidation

                                      strains are enhanced

   ================================   ===========================================================================



The material formulations for the PM4Sand object are:



* ``'PlaneStrain'``



See als `here <http://opensees.berkeley.edu/wiki/index.php/PM4Sand_Material>`_





References



R.W.Boulanger, K.Ziotopoulou. "PM4Sand(Version 3.1): A Sand Plasticity Model for Earthquake Engineering Applications". Report No. UCD/CGM-17/01 2017

    """
    uniqueArgs = []
    ops.nDMaterial('PM4Sand', matTag, D_r, G_o, h_po, Den, P_atm, h_o, e_max, e_min, n_b, n_d, A_do, z_max, c_z, c_e, phi_cv, nu, g_degr, c_dr, c_kaf, Q_bolt, R_bolt, m_par, F_sed, p_sed, *uniqueArgs)

def stressDensity(matTag, mDen, eNot, A, n, nu, a1, b1, a2, b2, a3, b3, fd, muNot, muCyc, sc, M, patm, ssls, hsl, p1):
    """


   This command is used to construct a multi-dimensional stress density material object for modeling sand behaviour following the work of Cubrinovski and Ishihara (1998a,b).



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``mDen`` |float|                   mass density

   ``eNot`` |float|                   initial void ratio

   ``A`` |float|                      constant for elastic shear modulus

   ``n`` |float|                      pressure dependency exponent for elastic shear modulus

   ``nu`` |float|                     Poisson's ratio

   ``a1`` |float|                     peak stress ratio coefficient (:math:`etaMax = a1 + b1*Is`)

   ``b1`` |float|                     peak stress ratio coefficient (:math:`etaMax = a1 + b1*Is`)

   ``a2`` |float|                     max shear modulus coefficient (:math:`Gn_max = a2 + b2*Is`)

   ``b2`` |float|                     max shear modulus coefficient (:math:`Gn_max = a2 + b2*Is`)

   ``a3`` |float|                     min shear modulus coefficient (:math:`Gn_min = a3 + b3*Is`)

   ``b3`` |float|                     min shear modulus coefficient (:math:`Gn_min = a3 + b3*Is`)

   ``fd`` |float|                     degradation constant

   ``muNot`` |float|                  dilatancy coefficient (monotonic loading)

   ``muCyc`` |float|                  dilatancy coefficient (cyclic loading)

   ``sc`` |float|                     dilatancy strain

   ``M`` |float|                      critical state stress ratio

   ``patm`` |float|                   atmospheric pressure (in appropriate units)

   ``ssls`` |listf|                   void ratio of quasi steady state (QSS-line) at pressures

                                      [pmin, 10kPa, 30kPa, 50kPa, 100kPa, 200kPa, 400kPa]

                                      (default = [0.877, 0.877, 0.873, 0.870, 0.860, 0.850, 0.833])

   ``hsl`` |float|                    void ratio of upper reference state (UR-line) for all pressures

                                      (default = 0.895)

   ``p1`` |float|                     pressure corresponding to ssl1 (default = 1.0 kPa)

   ================================   ===========================================================================



The material formulations for the StressDensityModel object are:



* ``'ThreeDimensional'``

* ``'PlaneStrain'``



References



Cubrinovski, M. and Ishihara K. (1998a) 'Modelling of sand behaviour based on state concept,' Soils and Foundations, 38(3), 115-127.



Cubrinovski, M. and Ishihara K. (1998b) 'State concept and modified elastoplasticity for sand modelling,' Soils and Foundations, 38(4), 213-225.



Das, S. (2014) Three Dimensional Formulation for the Stress-Strain-Dilatancy Elasto-Plastic Constitutive Model for Sand Under Cyclic Behaviour, Master's Thesis, University of Canterbury.

    """
    uniqueArgs = []
    ops.nDMaterial('stressDensity', matTag, mDen, eNot, A, n, nu, a1, b1, a2, b2, a3, b3, fd, muNot, muCyc, sc, M, patm, *ssls, hsl, p1, *uniqueArgs)

def AcousticMedium(matTag, K, rho):
    """


   This command is used to construct an acoustic medium NDMaterial object.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``K`` |float|                      bulk module of the acoustic medium

   ``rho`` |float|                    mass density of the acoustic medium

   ================================   ===========================================================================

    """
    uniqueArgs = []
    ops.nDMaterial('AcousticMedium', matTag, K, rho, *uniqueArgs)

def CycLiqCP(matTag, G0, kappa, h, Mfc, dre1, Mdc, dre2, rdr, alpha, dir, ein, rho):
    """


   This command is used to construct a multi-dimensional material object that that follows the constitutive behavior of a cyclic elastoplasticity model for large post- liquefaction deformation.



   CycLiqCP material is a cyclic elastoplasticity model for large post-liquefaction deformation, and is implemented using a cutting plane algorithm. The model is capable of reproducing small to large deformation in the pre- to post-liquefaction regime. The elastic moduli of the model are pressure dependent. The plasticity in the model is developed within the framework of bounding surface plasticity, with special consideration to the formulation of reversible and irreversible dilatancy.



The model does not take into consideration of the state of sand, and requires different parameters for sand under different densities and confining pressures. The surfaces (i.e. failure and maximum pre-stress) are considered as circles in the pi plane.



The model has been validated against VELACS centrifuge model tests and has used on numerous simulations of liquefaction related problems.



When this material is employed in regular solid elements (e.g., FourNodeQuad, Brick), it simulates drained soil response. When solid-fluid coupled elements (u-p elements and SSP u-p elements) are used, the model is able to simulate undrained and partially drained behavior of soil.





   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``G0`` |float|                     A constant related to elastic shear modulus

   ``kappa`` |float|                  bulk modulus

   ``h`` |float|                      Model parameter for plastic modulus

   ``Mfc`` |float|                    Stress ratio at failure in triaxial compression

   ``dre1`` |float|                   Coefficient for reversible dilatancy generation

   ``Mdc`` |float|                    Stress ratio at which the reversible dilatancy sign changes

   ``dre2`` |float|                   Coefficient for reversible dilatancy release

   ``rdr`` |float|                    Reference shear strain length

   ``alpha`` |float|                  Parameter controlling the decrease rate of irreversible dilatancy

   ``dir`` |float|                    Coefficient for irreversible dilatancy potential

   ``ein`` |float|                    Initial void ratio

   ``rho`` |float|                    Saturated mass density

   ================================   ===========================================================================



The material formulations for the CycLiqCP object are:



* ``'ThreeDimensional'``

* ``'PlaneStrain'``



See also `here <http://opensees.berkeley.edu/wiki/index.php/CycLiqCP_Material_(Cyclic_ElasticPlasticity)>`_

    """
    uniqueArgs = []
    ops.nDMaterial('CycLiqCP', matTag, G0, kappa, h, Mfc, dre1, Mdc, dre2, rdr, alpha, dir, ein, rho, *uniqueArgs)

def CycLiqCPSP(matTag, G0, kappa, h, M, dre1, dre2, rdr, alpha, dir, lambdac, ksi, e0, np, nd, ein, rho):
    """


   This command is used to construct a multi-dimensional material object that that follows the constitutive behavior of a cyclic elastoplasticity model for large post- liquefaction deformation.



   CycLiqCPSP material is a constitutive model for sand with special considerations for cyclic behaviour and accumulation of large post-liquefaction shear deformation, and is implemented using a cutting plane algorithm. The model: (1) achieves the simulation of post-liquefaction shear deformation based on its physics, allowing the unified description of pre- and post-liquefaction behavior of sand; (2) directly links the cyclic mobility of sand with reversible and irreversible dilatancy, enabling the unified description of monotonic and cyclic loading; (3) introduces critical state soil mechanics concepts to achieve unified modelling of sand under different states.



The critical, maximum stress ratio and reversible dilatancy surfaces follow a rounded triangle in the pi plane similar to the Matsuoka-Nakai criterion.



When this material is employed in regular solid elements (e.g., FourNodeQuad, Brick), it simulates drained soil response. When solid-fluid coupled elements (u-p elements and SSP u-p elements) are used, the model is able to simulate undrained and partially drained behavior of soil.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``G0`` |float|                     A constant related to elastic shear modulus

   ``kappa`` |float|                  bulk modulus

   ``h`` |float|                      Model parameter for plastic modulus

   ``M`` |float|                      Critical state stress ratio

   ``dre1`` |float|                   Coefficient for reversible dilatancy generation

   ``dre2`` |float|                   Coefficient for reversible dilatancy release

   ``rdr`` |float|                    Reference shear strain length

   ``alpha`` |float|                  Parameter controlling the decrease rate of irreversible dilatancy

   ``dir`` |float|                    Coefficient for irreversible dilatancy potential

   ``lambdac`` |float|                Critical state constant

   ``ksi`` |float|                    Critical state constant

   ``e0`` |float|                     Void ratio at pc=0

   ``np`` |float|                     Material constant for peak mobilized stress ratio

   ``nd`` |float|                     Material constant for reversible dilatancy generation stress ratio

   ``ein`` |float|                    Initial void ratio

   ``rho`` |float|                    Saturated mass density

   ================================   ===========================================================================



The material formulations for the CycLiqCP object are:



* ``'ThreeDimensional'``

* ``'PlaneStrain'``



See also `here <http://opensees.berkeley.edu/wiki/index.php/CycLiqCPSP_Material>`_



REFERENCES: Wang R., Zhang J.M., Wang G., 2014. A unified plasticity model for large post-liquefaction shear deformation of sand. Computers and Geotechnics. 59, 54-66.

    """
    uniqueArgs = []
    ops.nDMaterial('CycLiqCPSP', matTag, G0, kappa, h, M, dre1, dre2, rdr, alpha, dir, lambdac, ksi, e0, np, nd, ein, rho, *uniqueArgs)

def PlaneStressUserMaterial(matTag, nstatevs, nprops, fc, ft, fcu, epsc0, epscu, epstu, stc):
    """


   This command is used to create the multi-dimensional concrete material model that is based on the damage mechanism and smeared crack model.



   ================================   ===========================================================================

   ``nstatevs`` |int|                 number of state/history variables (usually 40)

   ``nprops`` |int|                   number of material properties (usually 7)

   ``matTag`` |int|                   integer tag identifying material

   ``fc`` |float|                     concrete compressive strength at 28 days (positive)

   ``ft`` |float|                     concrete tensile strength (positive)

   ``fcu`` |float|                    concrete crushing strength (negative)

   ``epsc0`` |float|                  concrete strain at maximum strength (negative)

   ``epscu`` |float|                  concrete strain at crushing strength (negative)

   ``epstu`` |float|                  ultimate tensile strain (positive)

   ``stc`` |float|                    shear retention factor

   ================================   ===========================================================================

    """
    uniqueArgs = []
    ops.nDMaterial('PlaneStressUserMaterial', matTag, nstatevs, nprops, fc, ft, fcu, epsc0, epscu, epstu, stc, *uniqueArgs)

def PlateFromPlaneStress(matTag, pre_def_matTag, OutofPlaneModulus):
    """


   This command is used to create the multi-dimensional concrete material model that is based on the damage mechanism and smeared crack model.



   ================================   ===========================================================================

   ``matTag`` |int|                   new integer tag identifying material deriving from pre-defined

                                      PlaneStress material

   ``pre_def_matTag`` |int|           integer tag identifying PlaneStress material

   ``OutofPlaneModulus`` |float|      shear modulus for out of plane stresses

   ================================   ===========================================================================

    """
    uniqueArgs = []
    ops.nDMaterial('PlateFromPlaneStress', matTag, pre_def_matTag, OutofPlaneModulus, *uniqueArgs)

def PlateRebar(matTag, pre_def_matTag, sita):
    """


   This command is used to create the multi-dimensional reinforcement material.



   ================================   ===========================================================================

   ``matTag`` |int|                   new integer tag identifying material deriving from pre-defined

                                      uniaxial material

   ``pre_def_matTag`` |int|                   integer tag identifying uniaxial material

   ``sita`` |float|                   define the angle of reinforcement layer,

                                      90 (longitudinal), 0 (tranverse)

   ================================   ===========================================================================

    """
    uniqueArgs = []
    ops.nDMaterial('PlateRebar', matTag, pre_def_matTag, sita, *uniqueArgs)

def PlasticDamageConcretePlaneStress(matTag, E, nu, ft, fc, Ap=None, An=None, Bn=None):
    """


   No documentation is available yet. If you have the manual, please let me know.



    """
    uniqueArgs = []
    if Ap:
        uniqueArgs.append(beta)
        uniqueArgs.append(Ap)
        uniqueArgs.append(An)
        uniqueArgs.append(Bn)
    ops.nDMaterial('PlasticDamageConcretePlaneStress', matTag, E, nu, ft, fc, *uniqueArgs)

def ContactMaterial2D(matTag, mu, G, c, t):
    """


   This command is used to construct a ContactMaterial2D nDMaterial object.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``mu`` |float|                     interface frictional coefficient

   ``G`` |float|                      interface stiffness parameter

   ``c`` |float|                      interface cohesive intercept

   ``t`` |float|                      interface tensile strength

   ================================   ===========================================================================





The ContactMaterial2D nDMaterial defines the constitutive behavior of a frictional interface between two bodies in contact. The interface defined by this material object allows for sticking, frictional slip, and separation between the two bodies in a two-dimensional analysis. A regularized Coulomb frictional law is assumed. Information on the theory behind this material can be found in, e.g. Wriggers (2002).



.. note::



   #. The ContactMaterial2D nDMaterial has been written to work with the SimpleContact2D and BeamContact2D element objects.

   #. There are no valid recorder queries for this material other than those which are listed with those elements





References:



Wriggers, P. (2002). Computational Contact Mechanics. John Wilely & Sons, Ltd, West Sussex, England.

    """
    uniqueArgs = []
    ops.nDMaterial('ContactMaterial2D', matTag, mu, G, c, t, *uniqueArgs)

def ContactMaterial3D(matTag, mu, G, c, t):
    """


   This command is used to construct a ContactMaterial3D nDMaterial object.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``mu`` |float|                     interface frictional coefficient

   ``G`` |float|                      interface stiffness parameter

   ``c`` |float|                      interface cohesive intercept

   ``t`` |float|                      interface tensile strength

   ================================   ===========================================================================







The ContactMaterial3D nDMaterial defines the constitutive behavior of a frictional interface between two bodies in contact. The interface defined by this material object allows for sticking, frictional slip, and separation between the two bodies in a three-dimensional analysis. A regularized Coulomb frictional law is assumed. Information on the theory behind this material can be found in, e.g. Wriggers (2002).



.. note::



   #. The ContactMaterial3D nDMaterial has been written to work with the SimpleContact3D and BeamContact3D element objects.

   #. There are no valid recorder queries for this material other than those which are listed with those elements.





References:



Wriggers, P. (2002). Computational Contact Mechanics. John Wilely & Sons, Ltd, West Sussex, England.

    """
    uniqueArgs = []
    ops.nDMaterial('ContactMaterial3D', matTag, mu, G, c, t, *uniqueArgs)

def InitialStateAnalysisWrapper(matTag, nDMatTag, nDim):
    """


   The InitialStateAnalysisWrapper nDMaterial allows for the use of the InitialStateAnalysis command for setting initial conditions. The InitialStateAnalysisWrapper can be used with any nDMaterial. This material wrapper allows for the development of an initial stress field while maintaining the original geometry of the problem. An example analysis is provided below to demonstrate the use of this material wrapper object.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``nDMatTag`` |int|                 the tag of the associated nDMaterial object

   ``nDim`` |int|                     number of dimensions (2 for 2D, 3 for 3D)

   ================================   ===========================================================================





.. note::



   #. There are no valid recorder queries for the InitialStateAnalysisWrapper.

   #. The InitialStateAnalysis off command removes all previously defined recorders. Two sets of recorders are needed if the results before and after this command are desired. See the example below for more.

   #. The InitialStateAnalysisWrapper material is somewhat tricky to use in dynamic analysis. Sometimes setting the displacement to zero appears to be interpreted as an initial displacement in subsequent steps, resulting in undesirable vibrations.

    """
    uniqueArgs = []
    ops.nDMaterial('InitialStateAnalysisWrapper', matTag, nDMatTag, nDim, *uniqueArgs)

def InitStressNDMaterial(matTag, otherTag, initStress, nDim):
    """


   This command is used to construct an Initial Stress material object.

   The stress-strain behaviour for this material is defined by another material.

   Initial Stress Material enables definition of initial stress for the material under consideration.

   The strain that corresponds to the initial stress will be calculated from the other material.



   ===================================   ===========================================================================

   ``matTag`` |int|                      integer tag identifying material

   ``otherTag`` |float|                  tag of the other material

   ``initStress`` |float|                initial stress

   ``nDim`` |int|                        Number of dimensions (e.g. if plane strain nDim=2)

   ===================================   ===========================================================================



.. seealso::





   `Notes <http://opensees.berkeley.edu/wiki/index.php/Initial_Stress_Material>`_

    """
    uniqueArgs = []
    ops.nDMaterial('InitStressNDMaterial', matTag, otherTag, initStress, nDim, *uniqueArgs)

def InitStrainNDMaterial(matTag, otherTag, initStrain, nDim):
    """


   This command is used to construct an Initial Strain material object. The stress-strain behaviour for this material is defined by another material. Initial Strain Material enables definition of initial strains for the material under consideration. The stress that corresponds to the initial strain will be calculated from the other material.



   ===================================   ===========================================================================

   ``matTag`` |int|                      integer tag identifying material

   ``otherTag`` |int|                    tag of the other material

   ``initStrain`` |float|                initial strain

   ``nDim`` |float|                      Number of dimensions

   ===================================   ===========================================================================



.. seealso::





   `Notes <http://opensees.berkeley.edu/wiki/index.php/Initial_Strain_Material>`_

    """
    uniqueArgs = []
    ops.nDMaterial('InitStrainNDMaterial', matTag, otherTag, initStrain, nDim, *uniqueArgs)

def PressureIndependMultiYield(matTag, nd, rho, refShearModul, refBulkModul, cohesi, peakShearStra, frictionAng, refPress, pressDependCoe, noYieldSurf, yieldSurf):
    """


   PressureIndependMultiYield material is an elastic-plastic material in which plasticity exhibits only in the deviatoric stress-strain response. The volumetric stress-strain response is linear-elastic and is independent of the deviatoric response. This material is implemented to simulate monotonic or cyclic response of materials whose shear behavior is insensitive to the confinement change. Such materials include, for example, organic soils or clay under fast (undrained) loading conditions.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``nd`` |float|                     Number of dimensions, 2 for plane-strain, and 3 for 3D analysis.

   ``rho`` |float|                    Saturated soil mass density.

   ``refShearModul`` |float|          (:math:`G_r`) Reference low-strain shear modulus,

                                      specified at a reference mean effective confining

                                      pressure refPress of p'r (see below).

   ``refBulkModul`` |float|           (:math:`B_r`) Reference bulk modulus,

                                      specified at a reference

                                      mean effective confining pressure refPress

                                      of p'r (see below).

   ``cohesi`` |float|                 (:math:`c`) Apparent cohesion at zero

                                      effective confinement.

   ``peakShearStra`` |float|          (:math:`\gamma_{max}`) An octahedral shear strain at

                                      which the maximum shear strength is reached,

                                      specified at a reference mean effective confining

                                      pressure refPress of p'r (see below).

   ``frictionAng`` |float|            (:math:`phi`) Friction angle at peak shear

                                      strength in degrees, optional (default is 0.0).

   ``refPress`` |float|               (:math:`p'_r`) Reference mean effective confining

                                      pressure at which

                                      :math:`G_r`, :math:`B_r`, and :math:`\gamma_{max}`

                                      are defined, optional (default is 100. kPa).

   ``pressDependCoe`` |float|         (:math:`d`) A positive constant defining variations

                                      of :math:`G` and :math:`B` as a function of

                                      instantaneous effective

                                      confinement :math:`p'` (default is 0.0)



                                      :math:`G=G_r(\frac{p'}{p'_r})^d`



                                      :math:`B=B_r(\frac{p'}{p'_r})^d`



                                      If :math:`\phi=0`, :math:`d` is reset to 0.0.



   ``noYieldSurf`` |float|            Number of yield surfaces, optional (must be less

                                      than 40, default is 20). The surfaces are generated

                                      based on the hyperbolic relation defined in Note 2

                                      below.

   ``yieldSurf`` |listf|              Instead of automatic surfaces generation (Note 2),

                                      you can define yield surfaces directly based on

                                      desired shear modulus reduction curve. To do so,

                                      add a minus sign in front of noYieldSurf, then

                                      provide noYieldSurf pairs of shear strain (r) and

                                      modulus ratio (Gs) values. For example, to define

                                      10 surfaces: yieldSurf = [r1, Gs1, ..., r10, Gs10]

   ================================   ===========================================================================







See also `notes <http://opensees.berkeley.edu/wiki/index.php/PressureIndependMultiYield_Material>`_

    """
    uniqueArgs = []
    ops.nDMaterial('PressureIndependMultiYield', matTag, nd, rho, refShearModul, refBulkModul, cohesi, peakShearStra, frictionAng, refPress, pressDependCoe, noYieldSurf, *yieldSurf, *uniqueArgs)

def PressureDependMultiYield(matTag, nd, rho, refShearModul, refBulkModul, frictionAng, peakShearStra, refPress, pressDependCoe, PTAng, contrac, dilat, liquefac, noYieldSurf, *yieldSurf, e, *params, 0.02, 0.7, 101.0], c):
    """


   PressureDependMultiYield material is an elastic-plastic material for simulating the essential response characteristics of pressure sensitive soil materials under general loading conditions. Such characteristics include dilatancy (shear-induced volume contraction or dilation) and non-flow liquefaction (cyclic mobility), typically exhibited in sands or silts during monotonic or cyclic loading.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``nd`` |float|                     Number of dimensions, 2 for plane-strain, and 3 for 3D analysis.

   ``rho`` |float|                    Saturated soil mass density.

   ``refShearModul`` |float|          (:math:`G_r`) Reference low-strain shear modulus,

                                      specified at a reference mean effective confining

                                      pressure refPress of p'r (see below).

   ``refBulkModul`` |float|           (:math:`B_r`) Reference bulk modulus,

                                      specified at a reference

                                      mean effective confining pressure refPress

                                      of p'r (see below).

   ``frictionAng`` |float|            (:math:`phi`) Friction angle at peak shear

                                      strength in degrees, optional (default is 0.0).

   ``peakShearStra`` |float|          (:math:`\gamma_{max}`) An octahedral shear strain at

                                      which the maximum shear strength is reached,

                                      specified at a reference mean effective confining

                                      pressure refPress of p'r (see below).

   ``refPress`` |float|               (:math:`p'_r`) Reference mean effective confining

                                      pressure at which

                                      :math:`G_r`, :math:`B_r`, and :math:`\gamma_{max}`

                                      are defined, optional (default is 100. kPa).

   ``pressDependCoe`` |float|         (:math:`d`) A positive constant defining variations

                                      of :math:`G` and :math:`B` as a function of

                                      instantaneous effective

                                      confinement :math:`p'` (default is 0.0)



                                      :math:`G=G_r(\frac{p'}{p'_r})^d`



                                      :math:`B=B_r(\frac{p'}{p'_r})^d`



                                      If :math:`\phi=0`, :math:`d` is reset to 0.0.



   ``PTAng`` |float|                  (:math:`\phi_{PT}`) Phase transformation angle,

                                      in degrees.

   ``contrac`` |float|                A non-negative constant defining the rate of

                                      shear-induced volume decrease (contraction) or

                                      pore pressure buildup. A larger value corresponds

                                      to faster contraction rate.

   ``dilat`` |listf|                  Non-negative constants defining the rate of

                                      shear-induced volume increase (dilation).

                                      Larger values correspond to stronger dilation rate.

                                      ``dilat = [dilat1, dilat2]``.

   ``liquefac`` |listf|               Parameters controlling the mechanism of

                                      liquefaction-induced perfectly plastic shear strain

                                      accumulation, i.e., cyclic mobility.

                                      Set ``liquefac[0] = 0`` to deactivate this mechanism

                                      altogether. ``liquefac[0]`` defines the effective

                                      confining pressure (e.g., 10 kPa in SI units or

                                      1.45 psi in English units) below which the mechanism

                                      is in effect. Smaller values should be assigned to

                                      denser sands. ``Liquefac[1]`` defines the maximum

                                      amount of perfectly plastic shear strain developed

                                      at zero effective confinement during each loading

                                      phase. Smaller values should be assigned to denser

                                      sands. ``Liquefac[2]`` defines the maximum amount

                                      of biased

                                      perfectly plastic shear strain :math:`\gamma_b`

                                      accumulated at

                                      each loading phase under biased shear loading

                                      conditions, as

                                      :math:`\gamma_b=liquefac[1]\times liquefac[2]`.

                                      Typically, :math:`liquefac[2]` takes a value

                                      between 0.0 and 3.0. Smaller values should be

                                      assigned to denser sands. See the references listed

                                      at the end of this chapter for more information.

   ``noYieldSurf`` |float|            Number of yield surfaces, optional (must be less

                                      than 40, default is 20). The surfaces are generated

                                      based on the hyperbolic relation defined in Note 2

                                      below.

   ``yieldSurf`` |listf|              If ``noYieldSurf<0 && >-100``, the user defined

                                      yield surface is used. You have to provide

                                      a list of ``2*(-noYieldSurf)``, otherwise, the arguments

                                      will be messed up. Also don't provide user defined

                                      yield surface if ``noYieldSurf>0``, it will

                                      mess up the argument list too.

                                      Instead of automatic surfaces generation (Note 2),

                                      you can define yield surfaces directly based on

                                      desired shear modulus reduction curve. To do so,

                                      add a minus sign in front of noYieldSurf, then

                                      provide noYieldSurf pairs of shear strain (r) and

                                      modulus ratio (Gs) values. For example, to define

                                      10 surfaces: yieldSurf = [r1, Gs1, ..., r10, Gs10]

   ``e`` |float|                      Initial void ratio, optional (default is 0.6).

   ``params`` |listf|                 ``params=[cs1, cs2, cs3, pa]``

                                      defining a straight critical-state line ec

                                      in e-p' space.



                                      If cs3=0,



                                      ec = cs1-cs2 log(p'/pa)



                                      else (Li and Wang, JGGE, 124(12)),



                                      ec = cs1-cs2(p'/pa)cs3



                                      where pa is atmospheric pressure for normalization

                                      (typically 101 kPa in SI units, or 14.65 psi in

                                      English units). All four constants are optional



   ``c`` |float|                      Numerical constant (default value = 0.3 kPa)

   ================================   ===========================================================================







See also `notes <http://opensees.berkeley.edu/wiki/index.php/PressureDependMultiYield_Material>`_

    """
    uniqueArgs = []
    ops.nDMaterial('PressureDependMultiYield', matTag, nd, rho, refShearModul, refBulkModul, frictionAng, peakShearStra, refPress, pressDependCoe, PTAng, contrac, *dilat, *liquefac, noYieldSurf, *yieldSurf, e, *params, 0.02, 0.7, 101.0], c, *uniqueArgs)

def PressureDependMultiYield02(matTag, nd, rho, refShearModul, refBulkModul, frictionAng, peakShearStra, refPress, pressDependCoe, PTAng, contrac[0], contrac[2], dilat[0], dilat[2], noYieldSurf, *yieldSurf, contrac[1], dilat[1], *liquefac, 0.0], e, *params, 0.02, 0.7, 101.0], c):
    """


   PressureDependMultiYield02 material is modified from PressureDependMultiYield material, with:



   #. additional parameters (``contrac[2]`` and ``dilat[2]``) to account for :math:`K_{\sigma}` effect,

   #. a parameter to account for the influence of previous dilation history on subsequent contraction phase (``contrac[1]``), and

   #. modified logic related to permanent shear strain accumulation (``liquefac[0]`` and ``liquefac[1]``).



   ================================   ================================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``nd`` |float|                     Number of dimensions, 2 for plane-strain, and 3 for 3D analysis.

   ``rho`` |float|                    Saturated soil mass density.

   ``refShearModul`` |float|          (:math:`G_r`) Reference low-strain shear modulus,

                                      specified at a reference mean effective confining

                                      pressure refPress of p'r (see below).

   ``refBulkModul`` |float|           (:math:`B_r`) Reference bulk modulus,

                                      specified at a reference

                                      mean effective confining pressure refPress

                                      of p'r (see below).

   ``frictionAng`` |float|            (:math:`phi`) Friction angle at peak shear

                                      strength in degrees, optional (default is 0.0).

   ``peakShearStra`` |float|          (:math:`\gamma_{max}`) An octahedral shear strain at

                                      which the maximum shear strength is reached,

                                      specified at a reference mean effective confining

                                      pressure refPress of p'r (see below).

   ``refPress`` |float|               (:math:`p'_r`) Reference mean effective confining

                                      pressure at which

                                      :math:`G_r`, :math:`B_r`, and :math:`\gamma_{max}`

                                      are defined, optional (default is 100. kPa).

   ``pressDependCoe`` |float|         (:math:`d`) A positive constant defining variations

                                      of :math:`G` and :math:`B` as a function of

                                      instantaneous effective

                                      confinement :math:`p'` (default is 0.0)



                                      :math:`G=G_r(\frac{p'}{p'_r})^d`



                                      :math:`B=B_r(\frac{p'}{p'_r})^d`



                                      If :math:`\phi=0`, :math:`d` is reset to 0.0.



   ``PTAng`` |float|                  (:math:`\phi_{PT}`) Phase transformation angle,

                                      in degrees.

   ``contrac[2]`` |float|             A non-negative constant reflecting :math:`K_\sigma` effect.

   ``dilat[2]`` |float|               A non-negative constant reflecting :math:`K_\sigma` effect.

   ``contrac[1]`` |float|             A non-negative constant reflecting dilation history on contraction tendency.

   ``liquefac[0]`` |float|            Damage parameter to define accumulated permanent

                                      shear strain as a function of dilation

                                      history. (Redefined and different from

                                      PressureDependMultiYield material).

   ``liquefac[1]`` |float|            Damage parameter to define biased accumulation of

                                      permanent shear strain as a function of load reversal

                                      history. (Redefined and different from

                                      PressureDependMultiYield material).

   ``c`` |float|                      Numerical constant (default value = 0.1 kPa)

   ================================   ================================================================================







See also `notes <http://opensees.berkeley.edu/wiki/index.php/PressureDependMultiYield02_Material>`_

    """
    uniqueArgs = []
    ops.nDMaterial('PressureDependMultiYield02', matTag, nd, rho, refShearModul, refBulkModul, frictionAng, peakShearStra, refPress, pressDependCoe, PTAng, contrac[0], contrac[2], dilat[0], dilat[2], noYieldSurf, *yieldSurf, contrac[1], dilat[1], *liquefac, 0.0], e, *params, 0.02, 0.7, 101.0], c, *uniqueArgs)

def PressureDependMultiYield03(matTag, nd, rho, refShearModul, refBulkModul, frictionAng, peakShearStra, refPress, pressDependCoe, PTAng, ca, cb, cc, cd, ce, da, db, dc, noYieldSurf, *yieldSurf, liquefac1, liquefac2, pa, s0):
    """


   The reference for PressureDependMultiYield03 material: Khosravifar, A., Elgamal, A., Lu, J., and Li, J. [2018]. "A 3D model for earthquake-induced liquefaction triggering and post-liquefaction response." Soil Dynamics and Earthquake Engineering, 110, 43-52)



   PressureDependMultiYield03 is modified from PressureDependMultiYield02 material to comply with the established guidelines on the dependence of liquefaction triggering to the number of loading cycles, effective overburden stress (Kσ), and static shear stress (Kα).

  

   The explanations of parameters



   See `notes <http://opensees.berkeley.edu/wiki/index.php/PressureDependMultiYield02_Material>`_

    """
    uniqueArgs = []
    ops.nDMaterial('PressureDependMultiYield03', matTag, nd, rho, refShearModul, refBulkModul, frictionAng, peakShearStra, refPress, pressDependCoe, PTAng, ca, cb, cc, cd, ce, da, db, dc, noYieldSurf, *yieldSurf, liquefac1, liquefac2, pa, s0, *uniqueArgs)

def FluidSolidPorous(matTag, nd, soilMatTag, combinedBulkModul, pa):
    """


   FluidSolidPorous material couples the responses of two phases: fluid and solid. The fluid phase response is only volumetric and linear elastic. The solid phase can be any NDMaterial. This material is developed to simulate the response of saturated porous media under fully undrained condition.



   ================================   ===========================================================================

   ``matTag`` |int|                   integer tag identifying material

   ``nd`` |float|                     Number of dimensions, 2 for plane-strain, and 3 for 3D analysis.

   ``soilMatTag`` |int|               The material number for the solid phase material (previously defined).

   ``combinedBulkModul`` |float|      Combined undrained bulk modulus :math:`B_c`

                                      relating changes in pore pressure and volumetric

                                      strain, may be approximated by:



                                      :math:`B_c \approx B_f /n`



                                      where :math:`B_f` is the bulk modulus of fluid

                                      phase (2.2x106 kPa (or 3.191x105 psi) for water),

                                      and :math:`n` the initial porosity.



   ``pa`` |float|                     Optional atmospheric pressure for

                                      normalization (typically 101 kPa in SI units,

                                      or 14.65 psi in English units)

   ================================   ===========================================================================







See also `notes <http://opensees.berkeley.edu/wiki/index.php/FluidSolidPorousMaterial>`_

    """
    uniqueArgs = []
    ops.nDMaterial('FluidSolidPorous', matTag, nd, soilMatTag, combinedBulkModul, pa, *uniqueArgs)

