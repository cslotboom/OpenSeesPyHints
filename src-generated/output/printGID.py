import openseespy.opensees as ops

def filename(filename, startEle=None, endEle=None):
    """
   Print in GID format.



   ========================   ===========================================================================

   ``filename`` |str|         output file name.

   ``'-append'`` |str|        append to existing file. (optional)

   ``startEle`` |int|         start element tag. (optional)

   ``endEle`` |int|           end element tag. (optional)

   ========================   ===========================================================================

    """
    uniqueArgs = []
    if '-eleRange':
        uniqueArgs.append('-append')
    if startEle:
        uniqueArgs.append('-eleRange')
        uniqueArgs.append(startEle)
        uniqueArgs.append(endEle)
    ops.printGID(filename, *uniqueArgs)

