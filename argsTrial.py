# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 02:00:06 2022

@author: Christian
"""
import openseespy.opensees as op
import numpy as np 
# File Structure Modelcmds - > Element

# from populateSRC import getArgsFromTxt

import openseespyhint.getsrc.parseArgs as pa

# ('ElasticTimoshenkoBeam', eleTag, *eleNodes, E_mod, G_mod, Area, Iz, Avy, transfTag, <'-mass', massDens>, <'-cMass'>)
inputText1 = "element('ElasticTimoshenkoBeam', eleTag, *eleNodes, E_mod, G_mod, Area, Iz, Jxx, Iy, Iz, Avy, Avz, transfTag, <'-mass', massDens>, <'-cMass'>)"
solution1 = ['startTag', 'basic', 'basic', *['basic']*10, 'optional_group_start', 'optional_group_end', 'optional_group_tag']

args1       = pa.getArgsFromTxt(inputText1)
argTypes    = pa.parseAllArgs(args1)
solution    = np.array(solution1)
argTypes    = np.array(argTypes)
# print(solution)
# print(argTypes)
print(np.all(solution == argTypes))

inputText2 = "element('ElasticTimoshenkoBeam', eleTag, *eleNodes, E_mod, G_mod, Area, Iz, Avy, transfTag, <'-mass', massDens>, <'-cMass'>)"
solution2 = ['startTag', 'basic', 'basic', *['basic']*6,  'optional_group_start', 'optional_group_end', 'optional_group_tag']

args2       = pa.getArgsFromTxt(inputText2)
argTypes    = pa.parseAllArgs(args2)
solution    = np.array(solution2)
argTypes    = np.array(argTypes)
# print(solution)
# print(argTypes)

print(np.all(solution == argTypes))


InputText =  "element('zeroLength', eleTag, *eleNodes, '-mat', *matTags, '-dir', *dirs, <'-doRayleigh', rFlag=0>, <'-orient', *vecx, *vecyp>)"
solution  =  ['startTag', 'basic', 'basic', 'tag', 'tag_arg', 'tag', 'tag_arg',  'optional_group_start', 'optional_group_end', 'optional_group_start', 'optional_group_middle' , 'optional_group_end']

args        = pa.getArgsFromTxt(InputText)
argTypes    = pa.parseAllArgs(args)
solution    = np.array(solution)
argTypes    = np.array(argTypes)
# print(solution)
# print(argTypes)
print(np.all(solution == argTypes))


InputText =  " element('zeroLengthND', eleTag, *eleNodes, matTag, <uniTag>, <'-orient', *vecx, *vecyp>)"
solution  =  ['startTag', 'basic', 'basic', 'basic', 'optional_wrapped', 'optional_group_start', 'optional_group_middle' , 'optional_group_end']

args        = pa.getArgsFromTxt(InputText)
argTypes    = pa.parseAllArgs(args)
solution    = np.array(solution)
argTypes    = np.array(argTypes)
print(np.all(solution == argTypes))



InputText = "eleLoad('-ele', *eleTags, '-range', eleTag1, eleTag2, '-type', '-beamUniform', Wy, <Wz>, Wx=0.0, '-beamPoint', Py, <Pz>, xL, Px=0.0, '-beamThermal', *tempPts)"
solution  =  ['startTag',    'basic',  'tag',  'tag_arg','tag_arg', 'tag',  'tag',  'tag_arg', 'optional_wrapped','optional', 'tag','tag_arg', 'optional_wrapped','basic','optional','tag', 'tag_arg']

args        = pa.getArgsFromTxt(InputText)
argTypes    = pa.parseAllArgs(args)
solution    = np.array(solution)
argTypes    = np.array(argTypes)
print(np.all(solution == argTypes))


InputText = "element('SFI_MVLEM', eleTag,*eleNodes,m,c, '-thick',*thick,'-width',*widths,'-mat',*mat_tags)"
args        = pa.getArgsFromTxt(InputText)
argTypes    = pa.parseAllArgs(args)
argTypes    = np.array(argTypes)

InputText = "node(nodeTag, *crds, '-ndf', ndf, '-mass', *mass, '-disp', *disp, '-vel', *vel, '-accel', *accel)"
args        = pa.getArgsFromTxt(InputText)
argTypes    = pa.parseAllArgs(args)
argTypes    = np.array(argTypes)



InputText = "timeSeries('Path',tag,'-dt',dt=0.0,'-values',*values,'-time',*time,'-filePath',filePath='','-fileTime',fileTime='','-factor',factor=1.0,'-startTime',startTime=0.0,'-useLast','-prependZero')"
print()
args        = pa.getArgsFromTxt(InputText)
argTypes    = pa.parseAllArgs(args)
argTypes    = np.array(argTypes)



InputText = "model('basic', '-ndm', ndm, '-ndf', ndf=ndm*(ndm+1)/2)"
args        = pa.getArgsFromTxt(InputText)
argTypes    = pa.parseAllArgs(args)
argTypes    = np.array(argTypes)


# =============================================================================
# 
# =============================================================================


Nargs = len(argTypes)
argClasses = pa.setArgObjs(args, argTypes)

# Nargs = ;en()

defText  = []
funcText = []
intText  = []
for obj in argClasses:
    print(obj.text)
    defText.append(obj.getDefText())
    funcText.append(obj.getCallText())
    intText.append(obj.getIntermediateText())
print(argTypes)
# print(defText)
# print(funcText)

defText = [item for item in defText if 0 < len(item) ]
defText = '(' + ', '.join(defText) + ')'

funcText = [item for item in funcText if 0 < len(item) ]
funcText = '(' + ', '.join(funcText) + ', *uniqueArgs' + ')'


tagsInds = []
filteredText = []
for text in intText:
    # print(text)
    if 0 < len(text): 
        # print(text)
        filteredText = filteredText + text


a,b,c = pa.getFunctionText(InputText)

print(c)
print(funcText)





