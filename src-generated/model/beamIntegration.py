import openseespy.opensees as ops

def Lobatto(tag, secTag, N):
    """


   Create a Gauss-Lobatto beamIntegration object.

   Gauss-Lobatto integration is the most common approach for evaluating the response of

   :ref:`forceBeamColumn-Element` (`Neuenhofer and Filippou 1997`_) because it places an integration point at each end of the element, where bending moments are largest in the absence of interior element loads.



   ========================   =============================================================

   ``tag`` |int|              tag of the beam integration.

   ``secTag`` |int|           A previous-defined section object.

   ``N`` |int|                Number of integration points along the element.

   ========================   =============================================================



    """
    uniqueArgs = []
    ops.beamIntegration('Lobatto', tag, secTag, N, *uniqueArgs)

def Legendre(tag, secTag, N):
    """


   Create a Gauss-Legendre beamIntegration object.

   Gauss-Legendre integration is more accurate than Gauss-Lobatto; however, it is not common

   in force-based elements because there are no integration points at the element ends.





   Places ``N`` Gauss-Legendre integration points along the element. The location and weight

   of each integration point are tabulated in references on numerical analysis.

   The force deformation response at each integration point is defined by the section.

   The order of accuracy for Gauss-Legendre integration is 2N-1.



   Arguments and examples see :ref:`Lobatto-BeamIntegration`.



    """
    uniqueArgs = []
    ops.beamIntegration('Legendre', tag, secTag, N, *uniqueArgs)

def NewtonCotes(tag, secTag, N):
    """


   Create a Newton-Cotes beamIntegration object.

   Newton-Cotes places integration points uniformly along the element, including a point at

   each end of the element.



   Places ``N`` Newton-Cotes integration points along the element. The weights for the uniformly

   spaced integration points are tabulated in references on numerical analysis. The force deformation

   response at each integration point is defined by the section.

   The order of accuracy for Gauss-Radau integration is N-1.



   Arguments and examples see :ref:`Lobatto-BeamIntegration`.



    """
    uniqueArgs = []
    ops.beamIntegration('NewtonCotes', tag, secTag, N, *uniqueArgs)

def Radau(tag, secTag, N):
    """


   Create a Gauss-Radau beamIntegration object.

   Gauss-Radau integration is not common in force-based elements because it places an integration point at only one end of the element; however, it forms the basis for optimal plastic

   hinge integration methods.



   Places ``N`` Gauss-Radau integration points along the element with a point constrained to be at ndI. The location and weight of each integration point are tabulated in references on

   numerical analysis. The force-deformation response at each integration point is defined

   by the section. The order of accuracy for Gauss-Radau integration is 2N-2.



   Arguments and examples see :ref:`Lobatto-BeamIntegration`.

    """
    uniqueArgs = []
    ops.beamIntegration('Radau', tag, secTag, N, *uniqueArgs)

def Trapezoidal(tag, secTag, N):
    """


   Create a Trapezoidal beamIntegration object.



   Arguments and examples see :ref:`Lobatto-BeamIntegration`.



    """
    uniqueArgs = []
    ops.beamIntegration('Trapezoidal', tag, secTag, N, *uniqueArgs)

def CompositeSimpson(tag, secTag, N):
    """


   Create a CompositeSimpson beamIntegration object.



   Arguments and examples see :ref:`Lobatto-BeamIntegration`.









    """
    uniqueArgs = []
    ops.beamIntegration('CompositeSimpson', tag, secTag, N, *uniqueArgs)

def UserDefined(tag, N, secTags, locs, wts):
    """


   Create a UserDefined beamIntegration object.

   This option allows user-specified locations and weights of the integration points.



   ========================   =============================================================

   ``tag`` |int|              tag of the beam integration

   ``N`` |int|                number of integration points along the element.

   ``secTags`` |listi|        A list previous-defined section objects.

   ``locs`` |listf|           Locations of integration points along the element.

   ``wts`` |listf|            weights of integration points.

   ========================   =============================================================



   ::



      locs = [0.1, 0.3, 0.5, 0.7, 0.9]

      wts = [0.2, 0.15, 0.3, 0.15, 0.2]

      secs = [1, 2, 2, 2, 1]

      beamIntegration('UserDefined',1,len(secs),*secs,*locs,*wts)



   Places ``N`` integration points along the element, which are defined in ``locs``

   on the natural domain [0, 1]. The weight of each integration point is

   defined in the ``wts`` also on the [0, 1] domain.

   The force-deformation response at each integration point

   is defined by the ``secs``. The ``locs``, ``wts``, and ``secs``

   should be of length ``N``. In general, there is no accuracy for this approach

   to numerical integration.









    """
    uniqueArgs = []
    ops.beamIntegration('UserDefined', tag, N, *secTags, *locs, *wts, *uniqueArgs)

