import openseespy.opensees as ops

def Steel01(matTag, Fy, E0, b, a1=None, a2=None, a3=None, a4=None):
    
    """
    This command is used to construct a uniaxial bilinear steel material 
    object with kinematic hardening and optional isotropic hardening 
    described by a non-linear evolution equation (REF: Fedeas).
    
    ================================   ===========================================================================
    ``matTag`` |int|                   integer tag identifying material
    ``Fy`` |float|                     yield strength
    ``E0`` |float|                     initial elastic tangent
    ``b`` |float|                      strain-hardening ratio (ratio between post-yield
                                       tangent and initial elastic tangent)
    ``a1`` |float|                     isotropic hardening parameter, increase of
                                       compression yield envelope as proportion of yield
                                       strength after a plastic strain of
                                       :math:`a_2*(F_y/E_0)` (optional)
    ``a2`` |float|                     isotropic hardening parameter
                                       (see explanation under ``a1``). (optional).
    ``a3`` |float|                     isotropic hardening parameter, increase of tension
                                       yield envelope as proportion of yield strength
                                       after a plastic strain
                                       of :math:`a_4*(F_y/E_0)`. (optional)
    ``a4`` |float|                     isotropic hardening parameter (see explanation
                                       under ``a3``). (optional)
    
    ================================   ===========================================================================

    .. note::
    
    
        If strain-hardening ratio is zero and you do not expect softening of your system use BandSPD solver.

    Hints:
        untested

    """
    uniqueArgs = []
    if a1:
        uniqueArgs.append(a1)
    if a2:
        uniqueArgs.append(a2)    
    if a3:
        uniqueArgs.append(a3)    
    if a4:
        uniqueArgs.append(a4)
        
    ops.uniaxialMaterial('Steel01', matTag, Fy, E0, b, *uniqueArgs)

def Steel02(matTag, Fy, E0, b, params, a1=None, a2=None, a3=None, a4=None, sigInit=0.0):
    """
    This command is used to construct a uniaxial Giuffre-Menegotto-Pinto steel material object with isotropic strain hardening.
    
    ================================   ===========================================================================
    ``matTag`` |int|                   integer tag identifying material
    ``Fy`` |float|                     yield strength
    ``E0`` |float|                     initial elastic tangent
    ``b`` |float|                      strain-hardening ratio (ratio between post-yield
                                       tangent and initial elastic tangent)
    ``params`` |listf|                 parameters to control the transition from elastic to
                                       plastic branches.
                                       ``params=[R0,cR1,cR2]``.
                                       Recommended values: R0=between 10 and 20,
                                       cR1=0.925, cR2=0.15
    ``a1`` |float|                     isotropic hardening parameter, increase of
                                       compression yield envelope as proportion of yield
                                       strength after a plastic strain of
                                       :math:`a_2*(F_y/E_0)` (optional)
    ``a2`` |float|                     isotropic hardening parameter
                                       (see explanation under ``a1``). (optional).
    ``a3`` |float|                     isotropic hardening parameter, increase of tension
                                       yield envelope as proportion of yield strength
                                       after a plastic strain
                                       of :math:`a_4*(F_y/E_0)`. (optional)
    ``a4`` |float|                     isotropic hardening parameter (see explanation
                                       under ``a3``). (optional)
    ``sigInit`` |float|                Initial Stress Value (optional, default: 0.0)
                                       the strain is calculated from ``epsP=sigInit/E``
                                       ::
                                          if (sigInit!= 0.0) {
    
                                            double epsInit = sigInit/E;
    
                                            eps = trialStrain+epsInit;
    
                                          } else {
    
                                            eps = trialStrain;
    
                                          }
    ================================   ===========================================================================

    .. seealso::

       `Steel02 <http://opensees.berkeley.edu/wiki/index.php/Steel02_Material_--_Giuffr%C3%A9-Menegotto-Pinto_Model_with_Isotropic_Strain_Hardening>`_
       
       `Steel02 wiki 2 <https://opensees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/Steel02.html>`_

    Hints:
        note, a1/a2/a3/a4 are all grouped. If you need an initial stress, all
        must be input.

    """
    uniqueArgs = []
    if a1:
        uniqueArgs.append(a1)
        uniqueArgs.append(a2)    
        uniqueArgs.append(a3)    
        uniqueArgs.append(a4)
    if sigInit:
        uniqueArgs.append(sigInit)
        
        
    ops.uniaxialMaterial('Steel02', matTag, Fy, E0, b, *params, *uniqueArgs)

def Steel4(matTag, Fy, E0, asym = False, kin = False, b_k=None, params=None, b_kc=None, paramsC=None, 
           iso = True, b_i=None, rho_i=None, b_l=None, R_i=None, l_yp=None, b_ic=None, rho_ic=None, b_lc=None, R_ic=None, f_u=None, R_u=None, f_uc=None, R_uc=None, sig_init=None, cycNum=None):
    """

    This command is used to construct a general uniaxial material with combined kinematic and isotropic hardening and optional non-symmetric behavior.
    
    ===================================   ===========================================================================
    ``matTag`` |int|                      integer tag identifying material
    
    ``Fy`` |float|                        yield strength
    
    ``E0`` |float|                        initial elastic tangent
    
    ``'-asym'`` |str|                     assume non-symmetric behavior. If toggled, then b_kc and paramsC must be input.
    
    ``'-kin'`` |str|                      apply kinematic hardening
    
    ``b_k`` |float|                       hardening ratio (E_k/E_0)
    
    ``params`` |listf|                    control the exponential transition from linear elastic to hardening asymptote
                                          ``params=[R_0,r_1,r_2]``.
                                          Recommended values: ``R_0 = 20, r_1 = 0.90, r_2 = 0.15``
                                          
    ``b_kc`` |float|                      hardening ratio for compression(E_k/E_0)
    
    ``paramsC`` |listf|                    control the compression exponential transition from linear elastic to hardening asymptote
                                          ``params=[R_0,r_1,r_2]``.
                                          Recommended values: ``R_0 = 20, r_1 = 0.90, r_2 = 0.15``

    ``'-iso'`` |str|                      apply isotropic hardening
    
    ``b_i`` |float|                       initial hardening ratio (E_i/E_0)
    
    ``b_l`` |float|                       saturated hardening ratio (E_is/E_0)
    
    ``rho_i`` |float|                     specifies the position of the intersection point
                                          between initial and saturated hardening asymptotes
    
    ``R_i`` |float|                       control the exponential transition from initial
                                          to saturated asymptote
    
    ``l_yp`` |float|                      length of the yield plateau in eps_y0 = f_y / E_0 units
    
    ``'-ult'`` |str|                      apply an ultimate strength limit
    
    ``f_u`` |float|                       ultimate strength
    
    ``R_u`` |float|                       control the exponential transition from
                                          kinematic hardening to perfectly plastic asymptote

    ``'-init'`` |str|                     apply initial stress
    
    ``sig_init`` |float|                  initial stress value
    
    ``'-mem'`` |str|                      configure the load history memory
    
    ``cycNum`` |float|                    expected number of half-cycles during the loading
                                          process
                                          Efficiency of the material can be slightly
                                          increased by correctly setting this value.
                                          The default value is ``cycNum = 50``
                                          Load history memory can be turned off by
                                          setting ``cycNum = 0``.
    
    ===================================   ===========================================================================

    .. seealso::


        `Steel4 <http://opensees.berkeley.edu/wiki/index.php/Steel4_Material>`_


    Hints:
        Untested
    """
    uniqueArgs = []
    if asym:
        uniqueArgs.append('-asym')
    if b_k:
        uniqueArgs.append('-kin')
        uniqueArgs.append(b_k)
        uniqueArgs += params
    if asym and b_kc:
        uniqueArgs.append(b_kc)
        uniqueArgs += paramsC
                
        
    if iso:
        uniqueArgs.append('-iso')
        uniqueArgs.append(b_i)
        uniqueArgs.append(b_l)
        uniqueArgs.append(R_i)
        uniqueArgs.append(l_yp)
        uniqueArgs.append(b_ic)
        uniqueArgs.append(rho_ic)
        uniqueArgs.append(b_lc)
        uniqueArgs.append(R_ic)
        
    if f_u:
        uniqueArgs.append('-ult')
        uniqueArgs.append(f_u)
        uniqueArgs.append(R_u)
        uniqueArgs.append(f_uc)
        uniqueArgs.append(R_uc)
    if sig_init:
        uniqueArgs.append('-init')
        uniqueArgs.append(sig_init)
    if cycNum:
        uniqueArgs.append('-mem')
        uniqueArgs.append(cycNum)
    ops.uniaxialMaterial('Steel4', matTag, Fy, E0, *uniqueArgs)

def Hysteretic(matTag, p1, p2, p3, n1, n2, n3, pinchX, pinchY, damage1, damage2, beta):
    """

    This command is used to construct a uniaxial bilinear hysteretic material object with pinching of force and deformation, damage due to ductility and energy, and degraded unloading stiffness based on ductility.

    ===================================   ===========================================================================

    ``matTag`` |int|                      integer tag identifying material

    ``p1`` |listf|                        ``p1=[s1p, e1p]``, stress and strain (or force
                                          & deformation) at first point of the envelope
                                          in the positive direction

    ``p2`` |listf|                        ``p2=[s2p, e2p]``, stress and strain (or force
                                          & deformation) at second point of the envelope
                                          in the positive direction

    ``p3`` |listf|                        ``p3=[s3p, e3p]``, stress and strain (or force
                                          & deformation) at third point of the envelope
                                          in the positive direction

    ``n1`` |listf|                        ``n1=[s1n, e1n]``, stress and strain (or force
                                          & deformation) at first point of the envelope
                                          in the negative direction

    ``n2`` |listf|                        ``n2=[s2n, e2n]``, stress and strain (or force
                                          & deformation) at second point of the envelope
                                          in the negative direction

    ``n3`` |listf|                        ``n3=[s3n, e3n]``, stress and strain (or force
                                          & deformation) at third point of the envelope
                                          in the negative direction

    ``pinchX`` |float|                    pinching factor for strain (or deformation) during reloading

    ``pinchY`` |float|                    pinching factor for stress (or force) during reloading

    ``damage1`` |float|                   damage due to ductility: D1(mu-1)

    ``damage2`` |float|                   damage due to energy: D2(Eii/Eult)

    ``beta`` |float|                      power used to determine the degraded unloading
                                          stiffness based on ductility, mu-beta (optional, default=0.0)

    ===================================   ===========================================================================

    .. seealso::
    
    
        `Hysteretic <http://opensees.berkeley.edu/wiki/index.php/Hysteretic_Material>`_

    Hints:
        Untested
    """
    ops.uniaxialMaterial('Hysteretic', matTag, *p1, *p2, *p3, *n1, *n2, *n3, pinchX, pinchY, damage1, damage2, beta)

# def ReinforcingSteel(matTag, fy, fu, Es, Esh, eps_sh, eps_ult, lsr=None, beta=None, r=None, gamma=None, lsr=None, alpha, Cf=None, alpha=None, Cd=None, a1, limit, R1, R2, R3):
#     """

#    This command is used to construct a ReinforcingSteel uniaxial material object. This object is intended to be used in a reinforced concrete fiber section as the steel reinforcing material.

#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``fy`` |float|                        Yield stress in tension

#    ``fu`` |float|                        Ultimate stress in tension

#    ``Es`` |float|                        Initial elastic tangent

#    ``Esh`` |float|                       Tangent at initial strain hardening

#    ``eps_sh`` |float|                       Strain corresponding to initial strain hardening

#    ``eps_ult`` |float|                      Strain at peak stress

#    ``'-GABuck'`` |str|                   Buckling Model Based on Gomes and Appleton (1997)

#    ``lsr`` |float|                       Slenderness Ratio

#    ``beta`` |float|                      Amplification factor for the buckled stress strain curve.

#    ``r`` |float|                         Buckling reduction factor

#                                          r can be a real number between [0.0 and 1.0]

#                                          r=1.0 full reduction (no buckling)

#                                          r=0.0 no reduction

#                                          0.0<r<1.0 linear interpolation between buckled and unbuckled curves

#    ``gamma`` |float|                     Buckling constant

#    ``'-DMBuck'`` |str|                   Buckling model based on Dhakal and Maekawa (2002)

#    ``lsr`` |float|                       Slenderness Ratio

#    ``alpha`` |float|                     Adjustment Constant usually between 0.75 and 1.0
#                                          Default: alpha=1.0, this parameter is optional.

#    ``'-CMFatigue'`` |str|                Coffin-Manson Fatigue and Strength Reduction

#    ``Cf`` |float|                        Coffin-Manson constant C

#    ``alpha`` |float|                     Coffin-Manson constant a

#    ``Cd`` |float|                        Cyclic strength reduction constant

#    ``'-IsoHard'`` |str|                  Isotropic Hardening / Diminishing Yield Plateau

#    ``a1`` |float|                        Hardening constant (default = 4.3)

#    ``limit`` |float|                     Limit for the reduction of the yield plateau.
#                                          % of original plateau length to remain (0.01 < limit < 1.0 )
#                                          Limit =1.0, then no reduction takes place (default =0.01)

#    ``'-MPCurveParams'`` |str|            Menegotto and Pinto Curve Parameters

#    ``R1`` |float|                        (default = 0.333)

#    ``R2`` |float|                        (default = 18)

#    ``R3`` |float|                        (default = 4)

#    ===================================   ===========================================================================


# .. seealso::


#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Reinforcing_Steel_Material>`_

#     """
#     uniqueArgs = []
#     if lsr:
#         uniqueArgs.append('-GABuck')
#         uniqueArgs.append(lsr)
#         uniqueArgs.append(beta)
#         uniqueArgs.append(r)
#         uniqueArgs.append(gamma)
#     if lsr:
#         uniqueArgs.append('-DMBuck')
#         uniqueArgs.append(lsr)
#     if Cf:
#         uniqueArgs.append('-CMFatigue')
#         uniqueArgs.append(Cf)
#         uniqueArgs.append(alpha)
#         uniqueArgs.append(Cd)
#     if a1=4.3:
#         uniqueArgs.append('-IsoHard')
#     if R1=0.333:
#         uniqueArgs.append('-MPCurveParams')
#     ops.uniaxialMaterial('ReinforcingSteel', matTag, fy, fu, Es, Esh, eps_sh, eps_ult, alpha, a1, limit, R1, R2, R3, *uniqueArgs)

# def Dodd_Restrepo(matTag, Fy, Fsu, ESH, ESU, Youngs, ESHI, FSHI, OmegaFac):
#     """


#    This command is used to construct a Dodd-Restrepo steel material



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``Fy`` |float|                        Yield strength

#    ``Fsu`` |float|                       Ultimate tensile strength (UTS)

#    ``ESH`` |float|                       Tensile strain at initiation of strain hardening

#    ``ESU`` |float|                       Tensile strain at the UTS

#    ``Youngs`` |float|                    Modulus of elasticity

#    ``ESHI`` |float|                      Tensile strain for a point on strain hardening

#                                          curve, recommended range of values for ESHI: [ (ESU + 5*ESH)/6, (ESU + 3*ESH)/4]

#    ``FSHI`` |float|                      Tensile stress at point on strain hardening curve corresponding to ESHI

#    ``OmegaFac`` |float|                  Roundedness factor for Bauschinger curve in cycle reversals from the strain hardening curve.

#                                          Range: [0.75, 1.15]. Largest value tends to near a bilinear Bauschinger curve. Default = 1.0.

#    ===================================   ===========================================================================







# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/DoddRestrepo>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('Dodd_Restrepo', matTag, Fy, Fsu, ESH, ESU, Youngs, ESHI, FSHI, OmegaFac, *uniqueArgs)

# def RambergOsgoodSteel(matTag, fy, E0, a, n):
#     """


#    This command is used to construct a Ramberg-Osgood steel material object.



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``fy`` |float|                        Yield strength

#    ``E0`` |float|                        initial elastic tangent

#    ``a`` |float|                         "yield offset" and the Commonly used value for a is 0.002

#    ``n`` |float|                         Parameters to control the transition from elastic

#                                          to plastic branches. And controls the hardening

#                                          of the material by increasing the "n" hardening ratio will be decreased.

#                                          Commonly used values for n are ~5 or greater.

#    ===================================   ===========================================================================







# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/RambergOsgoodSteel_Material>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('RambergOsgoodSteel', matTag, fy, E0, a, n, *uniqueArgs)


def SteelMPF(matTag, fyp, fyn, E0, bp, bn, params, a1, a2, a3, a4):
    """

    This command is used to construct a uniaxialMaterial SteelMPF 
    (Kolozvari et al., 2015), which represents the well-known uniaxial c
    onstitutive nonlinear hysteretic material model for steel proposed by 
    Menegotto and Pinto (1973), and extended by Filippou et al. (1983) to 
    include isotropic strain hardening effects.

    ===================================   ===========================================================================

    ``matTag`` |int|                      integer tag identifying material

    ``fyp`` |float|                       Yield strength in tension (positive loading direction)

    ``fyn`` |float|                       Yield strength in compression (negative loading direction)

    ``E0`` |float|                        Initial tangent modulus

    ``bp`` |float|                        Strain hardening ratio in tension (positive loading direction)

    ``bn`` |float|                        Strain hardening ratio in compression (negative loading direction)

    ``params`` |listf|                    parameters to control the transition from elastic to plastic branches.
                                          ``params=[R0,cR1,cR2]``.
                                          Recommended values: ``R0=20``, ``cR1=0.925``, ``cR2=0.15`` or ``cR2=0.0015``

    ``a1`` |float|                        Isotropic hardening in compression parameter (optional, default = 0.0). Shifts compression
                                          yield envelope by a proportion of compressive yield strength after a maximum plastic tensile
                                          strain of a2(fyp/E0)

    ``a2`` |float|                        Isotropic hardening in compression parameter (optional, default = 1.0).

    ``a3`` |float|                        Isotropic hardening in tension parameter (optional, default = 0.0). Shifts tension yield
                                          envelope by a proportion of tensile yield strength after a maximum plastic compressive
                                          strain of a3(fyn/E0).

    ``a4`` |float|                        Isotropic hardening in tension parameter (optional, default = 1.0). See explanation of a3.

    ===================================   ===========================================================================

    .. seealso::

        `Notes <http://opensees.berkeley.edu/wiki/index.php/SteelMPF_-_Menegotto_and_Pinto_(1973)_Model_Extended_by_Filippou_et_al._(1983)>`_

    Hints:
        Untested
    """
    uniqueArgs = []
    if a1:
        uniqueArgs.append(a1)
        uniqueArgs.append(a2)    
        uniqueArgs.append(a3)    
        uniqueArgs.append(a4)
    ops.uniaxialMaterial('SteelMPF', matTag, fyp, fyn, E0, bp, bn, *params *uniqueArgs)

