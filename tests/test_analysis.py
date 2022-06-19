# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:06:21 2022

@author: Christian
"""

import openseespyhint as op
import openseespy.opensees as ops



ops.wipe()
op.model.basic(2, 3)

# ops.wipe()
# ops.node(1, *[0.,0.])

# import numpy as np

# constraints
# op.analysis.constraints
op.analysis.constraints.Plain()
op.analysis.constraints.Lagrange(0.2, 0.3)
op.analysis.constraints.Penalty(0.2, 0.3)
op.analysis.constraints.Transformation()

tol = 10.**-6
Niter = 20
op.analysis.test.NormUnbalance(tol, Niter)
op.analysis.test.NormDispIncr(tol, Niter)
op.analysis.test.EnergyIncr(tol, Niter)
op.analysis.test.RelativeNormUnbalance(tol, Niter)
# op.analysis.test.Re

op.analysis.test.NormDispAndUnbalance(tol, tol, Niter)
# ops.test('NormUnbalance',tol, Niter)
# ops.wipe()


op.analysis.algorithm.Linear()
op.analysis.algorithm.Newton()
op.analysis.algorithm.NewtonLineSearch()
op.analysis.algorithm.ModifiedNewton()
op.analysis.algorithm.KrylovNewton()
op.analysis.algorithm.SecantNewton()
op.analysis.algorithm.RaphsonNewton()
op.analysis.algorithm.PeriodicNewton()
op.analysis.algorithm.BFGS()
op.analysis.algorithm.Broyden()








coord = [1.,1.]
mass = [0.,0., 0.]
# ops.node(1, *coord,'-mass',  *mass)

op.model.node(1, coord,mass=mass)



incr = 1
nodeTag = 1
dof = 1
s = 1
alpha = 1
# op.analysis.analysis('Static')
# op.analysis.integrator.LoadControl(incr)
# op.analysis.integrator.DisplacementControl(nodeTag, dof, incr)
# op.analysis.integrator.ParallelDisplacementControl(nodeTag, dof, incr)
# op.analysis.integrator.MinUnbalDispNorm(1)
# op.analysis.integrator.ArcLength(s, alpha)]


# gamma = 1
# beta = 1
# op.analysis.analysis('Transient')

# op.analysis.integrator.Newmark(gamma, beta)


# op.utility.stop()
# op.utility.updateElementDomain()
# op.utility.updateMaterialStage(1, 1)
# op.utility.wipe()
# op.utility.wipeAnalysis()


# op.analysis.analysis('Transient')

# op.analysis.analysis.analysis('Static')
# op.analysis.analyze.

# ops.algorithm('Linear')

matTag = 1
Fy = 50.
E0 = 100.
b = 0.01
params = [15,.925,0.15]

a = [1.,1.,1.,1.]
# op.model.uniaxialMaterial.Steel02(matTag, Fy, E0, b, params, *a, sigInit=1.)
# ops.uniaxialMaterial('Steel02', matTag, Fy, E0, b, *params, *uniqueArgs)
ops.uniaxialMaterial('Steel02', matTag, Fy, E0, b, *params, 1*Fy/E0, 1.0, 1*Fy/E0, 1.0)


# ops.uniaxialMaterial('DowelType', 1, 90, 98.9, 4.3, 1.2, 1.09, 1.01, 0.21, 1.6, 1.32, 0, 0.66, '-exponential', 823, 0.02, 955, 10.7, 123)









# Transformation


# import openseespyhint.analysis as op

# op.analysis.analysis()
# op.model.model
# print(op.model)


# op.analysis.constraints.Plain()
# op.analysis.


# import openseespy.opensees as op

# op.wipe()
# op.model('basic', '-ndm', 2, '-ndf', 3)
# # op.model('ndm', 2)


# op.geomTransf('Linear', 1)

# op.node(1, *[0,0])
# op.node(2, *[1,0])
# op.node(3, *[0,0])
# massDens = 1
# # op.element('ElasticTimoshenkoBeam', eleTag, *eleNodes, E_mod, G_mod, Area, Iz, Avy, transfTag, *optionalArgs)
# op.element('ElasticTimoshenkoBeam',     1, *[1,2], 1., 1., 1., 1., 1., 1, '-cMass')


# op.wipe()
# op.model('basic', '-ndm', 3)

# matTag = 1
# op.uniaxialMaterial('Elastic', matTag, 10.**9)
# op.nDMaterial('ElasticIsotropic', 2, 10.**9,0.2)
# op.element('zeroLengthND', 2, *[1,3], 2)