def FixedLocation(tag, N, secTags, locs):
    """


   Create a FixedLocation beamIntegration object.

   This option allows user-specified locations of the integration points. The associated integration

   weights are computed by the method of undetermined coefficients (Vandermonde

   system)



   .. math::



      \sum^N_{i=1}x_i^{j-1}w_i = \int_0^1x^{j-1}dx = \frac{1}{j},\qquad (j=1,...,N)



   Note that :ref:`NewtonCotes-BeamIntegration` integration is recovered when the integration point locations are equally spaced.



   ========================   =============================================================

   ``tag`` |int|              tag of the beam integration

   ``N`` |int|                number of integration points along the element.

   ``secTags`` |listi|        A list previous-defined section objects.

   ``locs`` |listf|           Locations of integration points along the element.

   ========================   =============================================================





   Places ``N`` integration points along the element, whose locations are defined in ``locs``.

   on the natural domain [0, 1]. The force-deformation response at each integration

   point is defined by the ``secs``. Both the ``locs`` and ``secs``

   should be of length ``N``. The order of accuracy for Fixed Location integration is N-1.

    """
    uniqueArgs = []
    ops.beamIntegration('FixedLocation', tag, N, *secTags, *locs, *uniqueArgs)

def LowOrder(tag, N, secTags, locs, wts):
    """


   Create a LowOrder beamIntegration object.

   This option is a generalization of the :ref:`FixedLocation-BeamIntegration` and :ref:`UserDefined-BeamIntegration` integration approaches and is useful for moving load analysis (`Kidarsa, Scott and Higgins 2008`_). The locations of the integration points are user defined,

   while a selected number of weights are specified and the remaining weights are

   computed by the method of undetermined coefficients.



   .. math::



      \sum_{i=1}^{N_f}x_{fi}^{j-1}w_{fi}=\frac{1}{j}-\sum_{i=1}^{N_c}x_{ci}^{j-1}w_{ci}



   Note that :ref:`FixedLocation-BeamIntegration` integration is recovered when ``Nc`` is zero.



   ========================   =============================================================

   ``tag`` |int|              tag of the beam integration

   ``N`` |int|                number of integration points along the element.

   ``secTags`` |listi|        A list previous-defined section objects.

   ``locs`` |listf|           Locations of integration points along the element.

   ``wts`` |listf|            weights of integration points.

   ========================   =============================================================







   ::



      locs = [0.0, 0.2, 0.5, 0.8, 1.0]

      wts = [0.2, 0.2]

      secs = [1, 2, 2, 2, 1]

      beamIntegration('LowOrder',1,len(secs),*secs,*locs,*wts)



   Places ``N`` integration points along the element, which are defined in ``locs``.

   on the natural domain [0, 1]. The force-deformation response at each integration point is

   defined by the ``secs``. Both the ``locs`` and ``secs``

   should be of length ``N``. The ``wts`` at user-selected integration

   points are specified on [0, 1],

   which can be of length ``Nc`` equals ``0`` up to ``N``. These specified weights

   are assigned to the first ``Nc`` entries in the ``locs`` and ``secs``, respectively. The

   order of accuracy for Low Order integration is N-Nc-1.



   .. note::



      ``Nc`` is determined from the length of the ``wts`` list. Accordingly,

      :ref:`FixedLocation-BeamIntegration`

      integration is recovered when ``wts`` is an empty list and

      :ref:`UserDefined-BeamIntegration` integration is

      recovered when the ``wts`` and ``locs`` lists are of equal length.









    """
    uniqueArgs = []
    ops.beamIntegration('LowOrder', tag, N, *secTags, *locs, *wts, *uniqueArgs)

def MidDistance(tag, N, secTags, locs):
    """


   Create a MidDistance beamIntegration object.

   This option allows user-specified locations of the integration points. The associated integration weights are determined from the midpoints between adjacent integration point locations.

   :math:`w_i=(x_{i+1}-x_{i-1})/2` for :math:`i=2...N-1`, :math:`w_1=(x_1+x_2)/2`, and :math:`w_N=1-(x_{N-1}+x_N)/2`.



   ========================   =============================================================

   ``tag`` |int|              tag of the beam integration

   ``N`` |int|                number of integration points along the element.

   ``secTags`` |listi|        A list previous-defined section objects.

   ``locs`` |listf|           Locations of integration points along the element.

   ========================   =============================================================



   ::



      locs = [0.0, 0.2, 0.5, 0.8, 1.0]

      secs = [1,2,2,2,1]

      beamIntegration('MidDistance',1,len(secs),*secs,*locs)





   Places ``N`` integration points along the element, whose locations are defined

   in ``locs`` on the natural domain [0, 1].

   The force-deformation response at each integration

   point is defined by the ``secs``.

   Both the ``locs`` and ``secs`` should be of length N.

   This integration rule can only integrate constant

   functions exactly since the sum of the integration weights is one.



   For the ``locs`` shown above, the associated integration weights

   will be ``[0.15, 0.2, 0.3, 0.2, 0.15]``.











    """
    uniqueArgs = []
    ops.beamIntegration('MidDistance', tag, N, *secTags, *locs, *uniqueArgs)