# def Steel01Thermal(matTag, Fy, E0, b, a1, a2, a3, a4):
#     """


#    This command is the thermal version for ``'Steel01'``.



#    ================================   ===========================================================================

#    ``matTag`` |int|                   integer tag identifying material

#    ``Fy`` |float|                     yield strength

#    ``E0`` |float|                     initial elastic tangent

#    ``b`` |float|                      strain-hardening ratio (ratio between post-yield

#                                       tangent and initial elastic tangent)

#    ``a1`` |float|                     isotropic hardening parameter, increase of

#                                       compression yield envelope as proportion of yield

#                                       strength after a plastic strain of

#                                       :math:`a_2*(F_y/E_0)` (optional)

#    ``a2`` |float|                     isotropic hardening parameter

#                                       (see explanation under ``a1``). (optional).

#    ``a3`` |float|                     isotropic hardening parameter, increase of tension

#                                       yield envelope as proportion of yield strength

#                                       after a plastic strain

#                                       of :math:`a_4*(F_y/E_0)`. (optional)

#    ``a4`` |float|                     isotropic hardening parameter (see explanation

#                                       under ``a3``). (optional)

#    ================================   ===========================================================================



#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('Steel01Thermal', matTag, Fy, E0, b, a1, a2, a3, a4, *uniqueArgs)

def Concrete01(matTag, fpc, epsc0, fpcu, epsU):
    """

    This command is used to construct a uniaxial Kent-Scott-Park concrete 
    material object with degraded linear unloading/reloading stiffness 
    according to the work of Karsan-Jirsa and no tensile strength. 
    (REF: Fedeas).

    ===================================   ===========================================================================
    ``matTag`` |int|                      integer tag identifying material

    ``fpc`` |float|                       concrete compressive strength at 28 days (compression is negative)

    ``epsc0`` |float|                     concrete strain at maximum strength

    ``fpcu`` |float|                      concrete crushing strength

    ``epsU`` |float|                      concrete strain at crushing strength

    ===================================   ===========================================================================

    .. note::

    #. Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).
    
    #. The initial slope for this model is (2*fpc/epsc0)


    .. seealso::
    
    
        `Notes <http://opensees.berkeley.edu/wiki/index.php/Concrete01_Material_--_Zero_Tensile_Strength>`_

    Hints:
        Untested
    """
    ops.uniaxialMaterial('Concrete01', matTag, fpc, epsc0, fpcu, epsU)

def Concrete02(matTag, fpc, epsc0, fpcu, epsU, Lambda, ft, Ets):
    """
    This command is used to construct a uniaxial Kent-Scott-Park concrete 
    material object with degraded linear unloading/reloading stiffness 
    according to the work of Karsan-Jirsa and no tensile strength. (REF: Fedeas).

    ===================================   ===========================================================================
    ``matTag`` |int|                      integer tag identifying material

    ``fpc`` |float|                       concrete compressive strength at 28 days (compression is negative)

    ``epsc0`` |float|                     concrete strain at maximum strength

    ``fpcu`` |float|                      concrete crushing strength

    ``epsU`` |float|                      concrete strain at crushing strength

    ``lambda`` |float|                    ratio between unloading slope at $epscu and initial slope

    ``ft`` |float|                        tensile strength

    ``Ets`` |float|                       tension softening stiffness (absolute value) (slope of the linear tension softening branch)
    ===================================   ===========================================================================

    .. note::
    
    
        #. Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).
    
        #. The initial slope for this model is (2*fpc/epsc0)

    .. seealso::
    
   
        `Notes <http://opensees.berkeley.edu/wiki/index.php/Concrete02_Material_--_Linear_Tension_Softening>`_

    Hints:
        Untested
    """
    ops.uniaxialMaterial('Concrete02', matTag, fpc, epsc0, fpcu, epsU, Lambda, ft, Ets)

def Concrete04(matTag, fc, epsc, epscu, Ec, fct, et, beta):
    """

    This command is used to construct a uniaxial Popovics concrete material 
    object with degraded linear unloading/reloading stiffness according to the 
    work of Karsan-Jirsa and tensile strength with exponential decay.

    ===================================   ===========================================================================
    ``matTag`` |int|                      integer tag identifying material

    ``fc`` |float|                        floating point values defining concrete
                                          compressive strength at 28 days (compression is negative)

    ``epsc`` |float|                      floating point values defining concrete strain at maximum strength

    ``epscu`` |float|                     floating point values defining concrete strain at crushing strength

    ``Ec`` |float|                        floating point values defining initial stiffness

    ``fct`` |float|                       floating point value defining the maximum tensile strength of concrete (optional)

    ``et`` |float|                        floating point value defining ultimate tensile strain of concrete (optional)

    ``beta`` |float|                      loating point value defining the exponential curve parameter to define the residual
                                          stress (as a factor of ft) at etu
    ===================================   ===========================================================================


    .. note::
    
        #. Compressive concrete parameters should be input as negative values.
    
        #. The envelope of the compressive stress-strain response is defined using the model proposed by Popovics (1973). If the user defines :math:`Ec = 57000*sqrt(|fcc|)` (in psi)' then the envelope curve is identical to proposed by Mander et al. (1988).
    
        #. Model Characteristic: For loading in compression, the envelope to the stress-strain curve follows the model proposed by Popovics (1973) until the concrete crushing strength is achieved and also for strains beyond that corresponding to the crushing strength. For unloading and reloading in compression, the Karsan-Jirsa model (1969) is used to determine the slope of the curve. For tensile loading, an exponential curve is used to define the envelope to the stress-strain curve. For unloading and reloading in tensile, the secant stiffness is used to define the path.
    
    
    .. seealso::
    
        `Notes <http://opensees.berkeley.edu/wiki/index.php/Concrete04_Material_--_Popovics_Concrete_Material>`_

    Hints:
        Untested
    """
    ops.uniaxialMaterial('Concrete04', matTag, fc, epsc, epscu, Ec, fct, et, beta)

def Concrete06(matTag, fc, e0, n, k, alpha1, fcr, ecr, b, alpha2):
    """
    This command is used to construct a uniaxial concrete material object with 
    tensile strength, nonlinear tension stiffening and compressive behavior 
    based on Thorenfeldt curve.

    ===================================   ===========================================================================
    ``matTag`` |int|                      integer tag identifying material

    ``fc`` |float|                        concrete compressive strength (compression is negative)

    ``e0`` |float|                        strain  at compressive strength

    ``n`` |float|                         compressive shape factor

    ``k`` |float|                         post-peak compressive shape factor

    ``alpha1`` |float|                    :math:`\alpha_1` parameter for compressive plastic strain definition

    ``fcr`` |float|                       tensile strength

    ``ecr`` |float|                       tensile strain at peak stress (fcr)

    ``b`` |float|                         exponent of the tension stiffening curve

    ``alpha2`` |float|                    :math:`\alpha_2` parameter for tensile plastic strain definition
    ===================================   ===========================================================================

    .. note::
    
        #. Compressive concrete parameters should be input as negative values.
    
    .. seealso::
    
    
        `Notes <http://opensees.berkeley.edu/wiki/index.php/Concrete06_Material>`_

    Hints:
        Untested
    """
    ops.uniaxialMaterial('Concrete06', matTag, fc, e0, n, k, alpha1, fcr, ecr, b, alpha2)

def Concrete07(matTag, fc, epsc, Ec, ft, et, xp, xn, r):
    """

    Concrete07 is an implementation of Chang & Mander's 1994 concrete model 
    with simplified unloading and reloading curves. Additionally the tension 
    envelope shift with respect to the origin proposed by Chang and Mander has 
    been removed. The model requires eight input parameters to define the 
    monotonic envelope of confined and unconfined concrete in the following 
    form:

    ===================================   ===========================================================================

    ``matTag`` |int|                      integer tag identifying material

    ``fc`` |float|                        concrete compressive strength (compression is negative)

    ``epsc`` |float|                      concrete strain at maximum compressive strength

    ``Ec`` |float|                        Initial Elastic modulus of the concrete

    ``ft`` |float|                        tensile strength of concrete (tension is positive)

    ``et`` |float|                        tensile strain at max tensile strength of concrete

    ``xp`` |float|                        Non-dimensional term that defines the strain at
                                          which the straight line descent begins in tension

    ``xn`` |float|                        Non-dimensional term that defines the strain at
                                          which the straight line descent begins in compression

    ``r`` |float|                         Parameter that controls the nonlinear descending branch

    ===================================   ===========================================================================


.. seealso::

    `Notes <http://opensees.berkeley.edu/wiki/index.php/Concrete07_%E2%80%93_Chang_%26_Mander%E2%80%99s_1994_Concrete_Model>`_

    Hints:
        Untested
    """
    uniqueArgs = []
    ops.uniaxialMaterial('Concrete07', matTag, fc, epsc, Ec, ft, et, xp, xn, r, *uniqueArgs)

def Concrete01WithSITC(matTag, fpc, epsc0, fpcu, epsU, endStrainSITC):
    """
    This command is used to construct a modified uniaxial Kent-Scott-Park 
    concrete material object with degraded linear unloading/reloading stiffness
    according to the work of Karsan-Jirsa and no tensile strength. The 
    modification is to model the effect of Stuff In The Cracks (SITC).

    ===================================   ===========================================================================

    ``matTag`` |int|                      integer tag identifying material

    ``fpc`` |float|                       concrete compressive strength at 28 days (compression is negative)

    ``epsc0`` |float|                     concrete strain at maximum strength

    ``fpcu`` |float|                      concrete crushing strength

    ``epsU`` |float|                      concrete strain at crushing strength

    ``endStrainSITC`` |float|                     optional, default = 0.03

    ===================================   ===========================================================================

    .. note::
    
    
        #. Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).
    
        #. The initial slope for this model is (2*fpc/epsc0)
    
    .. seealso::
    
    
        `Notes <http://opensees.berkeley.edu/wiki/index.php/Concrete01_Material_With_Stuff_in_the_Cracks>`_

    Hints:
        Untested
    """
    uniqueArgs = []
    ops.uniaxialMaterial('Concrete01WithSITC', matTag, fpc, epsc0, fpcu, epsU, endStrainSITC, *uniqueArgs)

def ConfinedConcrete01(matTag, secType, fpc, Ec, epscu_type, epscu_val, nu, L1, L2, L3, phis, S, fyh, Es0, haRatio, 
                       mu, phiLon, internalArgs=None, wrapArgs=None, gravel = False, silica=False, tol=None, maxNumIter=None, epscuLimit=None, stRatio=None):
    """


    ===================================   ===========================================================================

    ``matTag`` |int|                      integer tag identifying material

    ``secType`` |str|                     tag for the transverse reinforcement configuration.
                                          see `img <https://openseespydoc.readthedocs.io/en/latest/_images/545px-SectionTypes.png>`_
                                          
                                          - ``'S1'`` square section with S1 type of transverse reinforcement with or without external FRP wrapping
                                          - ``'S2'`` square section with S2 type of transverse reinforcement with or without external FRP wrapping
                                          - ``'S3'`` square section with S3 type of transverse reinforcement with or without external FRP wrapping
                                          - ``'S4a'`` square section with S4a type of transverse reinforcement with or without external FRP wrapping
                                          - ``'S4b'`` square section with S4b type of transverse reinforcement with or without external FRP wrapping
                                          - ``'S5'`` square section with S5 type of transverse reinforcement with or without external FRP wrapping
                                          - ``'C'`` circular section with or without external FRP wrapping
                                          - ``'R'`` rectangular section with or without external FRP wrapping.

    ``fpc`` |float|                       unconfined cylindrical strength of concrete specimen.

    ``Ec`` |float|                        initial elastic modulus of unconfined concrete.

    ``epscu_type`` |str|                  Method to define confined concrete ultimate strain
                                          - ``-epscu`` then value is confined concrete ultimate strain,
                                          - ``-gamma`` then value is the ratio of the strength corresponding to ultimate
                                          strain to the peak strength of the confined concrete
                                          stress-strain curve. If ``gamma`` cannot be achieved
                                          in the range [0, epscuLimit] then epscuLimit
                                          (optional, default: 0.05) will be assumed as
                                          ultimate strain.

    ``epscu_val`` |float|                 Value for the definition of the concrete ultimate strain

    ``nu`` |str| or |list|                Definition for Poisson's Ratio.
                                          - ``['-nu', <value of Poisson's ratio>]``
                                          - ``'-varub'`` Poisson's ratio is defined as a function of axial
                                          strain by means of the expression proposed by Braga et al. (2006) with the
                                          upper bound equal to 0.5
                                          -``'-varnoub'`` Poisson's ratio is defined as a function of axial
                                          strain by means of the expression proposed by Braga
                                          et al. (2006) without any upper bound.

    ``L1`` |float|                        length/diameter of square/circular core section
                                          measured respect to the hoop center line.

    ``L2`` |float|                        additional dimensions when multiple hoops are being used.

    ``L3`` |float|                        additional dimensions when multiple hoops are being used.

    ``phis`` |float|                      hoop diameter. If section arrangement has multiple
                                          hoops it refers to the external hoop.

    ``S`` |float|                         hoop spacing.

    ``fyh`` |float|                       yielding strength of the hoop steel.

    ``Es0`` |float|                       elastic modulus of the hoop steel.

    ``haRatio`` |float|                   hardening ratio of the hoop steel.

    ``mu`` |float|                        ductility factor of the hoop steel.

    ``phiLon`` |float|                    diameter of longitudinal bars.

    ``internalArgs`` |listf|              ``internalArgs= [phisi, Si, fyhi, Es0i, haRatioi, mui]``
                                          optional parameters for defining the internal
                                          transverse reinforcement. If they are not specified
                                          they will be assumed equal to the external ones
                                          (for ``S2``, ``S3``, ``S4a``, ``S4b`` and ``S5`` typed).

    ``wrapArgs`` |listf|                  ``wrapArgs=[cover, Am, Sw, ful, Es0w]``
                                          optional parameters required when section is
                                          strengthened with FRP wraps.

                                          - ``cover`` cover thickness measured from the outer line of hoop.
                                          - ``Am`` total area of FRP wraps (number of layers x wrap thickness x wrap width).
                                          - ``Sw`` spacing of FRP wraps (if continuous wraps are used the spacing is equal to the wrap width).
                                          - ``ful`` ultimate strength of FRP wraps.
                                          - ``Es0w`` elastic modulus of FRP wraps.

    ``'-gravel'`` |str|                   Unknown

    ``'-silica'`` |str|                   Unknown

    ``tol``       |float|                 Unknown

    ``maxNumIter`` |int|                  Unknown

    ``epscuLimit`` |float|                Unknown

    ``stRatio``                           Unknown

    ===================================   ===========================================================================



.. seealso::


    `wiki <https://openseespydoc.readthedocs.io/en/latest/src/ConfinedConcrete01.html>`_
    
    `Notes <http://opensees.berkeley.edu/wiki/index.php/ConfinedConcrete01_Material>`_

    Hints:
        Untested
    """
    uniqueArgs = []
    if internalArgs:
        uniqueArgs.append('-internal')
        uniqueArgs.append(internalArgs)
    if wrapArgs:
        uniqueArgs.append('-wrap')
        uniqueArgs.append(wrapArgs)
    if gravel:
        uniqueArgs.append('-gravel')
    if silica:
        uniqueArgs.append('-silica')
    if tol:
        uniqueArgs.append('-tol')
        uniqueArgs.append(tol)
    if maxNumIter:
        uniqueArgs.append('-maxNumIter')
        uniqueArgs.append(maxNumIter)
    if epscuLimit:
        uniqueArgs.append('-epscuLimit')
        uniqueArgs.append(epscuLimit)
    if stRatio:
        uniqueArgs.append('-stRatio')
        uniqueArgs.append(stRatio)
    ops.uniaxialMaterial('ConfinedConcrete01', matTag, secType, fpc, Ec, epscu_type, epscu_val, nu, L1, L2, L3, phis, S, fyh, Es0, haRatio, mu, phiLon, *uniqueArgs)

def ConcreteD(matTag, fc, epsc, ft, epst, Ec, alphac, alphat, cesp, etap):
    """

    This command is used to construct a concrete material based on the Chinese design code.

    ===================================   ===========================================================================
    ``matTag`` |int|                      integer tag identifying material

    ``fc`` |float|                        concrete compressive strength

    ``epsc`` |float|                      concrete strain at corresponding to compressive strength

    ``ft`` |float|                        concrete tensile strength

    ``epst`` |float|                      concrete strain at corresponding to tensile strength

    ``Ec`` |float|                        concrete initial Elastic modulus

    ``alphac`` |float|                    compressive descending parameter

    ``alphat`` |float|                    tensile descending parameter

    ``cesp`` |float|                      plastic parameter, recommended values: 0.2~0.3

    ``etap`` |float|                      plastic parameter, recommended values: 1.0~1.3
    ===================================   ===========================================================================

.. note::

    #. Concrete compressive strength and the corresponding strain should be input as negative values.

    #. The value ``fc/epsc`` and ``ft/epst`` should be smaller than ``Ec``.

.. seealso::

    `Notes <http://opensees.berkeley.edu/wiki/index.php/ConcreteD>`_

    """
    ops.uniaxialMaterial('ConcreteD', matTag, fc, epsc, ft, epst, Ec, alphac, alphat, cesp, etap)

