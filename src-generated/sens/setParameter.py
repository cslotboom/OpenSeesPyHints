import openseespy.opensees as ops

def val(newValue, eleTags=None, start=None, end=None, args=None):
    """
   set value for an element parameter



   ==============================   ===========================================================================

   ``newValue`` |float|             the updated value to which the parameter needs to be set.

   ``eleTags`` |listi|              a list of element tags

   ``start`` |int|                  start element tag 

   ``end`` |int|                    end element tag 

   ``args`` |lists|                 a list of strings for the element parameter

   ==============================   ===========================================================================







    """
    uniqueArgs = []
    if eleTags:
        uniqueArgs.append('-ele')
        uniqueArgs.append(*eleTags)
    if start:
        uniqueArgs.append('-eleRange')
        uniqueArgs.append(start)
        uniqueArgs.append(end)
    if args:
        uniqueArgs.append(*args)
    ops.setParameter('-val', newValue, *uniqueArgs)

