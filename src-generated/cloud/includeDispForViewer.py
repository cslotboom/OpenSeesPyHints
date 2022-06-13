import openseespy.opensees as ops

def on(on):
    """
   This command is used to turn on and off

   whether the displacement is included in

   the viewer.



   ========================   ===========================================================================

   ``on`` |bool|              - `True` - include displacement,

                              - `False` - not include displacement

   ========================   ===========================================================================

    """
    uniqueArgs = []
    ops.includeDispForViewer(on, *uniqueArgs)

