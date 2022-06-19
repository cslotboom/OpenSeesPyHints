import openseespy.opensees as ops

def rNodeTag(rNodeTag, cNodeTag, numDOF, rcdofs):
    """
   Create a multi-point constraint between nodes.



              

   ========================   ===========================================================================

   ``rNodeTag`` |int|         integer tag identifying the retained, or master node.

   ``cNodeTag`` |int|         integer tag identifying the constrained, or slave node.

   ``numDOF`` |int|           number of dofs to be constrained

   ``rcdofs`` |listi|         nodal degrees-of-freedom that are constrained at the

                              cNode to be the same as those at the rNode

                              Valid range is from 1 through

                              ndf, the number of nodal degrees-of-freedom.



                              ``rcdofs = [rdof1, cdof1, rdof2, cdof2, ...]``

   ========================   ===========================================================================





    """
    uniqueArgs = []
    ops.equalDOF_Mixed(rNodeTag, cNodeTag, numDOF, *rcdofs, *uniqueArgs)

def rNodeTag(rNodeTag, cNodeTag, numDOF, rcdofs):
    """
   Create a multi-point constraint between nodes.



              

   ========================   ===========================================================================

   ``rNodeTag`` |int|         integer tag identifying the retained, or master node.

   ``cNodeTag`` |int|         integer tag identifying the constrained, or slave node.

   ``numDOF`` |int|           number of dofs to be constrained

   ``rcdofs`` |listi|         nodal degrees-of-freedom that are constrained at the

                              cNode to be the same as those at the rNode

                              Valid range is from 1 through

                              ndf, the number of nodal degrees-of-freedom.



                              ``rcdofs = [rdof1, cdof1, rdof2, cdof2, ...]``

   ========================   ===========================================================================





    """
    uniqueArgs = []
    ops.equalDOF_Mixed(rNodeTag, cNodeTag, numDOF, *rcdofs, *uniqueArgs)

def perpDirn(perpDirn, rNodeTag, cNodeTags):
    """
   Create a multi-point constraint between nodes.

   These objects will constraint certain degrees-of-freedom at the listed slave nodes to move as if in a rigid plane with the master node. To enforce this constraint, ``Transformation``

   constraint is recommended. 



              

   ========================   ===========================================================================

   ``perpDirn`` |int|         direction perpendicular to the rigid plane (i.e. direction 3 corresponds to the 1-2 plane)

   ``rNodeTag`` |int|         integer tag identifying the master node

   ``cNodeTags`` |listi|      integar tags identifying the slave nodes

   ========================   ===========================================================================





    """
    uniqueArgs = []
    ops.rigidDiaphragm(perpDirn, rNodeTag, *cNodeTags, *uniqueArgs)

def type(type, rNodeTag, cNodeTag):
    """
   Create a multi-point constraint between nodes.

              

   ========================   ===========================================================================

   ``type`` |str|             string-based argument for rigid-link type:



                              * ``'bar'``: only the translational degree-of-freedom will be constrained to be exactly the same as those at the master node

                              * ``'beam'``: both the translational and rotational degrees of freedom are constrained.

   ``rNodeTag`` |int|         integer tag identifying the master node

   ``cNodeTag`` |int|         integar tag identifying the slave node

   ========================   ===========================================================================





    """
    uniqueArgs = []
    ops.rigidLink(type, rNodeTag, cNodeTag, *uniqueArgs)