def FRPConfinedConcrete(matTag, fpc1, fpc2, epsc0, D, c, Ej, Sj, tj, eju, S, fyl, fyh, dlong, dtrans, Es, nu0, k, useBuck):
    """
    This command is used to construct a uniaxial Megalooikonomou-Monti-Santini concrete material object with degraded linear unloading/reloading stiffness according to the work of Karsan-Jirsa and no tensile strength.

    ===================================   ===========================================================================

    ``matTag`` |int|                      integer tag identifying material

    ``fpc1`` |float|                      concrete core compressive strength.

    ``fpc2`` |float|                      concrete cover compressive strength.

    ``epsc0`` |float|                     strain corresponding to unconfined concrete strength.

    ``D`` |float|                         diameter of the circular section.

    ``c`` |float|                         dimension of concrete cover (until the outer edge of steel stirrups)

    ``Ej`` |float|                        elastic modulus of the fiber reinforced polymer (FRP) jacket.

    ``Sj`` |float|                        clear spacing of the FRP strips - zero if FRP jacket is continuous.

    ``tj`` |float|                        total thickness of the FRP jacket.

    ``eju`` |float|                       rupture strain of the FRP jacket from tensile coupons.

    ``S`` |float|                         spacing of the steel spiral/stirrups.

    ``fyl`` |float|                       yielding strength of longitudinal steel bars.

    ``fyh`` |float|                       yielding strength of the steel spiral/stirrups.

    ``dlong`` |float|                     diameter of the longitudinal bars of the circular section.

    ``dtrans`` |float|                    diameter of the steel spiral/stirrups.

    ``Es`` |float|                        elastic modulus of steel.

    ``nu0`` |float|                       initial Poisson's coefficient for concrete.

    ``k`` |float|                         reduction factor for the rupture strain of the FRP
                                          jacket, recommended values 0.5-0.8.

    ``useBuck`` |float|                   FRP jacket failure criterion due to buckling of longitudinal compressive steel bars (0 = not                                            include it, 1= to include it).

    ===================================   ===========================================================================


    .. note::
    
        #.IMPORTANT: The units of the input parameters should be in MPa, N, mm.
    
        #.Concrete compressive strengths and the corresponding strain should be input as positive values.
    
        #.When rupture of FRP jacket occurs due to dilation of concrete (lateral concrete strain exceeding reduced rupture strain of FRP jacket), the analysis is not terminated. Only a message "FRP Rupture" is plotted on the screen.
    
        #.When $useBuck input parameter is on (equal to 1) and the model's longitudinal steel buckling conditions are fulfilled, a message "Initiation of Buckling of Long.Bar under Compression" is plotted on the screen.
    
        #.When rupture of FRP jacket occurs due to its interaction with buckled longitudinal compressive steel bars, the analysis is not terminated. Only a message "FRP Rupture due to Buckling of Long.Bar under compression" is plotted on the screen.
    
    .. seealso::
    
    
    
        `Notes <http://opensees.berkeley.edu/wiki/index.php/FRPConfinedConcrete>`_

    """
    ops.uniaxialMaterial('FRPConfinedConcrete', matTag, fpc1, fpc2, epsc0, D, c, Ej, Sj, tj, eju, S, fyl, fyh, dlong, dtrans, Es, nu0, k, useBuck)

# def FRPConfinedConcrete02(matTag, fc0, Ec, ec0, tfrp=None, Efrp=None, erup=None, R=None, fcu=None, ecu=None, ft, Ets, Unit):
#     """


#    Figure 1 Hysteretic Stress-Strain Relation



#    .. image:: /_static/FRPConfinedConcrete02/Figure1.png



#    This command is used to construct a uniaxial hysteretic stress-strain model for fiber-reinforced polymer (FRP)-confined concrete. The envelope compressive stress-strain response is described by a parabolic first portion and a linear second portion with smooth connection between them (Figure 1). The hysteretic rules of compression are based on Lam and Teng’s (2009) model. The cyclic linear tension model of Yassin (1994) for unconfined concrete (as adopted in Concrete02) is used with slight modifications to describe the tensile behavior of FRP-confined concrete (Teng et al. 2015).



#    ===================================   ==============================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``fc0`` |float|                       compressive strength of unconfined concrete (compression is negative)

#    ``Ec`` |float|                                     elastic modulus of unconfined concrete (=4730√(-$fc0(MPa)))

#    ``ec0`` |float|                       axial strain corresponding to unconfined concrete strength (≈ 0.002)

#    ``-JacketC`` |str|                    input parameters of the FRP jacket in a circular section

#    ``tfrp`` |float|                      thickness of an FRP jacket

#    ``Efrp`` |float|                      tensile elastic modulus of an FRP jacket

#    ``erup`` |float|                      hoop rupture strain of an FRP jacket

#    ``R`` |float|                         radius of circular column section

#    ``-Ultimate`` |str|                   input ultimate stress/strain directly

#    ``fcu`` |float|                       ultimate stress of FRP-confined concrete ($fcu ≥ $fc0)

#    ``ecu`` |float|                       ultimate strain of FRP-confined concrete

#    ``ft`` |float|                        tensile strength of unconfined concrete (=0.632√(-$fc0(MPa)))

#    ``Ets`` |float|                       stiffness of tensile softening (≈ 0.05 Ec)

#    ``Unit`` |float|                      unit indicator, Unit = 1 for SI Metric Units; Unit = 0 for US Customary Units

#    ===================================   ==============================================================================





# .. note::





#     #. Compressive concrete parameters should be input as negative values.

#     #. The users are required to input either the FRP jacket properties in an FRP-confined circular column (<-JacketC>) or directly input the ultimate point (εcu, fcu) (<-Ultimate>). If <-JacketC> is used, the ultimate stress and strain are automatically calculated based on Teng et al.’s (2009) model which is a refined version of Lam and Teng’s (2003) stress-strain model for FRP-confined concrete in circular columns. If <-Ultimate> is used, the ultimate stress and strain can be calculated by the users in advance based on other stress-strain models of FRP-confined concrete and thus can be used for other cross section shapes (e.g., square, rectangular, or elliptical). If none of them is specified, a stress-strain curve (parabola + horizontal linear curve) for unconfined concrete will be defined (Figure 1). Both <-JacketC> and <-Ultimate> adopt the envelope compressive stress-strain curve with a parabolic first portion and a linear second portion.

#     #. Unit indicator: $Unit = 1 for SI Metric Units (e.g., N, mm, MPa); $Unit = 0 for US Customary Units (e.g., kip, in, sec, ksi).



#     Calibration:



#     #. The implemented new material has been calibrated using a simple-supported Force-Based Beam-Column element subjected to axial load only (http://opensees.berkeley.edu/wiki/index.php/Calibration_of_Maxwell_Material). The output stress-strain responses were compared with the desired curves defined by the input parameters.



#     Examples:



#     #. Example 1: Pin-ended FRP-confined reinforced concrete (RC) columns



#         Figure 2 Simulation of pin-ended FRP-confined RC column



#         .. image:: /_static/FRPConfinedConcrete02/Figure2.png



#         #. The first example is a pin-ended FRP-confined circular RC column subjected to eccentric compression (load eccentricity = 20 mm) at both ends tested by Bisby and Ranger (2010) (Figure 2). Due to the symmetry in geometry and loading, only half of the column needs to be modelled. In this case, three forceBeamColumn elements each with 5 integration points were used for the half column. The FRPConfinedConcrete02 model was used to describe the stress-strain behavior of FRP-confined concrete. Either <-JacketC> or <-Ultimate> can be used. If the former is used, the properties of the FRP jacket need to be input; if the latter is used, the ultimate stress and strain need to be calculated by the users and input directly. The eccentric loading is applied with a combined axial load and bending moment at each end node. An increasing vertical displacement is applied to the top node of the column model. The analysis terminated until the ultimate axial strain of FRP-confined concrete was reached by the extreme compression concrete fiber at the mid-height (equivalent to FRP rupture). SI Metric Unit (e.g., N, mm, MPa) is used in the script of this example ($Unit = 1).



#         #. Figure 3 shows the comparison of axial load-lateral displacement curve between the test results and the theoretical results. Figure 4 shows the variation of column slenderness ratio (l/D) on the axial load-lateral displacement response of the column. Please refer to Lin (2016) for more details about the modeling.



#             Figure 3 Experimental results vs theoretical results



#             .. image:: /_static/FRPConfinedConcrete02/Figure3.png



#             Figure 4 Parametric study (effect of column slenderness ratio)



#             .. image:: /_static/FRPConfinedConcrete02/Figure4.png



#     #. Example 2: Cantilever column subjected to constant axial compression and cyclic lateral loading



#         Figure 5 Simulation of columns under cyclic latera loading



#         .. image:: /_static/FRPConfinedConcrete02/Figure5.png



#         #. The second example is a cantilever FRP-confined circular RC column subjected to constant axial compression and cyclic lateral loading (Column C5 tested by Saadatmanesh et al. 1997). The US Customary Units (e.g., kip, in, sec, ksi) were used in this example. The twenty-five (25)-in.-height region (potential plastic hinge region) above the footing of the column was wrapped with an FRP jacket; the remaining portion of the column with a height of 71 in. was conventional RC section without FRP jacketing. The column was modelled using two forceBeamColumn elements to cater for the variation of section characteristic along the column height. A zero length section element at the column-footing interface was used to simulate fixed-end rotations due to the strain penetration of longitudinal steel bars (Figure 5) (Lin et al. 2012). The bond-slip model of Zhao and Sritharan (2007) (Bond_SP01) was used to depict the bar stress-slip response. In addition, another zero length section element was used at the column-footing interface to consider the possible rotations of the footing (Teng et al. 2015). The rotation stiffness of the zero length section element was adjusted to achieve close matching between the test response and the predicted response during the initial stage of loading. This zero length section element was found to have little effect on the ultimate displacement of the column (Teng et al. 2015). Moreover, the inclination of axial load in the column test needs to be accounted for when comparing predicted results with test results (Teng et al. 2015). Figure 6 shows the comparison of lateral load-lateral displacement curve between the test results and the theoretical results.



#     References:



#     #. Bisby, L. and Ranger, M. (2010). “Axial-flexural interaction in circular FRP-confined reinforced concrete columns”, Construction and Building Materials, Vol. 24, No. 9, pp. 1672-1681.

#     #. Lam, L. and Teng, J.G. (2003). “Design-oriented stress-strain model for FRP-confined concrete”, Construction and Building Materials, Vol. 17, No. 6, pp. 471-489.

#     #. Lam, L. and Teng, J.G. (2009). “Stress-strain model for FRP-confined concrete under cyclic axial compression”, Engineering Structures, Vol. 31, No. 2, pp. 308-321.

#     #. Lin, G. (2016). Seismic Performance of FRP-confined RC Columns: Stress-Strain Models and Numerical Simulation, Ph.D. thesis, Department of Civil and Environmental Engineering, The Hong Kong Polytechnic University, Hong Kong, China.

#     #. Lin, G. and Teng, J.G. (2015). “Numerical simulation of cyclic/seismic lateral response of square RC columns confined with fibre-reinforced polymer jackets”, Proceedings, Second International Conference on Performance-based and Life-cycle Structural Engineering (PLSE 2015), pp. 481-489 (http://plse2015.org/cms/USB/pdf/full-paper_7408.pdf).

#     #. Lin, G., Teng, J.G. and Lam, L. (2012). “Numerical simulation of FRP-jacketed RC columns under cyclic loading: modeling of the strain penetration effect”, First International Conference on Performance-based and Life-cycle Structural Engineering (PLSE2012), December 5-7, Hong Kong, China.

#     #. Saadatmanesh, H., Ehsani, M. and Jin, L. (1997). “Seismic retrofitting of rectangular bridge columns with composite straps”, Earthquake Spectra, Vol. 13, No. 2, pp. 281-304.

#     #. Teng, J.G., Lam, L., Lin, G., Lu, J.Y. and Xiao, Q.G. (2015). “Numerical Simulation of FRP-Jacketed RC Columns Subjected to Cyclic and Seismic Loading”, Journal of Composites for Construction, ASCE, Vol. 20, No. 1, pp. 04015021.

#     #. Yassin, M.H.M. (1994). Nonlinear Analysis of Prestressed Concrete Structures under Monotonic and Cyclic Loads, Ph.D. thesis, University of California at Berkeley, California, USA.

#     #. Zhao, J. and Sritharan, S. (2007). “Modeling of strain penetration effects in fiber-based analysis of reinforced concrete structuresconcrete structures”, ACI Structural Journal, Vol. 104, No. 2, pp. 133-141.

#     """
#     uniqueArgs = []
#     if tfrp:
#         uniqueArgs.append('-JacketC')
#         uniqueArgs.append(tfrp)
#         uniqueArgs.append(Efrp)
#         uniqueArgs.append(erup)
#         uniqueArgs.append(R)
#     if fcu:
#         uniqueArgs.append('-Ultimate')
#         uniqueArgs.append(fcu)
#         uniqueArgs.append(ecu)
#     ops.uniaxialMaterial('FRPConfinedConcrete02', matTag, fc0, Ec, ec0, ft, Ets, Unit, *uniqueArgs)

# def ConcreteCM(matTag, fpcc, epcc, Ec, rc, xcrn, ft, et, rt, xcrp, mon, GapClose):
#     """


#    This command is used to construct a uniaxialMaterial ConcreteCM (Kolozvari et al., 2015), which is a uniaxial hysteretic constitutive model for concrete developed by Chang and Mander (1994).



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``fpcc`` |float|                      Compressive strength (:math:`f'_c`)

#    ``epcc`` |float|                      Strain at compressive strength (:math:`\epsilon'_c`)

#    ``Ec`` |float|                        Initial tangent modulus (:math:`E_c`)

#    ``rc`` |float|                        Shape parameter in Tsai's equation defined for compression (:math:`r_c`)

#    ``xcrn`` |float|                      Non-dimensional critical strain on compression

#                                          envelope (:math:`\epsilon^{-}_{cr}`, where the envelope

#                                          curve starts following a straight line)

#    ``ft`` |float|                        Tensile strength (:math:`f_t`)

#    ``et`` |float|                        Strain at tensile strength (:math:`\epsilon_t`)

#    ``rt`` |float|                        Shape parameter in Tsai's equation defined for tension (:math:`r_t`)

#    ``xcrp`` |float|                      Non-dimensional critical strain on tension envelope

#                                          (:math:`\epsilon^{+}_{cr}`, where the envelope curve

#                                          starts following a straight line - large value

#                                          [e.g., 10000] recommended when tension stiffening

#                                          is considered)

#    ``mon``                               optional, monotonic stress-strain relationship only:  mon=1 (invoked in FSAM only), mon=0 (no impact since monotonic)

#    ``'-GapClose'`` |str|                 optional, denote next parameter is ``GapClose``

#    ``GapClose`` |float|                  optional, GapClose = 0, less gradual gap closure (default);

#                                          GapClose = 1, more gradual gap closure

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/ConcreteCM_-_Complete_Concrete_Model_by_Chang_and_Mander_(1994)>`_

#     """
#     uniqueArgs = []
#     if GapClose=0:
#         uniqueArgs.append('-GapClose')
#     ops.uniaxialMaterial('ConcreteCM', matTag, fpcc, epcc, Ec, rc, xcrn, ft, et, rt, xcrp, mon, GapClose, *uniqueArgs)

# def TDConcrete(matTag, fc, fct, Ec, beta, tD, epsshu, psish, Tcr, phiu, psicr1, psicr2, tcast):
#     """


#    This command is used to construct a uniaxial time-dependent concrete material object with linear behavior in compression, nonlinear behavior in tension (REF: Tamai et al., 1988) and creep and shrinkage according to ACI 209R-92.



#    ===================================   ============================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``fc`` |float|                        concrete compressive strength (compression is negative)

#    ``fct`` |float|                       concrete tensile strength (tension is positive)

#    ``Ec`` |float|                        concrete modulus of elasticity

#    ``beta`` |float|                      tension softening parameter (tension softening exponent)

#    ``tD`` |float|                         analysis time at initiation of drying (in days)

#    ``epsshu`` |float|                    ultimate shrinkage strain as per ACI 209R-92 (shrinkage is negative)

#    ``psish`` |float|                     fitting parameter of the shrinkage time evolution function as per ACI 209R-92

#    ``Tcr`` |float|                       creep model age (in days)

#    ``phiu`` |float|                      ultimate creep coefficient as per ACI 209R-92

#    ``psicr1`` |float|                    fitting parameter of the creep time evolution function as per ACI 209R-92

#    ``psicr2`` |float|                    fitting parameter of the creep time evolution function as per ACI 209R-92

#    ``tcast`` |float|                     analysis time corresponding to concrete casting (in days; minimum value 2.0)

#    ===================================   ============================================================================



# .. note::



#    #. Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).

#    #. Shrinkage concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).





# .. seealso::





#    `Detailed descriptions of the model and its implementation can be found in the following:`

#    `(1) Knaack, A.M., Kurama, Y.C. 2018. Modeling Time-Dependent Deformations: Application for Reinforced Concrete Beams with Recycled Concrete Aggregates. ACI Structural J. 115, 175-190. doi:10.14359/51701153`

#    `(2) Knaack, A.M., 2013. Sustainable concrete structures using recycled concrete aggregate: short-term and long-term behavior considering material variability. PhD Dissertation, Civil and Environmental Engineering and Earth Sciences, University of Notre Dame, Notre Dame, Indiana, USA, 680 pp`

#    `A manual describing the use of the model and sample files can be found at:`  

#    `<https://data.mendeley.com/datasets/z4gxnhchky/1>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('TDConcrete', matTag, fc, fct, Ec, beta, tD, epsshu, psish, Tcr, phiu, psicr1, psicr2, tcast, *uniqueArgs)

# def TDConcreteEXP(matTag, fc, fct, Ec, beta, tD, epsshu, psish, Tcr, epscru, sigCr, psicr1, psicr2, tcast):
#     """


#    This command is used to construct a uniaxial time-dependent concrete material object with linear behavior in compression, nonlinear behavior in tension (REF: Tamai et al., 1988) and creep and shrinkage according to ACI 209R-92.



#    ===================================   =====================================================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``fc`` |float|                        concrete compressive strength (compression is negative)

#    ``fct`` |float|                       concrete tensile strength (tension is positive)

#    ``Ec`` |float|                        concrete modulus of elasticity

#    ``beta`` |float|                      tension softening parameter (tension softening exponent)

#    ``tD`` |float|                                                 analysis time at initiation of drying (in days)

#    ``epsshu`` |float|                    ultimate shrinkage strain as per ACI 209R-92 (shrinkage is negative)

#    ``psish`` |float|                     fitting parameter of the shrinkage time evolution function as per ACI 209R-92

#    ``Tcr`` |float|                       creep model age (in days)

#    ``epscru`` |float|                    ultimate creep strain (e.g., taken from experimental measurements)

#    ``sigCr`` |float|                     concrete compressive stress (input as negative) associated with $epscru (e.g., experimentally applied)

#    ``psicr1`` |float|                    fitting parameter of the creep time evolution function as per ACI 209R-92

#    ``psicr2`` |float|                    fitting parameter of the creep time evolution function as per ACI 209R-92

#    ``tcast`` |float|                     analysis time corresponding to concrete casting (in days; minimum value 2.0)

#    ===================================   =====================================================================================================



# .. note::



