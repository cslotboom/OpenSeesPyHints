import openseespy.opensees as ops

def Constant(tag, factor):
    """


   This command is used to construct a TimeSeries object in which the load factor applied remains constant and is independent of the time in the domain, i.e. :math:`\lambda = f(t) = C`.

      

   ================================   ===========================================================================

   ``tag`` |int|                      unique tag among TimeSeries objects.

   ``factor`` |float|                 the load factor applied (optional)

   ================================   ===========================================================================

    """
    uniqueArgs = []
    if factor=1.0:
        uniqueArgs.append('-factor')
    ops.timeSeries('Constant', tag, factor, *uniqueArgs)

def Linear(tag, factor, tStart):
    """


   This command is used to construct a TimeSeries object in which the load factor applied is linearly proportional to the time in the domain, i.e.



   :math:`\lambda = f(t) = cFactor * (t-tStart)`. (0 if t < tStart)



   ========================   =============================================================

   ``tag`` |int|              unique tag among TimeSeries objects

   ``factor`` |float|         Linear factor (optional)

   ``tStart`` |float|         start time (optional)

   ========================   =============================================================



    """
    uniqueArgs = []
    if factor=1.0:
        uniqueArgs.append('-factor')
    if tStart=0.0:
        uniqueArgs.append('-tStart')
    ops.timeSeries('Linear', tag, factor, tStart, *uniqueArgs)

def Trig(tag, tStart, tEnd, period, factor, shift, zeroShift):
    """


   This command is used to construct a TimeSeries object in which the load factor is some trigonemtric function of the time in the domain



   .. math::



      \lambda = f(t) = 

      \begin{cases}

          cFactor * sin(\frac{2.0\pi(t-tStart)}{period}+\phi), &  tStart<=t<=tEnd\\

          0.0, & otherwise

      \end{cases}



      \phi = shift - \frac{period}{2.0\pi} * \arcsin(\frac{zeroShift}{cFactor})



   ========================   =============================================================

   ``tag`` |int|              unique tag among TimeSeries objects.

   ``tStart`` |float|         Starting time of non-zero load factor.

   ``tEnd`` |float|           Ending time of non-zero load factor.

   ``period`` |float|         Characteristic period of sine wave.

   ``shift`` |float|          Phase shift in radians. (optional)

   ``factor`` |float|         Load factor. (optional)

   ``zeroShift`` |float|      Zero shift. (optional)

   ========================   =============================================================



    """
    uniqueArgs = []
    if factor=1.0:
        uniqueArgs.append('-factor')
    if shift=0.0:
        uniqueArgs.append('-shift')
    if zeroShift=0.0:
        uniqueArgs.append('-zeroShift')
    ops.timeSeries('Trig', tag, tStart, tEnd, period, factor, shift, zeroShift, *uniqueArgs)

def Triangle(tag, tStart, tEnd, period, factor, shift, zeroShift):
    """


   This command is used to construct a TimeSeries object in which the load factor is some triangular function of the time in the domain.

      

   .. math::



      \lambda = f(t) = 

      \begin{cases}

          slope*k*period+zeroShift, & k < 0.25\\

          cFactor-slope*(k-0.25)*period+zeroShift, & k < 0.75\\

          -cFactor+slope*(k-0.75)*period+zeroShift, & k < 1.0\\

          0.0, & otherwise

      \end{cases}



   .. math::

      

      slope = \frac{cFactor}{period/4}

      

      k = \frac{t+\phi-tStart}{period}-floor(\frac{t+\phi-tStart}{period})

      

      \phi = shift - \frac{zeroShift}{slope}



   ========================   =============================================================

   ``tag`` |int|              unique tag among TimeSeries objects.

   ``tStart`` |float|         Starting time of non-zero load factor.

   ``tEnd`` |float|           Ending time of non-zero load factor.

   ``period`` |float|         Characteristic period of sine wave.

   ``shift`` |float|          Phase shift in radians. (optional)

   ``factor`` |float|         Load factor. (optional)

   ``zeroShift`` |float|      Zero shift. (optional)

   ========================   =============================================================







    """
    uniqueArgs = []
    if factor=1.0:
        uniqueArgs.append('-factor')
    if shift=0.0:
        uniqueArgs.append('-shift')
    if zeroShift=0.0:
        uniqueArgs.append('-zeroShift')
    ops.timeSeries('Triangle', tag, tStart, tEnd, period, factor, shift, zeroShift, *uniqueArgs)

