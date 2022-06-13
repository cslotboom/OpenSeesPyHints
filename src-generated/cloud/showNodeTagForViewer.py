import openseespy.opensees as ops

def on(on):
    """
   This command is used to turn on and off

   the display of node tags cloud viewer.



   ========================   ===========================================================================

   ``on`` |bool|              `True` - turn on, `False` - turn off

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.showNodeTagForViewer(on, *uniqueArgs)