#    #. Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).

#    #. Shrinkage concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).





# .. seealso::





#    `Detailed descriptions of the model and its implementation can be found in the following:`

#    `(1) Knaack, A.M., Kurama, Y.C. 2018. Modeling Time-Dependent Deformations: Application for Reinforced Concrete Beams with Recycled Concrete Aggregates. ACI Structural J. 115, 175-190. doi:10.14359/51701153`

#    `(2) Knaack, A.M., 2013. Sustainable concrete structures using recycled concrete aggregate: short-term and long-term behavior considering material variability. PhD Dissertation, Civil and Environmental Engineering and Earth Sciences, University of Notre Dame, Notre Dame, Indiana, USA, 680 pp`

#    `A manual describing the use of the model and sample files can be found at:`  

#    `<https://data.mendeley.com/datasets/z4gxnhchky/1>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('TDConcreteEXP', matTag, fc, fct, Ec, beta, tD, epsshu, psish, Tcr, epscru, sigCr, psicr1, psicr2, tcast, *uniqueArgs)

# def TDConcreteMC10(matTag, fc, fct, Ec, Ecm, beta, tD, epsba, epsbb, epsda, epsdb, phiba, phibb, phida, phidb, tcast, cem):
#     """


#    This command is used to construct a uniaxial time-dependent concrete material object with linear behavior in compression, nonlinear behavior in tension (REF: Tamai et al., 1988) and creep and shrinkage according to fib Model Code 2010.



#    ===================================   =============================================================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``fc`` |float|                        concrete compressive strength (compression is negative)

#    ``fct`` |float|                       concrete tensile strength (tension is positive)

#    ``Ec`` |float|                        concrete modulus of elasticity at loading age

#    ``Ecm`` |float|                       concrete modulus of elasticity at 28 days

#    ``beta`` |float|                      tension softening parameter (tension softening exponent)

#    ``tD`` |float|                         analysis time at initiation of drying (in days)

#    ``epsba`` |float|                     ultimate basic shrinkage strain (input as negative) as per fib Model Code 2010

#    ``epsbb`` |float|                     fitting parameter of the basic shrinkage time evolution function as per fib Model Code 2010

#    ``epsda`` |float|                     product of ultimate drying shrinkage strain and relative humidity function as per fib Model Code 2010

#    ``epsdb`` |float|                     fitting parameter of the basic shrinkage time evolution function as per fib Model Code 2010

#    ``phiba`` |float|                     parameter for the effect of compressive strength on basic creep as per fib Model Code 2010

#    ``phibb`` |float|                     fitting parameter of the basic creep time evolution function as per fib Model Code 2010

#    ``phida`` |float|                     product of the effect of compressive strength and relative humidity on drying creep as per fib Model Code 2010

#    ``phidb`` |float|                     fitting parameter of the drying creep time evolution function as per fib Model Code 2010

#    ``tcast`` |float|                     analysis time corresponding to concrete casting (in days; minimum value 2.0)

#    ``cem`` |float|                       coefficient dependent on the type of cement as per fib Model Code 2010

#    ===================================   =============================================================================================================



# .. note::



#    #. Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).

#    #. Shrinkage concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).





# .. seealso::





#    `Detailed descriptions of the model and its implementation can be found in the following:`

#    `(1) Knaack, A.M., Kurama, Y.C. 2018. Modeling Time-Dependent Deformations: Application for Reinforced Concrete Beams with Recycled Concrete Aggregates. ACI Structural J. 115, 175-190. doi:10.14359/51701153`

#    `(2) Knaack, A.M., 2013. Sustainable concrete structures using recycled concrete aggregate: short-term and long-term behavior considering material variability. PhD Dissertation, Civil and Environmental Engineering and Earth Sciences, University of Notre Dame, Notre Dame, Indiana, USA, 680 pp`

#    `A manual describing the use of the model and sample files can be found at:`  

#    `<https://data.mendeley.com/datasets/z4gxnhchky/1>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('TDConcreteMC10', matTag, fc, fct, Ec, Ecm, beta, tD, epsba, epsbb, epsda, epsdb, phiba, phibb, phida, phidb, tcast, cem, *uniqueArgs)

# def TDConcreteMC10NL(matTag, fc, fcu, epscu, fct, Ec, Ecm, beta, tD, epsba, epsbb, epsda, epsdb, phiba, phibb, phida, phidb, tcast, cem):
#     """


#    This command is used to construct a uniaxial time-dependent concrete material object with non-linear behavior in compression (REF: Concrete02), nonlinear behavior in tension (REF: Tamai et al., 1988) and creep and shrinkage according to fib Model Code 2010.



#    ===================================   =============================================================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``fc`` |float|                        concrete compressive strength (compression is negative)

#    ``fcu`` |float|                       concrete crushing strength (compression is negative)

#    ``epscu`` |float|                     concrete strain at crushing strength (input as negative)

#    ``fct`` |float|                       concrete tensile strength (tension is positive)

#    ``Ec`` |float|                        concrete modulus of elasticity at loading age

#    ``Ecm`` |float|                       concrete modulus of elasticity at 28 days

#    ``beta`` |float|                      tension softening parameter (tension softening exponent)

#    ``tD`` |float|                         analysis time at initiation of drying (in days)

#    ``epsba`` |float|                     ultimate basic shrinkage strain (input as negative) as per fib Model Code 2010

#    ``epsbb`` |float|                     fitting parameter of the basic shrinkage time evolution function as per fib Model Code 2010

#    ``epsda`` |float|                     product of ultimate drying shrinkage strain and relative humidity function as per fib Model Code 2010

#    ``epsdb`` |float|                     fitting parameter of the basic shrinkage time evolution function as per fib Model Code 2010

#    ``phiba`` |float|                     parameter for the effect of compressive strength on basic creep as per fib Model Code 2010

#    ``phibb`` |float|                     fitting parameter of the basic creep time evolution function as per fib Model Code 2010

#    ``phida`` |float|                     product of the effect of compressive strength and relative humidity on drying creep as per fib Model Code 2010

#    ``phidb`` |float|                     fitting parameter of the drying creep time evolution function as per fib Model Code 2010

#    ``tcast`` |float|                     analysis time corresponding to concrete casting (in days; minimum value 2.0)

#    ``cem`` |float|                       coefficient dependent on the type of cement as per fib Model Code 2010

#    ===================================   =============================================================================================================



# .. note::



#    #. Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).

#    #. Shrinkage concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).





# .. seealso::





#    `Detailed descriptions of the model and its implementation can be found in the following:`

#    `(1) Knaack, A.M., Kurama, Y.C. 2018. Modeling Time-Dependent Deformations: Application for Reinforced Concrete Beams with Recycled Concrete Aggregates. ACI Structural J. 115, 175-190. doi:10.14359/51701153`

#    `(2) Knaack, A.M., 2013. Sustainable concrete structures using recycled concrete aggregate: short-term and long-term behavior considering material variability. PhD Dissertation, Civil and Environmental Engineering and Earth Sciences, University of Notre Dame, Notre Dame, Indiana, USA, 680 pp`

#    `A manual describing the use of the model and sample files can be found at:`  

#    `<https://data.mendeley.com/datasets/z4gxnhchky/1>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('TDConcreteMC10NL', matTag, fc, fcu, epscu, fct, Ec, Ecm, beta, tD, epsba, epsbb, epsda, epsdb, phiba, phibb, phida, phidb, tcast, cem, *uniqueArgs)

def Elastic(matTag, E, eta=None, Eneg=None):
    """

    This command is used to construct an elastic uniaxial material object.

    ===================================   ===========================================================================
    ``matTag`` |int|                      integer tag identifying material

    ``E`` |float|                         tangent

    ``eta`` |float|                       damping tangent (optional, default=0.0)

    ``Eneg`` |float|                      tangent in compression (optional, default=E)
    ===================================   ===========================================================================

    .. seealso::
    
        `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastic_Uniaxial_Material>`_

    Hints:
        untested

    """
    uniqueArgs = []
    if eta:
        uniqueArgs.append(eta)
    if Eneg:
        uniqueArgs.append(Eneg)    
    ops.uniaxialMaterial('Elastic', matTag, E, *uniqueArgs)

def ElasticPP(matTag, E, epsyP, epsyN, eps0):
    """


    This command is used to construct an elastic perfectly-plastic uniaxial material object.

    ===================================   ===========================================================================
    ``matTag`` |int|                      integer tag identifying material

    ``E`` |float|                         tangent

    ``epsyP`` |float|                     strain or deformation at which material reaches plastic state in tension

    ``epsyN`` |float|                     strain or deformation at which material
                                          reaches plastic state in compression.
                                          (optional, default is tension value)

    ``eps0`` |float|                      initial strain (optional, default: zero)
    ===================================   ===========================================================================


    .. seealso::
    
        `Wiki <https://openseespydoc.readthedocs.io/en/latest/src/ElasticPP.html>`_
        
        `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastic-Perfectly_Plastic_Material>`_

    Hints:
        untested

    """
    uniqueArgs = []
    if epsyN:
        uniqueArgs.append(epsyN)
    if eps0:
        uniqueArgs.append(eps0)    
    ops.uniaxialMaterial('ElasticPP', matTag, E, epsyP, *uniqueArgs)

def ElasticPPGap(matTag, E, Fy, gap, eta, damage):
    """

    This command is used to construct an elastic perfectly-plastic gap uniaxial material object.

    ===================================   ===========================================================================

    ``matTag`` |int|                      integer tag identifying material

    ``E`` |float|                         tangent

    ``Fy`` |float|                        stress or force at which material reaches plastic state

    ``gap`` |float|                       initial gap (strain or deformation)

    ``eta`` |float|                       hardening ratio (=Eh/E), which can be negative

    ``damage`` |str|                      an optional string to specify whether to accumulate
                                          damage or not in the material. With the default
                                          string, ``'noDamage'`` the gap material will
                                          re-center on load reversal.
                                          If the string ``'damage'``
                                          is provided this recentering will not occur and gap
                                          will grow.

    ===================================   ===========================================================================

    .. seealso::


    `Wiki <https://openseespydoc.readthedocs.io/en/latest/src/ElasticPPGap.html>`_
    
    `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastic-Perfectly_Plastic_Gap_Material>`_

    Hints:
        untested

    """
    ops.uniaxialMaterial('ElasticPPGap', matTag, E, Fy, gap, eta, damage)

def ENT(matTag, E):
    """
    This command is used to construct a uniaxial elastic-no tension material object.

    ===================================   ===========================================================================

    ``matTag`` |int|                      integer tag identifying material

    ``E`` |float|                         tangent

    ===================================   ===========================================================================

    .. seealso::
    
        `Notes <https://openseespydoc.readthedocs.io/en/latest/src/ENT.html>`_

        `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastic-No_Tension_Material>`_

    Hints:
        untested

    """
    uniqueArgs = []
    ops.uniaxialMaterial('ENT', matTag, E, *uniqueArgs)

def Parallel(matTag, MatTags, factorArgs=None):
    """
    This command is used to construct a parallel material object made up of an arbitrary number of previously-constructed UniaxialMaterial objects.

    ===================================   ===========================================================================

    ``matTag`` |int|                      integer tag identifying material

    ``MatTags`` |listi|                   identification tags of materials making up the material model

    ``factorArgs`` |listf|                factors to create a linear combination of the
                                          specified materials. Factors can be negative to
                                          subtract one material from an other. (optional, default = 1.0)

    ===================================   ===========================================================================

    .. seealso::
    
        `Wiki <https://openseespydoc.readthedocs.io/en/latest/src/ParallelUni.html>`_
        
        `Notes <http://opensees.berkeley.edu/wiki/index.php/Parallel_Material>`_
    Hints:
        untested

    """
    uniqueArgs = []
    if factorArgs:
        uniqueArgs.append('-factors')
        uniqueArgs.append(factorArgs)
    ops.uniaxialMaterial('Parallel', matTag, *MatTags, *uniqueArgs)

def Series(matTag, matTags):
    """

    This command is used to construct a series material object made up of an 
    arbitrary number of previously-constructed UniaxialMaterial objects.

    ===================================   ===========================================================================
    ``matTag`` |int|                      integer tag identifying material

    ``matTags`` |listi|                   identification tags of materials making up the material model
    ===================================   ===========================================================================

    .. seealso::
    
        `Wiki <https://openseespydoc.readthedocs.io/en/latest/src/SeriesUni.html>`_
        
        `Notes <http://opensees.berkeley.edu/wiki/index.php/Series_Material>`_

    Hints:
        untested

    """
    uniqueArgs = []
    ops.uniaxialMaterial('Series', matTag, *matTags, *uniqueArgs)

def PySimple1(matTag, soilType, pult, Y50, Cd, c=0.0):
    """
    This command is used to construct a PySimple1 uniaxial material object.

    ===================================   ===========================================================================
    ``matTag`` |int|                      integer tag identifying material

    ``soilType`` |int|                    soilType = 1 Backbone of p-y curve approximates Matlock (1970) soft clay relation.

                                          soilType = 2 Backbone of p-y curve approximates API (1993) sand relation.

    ``pult`` |float|                      Ultimate capacity of the p-y material. Note that "p" or "pult" are distributed loads [force per length of pile] in common design equations, but are both loads for this uniaxialMaterial [i.e., distributed load times the tributary length of the pile].

    ``Y50`` |float|                       Displacement at which 50% of pult is mobilized in monotonic loading.

    ``Cd`` |float|                        Variable that sets the drag resistance within a fully-mobilized gap as Cd*pult.

    ``c`` |float|                         The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity). (optional Default = 0.0). Nonzero c values are used to represent radiation damping effects

    ===================================   ===========================================================================


    .. seealso::
    
        
        `Wiki <https://openseespydoc.readthedocs.io/en/latest/src/PySimple1.html>`_
        
        `Notes <http://opensees.berkeley.edu/wiki/index.php/PySimple1_Material>`_

    Hints:
        untested

    """
    ops.uniaxialMaterial('PySimple1', matTag, soilType, pult, Y50, Cd, c)

def TzSimple1(matTag, soilType, tult, z50, c=0.0):
    """

    This command is used to construct a TzSimple1 uniaxial material object.

    ===================================   ===========================================================================

    ``matTag`` |int|                      integer tag identifying material

    ``soilType`` |int|                    soilType = 1 Backbone of t-z curve approximates Reese and O'Neill (1987).
                                          soilType = 2 Backbone of t-z curve approximates Mosher (1984) relation.

    ``tult`` |float|                      Ultimate capacity of the t-z material. SEE NOTE 1.

    ``z50`` |float|                       Displacement at which 50% of tult is mobilized in monotonic loading.

    ``c`` |float|                         The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity). (optional Default = 0.0). See NOTE 2.

    ===================================   ===========================================================================

    .. note::
    
        #. The argument tult is the ultimate capacity of the t-z material. Note that "t" or "tult" are shear stresses [force per unit area of pile surface] in common design equations, but are both loads for this uniaxialMaterial [i.e., shear stress times the tributary area of the pile].
    
        #. Nonzero c values are used to represent radiation damping effects
    
    .. seealso::
    
        `Wiki <https://openseespydoc.readthedocs.io/en/latest/src/TzSimple1.html>`_
    
        `Notes <http://opensees.berkeley.edu/wiki/index.php/TzSimple1_Material>`_

    """
    uniqueArgs = []
    ops.uniaxialMaterial('TzSimple1', matTag, soilType, tult, z50, c, *uniqueArgs)

def QzSimple1(matTag, qzType, qult, Z50, suction=0.0, c=0.0):
    """
    This command is used to construct a QzSimple1 uniaxial material object.

    ===================================   ===========================================================================

    ``matTag`` |int|                      integer tag identifying material

    ``qzType`` |int|                      qzType = 1 Backbone of q-z curve approximates Reese and O'Neill's (1987) relation for drilled shafts in clay.



                                          qzType = 2 Backbone of q-z curve approximates Vijayvergiya's (1977) relation for piles in sand.

    ``qult`` |float|                      Ultimate capacity of the q-z material. SEE NOTE 1.

    ``Z50`` |float|                       Displacement at which 50% of qult is mobilized in monotonic loading. SEE NOTE 2.

    ``suction`` |float|                   Uplift resistance is equal to suction*qult. Default = 0.0. The value of suction must be 0.0 to 0.1.*

    ``c`` |float|                         The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity). Default = 0.0. Nonzero c values are used to represent radiation damping effects.*
    ===================================   ===========================================================================


    .. note::
    
        #. ``qult``: Ultimate capacity of the q-z material. Note that ``q1`` or ``qult`` are stresses [force per unit area of pile tip] in common design equations, but are both loads for this uniaxialMaterial [i.e., stress times tip area].
    
        #. ``Y50``: Displacement at which 50% of pult is mobilized in monotonic loading. Note that Vijayvergiya's relation (qzType=2) refers to a "critical" displacement (zcrit) at which qult is fully mobilized, and that the corresponding z50 would be 0. 125zcrit.
    
        #. optional args    ``suction`` and    ``c`` must either both be omitted or both provided.


    .. seealso::
    
    
        `Notes <http://opensees.berkeley.edu/wiki/index.php/QzSimple1_Material>`_

    Hints:
        untested

    """
    ops.uniaxialMaterial('QzSimple1', matTag, qzType, qult, Z50, suction, c)

