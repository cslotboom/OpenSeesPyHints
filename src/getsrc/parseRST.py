# -*- coding: utf-8 -*-
"""
Created on Sun May 29 21:25:27 2022

@author: Christian
"""


import os
import numpy as np
rstDir = 'rst'
cmdIdentifier = 'cmds.' # finds command rst files
tocIdentifier = '.. toctree::' # finds the TOC in the RST file
tabIdentifier = '\t'
tabReplacement = '        '
functionIdentifier = '.. function::' # finds the TOC in the RST file
argText = ', '
argText = ','
tabText = '    '
headingIdentifier = '====='



def getRstFilePaths(rstDir):
    files = os.listdir(rstDir)
    filePaths = [os.path.join(rstDir, file) for file in files if '.rst' in file]
    return files, filePaths


# =============================================================================
# Read TOC files
# =============================================================================

def getCmdPaths(files):

    cmdPaths = [file for file in files if cmdIdentifier in file]
    return cmdPaths

def readFile(cmdPath):
    
    with open(cmdPath, encoding='utf-8') as f:
        
        cmdFileTxt = f.readlines()
    return cmdFileTxt


def checkIfTOC(fileTxt):
    """
    Finds where the TOC Identifer is in the input text is for the input
    """
    
    tocIndicies = []
    tocIndex = 0
    isToc = False
    for line in fileTxt:
        if tocIdentifier in line:
            # print(line)
            isToc = True
            tocIndicies.append(tocIndex)
            
        tocIndex+=1
    
    return isToc, tocIndicies

# ???: old
def getTOCIndex(fileTxt):
    """
    Finds where the TOC Identifer is in the input text is for the input
    """
    
    tocIndex = 0
    for line in fileTxt:
        if tocIdentifier in line:
            # print(line)
            break
        tocIndex+=1
    
    return tocIndex


def getTocEntries(cmdTocTxt, tocIndex):

    entries = []
    splitInd = (tocIndex + 1)
    # print(cmdTocTxt[splitInd:])
    for line in cmdTocTxt[splitInd:]:
        item = line.split('\n')[0]
        # print(item)
        if  1 < len(item) :
            entries.append(item.strip(tabText))
    # print(item)
    return entries




# =============================================================================
# Read individual files
# =============================================================================



def getFunctionDefinitionInd(functionFileText):
    """
    Finds where the actual function. This is used for the definition and the 
    function call statement.
    """
    funcInd = 0
    # for line in functionFileText:
        
    #     if functionIdentifier in line:
    #         # print(funcInd)
    #         break
    #     funcInd+=1
    # return funcInd
    
    fileText = np.array(functionFileText)
    # print(fileText)
    condition = np.char.find(fileText, functionIdentifier)
    Inds = np.where(condition == 0)[0]
    return Inds



def getFunctionArgs(functionFileText, funcInd):
    """
    Parses the input text for the function arguements.
    """
    tmp = functionFileText[funcInd]
    return getArgsFromTxt(tmp)


def getArgsFromTxt(text):
    """
    Parses the input text for the function arguements.
    """
    tmp = text.split('(')
    tmp = tmp[1].split(')')[0]
    arguments = tmp.split(argText)
    arguments = [arg.strip(' ') for arg in arguments]
    return arguments




def getDocstring(functionFileText,funcInd):

    baseText  = functionFileText[(funcInd+1):]
    return getDocstringFromTxt(baseText)



def getDocstringFromTxt(test):
    docstring = ['"""\n', *test, '"""\n']
    docstring = [tabText + text for text in docstring]
    return docstring  

def findNargDefs(text):
    inds = []
    ii = 0
    for line in text:
        if headingIdentifier in line:
            # print(line)
            inds.append(ii)
        ii +=1
    return inds


def getDocstringText(rstText, funcInds, offset = 2):
    """
    rstText:  A list that contains the rst text file broken up by lines.
    funcInds: The indexes where hte function text is stored.
    """
    
    docstrings = []
    
    Nargs = len(funcInds) 
    # print(Nargs)
    if Nargs == 0:
        return ['Error, no docstring found']
    
    # If there is only one docstring, make the whole function up the end the docstring
    if Nargs == 1:
        Ind = funcInds[0] + offset
        docstring = rstText[Ind:]
        docstring = [tabText + '"""'] + docstring + [tabText + '"""']
        docstrings.append(docstring)
    
    # If there is only more than one function in the file, each funciton gets it's own docstring.
    else:
        for ii in range(Nargs):
            ind1 = funcInds[ii] + offset
            if ii < Nargs - 1:
                ind2 = funcInds[ii+1]
                docstring = rstText[ind1:ind2]
            else:
                docstring = rstText[ind1:]
            docstrings.append(docstring)
            docstring = [tabText + '"""'] + docstring + [tabText + '"""']
    return docstrings
        
 

def cleanDocstring(docstring, identifier = tabIdentifier, replacement = tabReplacement):
    
    nline = len(docstring)
    for ii in range(nline):
        # print()
        # line = docstring[ii]
        docstring[ii] = docstring[ii].replace(identifier, replacement)
    return docstring






rstTabText = '   '
tabText2 = rstTabText*2

def parseTocForFunctionFiles(rstText, functionFiles, currentInd):
    # currentInd = ind + tocOffset
    while rstTabText in rstText[currentInd] and not tabText2 in rstText[currentInd]:
        
        # Remove the leading space and trailing break.
        funcName = rstText[currentInd].strip('\n ')
        functionFiles.append(funcName)
        currentInd += 1
    return functionFiles







