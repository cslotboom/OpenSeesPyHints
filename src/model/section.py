import openseespy.opensees as ops

def Elastic(secTag, E_mod, A, Iz, Iy, G_mod, Jxx, alphaY, alphaZ):


   This command allows the user to construct an ElasticSection. The inclusion of shear deformations is optional. The dofs for 2D elastic section are ``[P, Mz]``,

   for 3D are ``[P,Mz,My,T]``.



   ================================   ===========================================================================

   ``secTag`` |int|                   unique section tag

   ``E_mod`` |float|                  Young's Modulus

   ``A`` |float|                      cross-sectional area of section

   ``Iz`` |float|                     second moment of area about the local z-axis

   ``Iy`` |float|                     second moment of area about the local y-axis

                                      (required for 3D analysis)

   ``G_mod`` |float|                  Shear Modulus (optional for 2D analysis,

                                      required for 3D analysis)

   ``Jxx`` |float|                    torsional moment of inertia of section

                                      (required for 3D analysis)

   ``alphaY`` |float|                 shear shape factor along the local y-axis (optional)

   ``alphaZ`` |float|                 shear shape factor along the local z-axis (optional)

   ================================   ===========================================================================





.. note::



   The elastic section can be used in the nonlinear beam column elements, which is useful in the initial stages of developing a complex model.

    uniqueArgs = []
    ops.section('Elastic', secTag, E_mod, A, Iz, Iy, G_mod, Jxx, alphaY, alphaZ, *uniqueArgs)

def Elastic(secTag, E_mod, A, Iz, Iy, G_mod, Jxx, alphaY, alphaZ):


   This command allows the user to construct an ElasticSection. The inclusion of shear deformations is optional. The dofs for 2D elastic section are ``[P, Mz]``,

   for 3D are ``[P,Mz,My,T]``.



   ================================   ===========================================================================

   ``secTag`` |int|                   unique section tag

   ``E_mod`` |float|                  Young's Modulus

   ``A`` |float|                      cross-sectional area of section

   ``Iz`` |float|                     second moment of area about the local z-axis

   ``Iy`` |float|                     second moment of area about the local y-axis

                                      (required for 3D analysis)

   ``G_mod`` |float|                  Shear Modulus (optional for 2D analysis,

                                      required for 3D analysis)

   ``Jxx`` |float|                    torsional moment of inertia of section

                                      (required for 3D analysis)

   ``alphaY`` |float|                 shear shape factor along the local y-axis (optional)

   ``alphaZ`` |float|                 shear shape factor along the local z-axis (optional)

   ================================   ===========================================================================





.. note::



   The elastic section can be used in the nonlinear beam column elements, which is useful in the initial stages of developing a complex model.

    uniqueArgs = []
    ops.section('Elastic', secTag, E_mod, A, Iz, Iy, G_mod, Jxx, alphaY, alphaZ, *uniqueArgs)

def Fiber(secTag, torsionMatTag=None):


   This command allows the user to construct a FiberSection object. Each FiberSection object is composed of Fibers, with each fiber containing a UniaxialMaterial, an area and a location (y,z). The dofs for 2D section are ``[P, Mz]``,

   for 3D are ``[P,Mz,My,T]``.



   ================================   ===========================================================================

   ``secTag`` |int|                   unique section tag

   ``torsionMatTag`` |int|            uniaxialMaterial tag assigned to the section

                                      for torsional response (can be nonlinear)

   ================================   ===========================================================================



.. note::





   #. The commands below should be called after the section command to generate all the fibers in the section.

   #. The patch and layer commands can be used to generate multiple fibers in a single command.





Commands to generate all fibers:



#. :doc:`fiber`

#. :doc:`patch`

#. :doc:`layer`

      

.. toctree::

   :maxdepth: 2

   :hidden:



   fiber

   patch

   layer

    uniqueArgs = []
    if torsionMatTag:
        uniqueArgs.append('-torsion')
        uniqueArgs.append(torsionMatTag)
    ops.section('Fiber', secTag, *uniqueArgs)