def PyLiq1(matTag, soilType, pult, Y50, Cd, c, pRes, ele1=None, ele2=None, timeSeriesTag=None):

    """
    This command constructs a uniaxial p-y material that incorporates 
    liquefaction effects. This p y material is used with a zeroLength element 
    to connect a pile (beam-column element) to a 2 D plane-strain FE mesh or 
    displacement boundary condition. The p-y material obtains the average mean 
    effective stress (which decreases with increasing excess pore pressure) 
    either from two specified soil elements, or from a time series. Currently, 
    the implementation requires that the specified soil elements consist of 
    FluidSolidPorousMaterials in FourNodeQuad elements, or 
    PressureDependMultiYield or PressureDependMultiYield02 materials in 
    FourNodeQuadUP or NineFourQuadUP elements. There are two possible forms:

    ===================================   ===========================================================================

    ``matTag`` |int|                      integer tag identifying material

    ``soilType`` |int|                    soilType = 1 Backbone of p-y curve approximates Matlock (1970) soft clay relation.

                                          soilType = 2 Backbone of p-y curve approximates API (1993) sand relation.

    ``pult`` |float|                      Ultimate capacity of the p-y material. Note that "p" or "pult" are distributed loads [force per length of pile] in common design equations, but are both loads for this uniaxialMaterial [i.e., distributed load times the tributary length of the pile].

    ``Y50`` |float|                       Displacement at which 50% of pult is mobilized in monotonic loading.

    ``Cd`` |float|                        Variable that sets the drag resistance within a fully-mobilized gap as Cd*pult.

    ``c`` |float|                         The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity). (optional Default = 0.0). Nonzero c values are used to represent radiation damping effects

    ``pRes`` |float|                      sets the minimum (or residual) peak resistance that the material retains as the adjacent solid soil elements liquefy

    ``ele1``    ``ele2`` |float|          are the eleTag (element numbers) for the two solid elements from which PyLiq1 will obtain mean effective stresses and excess pore pressures. If the elements are specified, timeseries can not be specified.

    ``timeSeriesTag`` |float|             Alternatively, mean effective stress can be supplied by a time series by specifying the text string ``'-timeSeries'`` and the tag of the series    ``seriesTag``. If the timeseries are specified, elements can not be specified.

    ===================================   ===========================================================================

    .. seealso::
        
        `Notes <http://opensees.berkeley.edu/wiki/index.php/PyLiq1_Material>`_
        
    Hints:
        untested

    """
    
    uniqueArgs = []
    if timeSeriesTag:
        uniqueArgs.append(ele1)    
        uniqueArgs.append(ele2)    
    if timeSeriesTag:
        uniqueArgs.append('-timeSeries')
        uniqueArgs.append(timeSeriesTag)
    ops.uniaxialMaterial('PyLiq1', matTag, soilType, pult, Y50, Cd, c, pRes, *uniqueArgs)

# def TzLiq1(matTag, tzType, tult, z50, c, timeSeriesTag=None):


#    The command constructs a uniaxial t-z material that incorporates liquefaction effects. This t z material is used with a zeroLength element to connect a pile (beam-column element) to a 2 D plane-strain FE mesh. The t-z material obtains the average mean effective stress (which decreases with increasing excess pore pressure) from two specified soil elements. Currently, the implementation requires that the specified soil elements consist of FluidSolidPorousMaterials in FourNodeQuad elements.



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``tzType`` |int|                      tzType = 1 Backbone of t-z curve approximates Reese and O'Neill (1987).

#                                          tzType = 2 Backbone of t-z curve approximates Mosher (1984) relation.

#    ``tult`` |float|                      Ultimate capacity of the t-z material. SEE NOTE 1.

#    ``z50`` |float|                       Displacement at which 50% of tult is mobilized in monotonic loading.

#    ``c`` |float|                         The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity).

#    ``ele1``    ``ele2`` |float|          are the eleTag (element numbers) for the two solid elements from which PyLiq1 will obtain mean effective stresses and excess pore pressures

#    ``timeSeriesTag`` |float|             Alternatively, mean effective stress can be supplied by a time series by specifying the text string ``'-timeSeries'`` and the tag of the seriesm    ``seriesTag``.

#    ===================================   ===========================================================================



# .. note::



#    #. The argument ``tult`` is the ultimate capacity of the t-z material. Note that "t" or "tult" are shear stresses [force per unit area of pile surface] in common design equations, but are both loads for this uniaxialMaterial [i.e., shear stress times the tributary area of the pile].

#    #. Nonzero c values are used to represent radiation damping effects



#    #. To model the effects of liquefaction with ``TzLiq1``, it is necessary to use the material stage updating command:



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/TzLiq1_Material>`_

#     uniqueArgs = []
#     if timeSeriesTag:
#         uniqueArgs.append('-timeSeries')
#         uniqueArgs.append(timeSeriesTag)
#     ops.uniaxialMaterial('TzLiq1', matTag, tzType, tult, z50, c, *uniqueArgs)

# def TzLiq1(matTag, tzType, tult, z50, c, timeSeriesTag=None):


#    The command constructs a uniaxial t-z material that incorporates liquefaction effects. This t z material is used with a zeroLength element to connect a pile (beam-column element) to a 2 D plane-strain FE mesh. The t-z material obtains the average mean effective stress (which decreases with increasing excess pore pressure) from two specified soil elements. Currently, the implementation requires that the specified soil elements consist of FluidSolidPorousMaterials in FourNodeQuad elements.



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``tzType`` |int|                      tzType = 1 Backbone of t-z curve approximates Reese and O'Neill (1987).

#                                          tzType = 2 Backbone of t-z curve approximates Mosher (1984) relation.

#    ``tult`` |float|                      Ultimate capacity of the t-z material. SEE NOTE 1.

#    ``z50`` |float|                       Displacement at which 50% of tult is mobilized in monotonic loading.

#    ``c`` |float|                         The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity).

#    ``ele1``    ``ele2`` |float|          are the eleTag (element numbers) for the two solid elements from which PyLiq1 will obtain mean effective stresses and excess pore pressures

#    ``timeSeriesTag`` |float|             Alternatively, mean effective stress can be supplied by a time series by specifying the text string ``'-timeSeries'`` and the tag of the seriesm    ``seriesTag``.

#    ===================================   ===========================================================================



# .. note::



#    #. The argument ``tult`` is the ultimate capacity of the t-z material. Note that "t" or "tult" are shear stresses [force per unit area of pile surface] in common design equations, but are both loads for this uniaxialMaterial [i.e., shear stress times the tributary area of the pile].

#    #. Nonzero c values are used to represent radiation damping effects



#    #. To model the effects of liquefaction with ``TzLiq1``, it is necessary to use the material stage updating command:



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/TzLiq1_Material>`_

#     uniqueArgs = []
#     if timeSeriesTag:
#         uniqueArgs.append('-timeSeries')
#         uniqueArgs.append(timeSeriesTag)
#     ops.uniaxialMaterial('TzLiq1', matTag, tzType, tult, z50, c, *uniqueArgs)

# def Hardening(matTag, E, sigmaY, H_iso, H_kin, eta):
#     """


#    This command is used to construct a uniaxial material object with combined linear kinematic and isotropic hardening. The model includes optional visco-plasticity using a Perzyna formulation.







#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``E`` |float|                         tangent stiffness

#    ``sigmaY`` |float|                    yield stress or force

#    ``H_iso`` |float|                     isotropic hardening Modulus

#    ``H_kin`` |float|                     kinematic hardening Modulus

#    ``eta`` |float|                       visco-plastic coefficient (optional, default=0.0)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Hardening_Material>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('Hardening', matTag, E, sigmaY, H_iso, H_kin, eta, *uniqueArgs)

# def Cast(matTag, n, bo, h, fy, E, L, b, Ro, cR1, cR2, a1, a2, a3, a4):
#     """


#    This command is used to construct a parallel material object made up of an arbitrary number of previously-constructed UniaxialMaterial objects.



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``n`` |int|                           Number of yield fingers of the CSF-brace

#    ``bo`` |float|                        Width of an individual yielding finger at its base of the CSF-brace

#    ``h`` |float|                         Thickness of an individual yielding finger

#    ``fy`` |float|                        Yield strength of the steel material of the yielding finger

#    ``E`` |float|                         Modulus of elasticity of the steel material of the yielding finger

#    ``L`` |float|                         Height of an individual yielding finger

#    ``b`` |float|                         Strain hardening ratio

#    ``Ro`` |float|                        Parameter that controls the Bauschinger effect.

#                                          Recommended Values for $Ro=between 10 to 30

#    ``cR1`` |float|                       Parameter that controls the Bauschinger effect.

#                                          Recommended Value cR1=0.925

#    ``cR2`` |float|                       Parameter that controls the Bauschinger effect.

#                                          Recommended Value cR2=0.150

#    ``a1`` |float|                        isotropic hardening parameter, increase of

#                                          compression yield envelope as proportion of yield

#                                          strength after a plastic deformation of a2*(Pp/Kp)

#    ``a2`` |float|                        isotropic hardening parameter (see explanation

#                                          under a1). (optional default = 1.0)

#    ``a3`` |float|                        isotropic hardening parameter, increase of tension

#                                          yield envelope as proportion of yield strength

#                                          after a plastic deformation of a4*(Pp/Kp)

#    ``a4`` |float|                        isotropic hardening parameter (see explanation

#                                          under a3). (optional default = 1.0)

#    ===================================   ===========================================================================





# Gray et al. [1] showed that the monotonic backbone curve of a CSF-brace with known properties (``n``, ``bo``, ``h``, ``L``, ``fy``, ``E``) after yielding can be expressed as a close-form solution that is given by,

# :math:`P = P_p/\cos(2d/L)`, in which :math:`d` is the axial deformation of the brace at increment :math:`i` and :math:`P_p` is the yield strength of the CSF-brace and is given by the following expression



# :math:`P_p = nb_oh^2f_y/4L`



# The elastic stiffness of the CSF-brace is given by,



# :math:`K_p = nb_oEh^3f_y/6L^3`



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/CastFuse_Material>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('Cast', matTag, n, bo, h, fy, E, L, b, Ro, cR1, cR2, a1, a2, a3, a4, *uniqueArgs)

# def ViscousDamper(matTag, K_el, Cd, alpha, LGap, NM, RelTol, AbsTol, MaxHalf):
#     """


#    This command is used to construct a ViscousDamper material, which represents the Maxwell Model (linear spring and nonlinear dashpot in series). The ViscousDamper material simulates the hysteretic response of nonlinear viscous dampers. An adaptive iterative algorithm has been implemented and validated to solve numerically the constitutive equations within a nonlinear viscous damper with a high-precision accuracy.



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``K_el`` |float|                      Elastic stiffness of linear spring to model the axial

#                                          flexibility of a

#                                          viscous damper (e.g. combined stiffness of the

#                                          supporting brace and

#                                          internal damper portion)

#    ``Cd`` |float|                        Damping coefficient

#    ``alpha`` |float|                     Velocity exponent

#    ``LGap`` |float|                      Gap length to simulate the gap length due to the

#                                          pin tolerance

#    ``NM`` |int|                          Employed adaptive numerical algorithm (default

#                                          value NM = 1;

#                                          * ``1`` = Dormand-Prince54,

#                                          * ``2`` = 6th order Adams-Bashforth-Moulton,

#                                          * ``3`` = modified Rosenbrock Triple)

#    ``RelTol`` |float|                    Tolerance for absolute relative error control of the adaptive

#                                          iterative algorithm (default value 10^-6)

#    ``AbsTol`` |float|                    Tolerance for absolute error control of adaptive iterative

#                                          algorithm (default value 10^-10)

#    ``MaxHalf`` |int|                     Maximum number of sub-step iterations within an

#                                          integration step (default value 15)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/ViscousDamper_Material>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('ViscousDamper', matTag, K_el, Cd, alpha, LGap, NM, RelTol, AbsTol, MaxHalf, *uniqueArgs)

# def BilinearOilDamper(matTag, K_el, Cd, Fr, p, LGap, NM, RelTol, AbsTol, MaxHalf):
#     """


#    This command is used to construct a BilinearOilDamper material, which simulates the hysteretic response of bilinear oil dampers with relief valve. Two adaptive iterative algorithms have been implemented and validated to solve numerically the constitutive equations within a bilinear oil damper with a high-precision accuracy.



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``K_el`` |float|                      Elastic stiffness of linear spring to model the axial flexibility of a

#                                          viscous damper (e.g. combined stiffness of the supporting brace and

#                                          internal damper portion)

#    ``Cd`` |float|                        Damping coefficient

#    ``Fr`` |float|                        Damper relief load (default=1.0, Damper property)

#    ``p`` |float|                         Post-relief viscous damping coefficient ratio

#                                          (default=1.0, linear oil damper)

#    ``LGap`` |float|                      Gap length to simulate the gap length due to the pin tolerance

#    ``NM`` |int|                          Employed adaptive numerical algorithm (default value NM = 1;



#                                          * ``1`` = Dormand-Prince54,

#                                          * ``2`` = 6th order Adams-Bashforth-Moulton,

#                                          * ``3`` = modified Rosenbrock Triple)

#    ``RelTol`` |float|                    Tolerance for absolute relative error control of the adaptive

#                                          iterative algorithm (default value 10^-6)

#    ``AbsTol`` |float|                    Tolerance for absolute error control of adaptive iterative

#                                          algorithm (default value 10^-10)

#    ``MaxHalf`` |int|                     Maximum number of sub-step iterations within an

#                                          integration step (default value 15)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/BilinearOilDamper_Material>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('BilinearOilDamper', matTag, K_el, Cd, Fr, p, LGap, NM, RelTol, AbsTol, MaxHalf, *uniqueArgs)

def Bilin(matTag, K0, as_Plus, as_Neg, My_Plus, My_Neg, Lamda_S, Lamda_C, 
          Lamda_A, Lamda_K, c_S, c_C, c_A, c_K, theta_p_Plus, theta_p_Neg, 
          theta_pc_Plus, theta_pc_Neg, Res_Pos, Res_Neg, theta_u_Plus, 
          theta_u_Neg, D_Plus, D_Neg, nFactor):
    """

    This command is used to construct a bilin material. The bilin material 
    simulates the modified Ibarra-Krawinkler deterioration model with bilinear 
    hysteretic response. Note that the hysteretic response of this material has 
    been calibrated with respect to more than 350 experimental data of steel 
    beam-to-column connections and multivariate regression formulas are 
    provided to estimate the deterioration parameters of the model for 
    different connection types. These relationships were developed by 
    Lignos and Krawinkler (2009, 2011) and have been adopted by PEER/ATC (2010). 
    The input parameters for this component model can be computed interactively 
    from this `link <http://dimitrios-lignos.research.mcgill.ca/databases/>`_. 
    **Use the module Component Model.**

    ===================================   ===========================================================================

    ``matTag`` |int|                      integer tag identifying material

    ``K0`` |float|                        elastic stiffness

    ``as_Plus`` |float|                   strain hardening ratio for positive loading direction

    ``as_Neg`` |float|                    strain hardening ratio for negative loading direction

    ``My_Plus`` |float|                   effective yield strength for positive loading direction

    ``My_Neg`` |float|                    effective yield strength for negative loading direction (negative value)

    ``Lamda_S`` |float|                   Cyclic deterioration parameter for strength
                                          deterioration [E_t=Lamda_S*M_y; set Lamda_S = 0 to
                                          disable this mode of deterioration]

    ``Lamda_C`` |float|                   Cyclic deterioration parameter for post-capping
                                          strength deterioration [E_t=Lamda_C*M_y;
                                          set Lamda_C = 0 to disable this mode of deterioration]

    ``Lamda_A`` |float|                   Cyclic deterioration parameter for acceleration
                                          reloading stiffness deterioration (is not a
                                          deterioration mode for a component with Bilinear
                                          hysteretic response) [Input value is required,
                                          but not used; set Lamda_A = 0].

    ``Lamda_K`` |float|                   Cyclic deterioration parameter for unloading
                                          stiffness deterioration [E_t=Lamda_K*M_y; set
                                          Lamda_k = 0 to disable this mode of deterioration]

    ``c_S`` |float|                       rate of strength deterioration. The default value is 1.0.

    ``c_C`` |float|                       rate of post-capping strength deterioration. The default value is 1.0.

    ``c_A`` |float|                       rate of accelerated reloading deterioration. The default value is 1.0.

    ``c_K`` |float|                       rate of unloading stiffness deterioration. The default value is 1.0.

    ``theta_p_Plus`` |float|              pre-capping rotation for positive loading direction
                                          (often noted as plastic rotation capacity)

    ``theta_p_Neg`` |float|               pre-capping rotation for negative loading direction
                                          (often noted as plastic rotation capacity) (positive value)

    ``theta_pc_Plus`` |float|             post-capping rotation for positive loading direction

    ``theta_pc_Neg`` |float|              post-capping rotation for negative loading direction (positive value)

    ``Res_Pos`` |float|                   residual strength ratio for positive loading direction

    ``Res_Neg`` |float|                   residual strength ratio for negative loading direction (positive value)

    ``theta_u_Plus`` |float|              ultimate rotation capacity for positive loading direction

    ``theta_u_Neg`` |float|               ultimate rotation capacity for negative loading direction (positive value)

    ``D_Plus`` |float|                    rate of cyclic deterioration in the positive loading direction
                                          (this parameter is used to create assymetric
                                          hysteretic behavior for the case of a
                                          composite beam). For symmetric hysteretic response use 1.0.

    ``D_Neg`` |float|                     rate of cyclic deterioration in the negative loading direction
                                          (this parameter is used to create assymetric hysteretic behavior
                                          for the case of a composite beam). For symmetric hysteretic response use 1.0.

    ``nFactor`` |float|                   elastic stiffness amplification factor, mainly for use
                                          with concentrated plastic hinge elements (optional, default = 0).
    ===================================   ===========================================================================


    .. seealso::
    
        `Wiki <https://openseespydoc.readthedocs.io/en/latest/src/Bilin.html>`_
    
    
        `Notes <http://opensees.berkeley.edu/wiki/index.php/Modified_Ibarra-Medina-Krawinkler_Deterioration_Model_with_Bilinear_Hysteretic_Response_(Bilin_Material)>`_


    """
    uniqueArgs = []
    ops.uniaxialMaterial('Bilin', matTag, K0, as_Plus, as_Neg, My_Plus, My_Neg, 
                         Lamda_S, Lamda_C, Lamda_A, Lamda_K, c_S, c_C, c_A, c_K, 
                         theta_p_Plus, theta_p_Neg, theta_pc_Plus, theta_pc_Neg, 
                         Res_Pos, Res_Neg, theta_u_Plus, theta_u_Neg, D_Plus, 
                         D_Neg, nFactor)