def UserHinge(tag, secETag, npL, secsLTags, locsL, wtsL, npR, secsRTags, locsR, wtsR):
    """


   Create a UserHinge beamIntegration object.



   ========================   ============================================================================

   ``tag`` |int|              tag of the beam integration

   ``secETag`` |int|             A previous-defined section objects for non-hinge area.

   ``npL`` |int|              number of integration points along the left hinge.

   ``secsLTags`` |listi|          A list of previous-defined section objects for left hinge area.

   ``locsL`` |listf|          A list of locations of integration points for left hinge area.

   ``wtsL`` |listf|           A list of weights of integration points for left hinge area.

   ``npR`` |int|              number of integration points along the right hinge.

   ``secsRTags`` |listi|          A list of previous-defined section objects for right hinge area.

   ``locsR`` |listf|          A list of locations of integration points for right hinge area.

   ``wtsR`` |listf|           A list of weights of integration points for right hinge area.

   ========================   ============================================================================



   ::



      tag = 1

      secE = 5

      

      npL = 2

      secsL = [1,2]

      locsL = [0.1,0.2]

      wtsL = [0.5,0.5]

      

      npR = 2

      secsR = [3,4]

      locsR = [0.8,0.9]

      wtsR = [0.5,0.5]



      beamIntegration('UserHinge',tag,secE,npL,*secsL,*locsL,*wtsL,npR,*secsR,*locsR,*wtsR)









    """
    uniqueArgs = []
    ops.beamIntegration('UserHinge', tag, secETag, npL, *secsLTags, *locsL, *wtsL, npR, *secsRTags, *locsR, *wtsR, *uniqueArgs)

def HingeMidpoint(tag, secI, lpI, secJ, lpJ, secE):
    """


   Create a HingeMidpoint beamIntegration object.

   Midpoint integration over each hinge region is the most accurate one-point integration rule;

   however, it does not place integration points at the element ends and there is a small integration

   error for linear curvature distributions along the element.



   ========================   ============================================================================

   ``tag`` |int|              tag of the beam integration.

   ``secI`` |int|             A previous-defined section object for hinge at I.

   ``lpI`` |float|            The plastic hinge length at I.

   ``secJ`` |int|             A previous-defined section object for hinge at J.

   ``lpJ`` |float|            The plastic hinge length at J.

   ``secE`` |int|             A previous-defined section object for the element interior.

   ========================   ============================================================================



   The plastic hinge length at end I (J) is equal to ``lpI`` (``lpJ``) and the associated force deformation response is defined by the ``secI`` (``secJ``). The force deformation

   response of the element interior is defined by the ``secE``.

   Typically, the interior section is linear-elastic, but this is not necessary.





   ::



      lpI = 0.1

      lpJ = 0.2

      beamIntegration('HingeMidpoint',tag,secI,lpI,secJ,lpJ,secE)









    """
    uniqueArgs = []
    ops.beamIntegration('HingeMidpoint', tag, secI, lpI, secJ, lpJ, secE, *uniqueArgs)

def HingeRadau(tag, secI, lpI, secJ, lpJ, secE):
    """


   Create a HingeRadau beamIntegration object.

   Modified two-point Gauss-Radau integration over each hinge region places an integration point at

   the element ends and at 8/3 the hinge length inside the element. This approach represents

   linear curvature distributions exactly and the characteristic length for softening plastic hinges is equal to the assumed palstic hinge length.



   Arguments and examples see :ref:`HingeMidPoint-BeamIntegration`.



    """
    uniqueArgs = []
    ops.beamIntegration('HingeRadau', tag, secI, lpI, secJ, lpJ, secE, *uniqueArgs)

def HingeRadauTwo(tag, secI, lpI, secJ, lpJ, secE):
    """


   Create a HingeRadauTwo beamIntegration object.

   Two-point Gauss-Radau integration over each hinge region places an integration

   point at the element ends and at 2/3 the hinge length inside the element. This approach

   represents linear curvature distributions exactly; however, the characteristic length for softening

   plastic hinges is not equal to the assumed plastic hinge length (equals 1/4 of the plastic hinge length).



   Arguments and examples see :ref:`HingeMidPoint-BeamIntegration`.



    """
    uniqueArgs = []
    ops.beamIntegration('HingeRadauTwo', tag, secI, lpI, secJ, lpJ, secE, *uniqueArgs)

def HingeEndpoint(tag, secI, lpI, secJ, lpJ, secE):
    """


   Create a HingeEndpoint beamIntegration object.

   Endpoint integration over each hinge region moves the integration points to the element ends;

   however, there is a large integration error for linear curvature distributions along the element.



   ========================   ============================================================================

   ``tag`` |int|              tag of the beam integration.

   ``secI`` |int|             A previous-defined section object for hinge at I.

   ``lpI`` |float|            The plastic hinge length at I.

   ``secJ`` |int|             A previous-defined section object for hinge at J.

   ``lpJ`` |float|            The plastic hinge length at J.

   ``secE`` |int|             A previous-defined section object for the element interior.

   ========================   ============================================================================



   Arguments and examples see :ref:`HingeMidPoint-BeamIntegration`.



    """
    uniqueArgs = []
    ops.beamIntegration('HingeEndpoint', tag, secI, lpI, secJ, lpJ, secE, *uniqueArgs)

