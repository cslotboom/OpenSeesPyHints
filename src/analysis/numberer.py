import openseespy.opensees as ops

def Plain():
    """

    This command is used to construct a Plain degree-of-freedom numbering object
    to provide the mapping between the degrees-of-freedom at the nodes and the 
    equation numbers. A Plain numberer just takes whatever order the domain 
    gives it nodes and numbers them, this ordering is both dependent on node 
    numbering and size of the model.

    .. note::

        For very small problems and for the sparse matrix solvers which provide 
        their own numbering scheme, order is not really important so plain numberer 
        is just fine. For large models and analysis using solver types other than 
        the sparse solvers, the order will have a major impact on performance of 
        the solver and the plain handler is a poor choice.

    Hints:
        untested

    """
    ops.numberer('Plain')

def RCM():
    """

    This command is used to construct an RCM degree-of-freedom numbering object 
    to provide the mapping between the degrees-of-freedom at the nodes and the 
    equation numbers. An RCM numberer uses the reverse Cuthill-McKee scheme 
    to order the matrix equations.

    Hints:
        untested

    """

    ops.numberer('RCM')

def AMD():
    """

    This command is used to construct an AMD degree-of-freedom numbering object 
    to provide the mapping between the degrees-of-freedom at the nodes and the 
    equation numbers. An AMD numberer uses the approximate minimum degree 
    scheme to order the matrix equations.

    Hints:
        untested

    """

    ops.numberer('AMD')

def ParallelPlain():
    """

    This command is used to construct a parallel version
    
    of Plain degree-of-freedom numbering object to provide the mapping between 
    the degrees-of-freedom at the nodes and the equation numbers. A Plain 
    numberer just takes whatever order the domain gives it nodes and numbers 
    them, this ordering is both dependent on node numbering and size of the 
    model.
    
    Use this command only for parallel model.

    .. warning::

        Don't use this command if model is not parallel, for example,
        parametric study.

    Hints:
        untested

    """

    ops.numberer('ParallelPlain')

def ParallelRCM():
    """
    This command is used to construct a parallel versionof RCM degree-of-freedom
    numbering object to provide the mapping between the degrees-of-freedom at 
    the nodes and the equation numbers. A Plain numberer just takes whatever 
    order the domain gives it nodes and numbers them, this ordering is both 
    dependent on node numbering and size of the model.
    
    Use this command only for parallel model.

    .. warning::

        Don't use this command if model is not parallel, for example, parametric study.

    Hints:
        untested

    """

    ops.numberer('ParallelRCM')