def ModIMKPeakOriented(matTag, K0, as_Plus, as_Neg, My_Plus, My_Neg, Lamda_S, 
                       Lamda_C, Lamda_A, Lamda_K, c_S, c_C, c_A, c_K, 
                       theta_p_Plus, theta_p_Neg, theta_pc_Plus, theta_pc_Neg, 
                       Res_Pos, Res_Neg, theta_u_Plus, theta_u_Neg, D_Plus, D_Neg):
    """

    This command is used to construct a ModIMKPeakOriented material. This material simulates the modified Ibarra-Medina-Krawinkler deterioration model with peak-oriented hysteretic response. Note that the hysteretic response of this material has been calibrated with respect to 200 experimental data of RC beams in order to estimate the deterioration parameters of the model. This information was developed by Lignos and Krawinkler (2012). NOTE: before you use this material make sure that you have downloaded the latest OpenSees version. A youtube video presents a summary of this model including the way to be used within openSees `youtube link <http://youtu.be/YHBHQ-xuybE>`_.

    ===================================   ===========================================================================

    ``matTag`` |int|                      integer tag identifying material

    ``K0`` |float|                        elastic stiffness

    ``as_Plus`` |float|                   strain hardening ratio for positive loading direction

    ``as_Neg`` |float|                    strain hardening ratio for negative loading direction

    ``My_Plus`` |float|                   effective yield strength for positive loading direction

    ``My_Neg`` |float|                    effective yield strength for negative loading direction (negative value)

    ``Lamda_S`` |float|                   Cyclic deterioration parameter for strength deterioration [E_t=Lamda_S*M_y, see Lignos and Krawinkler (2011); set Lamda_S = 0 to disable this mode of deterioration]

    ``Lamda_C`` |float|                   Cyclic deterioration parameter for post-capping strength deterioration [E_t=Lamda_C*M_y, see Lignos and Krawinkler (2011); set Lamda_C = 0 to disable this mode of deterioration]

    ``Lamda_A`` |float|                   Cyclic deterioration parameter for accelerated reloading stiffness deterioration [E_t=Lamda_A*M_y, see Lignos and Krawinkler (2011); set Lamda_A = 0 to disable this mode of deterioration]

    ``Lamda_K`` |float|                   Cyclic deterioration parameter for unloading stiffness deterioration [E_t=Lamda_K*M_y, see Lignos and Krawinkler (2011); set Lamda_K = 0 to disable this mode of deterioration]

    ``c_S`` |float|                       rate of strength deterioration. The default value is 1.0.

    ``c_C`` |float|                       rate of post-capping strength deterioration. The default value is 1.0.

    ``c_A`` |float|                       rate of accelerated reloading deterioration. The default value is 1.0.

    ``c_K`` |float|                       rate of unloading stiffness deterioration. The default value is 1.0.

    ``theta_p_Plus`` |float|              pre-capping rotation for positive loading direction (often noted as plastic rotation capacity)

    ``theta_p_Neg`` |float|               pre-capping rotation for negative loading direction (often noted as plastic rotation capacity) (must be defined as a positive value)

    ``theta_pc_Plus`` |float|             post-capping rotation for positive loading direction

    ``theta_pc_Neg`` |float|              post-capping rotation for negative loading direction (must be defined as a positive value)

    ``Res_Pos`` |float|                   residual strength ratio for positive loading direction

    ``Res_Neg`` |float|                   residual strength ratio for negative loading direction (must be defined as a positive value)

    ``theta_u_Plus`` |float|              ultimate rotation capacity for positive loading direction

    ``theta_u_Neg`` |float|               ultimate rotation capacity for negative loading direction (must be defined as a positive value)

    ``D_Plus`` |float|                    rate of cyclic deterioration in the positive loading direction (this parameter is used to create assymetric hysteretic behavior for the case of a composite beam). For symmetric hysteretic response use 1.0.

    ``D_Neg`` |float|                     rate  of cyclic deterioration in the negative loading direction (this parameter is used to create assymetric hysteretic behavior for the case of a composite beam). For symmetric hysteretic response use 1.0.

    ===================================   ===========================================================================


    .. seealso::
    
        `Notes <https://openseespydoc.readthedocs.io/en/latest/src/ModIMKPeakOriented.html>`_

        `Notes <http://opensees.berkeley.edu/wiki/index.php/Modified_Ibarra-Medina-Krawinkler_Deterioration_Model_with_Peak-Oriented_Hysteretic_Response_(ModIMKPeakOriented_Material)>`_

    """
    uniqueArgs = []
    ops.uniaxialMaterial('ModIMKPeakOriented', matTag, K0, as_Plus, as_Neg, My_Plus, My_Neg, Lamda_S, Lamda_C, Lamda_A, Lamda_K, c_S, c_C, c_A, c_K, theta_p_Plus, theta_p_Neg, theta_pc_Plus, theta_pc_Neg, Res_Pos, Res_Neg, theta_u_Plus, theta_u_Neg, D_Plus, D_Neg, *uniqueArgs)

def ModIMKPinching(matTag, K0, as_Plus, as_Neg, My_Plus, My_Neg, FprPos, 
                   FprNeg, A_pinch, Lamda_S, Lamda_C, Lamda_A, Lamda_K, c_S, 
                   c_C, c_A, c_K, theta_p_Plus, theta_p_Neg, theta_pc_Plus, 
                   theta_pc_Neg, Res_Pos, Res_Neg, theta_u_Plus, theta_u_Neg, 
                   D_Plus, D_Neg):
    """

    This command is used to construct a ModIMKPinching material. This material simulates the modified Ibarra-Medina-Krawinkler deterioration model with pinching hysteretic response. NOTE: **before you use this material make sure that you have downloaded the latest OpenSees version**. A youtube video presents a summary of this model including the way to be used within openSees `youtube link <http://youtu.be/YHBHQ-xuybE>`_.

    ===================================   ===========================================================================

    ``matTag`` |int|                      integer tag identifying material

    ``K0`` |float|                        elastic stiffness

    ``as_Plus`` |float|                   strain hardening ratio for positive loading direction

    ``as_Neg`` |float|                    strain hardening ratio for negative loading direction

    ``My_Plus`` |float|                   effective yield strength for positive loading direction

    ``My_Neg`` |float|                    effective yield strength for negative loading direction (Must be defined as a negative value)

    ``FprPos`` |float|                    Ratio of the force at which reloading begins to force corresponding to the maximum historic deformation demand (positive loading direction)

    ``FprNeg`` |float|                    Ratio of the force at which reloading begins to force corresponding to the absolute maximum historic deformation demand (negative loading direction)

    ``A_pinch`` |float|                   Ratio of reloading stiffness

    ``Lamda_S`` |float|                   Cyclic deterioration parameter for strength deterioration [E_t=Lamda_S*M_y, see Lignos and Krawinkler (2011); set Lamda_S = 0 to disable this mode of deterioration]

    ``Lamda_C`` |float|                   Cyclic deterioration parameter for post-capping strength deterioration [E_t=Lamda_C*M_y, see Lignos and Krawinkler (2011); set Lamda_C = 0 to disable this mode of deterioration]

    ``Lamda_A`` |float|                   Cyclic deterioration parameter for accelerated reloading stiffness deterioration [E_t=Lamda_A*M_y, see Lignos and Krawinkler (2011); set Lamda_A = 0 to disable this mode of deterioration]

    ``Lamda_K`` |float|                   Cyclic deterioration parameter for unloading stiffness deterioration [E_t=Lamda_K*M_y, see Lignos and Krawinkler (2011); set Lamda_K = 0 to disable this mode of deterioration]

    ``c_S`` |float|                       rate of strength deterioration. The default value is 1.0.

    ``c_C`` |float|                       rate of post-capping strength deterioration. The default value is 1.0.

    ``c_A`` |float|                       rate of accelerated reloading deterioration. The default value is 1.0.

    ``c_K`` |float|                       rate of unloading stiffness deterioration. The default value is 1.0.

    ``theta_p_Plus`` |float|              pre-capping rotation for positive loading direction (often noted as plastic rotation capacity)

    ``theta_p_Neg`` |float|               pre-capping rotation for negative loading direction (often noted as plastic rotation capacity) (must be defined as a positive value)

    ``theta_pc_Plus`` |float|             post-capping rotation for positive loading direction

    ``theta_pc_Neg`` |float|              post-capping rotation for negative loading direction (must be defined as a positive value)

    ``Res_Pos`` |float|                   residual strength ratio for positive loading direction

    ``Res_Neg`` |float|                   residual strength ratio for negative loading direction (must be defined as a positive value)

    ``theta_u_Plus`` |float|              ultimate rotation capacity for positive loading direction

    ``theta_u_Neg`` |float|               ultimate rotation capacity for negative loading direction (must be defined as a positive value)

    ``D_Plus`` |float|                    rate of cyclic deterioration in the positive loading direction (this parameter is used to create assymetric hysteretic behavior for the case of a composite beam). For symmetric hysteretic response use 1.0.

    ``D_Neg`` |float|                     rate of cyclic deterioration in the negative loading direction (this parameter is used to create assymetric hysteretic behavior for the case of a composite beam). For symmetric hysteretic response use 1.0.

    ===================================   ===========================================================================

    .. seealso::
    
        `Notes <https://openseespydoc.readthedocs.io/en/latest/src/ModIMKPinching.html`_

        `Notes <http://opensees.berkeley.edu/wiki/index.php/Modified_Ibarra-Medina-Krawinkler_Deterioration_Model_with_Pinched_Hysteretic_Response_(ModIMKPinching_Material)>`_

    """
    uniqueArgs = []
    ops.uniaxialMaterial('ModIMKPinching', matTag, K0, as_Plus, as_Neg, My_Plus, My_Neg, FprPos, FprNeg, A_pinch, Lamda_S, Lamda_C, Lamda_A, Lamda_K, c_S, c_C, c_A, c_K, theta_p_Plus, theta_p_Neg, theta_pc_Plus, theta_pc_Neg, Res_Pos, Res_Neg, theta_u_Plus, theta_u_Neg, D_Plus, D_Neg, *uniqueArgs)

def SAWS(matTag, F0, FI, DU, S0, R1, R2, R3, R4, alpha, beta):
    """

    This file contains the class definition for SAWSMaterial. SAWSMaterial 
    provides the implementation of a one-dimensional hysteretic model developed
    as part of the CUREe Caltech wood frame project.

    ===================================   ===========================================================================

    ``matTag`` |int|                      integer tag identifying material

    ``F0`` |float|                        Intercept strength of the shear wall spring element for the asymtotic line to the envelope curve F0 > FI > 0

    ``FI`` |float|                        Intercept strength of the spring element for the pinching branch of the hysteretic curve. (FI > 0).

    ``DU`` |float|                        Spring element displacement at ultimate load. (DU > 0).

    ``S0`` |float|                        Initial stiffness of the shear wall spring element (S0 > 0).

    ``R1`` |float|                        Stiffness ratio of the asymptotic line to the spring element envelope curve. The slope of this line is R1 S0. (0 < R1 < 1.0).

    ``R2`` |float|                        Stiffness ratio of the descending branch of the spring element envelope curve. The slope of this line is R2 S0. ( R2 < 0).

    ``R3`` |float|                        Stiffness ratio of the unloading branch off the spring element envelope curve. The slope of this line is R3 S0. ( R3 1).

    ``R4`` |float|                        Stiffness ratio of the pinching branch for the spring element. The slope of this line is R4 S0. ( R4 > 0).

    ``alpha`` |float|                     Stiffness degradation parameter for the shear wall spring element. (ALPHA > 0).

    ``beta`` |float|                      Stiffness degradation parameter for the spring element. (BETA > 0).

    ===================================   ===========================================================================

    .. seealso::
        
        `wiki <https://openseespydoc.readthedocs.io/en/latest/src/SAWS.html>`_    
    
        `Notes <http://opensees.berkeley.edu/wiki/index.php/SAWS_Material>`_

    """
    uniqueArgs = []
    ops.uniaxialMaterial('SAWS', matTag, F0, FI, DU, S0, R1, R2, R3, R4, alpha, beta, *uniqueArgs)

# def BarSlip(matTag, fc, fy, Es, fu, Eh, db, ld, nb, depth, height, ancLratio, bsFlag, type, damage, unit):
#     """


#    This command is used to construct a uniaxial material that simulates the bar force versus slip response of a reinforcing bar anchored in a beam-column joint. The model exhibits degradation under cyclic loading. Cyclic degradation of strength and stiffness occurs in three ways: unloading stiffness degradation, reloading stiffness degradation, strength degradation.



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``fc`` |float|                        positive floating point value defining the compressive strength of the concrete in which the reinforcing bar is anchored

#    ``fy`` |float|                        positive floating point value defining the yield strength of the reinforcing steel

#    ``Es`` |float|                        floating point value defining the modulus of elasticity of the reinforcing steel

#    ``fu`` |float|                        positive floating point value defining the ultimate strength of the reinforcing steel

#    ``Eh`` |float|                        floating point value defining the hardening modulus of the reinforcing steel

#    ``ld`` |float|                        floating point value defining the development length of the reinforcing steel

#    ``db`` |float|                        point value defining the diameter of reinforcing steel

#    ``nb`` |int|                          an integer defining the number of anchored bars

#    ``depth`` |float|                     floating point value defining the dimension of the member (beam or column) perpendicular to the dimension of the plane of the paper

#    ``height`` |float|                    floating point value defining the height of the flexural member, perpendicular to direction in which the reinforcing steel is placed, but in the plane of the paper

#    ``ancLratio`` |float|                 floating point value defining the ratio of anchorage length used for the reinforcing bar to the dimension of the joint in the direction of the reinforcing bar (optional, default: 1.0)

#    ``bsFlag`` |str|                      string indicating relative bond strength for the anchored reinforcing bar (options: ``'Strong'`` or ``'Weak'``)

#    ``type`` |str|                        string indicating where the reinforcing bar is placed. (options: ``'beamtop'``, ``'beambot'`` or ``'column'``)

#    ``damage`` |str|                      string indicating type of damage:whether there is full damage in the material or no damage (optional, options: ``'Damage'``, ``'NoDamage'`` ; default: ``'Damage'``)

#    ``unit`` |str|                        string indicating the type of unit system used (optional, options: ``'psi'``, ``'MPa'``, ``'Pa'``, ``'psf'``, ``'ksi'``, ``'ksf'``) (default: ``'psi'`` / ``'MPa'``)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/BARSLIP_Material>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('BarSlip', matTag, fc, fy, Es, fu, Eh, db, ld, nb, depth, height, ancLratio, bsFlag, type, damage, unit, *uniqueArgs)

# def Bond_SP01(matTag, Fy, Sy, Fu, Su, b, R):
#     """


#    This command is used to construct a uniaxial material object for capturing strain penetration effects at the column-to-footing, column-to-bridge bent caps, and wall-to-footing intersections. In these cases, the bond slip associated with strain penetration typically occurs along a portion of the anchorage length. This model can also be applied to the beam end regions, where the strain penetration may include slippage of the bar along the entire anchorage length, but the model parameters should be chosen appropriately.



#    This model is for fully anchored steel reinforcement bars that experience bond slip along a portion of the anchorage length due to strain penetration effects, which are usually the case for column and wall longitudinal bars anchored into footings or bridge joints



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``Fy`` |float|                        Yield strength of the reinforcement steel

#    ``Sy`` |float|                        Rebar slip at member interface under yield stress. (see NOTES below)

#    ``Fu`` |float|                        Ultimate strength of the reinforcement steel

#    ``Su`` |float|                        Rebar slip at the loaded end at the bar fracture strength

#    ``b`` |float|                         Initial hardening ratio in the monotonic slip vs. bar stress response (0.3~0.5)

#    ``R`` |float|                         Pinching factor for the cyclic slip vs. bar response (0.5~1.0)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Bond_SP01_-_-_Strain_Penetration_Model_for_Fully_Anchored_Steel_Reinforcing_Bars>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('Bond_SP01', matTag, Fy, Sy, Fu, Su, b, R, *uniqueArgs)

# def Fatigue(matTag, otherTag, E0, m, min, max):
#     """


#    The fatigue material uses a modified rainflow cycle counting algorithm to accumulate damage in a material using Miner's Rule. Element stress/strain relationships become zero when fatigue life is exhausted.



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``otherTag`` |float|                  Unique material object integer tag for the material that is being wrapped

#    ``E0`` |float|                        Value of strain at which one cycle will cause failure (default 0.191)

#    ``m`` |float|                         Slope of Coffin-Manson curve in log-log space (default -0.458)

#    ``min`` |float|                       Global minimum value for strain or deformation (default -1e16)

#    ``max`` |float|                       Global maximum value for strain or deformation (default 1e16)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Fatigue_Material>`_

#     """
#     uniqueArgs = []
#     if E0=0.191:
#         uniqueArgs.append('-E0')
#     if m=-0.458:
#         uniqueArgs.append('-m')
#     if min=-1e16:
#         uniqueArgs.append('-min')
#     if max=1e16:
#         uniqueArgs.append('-max')
#     ops.uniaxialMaterial('Fatigue', matTag, otherTag, E0, m, min, max, *uniqueArgs)

# def ImpactMaterial(matTag, K1, K2, sigy, gap):
#     """


#    This command is used to construct an impact material object



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``K1`` |float|                        initial stiffness

#    ``K2`` |float|                        secondary stiffness

#    ``sigy`` |float|                      yield displacement

#    ``gap`` |float|                       initial gap

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Impact_Material>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('ImpactMaterial', matTag, K1, K2, sigy, gap, *uniqueArgs)

# def HyperbolicGapMaterial(matTag, Kmax, Kur, Rf, Fult, gap):
#     """


#    This command is used to construct a hyperbolic gap material object.



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``Kmax`` |float|                      initial stiffness

#    ``Kur`` |float|                       unloading/reloading stiffness

#    ``Rf`` |float|                        failure ratio

#    ``Fult`` |float|                      ultimate (maximum) passive resistance

#    ``gap`` |float|                       initial gap

#    ===================================   ===========================================================================



# .. note::



#    #. This material is implemented as a compression-only gap material. ``Fult`` and ``gap`` should be input as negative values.

#    #. Recomended Values:



#       * ``Kmax``        = 20300 kN/m of abutment width

#       * ``Kcur``        = ``Kmax``

#       * ``Rf``        = 0.7

#       * ``Fult``        = -326 kN per meter of abutment width

#       * ``gap``        = -2.54 cm



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Hyperbolic_Gap_Material>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('HyperbolicGapMaterial', matTag, Kmax, Kur, Rf, Fult, gap, *uniqueArgs)

# def LimitState(matTag, s1p, e1p, s2p, e2p, s3p, e3p, s1n, e1n, s2n, e2n, s3n, e3n, pinchX, pinchY, damage1, damage2, beta, curveTag, curveType):
#     """


#    This command is used to construct a uniaxial hysteretic material object with pinching of force and deformation, damage due to ductility and energy, and degraded unloading stiffness based on ductility. Failure of the material is defined by the associated Limit Curve.





#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``s1p``  ``e1p`` |float|              stress and strain (or force & deformation) at first point of the envelope in the positive direction

#    ``s2p``  ``e2p`` |float|              stress and strain (or force & deformation) at second point of the envelope in the positive direction

#    ``s3p``  ``e3p`` |float|              stress and strain (or force & deformation) at third point of the envelope in the positive direction

#    ``s1n``  ``e1n`` |float|              stress and strain (or force & deformation) at first point of the envelope in the negative direction

