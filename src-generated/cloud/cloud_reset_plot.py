import openseespy.opensees as ops

def xLabel(xLabel, yLabel, labels):
    """
   This command is used to reset the :doc:`PlotModule` with labels.



   ========================   ===========================================================================

   ``xLabel`` |str|           the string for the label of x axis.

   ``yLabel`` |str|           the string for the label of y axis.

   ``labels`` |lists|         a list of ticks to be shown instead of x values.

   ========================   ===========================================================================





.. note::



   This must be the first command to call in :doc:`PlotModule`.

    """
    uniqueArgs = []
    ops.reset_plot(xLabel, yLabel, labels, *uniqueArgs)

