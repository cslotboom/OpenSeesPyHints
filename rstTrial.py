# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 23:09:48 2022

@author: Christian
"""

import os
import numpy as np

import openseespyhint.getsrc.parseRST as pr
import openseespyhint.getsrc.parseArgs as pa



headingIdentifier = '   ====='
srcDir = 'src-generated'

rstDir = 'rst'
tocOffset = 4
rstTabText = '   '
tabText2 = rstTabText*2

# Get all possible files
rstFiles, rstFilePaths = pr.getRstFilePaths(rstDir)

# Seperate command TOCs
cmdPaths = pr.getCmdPaths(rstFilePaths)

# manually remove the visfiles
cmdPaths.remove('rst\\ops_vis_fib_sec_list_to_cmds.rst')
cmdPaths.remove('rst\\plotcmds.rst')

# Iterate through all the possible command groups
for cmdPath in cmdPaths:

    # Get the name of the command file
    cmdName = cmdPath.strip('.rst')
    cmdName = cmdName.strip('\\')
    cmdName = cmdName[:-3]
    
    # Get the name of the output folder and make it
    oCmdFolder = os.path.join(srcDir, cmdName)
    os.makedirs(oCmdFolder, exist_ok=True)
    
    # Readad the command TOC file and get the text
    cmdTocTxt = pr.readFile(cmdPath)
    istoc, indexes = pr.checkIfTOC(cmdTocTxt)
    
    # Read the TOC file
    tocIndex = indexes[0] + 3
    tocEntries = pr.getTocEntries(cmdTocTxt, tocIndex)
    
    # For each command TOC, read the sub TOC files    
    for tocEntry in tocEntries:
        
        # Get the file name
        path = os.path.join(rstDir, tocEntry+ '.rst')
        rstText = pr.readFile(path)
        rstText.append('')
        
        # Initialize varialbes that will be used to contain extracted text
        docstrings = {}
        arguments = {}      # contains the function arguments
        functions = []      # contains the function name
        defLines = {}       # contains the function defition
        intLines = {}       # intermediate text needed for special arguments
        callLines = {}      # Contains the final function call
        functionFiles = []  # Contains all the function files.
    
    
        # Generate the first line of the file
        outText = 'import openseespy.opensees as ops' + '\n' + '\n' 
    
        # Check if the current file is also a TOC.
        istoc, indexes = pr.checkIfTOC(rstText)    
        
        # Find all the entries in the current TOC
        for ind in indexes:
            currentInd = ind + tocOffset
            functionFiles = pr.parseTocForFunctionFiles(rstText, functionFiles, currentInd)
        
                
        # If the the entry isn't a TOC, read functions from the index file the file
        if not istoc:
            functionFiles = [tocEntry]
            print(tocEntry)
            print('not toc')
        
        # If the file is a TOC
        for file in functionFiles:
            # Get the input and output directory paths
            ipath = os.path.join(rstDir, file + '.rst')
            opath = os.path.join(srcDir, file + '.rst')
            
            # read the rst text
            rstText = pr.readFile(ipath)
        
            # Find where the function definiton is:
            Inds = pr.getFunctionDefinitionInd(rstText)
            funcDocstrings = pr.getDocstringText(rstText, Inds)
    
            # parse the arguments and generate the text
            Nind = len(Inds)
            for ii in range(Nind):
                Ind = Inds[ii]
                args = pr.getArgsFromTxt(rstText[Ind])
                
                funcText = rstText[Ind].split(".. function:: ")[1]
                funcText = funcText.strip("\n")
                
                # print(funcText)
                defLine, interText, funcText = pa.getFunctionText(funcText)
                
                funcName = args[0].strip('"')
                funcName = funcName.strip("'")
                functions.append(funcName)
                defLines[funcName] = defLine
                intLines[funcName] = interText
                callLines[funcName] = funcText
                arguments[funcName] = rstText[Ind]
                docstrings[funcName] = pr.cleanDocstring(funcDocstrings[ii])
                
        # The name of the output file in the TOC
        tocFile = os.path.join(srcDir, cmdName, tocEntry + '.py')
        print(functions)
        for function in functions:
            outTextTmp = defLines[function] + docstrings[function] + intLines[function] + callLines[function]
            outTextTmp = '\n'.join(outTextTmp)
            outTextTmp += '\n'
            outTextTmp += '\n'
            # print(outText)
            outText += outTextTmp
        # print()
        
        # with tocFile as 
        with open(tocFile, 'w',encoding='utf-8') as f:
            f.write(outText)
    

    
# inds = []
# ii = 0
# for line in rstText:
#     if headingIdentifier in line:
#         print(line)
#         inds.append(ii)
#     ii +=1





# if there is only one function, then the docstring is the start of that funciton to the end.
# If there is more than one function, then either:
    # There are multiple docstrings
    # There are 
    

        
        
        
        # print(funcName)
# for each entry in the command TOC, find the sub-page
# - there may be more than one page
# - there may be more than one page
# - there may be more than one page

# Create a folder for each top level command file

# for each sub page, check if the page is a TOC

# If it is a TOC
# - create a directory in the cmd folder for the TOC entry
# - Extract all entries in the TOC.
# - For each entry, create a function for all functions in the file. (see function)


# If it isn't a TOC, extract all functions text from the file
# - check how many functions are in each file, parse each function into a 
# - for the raw text in each functon, extract the arguements
    # - Find optional tags, i.e. 'sp'
    # - Find optional arguements <- how will this work
    
# - check how many functions are in each file