def Fiber(secTag, torsionMatTag=None):


   This command allows the user to construct a FiberSection object. Each FiberSection object is composed of Fibers, with each fiber containing a UniaxialMaterial, an area and a location (y,z). The dofs for 2D section are ``[P, Mz]``,

   for 3D are ``[P,Mz,My,T]``.



   ================================   ===========================================================================

   ``secTag`` |int|                   unique section tag

   ``torsionMatTag`` |int|            uniaxialMaterial tag assigned to the section

                                      for torsional response (can be nonlinear)

   ================================   ===========================================================================



.. note::





   #. The commands below should be called after the section command to generate all the fibers in the section.

   #. The patch and layer commands can be used to generate multiple fibers in a single command.





Commands to generate all fibers:



#. :doc:`fiber`

#. :doc:`patch`

#. :doc:`layer`

      

.. toctree::

   :maxdepth: 2

   :hidden:



   fiber

   patch

   layer

    uniqueArgs = []
    if torsionMatTag:
        uniqueArgs.append('-torsion')
        uniqueArgs.append(torsionMatTag)
    ops.section('Fiber', secTag, *uniqueArgs)

def FiberThermal(secTag, GJ):
    """


   This command create a FiberSectionThermal object.

   The dofs for 2D section are ``[P, Mz]``,

   for 3D are ``[P,Mz,My]``.





.. note::





   #. The commands below should be called after the section command to generate all the fibers in the section.

   #. The patch and layer commands can be used to generate multiple fibers in a single command.



Commands to generate all fibers:



#. :doc:`fiber`

#. :doc:`patch`

#. :doc:`layer`
    """
    uniqueArgs = []
    if GJ=0.0:
        uniqueArgs.append('-GJ')
    ops.section('FiberThermal', secTag, GJ, *uniqueArgs)

def NDFiber(secTag):
    """


   This command allows the user to construct an NDFiberSection object. Each NDFiberSection object is composed of NDFibers, with each fiber containing an NDMaterial, an area, and a location (y,z). The NDFiberSection works for 2D and 3D frame elements and it queries the NDMaterial of each fiber for its axial and shear stresses. In 2D, stress components 11 and 12 are obtained from each fiber in order to provide stress resultants for axial force, bending moment, and shear ``[P, Mz, Vy]``. Stress components 11, 12, and 13 lead to all six stress resultants in 3D ``[P, Mz, Vy, My, Vz, T]``.



   The NDFiberSection works with any NDMaterial via wrapper classes that perform static condensation of the stress vector down to the 11, 12, and 13 components, or via specific NDMaterial subclasses that implement the appropriate fiber stress conditions.



   ================================   ===========================================================================

   ``secTag`` |int|                   unique section tag

   ================================   ===========================================================================



.. note::





   #. The commands below should be called after the section command to generate all the fibers in the section.

   #. The patch and layer commands can be used to generate multiple fibers in a single command.



#. :func:`fiber`

#. :func:`patch`

#. :func:`layer`

    """
    uniqueArgs = []
    ops.section('NDFiber', secTag, *uniqueArgs)

def WFSection2d(secTag, matTag, d, tw, bf, tf, Nfw, Nff):
    """


   This command allows the user to construct a WFSection2d object, which is an encapsulated fiber representation of a wide flange steel section appropriate for plane frame analysis.



   ================================   ===========================================================================

   ``secTag`` |int|                   unique section tag

   ``matTag`` |int|                   tag of uniaxialMaterial assigned to each fiber

   ``d`` |float|                      section depth

   ``tw`` |float|                     web thickness

   ``bf`` |float|                     flange width

   ``tf`` |float|                     flange thickness

   ``Nfw`` |float|                    number of fibers in the web

   ``Nff`` |float|                    number of fibers in each flange

   ================================   ===========================================================================



.. note::



   The section dimensions ``d``, ``tw``, ``bf``, and ``tf`` can be found in the AISC steel manual.

    """
    uniqueArgs = []
    ops.section('WFSection2d', secTag, matTag, d, tw, bf, tf, Nfw, Nff, *uniqueArgs)