#    ``s2n``  ``e2n`` |float|              stress and strain (or force & deformation) at second point of the envelope in the negative direction

#    ``s3n``  ``e3n`` |float|              stress and strain (or force & deformation) at third point of the envelope in the negative direction

#    ``pinchX`` |float|                    pinching factor for strain (or deformation) during reloading

#    ``pinchY`` |float|                    pinching factor for stress (or force) during reloading

#    ``damage1`` |float|                   damage due to ductility: D1(m-1)

#    ``damage2`` |float|                   damage due to energy: D2(Ei/Eult)

#    ``beta`` |float|                      power used to determine the degraded unloading stiffness based on ductility, m-b (optional, default=0.0)

#    ``curveTag`` |int|                    an integer tag for the Limit Curve defining the limit surface

#    ``curveType`` |int|                   an integer defining the type of LimitCurve (0 = no curve, 1 = axial curve, all other curves can be any other integer)

#    ===================================   ===========================================================================



# .. note::



#    * negative backbone points should be entered as negative numeric values



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Limit_State_Material>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('LimitState', matTag, s1p, e1p, s2p, e2p, s3p, e3p, s1n, e1n, s2n, e2n, s3n, e3n, pinchX, pinchY, damage1, damage2, beta, curveTag, curveType, *uniqueArgs)

# def MinMax(matTag, otherTag, minStrain, maxStrain):
#     """




#    This command is used to construct a MinMax material object. This stress-strain behaviour for this material is provided by another material. If however the strain ever falls below or above certain threshold values, the other material is assumed to have failed. From that point on, values of 0.0 are returned for the tangent and stress.



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``otherTag`` |float|                  tag of the other material

#    ``minStrain`` |float|                 minimum value of strain. optional default = -1.0e16.

#    ``maxStrain`` |float|                 max value of strain. optional default = 1.0e16.

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/MinMax_Material>`_

#     """
#     uniqueArgs = []
#     if minStrain=1e-16:
#         uniqueArgs.append('-min')
#     if maxStrain=1e16:
#         uniqueArgs.append('-max')
#     ops.uniaxialMaterial('MinMax', matTag, otherTag, minStrain, maxStrain, *uniqueArgs)

def ElasticBilin(matTag, EP1, EP2, epsP2, EN1=None, EN2=None, epsN2=None):
    """

    This command is used to construct an elastic bilinear uniaxial material object. Unlike all other bilinear materials, the unloading curve follows the loading curve exactly.

    ===================================   ===========================================================================

    ``matTag`` |int|                      integer tag identifying material

    ``EP1`` |float|                       tangent in tension for stains: 0 <= strains <=    ``epsP2``

    ``EP2`` |float|                       tangent when material in tension with strains >    ``epsP2``

    ``epsP2`` |float|                     strain at which material changes tangent in tension.

    ``EN1`` |float|                       optional, default =    ``EP1``. tangent in compression for stains: 0 < strains <=    ``epsN2``

    ``EN2`` |float|                       optional, default =    ``EP2``. tangent in compression with strains <    ``epsN2``

    ``epsN2`` |float|                     optional, default = ``-epsP2``. strain at which material changes tangent in compression.

    ===================================   ===========================================================================

    .. note::
    
        ``eps0`` can not be controlled. It is always zero.
    
    .. seealso::
     
        `wiki <https://openseespydoc.readthedocs.io/en/latest/src/ElasticBilin.html>`_   
    
        `Notes <http://opensees.berkeley.edu/wiki/index.php/ElasticBilin_Material>`_

    """
    
    
    
    uniqueArgs = []
    
    if EN1:
        uniqueArgs.append(EN1)
    if EN2:
        uniqueArgs.append(EN2)    
    if epsN2:
        uniqueArgs.append(epsN2)
        
    ops.uniaxialMaterial('ElasticBilin', matTag, EP1, EP2, epsP2, EN1, EN2, epsN2)

def ElasticMultiLinear(matTag, eta=None, strain=None, stress=None):
    """

    This command is used to construct a multi-linear elastic uniaxial material 
    object. The nonlinear stress-strain relationship is given by a multi-linear 
    curve that is define by a set of points. The behavior is nonlinear but it 
    is elastic. This means that the material loads and unloads along the same 
    curve, and no energy is dissipated. The slope given by the last two 
    specified points on the positive strain axis is extrapolated to infinite 
    positive strain. Similarly, the slope given by the last two specified 
    points on the negative strain axis is extrapolated to infinite negative 
    strain. The number of provided strain points needs to be equal to the 
    number of provided stress points.



    ===================================   ===========================================================================

    ``matTag`` |int|                      integer tag identifying material

    ``eta`` |float|                       damping tangent (optional, default=0.0)

    ``strain`` |listf|                    list of strain points along stress-strain curve

    ``stress`` |listf|                    list of stress points along stress-strain curve

    ===================================   ===========================================================================

    .. seealso::
        `wiki <https://openseespydoc.readthedocs.io/en/latest/src/ElasticMultiLinear.html>`_

    
        `Notes <http://opensees.berkeley.edu/wiki/index.php/ElasticMultiLinear_Material>`_

    """
    uniqueArgs = []
    
    if eta:
        uniqueArgs.append(eta) 
    if strain:
        uniqueArgs.append('-strain')
        uniqueArgs +=strain
    if stress:
        uniqueArgs.append('-stress')
        uniqueArgs +=stress
    ops.uniaxialMaterial('ElasticMultiLinear', matTag, *uniqueArgs)

def MultiLinear(matTag, pts):
    """

    This command is used to construct a uniaxial multilinear material object.

    ===================================   ===========================================================================
    ``matTag`` |int|                      integer tag identifying material

    ``pts`` |listf|                       a list of strain and stress points
                                          ``pts = [strain1, stress1, strain2, stress2, ..., ]``
    ===================================   ===========================================================================

    .. seealso::
        
        `Wiki <https://openseespydoc.readthedocs.io/en/latest/src/MultiLinear.html>`_
        
        `Notes <http://opensees.berkeley.edu/wiki/index.php/MultiLinear_Material>`_

    """
    ops.uniaxialMaterial('MultiLinear', matTag, *pts)

# def InitStrainMaterial(matTag, otherTag, initStrain):
#     """


#    This command is used to construct an Initial Strain material object. The stress-strain behaviour for this material is defined by another material. Initial Strain Material enables definition of initial strains for the material under consideration. The stress that corresponds to the initial strain will be calculated from the other material.



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``otherTag`` |int|                    tag of the other material

#    ``initStrain`` |float|                initial strain

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Initial_Strain_Material>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('InitStrainMaterial', matTag, otherTag, initStrain, *uniqueArgs)

# def InitStressMaterial(matTag, otherTag, initStress):
#     """


#    This command is used to construct an Initial Stress material object. The stress-strain behaviour for this material is defined by another material. Initial Stress Material enables definition of initial stress for the material under consideration. The strain that corresponds to the initial stress will be calculated from the other material.



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``otherTag`` |float|                  tag of the other material

#    ``initStress`` |float|                initial stress

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Initial_Stress_Material>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('InitStressMaterial', matTag, otherTag, initStress, *uniqueArgs)

# def PathIndependent(matTag, OtherTag):
#     """


#    This command is to create a PathIndependent material



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``OtherTag`` |int|                    a pre-defined material

#    ===================================   ===========================================================================

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('PathIndependent', matTag, OtherTag, *uniqueArgs)

# def Pinching4(matTag, ePf1, ePd1, ePf2, ePd2, ePf3, ePd3, ePf4, ePd4, eNd1=None, eNf2=None, eNd2=None, eNf3=None, eNd3=None, eNf4=None, eNd4=None, rDispP, rForceP, uForceP, rForceN=None, uForceN=None, gK1, gK2, gK3, gK4, gKLim, gD1, gD2, gD3, gD4, gDLim, gF1, gF2, gF3, gF4, gFLim, gE, dmgType):
#     """

#     This command is used to construct a uniaxial material that represents a 
#     'pinched' load-deformation response and exhibits degradation under cyclic 
#     loading. Cyclic degradation of strength and stiffness occurs in three ways:
#     unloading stiffness degradation, reloading stiffness degradation, 
#     strength degradation.


#     ==========================================================   ===========================================================================

#     ``matTag`` |int|                                             integer tag identifying material

#     ``ePf1``    ``ePf2``    ``ePf3``    ``ePf4`` |float|         floating point values defining force points on the positive response envelope

#     ``ePd1``    ``ePd2``    ``ePd3``    ``ePd4`` |float|         floating point values defining deformation points on the positive response envelope

#     ``eNf1``    ``eNf2``    ``eNf3``    ``eNf4`` |float|         floating point values defining force points on the negative response envelope

#     ``eNd1``    ``eNd2``    ``eNd3``    ``eNd4`` |float|         floating point values defining deformation points on the negative response envelope

#     ``rDispP`` |float|                                           floating point value defining the ratio of the deformation at which reloading occurs to the maximum historic deformation demand

#     ``fFoceP`` |float|                                           floating point value defining the ratio of the force at which reloading begins to force corresponding to the maximum historic deformation demand

#     ``uForceP`` |float|                                          floating point value defining the ratio of strength developed upon unloading from negative load to the maximum strength developed under monotonic loading

#     ``rDispN`` |float|                                           floating point value defining the ratio of the deformation at which reloading occurs to the minimum historic deformation demand

#     ``fFoceN`` |float|                                           floating point value defining the ratio of the force at which reloading begins to force corresponding to the minimum historic deformation demand

#     ``uForceN`` |float|                                          floating point value defining the ratio of strength developed upon unloading from negative load to the minimum strength developed under monotonic loading

#     ``gK1``  ``gK2``  ``gK3``  ``gK4``  ``gKLim`` |float|        floating point values controlling cyclic degradation model for unloading stiffness degradation

#     ``gD1``  ``gD2``  ``gD3``  ``gD4``  ``gDLim`` |float|        floating point values controlling cyclic degradation model for reloading stiffness degradation

#     ``gF1``  ``gF2``  ``gF3``  ``gF4``  ``gFLim`` |float|        floating point values controlling cyclic degradation model for strength degradation

#     ``gE`` |float|                                               floating point value used to define maximum energy dissipation under cyclic loading. Total energy dissipation capacity is defined as this factor multiplied by the energy dissipated under monotonic loading.

#     ``dmgType`` |str|                                            string to indicate type of damage (option: ``'cycle'``, ``'energy'``)

#     ==========================================================   ===========================================================================


# .. seealso::


#     `Notes <http://opensees.berkeley.edu/wiki/index.php/Pinching4_Material>`_

#     """
#     uniqueArgs = []
#     if eNd1:
#         uniqueArgs.append(eNf1)
#         uniqueArgs.append(eNd1)
#         uniqueArgs.append(eNf2)
#         uniqueArgs.append(eNd2)
#         uniqueArgs.append(eNf3)
#         uniqueArgs.append(eNd3)
#         uniqueArgs.append(eNf4)
#         uniqueArgs.append(eNd4)
#     if rForceN:
#         uniqueArgs.append(rDispN)
#         uniqueArgs.append(rForceN)
#         uniqueArgs.append(uForceN)
#     ops.uniaxialMaterial('Pinching4', matTag, ePf1, ePd1, ePf2, ePd2, ePf3, ePd3, ePf4, ePd4, rDispP, rForceP, uForceP, gK1, gK2, gK3, gK4, gKLim, gD1, gD2, gD3, gD4, gDLim, gF1, gF2, gF3, gF4, gFLim, gE, dmgType, *uniqueArgs)

# def ECC01(matTag, sigt0, epst0, sigt1, epst1, epst2, sigc0, epsc0, epsc1, alphaT1, alphaT2, alphaC, alphaCU, betaT, betaC):
#     """


#    This command is used to construct a uniaxial Engineered Cementitious Composites (ECC)material object based on the ECC material model of Han, et al. (see references). Reloading in tension and compression is linear.



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``sigt0`` |float|                     tensile cracking stress

#    ``epst0`` |float|                     strain at tensile cracking stress

#    ``sigt1`` |float|                     peak tensile stress

#    ``epst1`` |float|                     strain at peak tensile stress

#    ``epst2`` |float|                     ultimate tensile strain

#    ``sigc0`` |float|                     compressive strength (see NOTES)

#    ``epsc0`` |float|                     strain at compressive strength (see NOTES)

#    ``epsc1`` |float|                     ultimate compressive strain (see NOTES)

#    ``alphaT1`` |float|                   exponent of the unloading curve in tensile strain hardening region

#    ``alphaT2`` |float|                   exponent of the unloading curve in tensile softening region

#    ``alphaC`` |float|                    exponent of the unloading curve in the compressive softening

#    ``alphaCU`` |float|                   exponent of the compressive softening curve (use 1 for linear softening)

#    ``betaT`` |float|                     parameter to determine permanent strain in tension

#    ``betaC`` |float|                     parameter to determine permanent strain in compression

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Engineered_Cementitious_Composites_Material>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('ECC01', matTag, sigt0, epst0, sigt1, epst1, epst2, sigc0, epsc0, epsc1, alphaT1, alphaT2, alphaC, alphaCU, betaT, betaC, *uniqueArgs)

# def SelfCentering(matTag, k1, k2, sigAct, beta, epsSlip, epsBear, rBear):
#     """


#    This command is used to construct a uniaxial self-centering (flag-shaped) material object with optional non-recoverable slip behaviour and an optional stiffness increase at high strains (bearing behaviour).



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``k1`` |float|                        Initial Stiffness

#    ``k2`` |float|                        Post-Activation Stiffness (0<   ``k2``<   ``k1``)

#    ``sigAct`` |float|                    Forward Activation Stress/Force

#    ``beta`` |float|                      Ratio of Forward to Reverse Activation Stress/Force

#    ``epsSlip`` |float|                   slip Strain/Deformation (if    ``epsSlip`` = 0, there will be no slippage)

#    ``epsBear`` |float|                   Bearing Strain/Deformation (if    ``epsBear`` = 0, there will be no bearing)

#    ``rBear`` |float|                     Ratio of Bearing Stiffness to Initial Stiffness    ``k1``

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/SelfCentering_Material>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('SelfCentering', matTag, k1, k2, sigAct, beta, epsSlip, epsBear, rBear, *uniqueArgs)

# def Viscous(matTag, C, alpha):
#     """


#    This command is used to construct a uniaxial viscous material object. stress =C(strain-rate)^alpha



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``C`` |float|                         damping coeficient

#    ``alpha`` |float|                     power factor (=1 means linear damping)

#    ===================================   ===========================================================================



# .. note::



#    1. This material can only be assigned to truss and zeroLength elements.



#    2. This material can not be combined in parallel/series with other materials. When defined in parallel with other materials it is ignored.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Viscous_Material>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('Viscous', matTag, C, alpha, *uniqueArgs)

# def BoucWen(matTag, alpha, ko, n, gamma, beta, Ao, deltaA, deltaNu, deltaEta):
#     """


#    This command is used to construct a uniaxial Bouc-Wen smooth hysteretic material object. This material model is an extension of the original Bouc-Wen model that includes stiffness and strength degradation (Baber and Noori (1985)).







#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``alpha`` |float|                     ratio of post-yield stiffness to the initial elastic stiffenss (0< alpha <1)

#    ``ko`` |float|                        initial elastic stiffness

#    ``n`` |float|                         parameter that controls transition from linear to nonlinear range (as n increases the transition becomes sharper; n is usually grater or equal to 1)

#    ``gamma``    ``beta`` |float|         parameters that control shape of hysteresis loop; depending on the values of gamma and beta softening, hardening or quasi-linearity can be simulated (look at the NOTES)

#    ``Ao``    ``deltaA`` |float|          parameters that control tangent stiffness

#    ``deltaNu``    ``deltaEta`` |float|   parameters that control material degradation

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/BoucWen_Material>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('BoucWen', matTag, alpha, ko, n, gamma, beta, Ao, deltaA, deltaNu, deltaEta, *uniqueArgs)

# def BWBN(matTag, alpha, ko, n, gamma, beta, Ao, q, zetas, p, Shi, deltaShi, lambda, tol, maxIter):
#     """


#    This command is used to construct a uniaxial Bouc-Wen pinching hysteretic material object. This material model is an extension of the original Bouc-Wen model that includes pinching (Baber and Noori (1986) and Foliente (1995)).







#    =============================================================================   ===========================================================================

#    ``matTag`` |int|                                                                integer tag identifying material

#    ``alpha`` |float|                                                               ratio of post-yield stiffness to the initial elastic stiffenss (0< alpha <1)

#    ``ko`` |float|                                                                  initial elastic stiffness

#    ``n`` |float|                                                                   parameter that controls transition from linear to nonlinear range (as n increases the transition becomes sharper; n is usually grater or equal to 1)

#    ``gamma``    ``beta`` |float|                                                   parameters that control shape of hysteresis loop; depending on the values of gamma and beta softening, hardening or quasi-linearity can be simulated (look at the BoucWen Material)

#    ``Ao`` |float|                                                                  parameter that controls tangent stiffness

#    ``q``  ``zetas``  ``p``  ``Shi``  ``deltaShi``  ``lambda`` |float|              parameters that control pinching

#    ``tol`` |float|                                                                 tolerance

#    ``maxIter`` |float|                                                             maximum iterations

#    =============================================================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/BWBN_Material>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('BWBN', matTag, alpha, ko, n, gamma, beta, Ao, q, zetas, p, Shi, deltaShi, lambda, tol, maxIter, *uniqueArgs)

# def KikuchiAikenHDR(matTag, tp, ar, hr, cg=None, ch=None, cu=None, rs=None, rf=None):
#     """


#    This command is used to construct a uniaxial KikuchiAikenHDR material object. This material model produces nonlinear hysteretic curves of high damping rubber bearings (HDRs).







#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``tp`` |str|                          rubber type (see note 1)

#    ``ar`` |float|                        area of rubber [unit: m^2] (see note 2)

#    ``hr`` |float|                        total thickness of rubber [unit: m] (see note 2)

#    ``cg``  ``ch``  ``cu`` |float|        correction coefficients for equivalent shear modulus (``cg``), equivalent viscous daming ratio (``ch``), ratio of shear force at zero displacement (``cu``).

#    ``rs``  ``rf`` |float|                reduction rate for stiffness (``rs``) and force (``rf``) (see note 3)

#    ===================================   ===========================================================================



# .. note::



#    1) Following rubber types for    ``tp`` are available:



