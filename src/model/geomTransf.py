import openseespy.opensees as ops

def Linear(transfTag, vecxz, dI=None, dJ=None):


   This command is used to construct a linear coordinate transformation (LinearCrdTransf) object, which performs a linear geometric transformation of beam stiffness and resisting force from the basic system to the global-coordinate system.



   ================================   ===========================================================================

   ``transfTag`` |int|                integer tag identifying transformation

   ``vecxz`` |listf|                  X, Y, and Z components of vecxz, the vector used

                                      to define the local x-z plane of the local-coordinate

                                      system. The local y-axis is defined by taking the

                                      cross product of the vecxz vector and the x-axis.

                                      These components are specified in the global-coordinate

                                      system X,Y,Z and define a vector that is in a plane

                                      parallel to the x-z plane of the local-coordinate

                                      system. These items need to be specified for the

                                      three-dimensional problem.

   ``dI`` |listf|                     joint offset values -- offsets specified with respect

                                      to the global coordinate system for element-end

                                      node i (the number of arguments depends on the

                                      dimensions of the current model).

   ``dJ`` |listf|                     joint offset values -- offsets specified with respect

                                      to the global coordinate system for element-end

                                      node j (the number of arguments depends on the

                                      dimensions of the current model).

   ================================   ===========================================================================

    uniqueArgs = []
    if dI:
        uniqueArgs.append('-jntOffset')
        uniqueArgs.append(dI)
        uniqueArgs.append(dJ)
    ops.geomTransf('Linear', transfTag, *vecxz, *uniqueArgs)

def Linear(transfTag, vecxz, dI=None, dJ=None):


   This command is used to construct a linear coordinate transformation (LinearCrdTransf) object, which performs a linear geometric transformation of beam stiffness and resisting force from the basic system to the global-coordinate system.



   ================================   ===========================================================================

   ``transfTag`` |int|                integer tag identifying transformation

   ``vecxz`` |listf|                  X, Y, and Z components of vecxz, the vector used

                                      to define the local x-z plane of the local-coordinate

                                      system. The local y-axis is defined by taking the

                                      cross product of the vecxz vector and the x-axis.

                                      These components are specified in the global-coordinate

                                      system X,Y,Z and define a vector that is in a plane

                                      parallel to the x-z plane of the local-coordinate

                                      system. These items need to be specified for the

                                      three-dimensional problem.

   ``dI`` |listf|                     joint offset values -- offsets specified with respect

                                      to the global coordinate system for element-end

                                      node i (the number of arguments depends on the

                                      dimensions of the current model).

   ``dJ`` |listf|                     joint offset values -- offsets specified with respect

                                      to the global coordinate system for element-end

                                      node j (the number of arguments depends on the

                                      dimensions of the current model).

   ================================   ===========================================================================

    uniqueArgs = []
    if dI:
        uniqueArgs.append('-jntOffset')
        uniqueArgs.append(dI)
        uniqueArgs.append(dJ)
    ops.geomTransf('Linear', transfTag, *vecxz, *uniqueArgs)

def PDelta(transfTag, vecxz, dI=None, dJ=None):


   This command is used to construct the P-Delta Coordinate Transformation (PDeltaCrdTransf) object, which performs a linear geometric transformation of beam stiffness and resisting force from the basic system to the global coordinate system, considering second-order P-Delta effects.







   ================================   ===========================================================================

   ``transfTag`` |int|                integer tag identifying transformation

   ``vecxz`` |listf|                  X, Y, and Z components of vecxz, the vector used

                                      to define the local x-z plane of the local-coordinate

                                      system. The local y-axis is defined by taking the

                                      cross product of the vecxz vector and the x-axis.

                                      These components are specified in the global-coordinate

                                      system X,Y,Z and define a vector that is in a plane

                                      parallel to the x-z plane of the local-coordinate

                                      system. These items need to be specified for the

                                      three-dimensional problem.

   ``dI`` |listf|                     joint offset values -- offsets specified with respect

                                      to the global coordinate system for element-end

                                      node i (the number of arguments depends on the

                                      dimensions of the current model).

   ``dJ`` |listf|                     joint offset values -- offsets specified with respect

                                      to the global coordinate system for element-end

                                      node j (the number of arguments depends on the

                                      dimensions of the current model).

   ================================   ===========================================================================



.. note::



   P LARGE Delta effects do not include P small delta effects.

    uniqueArgs = []
    if dI:
        uniqueArgs.append('-jntOffset')
        uniqueArgs.append(dI)
        uniqueArgs.append(dJ)
    ops.geomTransf('PDelta', transfTag, *vecxz, *uniqueArgs)

