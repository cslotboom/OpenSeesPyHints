import openseespy.opensees as ops

def type(type, tag):
   This commmand is used to remove components from the model.



   ========================   ===========================================================================

   ``type`` |str|             type of the object, ``'ele'``, ``'loadPattern'``, ``'parameter'``, ``'node'``, ``'timeSeries'``, ``'sp'``, ``'mp'``.

   ``tag`` |int|              tag of the object

   ========================   ===========================================================================





    uniqueArgs = []
    ops.remove(type, tag, *uniqueArgs)

def recorders():


   Remove all recorder objects.





    uniqueArgs = []
    ops.remove('recorders', *uniqueArgs)

def sp(nodeTag, dofTag, patternTag):


   Remove a sp object based on node



   ========================   ===========================================================================

   ``nodeTag`` |int|          node tag

   ``dof`` |int|              dof the sp constrains

   ``patternTag`` |int|       pattern tag, (optional)

   ========================   ===========================================================================

    uniqueArgs = []
    ops.remove('sp', nodeTag, dofTag, patternTag, *uniqueArgs)

