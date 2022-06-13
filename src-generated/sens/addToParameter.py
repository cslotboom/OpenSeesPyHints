import openseespy.opensees as ops

def tag(tag, specific parameter args=None):
    """
   In case that more objects (e.g., element, section) are mapped to an existing parameter,

   the  command can be used to relate these additional objects to the specific parameter.



   ==============================   ===========================================================================

   ``tag`` |int|                    integer tag identifying the parameter.

   ``<specific parameter args>``    depend on the object in the FE model encapsulating the desired parameters.

   ==============================   ===========================================================================





    """
    uniqueArgs = []
    if specific parameter args:
        uniqueArgs.append(specific parameter args)
    ops.addToParameter(tag, *uniqueArgs)