#       * ``'X0.6'`` Bridgestone X0.6, standard compressive stress, up to 400% shear strain

#       * ``'X0.6-0MPa'`` Bridgestone X0.6, zero compressive stress, up to 400% shear strain

#       * ``'X0.4'`` Bridgestone X0.4, standard compressive stress, up to 400% shear strain

#       * ``'X0.4-0MPa'`` Bridgestone X0.4, zero compressive stress, up to 400% shear strain

#       * ``'X0.3'`` Bridgestone X0.3, standard compressive stress, up to 400% shear strain

#       * ``'X0.3-0MPa'`` Bridgestone X0.3, zero compressive stress, up to 400% shear strain



#    2) This material uses SI unit in calculation formula.    ``ar`` and    ``hr`` must be converted into [m^2] and [m], respectively.



#    3)    ``rs`` and    ``rf`` are　available if this material is applied to multipleShearSpring (MSS) element. Recommended values are    ``rs`` = :math:`\frac{1}{\sum_{i=0}^{n-1}\sin(\pi*i/n)^2}` and    ``rf`` = :math:`\frac{1}{\sum_{i=0}^{n-1}\sin(\pi*i/n)}`, where n is the number of springs in the MSS. For example, when n=8,    ``rs`` =0.2500,    ``rf`` =0.1989.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/KikuchiAikenHDR_Material>`_

#     """
#     uniqueArgs = []
#     if cg:
#         uniqueArgs.append('-coGHU')
#         uniqueArgs.append(cg)
#         uniqueArgs.append(ch)
#         uniqueArgs.append(cu)
#     if rs:
#         uniqueArgs.append('-coMSS')
#         uniqueArgs.append(rs)
#         uniqueArgs.append(rf)
#     ops.uniaxialMaterial('KikuchiAikenHDR', matTag, tp, ar, hr, *uniqueArgs)

# def KikuchiAikenLRB(matTag, type, ar, hr, gr, ap, tp, alph, beta, temp=None, rk=None, rq=None, rs=None, rf=None):
#     """


#    This command is used to construct a uniaxial KikuchiAikenLRB material object. This material model produces nonlinear hysteretic curves of lead-rubber bearings.







#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``type`` |int|                        rubber type (see note 1)

#    ``ar`` |float|                        area of rubber [unit: m^2]

#    ``hr`` |float|                        total thickness of rubber [unit: m]

#    ``gr`` |float|                        shear modulus of rubber [unit: N/m^2]

#    ``ap`` |float|                        area of lead plug [unit: m^2]

#    ``tp`` |float|                        yield stress of lead plug [unit: N/m^2]

#    ``alph`` |float|                      shear modulus of lead plug [unit: N/m^2]

#    ``beta`` |float|                      ratio of initial stiffness to yielding stiffness

#    ``temp`` |float|                      temperature [unit: °C]

#    ``rk``    ``rq`` |float|              reduction rate for yielding stiffness (   ``rk``) and force at zero displacement (   ``rq``)

#    ``rs``    ``rf`` |float|              reduction rate for stiffness (   ``rs``) and force (   ``rf``) (see note 3)

#    ===================================   ===========================================================================



# .. note::



#    1) Following rubber types for    ``type`` are available:



#       * ``1`` lead-rubber bearing, up to 400% shear strain [Kikuchi et al., 2010 & 2012]

#    2) This material uses SI unit in calculation formula. Input arguments must be converted into [m], [m^2], [N/m^2].



#    3)    ``rs`` and    ``rf`` are available if this material is applied to multipleShearSpring (MSS) element. Recommended values are    ``rs`` = :math:`\frac{1}{\sum_{i=0}^{n-1}\sin(\pi*i/n)^2}` and    ``rf`` = :math:`\frac{1}{\sum_{i=0}{n-1}\sin(\pi*i/n)}`, where n is the number of springs in the MSS. For example, when n=8,    ``rs`` = 0.2500 and ``rf`` = 0.1989.



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/KikuchiAikenLRB_Material>`_

#     """
#     uniqueArgs = []
#     if temp:
#         uniqueArgs.append('-T')
#         uniqueArgs.append(temp)
#     if rk:
#         uniqueArgs.append('-coKQ')
#         uniqueArgs.append(rk)
#         uniqueArgs.append(rq)
#     if rs:
#         uniqueArgs.append('-coMSS')
#         uniqueArgs.append(rs)
#         uniqueArgs.append(rf)
#     ops.uniaxialMaterial('KikuchiAikenLRB', matTag, type, ar, hr, gr, ap, tp, alph, beta, *uniqueArgs)

# def AxialSp(matTag, sce, fty, fcy, bty=None, bcy=None, fcr=None):
#     """


#    This command is used to construct a uniaxial AxialSp material object. This material model produces axial stress-strain curve of elastomeric bearings.







#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``sce`` |float|                       compressive modulus

#    ``fty``    ``fcy`` |float|            yield stress under tension (   ``fty``) and compression (   ``fcy``) (see note 1)

#    ``bte``  ``bty``  ``bcy`` |float|     reduction rate for tensile elastic range (   ``bte``), tensile yielding (   ``bty``) and compressive yielding (   ``bcy``) (see note 1)

#    ``fcr`` |float|                       target point stress (see note 1)

#    ===================================   ===========================================================================



# .. note::



#    #. Input parameters are required to satisfy followings.



#       ``fcy`` < 0.0 <    ``fty``



#       0.0 <=    ``bty`` <    ``bte`` <= 1.0



#       0.0 <=    ``bcy`` <= 1.0



#       ``fcy`` <=    ``fcr`` <= 0.0





# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/AxialSp_Material>`_

#     """
#     uniqueArgs = []
#     if bty:
#         uniqueArgs.append(bte)
#         uniqueArgs.append(bty)
#         uniqueArgs.append(bcy)
#         uniqueArgs.append(fcr)
#     ops.uniaxialMaterial('AxialSp', matTag, sce, fty, fcy, *uniqueArgs)

# def AxialSpHD(matTag, sce, fty, fcy, bty=None, bth=None, bcy=None, fcr=None, ath=None):
#     """


#    This command is used to construct a uniaxial AxialSpHD material object. This material model produces axial stress-strain curve of elastomeric bearings including hardening behavior.





#    ===========================================   ===========================================================================

#    ``matTag`` |int|                              integer tag identifying material

#    ``sce`` |float|                               compressive modulus

#    ``fty``    ``fcy`` |float|                    yield stress under tension (``fty``) and compression (``fcy``) (see note 1)

#    ``bte``  ``bty``  ``bth``  ``bcy`` |float|    reduction rate for tensile elastic range (``bte``), tensile yielding (``bty``), tensile hardening (   ``bth``) and compressive yielding (``bcy``) (see note 1)

#    ``fcr`` |float|                               target point stress (see note 1)

#    ``ath`` |float|                               hardening strain ratio to yield strain

#    ===========================================   ===========================================================================



# .. note::



#     #. Input parameters are required to satisfy followings.



#        ``fcy`` < 0.0 <    ``fty``



#        0.0 <=    ``bty`` <    ``bth`` <    ``bte`` <= 1.0



#        0.0 <=    ``bcy`` <= 1.0



#        ``fcy`` <=    ``fcr`` <= 0.0



#        1.0 <=    ``ath``



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/AxialSpHD_Material>`_

#     """
#     uniqueArgs = []
#     if bty:
#         uniqueArgs.append(bte)
#         uniqueArgs.append(bty)
#         uniqueArgs.append(bth)
#         uniqueArgs.append(bcy)
#         uniqueArgs.append(fcr)
#         uniqueArgs.append(ath)
#     ops.uniaxialMaterial('AxialSpHD', matTag, sce, fty, fcy, *uniqueArgs)

# def PinchingLimitStateMaterial(matTag, dnodeT, nodeB, driftAxis, Kelas, crvTyp, crvTag, eleTag, b, d, h, a, st, As, Acc, ld, db, rhot, fc, fy, fyt):


#    MODE 2: Calibrated Model for Shear-Critical Concrete Columns



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``nodeT`` |int|                       integer node tag to define the first node at the extreme end of the associated flexural frame member (L3 or D5 in Figure)

#    ``nodeB`` |int|                       integer node tag to define the last node at the extreme end of the associated flexural frame member (L2 or D2 in Figure)

#    ``driftAxis`` |int|                   integer to indicate the drift axis in which lateral-strength degradation will occur. This axis should be orthogonal to the axis of measured rotation (see    ``rotAxis``` in Rotation Shear Curve definition)



#                                          ``driftAxis`` = 1 - Drift along the x-axis

#                                          ``driftAxis`` = 2 - Drift along the y-axis

#                                          ``driftAxis`` = 3 - Drift along the z-axis



#    ``Kelas`` |float|                     floating point value to define the shear stiffness (Kelastic) of the shear spring prior to shear failure



#                                          ``Kelas`` = -4 - Shear stiffness calculated assuming double curvature and shear springs at both column element ends



#                                          ``Kelas`` = -3 - Shear stiffness calculated assuming double curvature and a shear spring at one column element end



#                                          ``Kelas`` = -2 - Shear stiffness calculated assuming single curvature and shear springs at both column element ends



#                                          ``Kelas`` = -1 - Shear stiffness calculated assuming single curvature and a shear spring at one column element end



#                                          ``Kelas`` > 0 - Shear stiffness is the input value



#                                          Note: integer inputs allow the model to know whether column height equals the shear span (cantelever) or twice the shear span (double curvature). For columns in frames, input the value for the case that best approximates column end conditions or manually input shear stiffness (typically double curvature better estimates framed column behavior)

#    ``crvTag`` |int|                      integer tag for the unique limit curve object associated with this material

#    ``eleTag`` |int|                      integer element tag to define the associated beam-column element used to extract axial load

#    ``b`` |float|                         floating point column width (inches)

#    ``d`` |float|                         floating point column depth (inches)

#    ``h`` |float|                         floating point column height (inches)

#    ``a`` |float|                         floating point shear span length (inches)

#    ``st`` |float|                        floating point transverse reinforcement spacing (inches) along column height

#    ``As`` |float|                        floating point total area (inches squared) of longitudinal steel bars in section

#    ``Acc`` |float|                       floating point gross confined concrete area (inches squared) bounded by the transverse reinforcement in column section

#    ``ld`` |float|                        floating point development length (inches) of longitudinal bars using ACI 318-11 Eq. 12-1 and Eq. 12-2

#    ``db`` |float|                        floating point diameter (inches) of longitudinal bars in column section

#    ``rhot`` |float|                      floating point transverse reinforcement ratio (Ast/st.db)

#    ``f'c`` |float|                       floating point concrete compressive strength (ksi)

#    ``fy`` |float|                        floating point longitudinal steel yield strength (ksi)

#    ``fyt`` |float|                       floating point transverse steel yield strength (ksi)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Pinching_Limit_State_Material>`_

#     uniqueArgs = []
#     ops.uniaxialMaterial('PinchingLimitStateMaterial', matTag, dnodeT, nodeB, driftAxis, Kelas, crvTyp, crvTag, eleTag, b, d, h, a, st, As, Acc, ld, db, rhot, fc, fy, fyt, *uniqueArgs)

# def PinchingLimitStateMaterial(matTag, dnodeT, nodeB, driftAxis, Kelas, crvTyp, crvTag, eleTag, b, d, h, a, st, As, Acc, ld, db, rhot, fc, fy, fyt):


#    MODE 2: Calibrated Model for Shear-Critical Concrete Columns



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``nodeT`` |int|                       integer node tag to define the first node at the extreme end of the associated flexural frame member (L3 or D5 in Figure)

#    ``nodeB`` |int|                       integer node tag to define the last node at the extreme end of the associated flexural frame member (L2 or D2 in Figure)

#    ``driftAxis`` |int|                   integer to indicate the drift axis in which lateral-strength degradation will occur. This axis should be orthogonal to the axis of measured rotation (see    ``rotAxis``` in Rotation Shear Curve definition)



#                                          ``driftAxis`` = 1 - Drift along the x-axis

#                                          ``driftAxis`` = 2 - Drift along the y-axis

#                                          ``driftAxis`` = 3 - Drift along the z-axis



#    ``Kelas`` |float|                     floating point value to define the shear stiffness (Kelastic) of the shear spring prior to shear failure



#                                          ``Kelas`` = -4 - Shear stiffness calculated assuming double curvature and shear springs at both column element ends



#                                          ``Kelas`` = -3 - Shear stiffness calculated assuming double curvature and a shear spring at one column element end



#                                          ``Kelas`` = -2 - Shear stiffness calculated assuming single curvature and shear springs at both column element ends



#                                          ``Kelas`` = -1 - Shear stiffness calculated assuming single curvature and a shear spring at one column element end



#                                          ``Kelas`` > 0 - Shear stiffness is the input value



#                                          Note: integer inputs allow the model to know whether column height equals the shear span (cantelever) or twice the shear span (double curvature). For columns in frames, input the value for the case that best approximates column end conditions or manually input shear stiffness (typically double curvature better estimates framed column behavior)

#    ``crvTag`` |int|                      integer tag for the unique limit curve object associated with this material

#    ``eleTag`` |int|                      integer element tag to define the associated beam-column element used to extract axial load

#    ``b`` |float|                         floating point column width (inches)

#    ``d`` |float|                         floating point column depth (inches)

#    ``h`` |float|                         floating point column height (inches)

#    ``a`` |float|                         floating point shear span length (inches)

#    ``st`` |float|                        floating point transverse reinforcement spacing (inches) along column height

#    ``As`` |float|                        floating point total area (inches squared) of longitudinal steel bars in section

#    ``Acc`` |float|                       floating point gross confined concrete area (inches squared) bounded by the transverse reinforcement in column section

#    ``ld`` |float|                        floating point development length (inches) of longitudinal bars using ACI 318-11 Eq. 12-1 and Eq. 12-2

#    ``db`` |float|                        floating point diameter (inches) of longitudinal bars in column section

#    ``rhot`` |float|                      floating point transverse reinforcement ratio (Ast/st.db)

#    ``f'c`` |float|                       floating point concrete compressive strength (ksi)

#    ``fy`` |float|                        floating point longitudinal steel yield strength (ksi)

#    ``fyt`` |float|                       floating point transverse steel yield strength (ksi)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/Pinching_Limit_State_Material>`_

#     uniqueArgs = []
#     ops.uniaxialMaterial('PinchingLimitStateMaterial', matTag, dnodeT, nodeB, driftAxis, Kelas, crvTyp, crvTag, eleTag, b, d, h, a, st, As, Acc, ld, db, rhot, fc, fy, fyt, *uniqueArgs)

# def CFSWSWP(matTag, height, width, fut, tf, Ife, Ifi, ts, np, ds, Vs, sc, nc, type, openingArea, openingLength):
#     """


#    This command is used to construct a uniaxialMaterial model that simulates the hysteresis response (Shear strength-Lateral displacement) of a wood-sheathed cold-formed steel shear wall panel (CFS-SWP). The hysteresis model has smooth curves and takes into account the strength and stiffness degradation, as well as pinching effect.



#    This uniaxialMaterial gives results in Newton and Meter units, for strength and displacement, respectively.



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``height`` |float|                    SWP's height (mm)

#    ``width`` |float|                     SWP's width (mm)

#    ``fut`` |float|                       Tensile strength of framing members (MPa)

#    ``tf`` |float|                        Framing thickness (mm)

#    ``Ife`` |float|                       Moment of inertia of the double end-stud (mm4)

#    ``Ifi`` |float|                       Moment of inertia of the intermediate stud (mm4)

#    ``ts`` |float|                        Sheathing thickness (mm)

#    ``np`` |float|                        Sheathing number (one or two sides sheathed)

#    ``ds`` |float|                        Screws diameter (mm)

#    ``Vs`` |float|                        Screws shear strength (N)

#    ``sc`` |float|                        Screw spacing on the SWP perimeter (mm)

#    ``nc`` |float|                        Total number of screws located on the SWP perimeter

#    ``type`` |int|                        Integer identifier used to define wood sheathing type (DFP=1, OSB=2, CSP=3)

#    ``openingArea`` |float|               Total area of openings (mm2)

#    ``openingLength`` |float|             Cumulative length of openings (mm)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/CFSWSWP>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('CFSWSWP', matTag, height, width, fut, tf, Ife, Ifi, ts, np, ds, Vs, sc, nc, type, openingArea, openingLength, *uniqueArgs)

# def CFSSSWP(matTag, height, width, fuf, fyf, tf, Af, fus, fys, ts, np, ds, Vs, sc, dt, openingArea, openingLength):
#     """


#    This command is used to construct a uniaxialMaterial model that simulates the hysteresis response (Shear strength-lateral Displacement) of a Steel-Sheathed Cold-Formed Steel Shear Wall Panel (CFS-SWP). The hysteresis model has smooth curves and takes into account the strength and stiffness degradation, as well as pinching effect.



#    This uniaxialMaterial gives results in Newton and Meter units, for strength and displacement, respectively.



#    ===================================   ===========================================================================

#    ``matTag`` |int|                      integer tag identifying material

#    ``height`` |float|                    SWP's height (mm)

#    ``width`` |float|                     SWP's width (mm)

#    ``fuf`` |float|                       Tensile strength of framing members (MPa)

#    ``fyf`` |float|                       Yield strength of framing members (MPa)

#    ``tf`` |float|                        Framing thickness (mm)

#    ``Af`` |float|                        Framing cross section area (mm2)

#    ``fus`` |float|                       Tensile strength of steel sheet sheathing (MPa)

#    ``fys`` |float|                       Yield strength of steel sheet sheathing (MPa)

#    ``ts`` |float|                        Sheathing thickness (mm)

#    ``np`` |float|                        Sheathing number (one or two sides sheathed)

#    ``ds`` |float|                        Screws diameter (mm)

#    ``Vs`` |float|                        Screws shear strength (N)

#    ``sc`` |float|                        Screw spacing on the SWP perimeter (mm)

#    ``dt`` |float|                        Anchor bolt's diameter (mm)

#    ``openingArea`` |float|               Total area of openings (mm2)

#    ``openingLength`` |float|             Cumulative length of openings (mm)

#    ===================================   ===========================================================================



# .. seealso::





#    `Notes <http://opensees.berkeley.edu/wiki/index.php/CFSSSWP>`_

#     """
#     uniqueArgs = []
#     ops.uniaxialMaterial('CFSSSWP', matTag, height, width, fuf, fyf, tf, Af, fus, fys, ts, np, ds, Vs, sc, dt, openingArea, openingLength, *uniqueArgs)