def RCSection2d(secTag, coreMatTag, coverMatTag, steelMatTag, d, b, cover_depth, Atop, Abot, Aside, Nfcore, Nfcover, Nfs):
    """


   This command allows the user to construct an RCSection2d object, which is an encapsulated fiber representation of a rectangular reinforced concrete section with core and confined regions of concrete and single top and bottom layers of reinforcement appropriate for plane frame analysis.



   ================================   ===========================================================================

   ``secTag`` |int|                   unique section tag

   ``coreMatTag`` |int|               tag of uniaxialMaterial assigned to each fiber in the core region

   ``coverMatTag`` |int|              tag of uniaxialMaterial assigned to each fiber in the cover region

   ``steelMatTag`` |int|              tag of uniaxialMaterial assigned to each reinforcing bar

   ``d`` |float|                      section depth

   ``b`` |float|                      section width

   ``cover_depth`` |float|            cover depth (assumed uniform around perimeter)

   ``Atop`` |float|                   area of reinforcing bars in top layer

   ``Abot`` |float|                   area of reinforcing bars in bottom layer

   ``Aside`` |float|                  area of reinforcing bars on intermediate layers

   ``Nfcore`` |float|                 number of fibers through the core depth

   ``Nfcover`` |float|                number of fibers through the cover depth

   ``Nfs`` |float|                    number of bars on the top and bottom rows of reinforcement (Nfs-2 bars will be placed on the side rows)

   ================================   ===========================================================================



.. note::



   For more general reinforced concrete section definitions, use the Fiber Section command.

    """
    uniqueArgs = []
    ops.section('RCSection2d', secTag, coreMatTag, coverMatTag, steelMatTag, d, b, cover_depth, Atop, Abot, Aside, Nfcore, Nfcover, Nfs, *uniqueArgs)

def RCCircularSection(secTag, coreMatTag, coverMatTag, steelMatTag, d, cover_depth, Ab, NringsCore, NringsCover, Nwedges, Nsteel, GJ <or '-torsion'=None, matTag=None):
    """


   This command allows the user to construct an RCCircularSection object, which is an encapsulated fiber representation of a circular reinforced concrete section with core and confined regions of concrete.



   ================================   ===========================================================================

   ``secTag`` |int|                   unique section tag

   ``coreMatTag`` |int|               tag of uniaxialMaterial assigned to each fiber in the core region

   ``coverMatTag`` |int|              tag of uniaxialMaterial assigned to each fiber in the cover region

   ``steelMatTag`` |int|              tag of uniaxialMaterial assigned to each reinforcing bar

   ``d`` |float|                      section radius

   ``cover_depth`` |float|            cover depth (assumed uniform around perimeter)

   ``Ab`` |float|                     area of each reinforcing bar

   ``NringsCore`` |int|               number of fiber rings in the core

   ``NringsCover`` |int|              number of fiber rings in the cover

   ``Nwedges`` |int|                  number of fiber wedges for the section

   ``Nsteel`` |int|                   number of reinforcing bars

   ``GJ`` |float|                     secton torsional stiffness

   ``matTag`` |int|                   tag of uniaxialMaterial assigned to section torsion response

   ================================   ===========================================================================



.. note::



   One of the -GJ or the -torsion inputs is required

   

   For more general reinforced concrete section definitions, use the Fiber Section command.

    """
    uniqueArgs = []
    if GJ <or '-torsion':
        uniqueArgs.append('-GJ')
        uniqueArgs.append(GJ <or '-torsion')
        uniqueArgs.append(matTag)
    ops.section('RCCircularSection', secTag, coreMatTag, coverMatTag, steelMatTag, d, cover_depth, Ab, NringsCore, NringsCover, Nwedges, Nsteel, *uniqueArgs)