def Rectangular(tag, tStart, tEnd, factor):
    """
   

   This command is used to construct a TimeSeries object in which the load factor is constant for a specified period and 0 otherwise, i.e.



   .. math::



      \lambda = f(t) = 

      \begin{cases}

          cFactor, &  tStart<=t<=tEnd\\

          0.0, & otherwise

      \end{cases}



   ========================   =============================================================

   ``tag`` |int|              unique tag among TimeSeries objects.

   ``tStart`` |float|         Starting time of non-zero load factor.

   ``tEnd`` |float|           Ending time of non-zero load factor.

   ``factor`` |float|         Load factor. (optional)

   ========================   =============================================================

    """
    uniqueArgs = []
    if factor=1.0:
        uniqueArgs.append('-factor')
    ops.timeSeries('Rectangular', tag, tStart, tEnd, factor, *uniqueArgs)

def Pulse(tag, tStart, tEnd, period, width, shift, factor, zeroShift):
    """


   This command is used to construct a TimeSeries object in which the load factor is some pulse function of the time in the domain.



   .. math::



      \lambda = f(t) = 

      \begin{cases}

          cFactor+zeroShift, &  k < width\\

          zeroshift, & k < 1\\

          0.0, & otherwise

      \end{cases}



   .. math::



      k = \frac{t+shift-tStart}{period}-floor(\frac{t+shift-tStart}{period})



   ========================   =============================================================

   ``tag`` |int|              unique tag among TimeSeries objects.

   ``tStart`` |float|         Starting time of non-zero load factor.

   ``tEnd`` |float|           Ending time of non-zero load factor.

   ``period`` |float|         Characteristic period of pulse.

   ``width`` |float|          Pulse width as a fraction of the period. (optinal)

   ``shift`` |float|          Phase shift in seconds. (optional)

   ``factor`` |float|         Load factor. (optional)

   ``zeroShift`` |float|      Zero shift. (optional)

   ========================   =============================================================



    """
    uniqueArgs = []
    if width=0.5:
        uniqueArgs.append('-width')
    if shift=0.0:
        uniqueArgs.append('-shift')
    if factor=1.0:
        uniqueArgs.append('-factor')
    if zeroShift=0.0:
        uniqueArgs.append('-zeroShift')
    ops.timeSeries('Pulse', tag, tStart, tEnd, period, width, shift, factor, zeroShift, *uniqueArgs)

def Path(tag, dt, values=None, time=None, filePath, fileTime, factor, startTime):
    """


   The relationship between load

   factor and time is input by the user as a series of discrete points in

   the 2d space (load factor, time). The input points can come from a

   file or from a list in the script. When the time specified does not match

   any of the input points, linear interpolation is used between points.

   There are many ways to specify the load path, for example,

   the load factors set with ``values`` or ``filePath``,

   and the time set with ``dt``, ``time``, or ``fileTime``.



   ========================   =============================================================

   ``tag`` |int|              unique tag among TimeSeries objects.

   ``dt`` |float|             Time interval between specified points. (optional)

   ``values`` |listf|         Load factor values in a |list|. (optional)

   ``time`` |listf|           Time values in a |list|. (optional)

   ``filePath`` |str|         File containing the load factors values. (optional)

   ``fileTime`` |str|         File containing the time values for corresponding

                              load factors. (optional)

   ``factor`` |float|         A factor to multiply load factors by. (optional)

   ``startTime`` |float|      Provide a start time for provided load factors. (optional)

   ``'-useLast'`` |str|       Use last value after the end of the series. (optional)

   ``'-prependZero'`` |str|   Prepend a zero value to the series of load factors. (optional)

   ========================   =============================================================





   * Linear interpolation between points.

   * If the specified time is beyond last point (AND WATCH FOR NUMERICAL ROUNDOFF), 0.0 is returned. Specify ``'-useLast'`` to use the last data point instead of 0.0.

   * The transient integration methods in OpenSees assume zero initial conditions. So it is important that any timeSeries that is being used in a transient analysis` starts from zero (first data point in the timeSeries = 0.0). To guarantee that this is the case the optional parameter ``'-prependZero'`` can be specified to prepend a zero value to the provided TimeSeries.



    """
    uniqueArgs = []
    if dt=0.0:
        uniqueArgs.append('-dt')
    if values:
        uniqueArgs.append('-values')
        uniqueArgs.append(values)
    if time:
        uniqueArgs.append('-time')
        uniqueArgs.append(time)
    if filePath='':
        uniqueArgs.append('-filePath')
    if fileTime='':
        uniqueArgs.append('-fileTime')
    if factor=1.0:
        uniqueArgs.append('-factor')
    if startTime=0.0:
        uniqueArgs.append('-startTime')
    if '-prependZero':
        uniqueArgs.append('-useLast')
    if '-prependZero':
        uniqueArgs.append('-prependZero')
    ops.timeSeries('Path', tag, dt, filePath, fileTime, factor, startTime, *uniqueArgs)