def PDelta(transfTag, vecxz, dI=None, dJ=None):


   This command is used to construct the P-Delta Coordinate Transformation (PDeltaCrdTransf) object, which performs a linear geometric transformation of beam stiffness and resisting force from the basic system to the global coordinate system, considering second-order P-Delta effects.







   ================================   ===========================================================================

   ``transfTag`` |int|                integer tag identifying transformation

   ``vecxz`` |listf|                  X, Y, and Z components of vecxz, the vector used

                                      to define the local x-z plane of the local-coordinate

                                      system. The local y-axis is defined by taking the

                                      cross product of the vecxz vector and the x-axis.

                                      These components are specified in the global-coordinate

                                      system X,Y,Z and define a vector that is in a plane

                                      parallel to the x-z plane of the local-coordinate

                                      system. These items need to be specified for the

                                      three-dimensional problem.

   ``dI`` |listf|                     joint offset values -- offsets specified with respect

                                      to the global coordinate system for element-end

                                      node i (the number of arguments depends on the

                                      dimensions of the current model).

   ``dJ`` |listf|                     joint offset values -- offsets specified with respect

                                      to the global coordinate system for element-end

                                      node j (the number of arguments depends on the

                                      dimensions of the current model).

   ================================   ===========================================================================



.. note::



   P LARGE Delta effects do not include P small delta effects.

    uniqueArgs = []
    if dI:
        uniqueArgs.append('-jntOffset')
        uniqueArgs.append(dI)
        uniqueArgs.append(dJ)
    ops.geomTransf('PDelta', transfTag, *vecxz, *uniqueArgs)

def Corotational(transfTag, vecxz):


   This command is used to construct the Corotational Coordinate Transformation (CorotCrdTransf) object. Corotational transformation can be used in large displacement-small strain problems.



   ================================   ===========================================================================

   ``transfTag`` |int|                integer tag identifying transformation

   ``vecxz`` |listf|                  X, Y, and Z components of vecxz, the vector used

                                      to define the local x-z plane of the local-coordinate

                                      system. The local y-axis is defined by taking the

                                      cross product of the vecxz vector and the x-axis.

                                      These components are specified in the global-coordinate

                                      system X,Y,Z and define a vector that is in a plane

                                      parallel to the x-z plane of the local-coordinate

                                      system. These items need to be specified for the

                                      three-dimensional problem.

   ``dI`` |listf|                     joint offset values -- offsets specified with respect

                                      to the global coordinate system for element-end

                                      node i (the number of arguments depends on the

                                      dimensions of the current model).

   ``dJ`` |listf|                     joint offset values -- offsets specified with respect

                                      to the global coordinate system for element-end

                                      node j (the number of arguments depends on the

                                      dimensions of the current model).

   ================================   ===========================================================================



.. note::



   Currently the transformation does not deal with element loads and will ignore any that are applied to the element.

    uniqueArgs = []
    ops.geomTransf('Corotational', transfTag, *vecxz, *uniqueArgs)

def Corotational(transfTag, vecxz):


   This command is used to construct the Corotational Coordinate Transformation (CorotCrdTransf) object. Corotational transformation can be used in large displacement-small strain problems.



   ================================   ===========================================================================

   ``transfTag`` |int|                integer tag identifying transformation

   ``vecxz`` |listf|                  X, Y, and Z components of vecxz, the vector used

                                      to define the local x-z plane of the local-coordinate

                                      system. The local y-axis is defined by taking the

                                      cross product of the vecxz vector and the x-axis.

                                      These components are specified in the global-coordinate

                                      system X,Y,Z and define a vector that is in a plane

                                      parallel to the x-z plane of the local-coordinate

                                      system. These items need to be specified for the

                                      three-dimensional problem.

   ``dI`` |listf|                     joint offset values -- offsets specified with respect

                                      to the global coordinate system for element-end

                                      node i (the number of arguments depends on the

                                      dimensions of the current model).

   ``dJ`` |listf|                     joint offset values -- offsets specified with respect

                                      to the global coordinate system for element-end

                                      node j (the number of arguments depends on the

                                      dimensions of the current model).

   ================================   ===========================================================================



.. note::



   Currently the transformation does not deal with element loads and will ignore any that are applied to the element.

    uniqueArgs = []
    ops.geomTransf('Corotational', transfTag, *vecxz, *uniqueArgs)