def Parallel(secTag, SecTags):
    """


   Connect sections in parallel.



   ================================   ===========================================================================

   ``secTag`` |int|                   unique section tag

   ``SecTags`` |listi|                tags of of predefined sections.

   ================================   ===========================================================================

    """
    uniqueArgs = []
    ops.section('Parallel', secTag, *SecTags, *uniqueArgs)

def Aggregator(secTag, mats, sectionTag=None):
    """


   This command is used to construct a SectionAggregator object which aggregates groups previously-defined UniaxialMaterial objects into a single section force-deformation model. Each UniaxialMaterial object represents the section force-deformation response for a particular section degree-of-freedom (dof). There is no interaction between responses in different dof directions. The aggregation can include one previously defined section.



   ================================   ===========================================================================

   ``secTag`` |int|                   unique section tag

   ``mats`` |list|                    list of tags and dofs of previously-defined

                                      UniaxialMaterial objects,

                                      ``mats = [matTag1,dof1,matTag2,dof2,...]``



                                      the force-deformation quantity to be modeled by

                                      this section object. One of the following section

                                      dof may be used:



                                      * ``'P'`` Axial force-deformation

                                      * ``'Mz'`` Moment-curvature about section local z-axis

                                      * ``'Vy'`` Shear force-deformation along section local y-axis

                                      * ``'My'`` Moment-curvature about section local y-axis

                                      * ``'Vz'`` Shear force-deformation along section local z-axis

                                      * ``'T'`` Torsion Force-Deformation

   ``sectionTag`` |int|               tag of previously-defined Section object to which the UniaxialMaterial objects are aggregated as additional force-deformation relationships (optional)

   ================================   ===========================================================================

    """
    uniqueArgs = []
    if sectionTag:
        uniqueArgs.append('-section')
        uniqueArgs.append(sectionTag)
    ops.section('Aggregator', secTag, *mats, *uniqueArgs)

def Uniaxial(secTag, matTag, quantity):
    """


   This command is used to construct a UniaxialSection object which uses a previously-defined UniaxialMaterial object to represent a single section force-deformation response quantity.



   ================================   ===========================================================================

   ``secTag`` |int|                   unique section tag

   ``matTag`` |int|                   tag of uniaxial material

   ``quantity`` |str|                 the force-deformation quantity to be modeled by

                                      this section object. One of the following section

                                      dof may be used:



                                      * ``'P'`` Axial force-deformation

                                      * ``'Mz'`` Moment-curvature about section local z-axis

                                      * ``'Vy'`` Shear force-deformation along section local y-axis

                                      * ``'My'`` Moment-curvature about section local y-axis

                                      * ``'Vz'`` Shear force-deformation along section local z-axis

                                      * ``'T'`` Torsion Force-Deformation

   ================================   ===========================================================================

    """
    uniqueArgs = []
    ops.section('Uniaxial', secTag, matTag, quantity, *uniqueArgs)

def ElasticMembranePlateSection(secTag, E_mod, nu, h, rho):
    """


   This command allows the user to construct an ElasticMembranePlateSection object, which is an isotropic section appropriate for plate and shell analysis.



   ================================   ===========================================================================

   ``secTag`` |int|                   unique section tag

   ``E_mod`` |float|                      Young's Modulus

   ``nu`` |float|                     Poisson's Ratio

   ``h`` |float|                      depth of section

   ``rho`` |float|                    mass density

   ================================   ===========================================================================

    """
    uniqueArgs = []
    ops.section('ElasticMembranePlateSection', secTag, E_mod, nu, h, rho, *uniqueArgs)

def PlateFiber(secTag, matTag, h):
    """


   This command allows the user to construct a MembranePlateFiberSection object, which is a section that numerically integrates through the plate thickness with "fibers" and is appropriate for plate and shell analysis.



   ================================   ===========================================================================

   ``secTag`` |int|                   unique section tag

   ``matTag`` |int|                   nDMaterial tag to be assigned to each fiber

   ``h`` |float|                      plate thickness

   ================================   ===========================================================================

    """
    uniqueArgs = []
    ops.section('PlateFiber', secTag, matTag, h, *uniqueArgs)

def Bidirectional(secTag, E_mod, Fy, Hiso, Hkin, code1, code2):
    """


   This command allows the user to construct a Bidirectional section, which is a stress-resultant plasticity model of two coupled forces. The yield surface is circular and there is combined isotropic and kinematic hardening.



   ================================   ===========================================================================

   ``secTag`` |int|                   unique section tag

   ``E_mod`` |float|                      elastic modulus

   ``Fy`` |float|                     yield force

   ``Hiso`` |float|                   isotropic hardening modulus

   ``Hkin`` |float|                   kinematic hardening modulus

   ``code1`` |str|                    section force code for direction 1 (optional)

   ``code2`` |str|                    section force code for direction 2 (optional)



                                      One of the following section

                                      code may be used:



                                      * ``'P'`` Axial force-deformation

                                      * ``'Mz'`` Moment-curvature about section local z-axis

                                      * ``'Vy'`` Shear force-deformation along section local y-axis

                                      * ``'My'`` Moment-curvature about section local y-axis

                                      * ``'Vz'`` Shear force-deformation along section local z-axis

                                      * ``'T'`` Torsion Force-Deformation

   ================================   ===========================================================================

    """
    uniqueArgs = []
    ops.section('Bidirectional', secTag, E_mod, Fy, Hiso, Hkin, code1, code2, *uniqueArgs)

def Isolator2spring(matTag, tol, k1, Fyo, k2o, kvo, hb, PE, Po):
    """


   This command is used to construct an Isolator2spring section object, which represents the buckling behavior of an elastomeric bearing for two-dimensional analysis in the lateral and vertical plane. An Isolator2spring section represents the resultant force-deformation behavior of the bearing, and should be used with a zeroLengthSection element. The bearing should be constrained against rotation.



   ================================   ===========================================================================

   ``secTag`` |int|                   unique section tag

   ``tol`` |float|                    tolerance for convergence of the element state. Suggested value: E-12 to E-10. OpenSees will warn if convergence is not achieved, however this usually does not prevent global convergence.

   ``k1`` |float|                     initial stiffness for lateral force-deformation

   ``Fyo`` |float|                    nominal yield strength for lateral force-deformation

   ``k2o`` |float|                    nominal postyield stiffness for lateral force-deformation

   ``kvo`` |float|                    nominal stiffness in the vertical direction

   ``hb`` |float|                     total height of elastomeric bearing

   ``PE`` |float|                     Euler Buckling load for the bearing

   ``Po`` |float|                     axial load at which nominal yield strength is achieved (optional)

   ================================   ===========================================================================

    """
    uniqueArgs = []
    ops.section('Isolator2spring', matTag, tol, k1, Fyo, k2o, kvo, hb, PE, Po, *uniqueArgs)

def LayeredShell(sectionTag, nLayers, mats):
    """


   This command will create the section of the multi-layer shell element, including the multi-dimensional concrete, reinforcement material and the corresponding thickness.



   ================================   ===========================================================================

   ``sectionTag`` |int|               unique tag among sections

   ``nLayers`` |int|                  total numbers of layers

   ``mats`` |list|                    a list of material tags and thickness, ``[[mat1,thk1], ..., [mat2,thk2]]``

   ================================   ===========================================================================

    """
    uniqueArgs = []
    ops.section('LayeredShell', sectionTag, nLayers, *mats, *uniqueArgs)

