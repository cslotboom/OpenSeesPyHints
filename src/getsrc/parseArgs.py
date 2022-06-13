cmdIdentifier = 'cmds.' # finds command rst files
tocIdentifier = '.. toctree::' # finds the TOC in the RST file
tocIdentifier = '   \n'

tabIdentifier = '\t'
tabReplacement = '    '

functionIdentifier = '.. function::' # finds the TOC in the RST file

argText = ', '
tabText = '    '
tabText2 = tabText*2

currentArg = None
lastArg = None


def getArgsFromTxt(text):
    """
    Parses the input text for the function arguements.
    """
    tmp = text.split('(')
    tmp = tmp[1].split(')')[0]
    arguments = tmp.split(',')
    arguments = [arg.strip(' ') for arg in arguments]
    return arguments


def getGroupName(text):
    tmp = text.split('(')
    return tmp[0]


def _checkStart(arg, text):
    """
    Checks the start of an arguemetn for generic text
    """
    if arg[0] == text:
        return True
    return False


def _checkIn(arg, text):
    """
    Checks the start of an arguemetn for generic text
    """
    if text in arg:
        return True
    return False

def _checkEnd(arg, text):
    """
    Checks the start of an arguemetn for generic text
    """
    if arg[-1] == text:
        return True
    return False

def checkIfOptionalArg(arg):
    """
    Finds out if the argument is an optional argument.
    """
    return _checkIn(arg, '=')

def checkIfOptionalWrapped(arg):
    """
    Finds out if the argument is an optional argument.
    """
    return _checkIn(arg, '-')


def checkIfOptionalArgGroupStart(arg):
    """
    Finds the first variable of a optional argue group, i.e.
    <'-mass', massDens>
    """
    return _checkStart(arg, '<')
        
def checkIfOptionalArgGroupEnd(arg):
    """
    Finds the first variable of a optional argue group, i.e.
    <'-mass', massDens>
    """     
    return _checkEnd(arg,'>')       

def checkIfCollapsedArg(arg):
    return _checkStart(arg, '*')

def checkIfTag(arg):
    """
    Find Tags. These indicate either 
        - the command type, if at the start of a function
        - Optional arguments, if in the middle
        - 
    """
    return _checkStart(arg, "'")



# All arguments need to be checked if they are condensed.
argTypes = ['basic', 'tag', 'startTag', 'tag_arg', 'optional', 'optional_wrapped', 'optional_group_start',
            'optional_group_middle','optional_group_end','optional_group_tag']

def parseArgType(arg, lastArgType):
    
    # Check if the argument is a tag. Start tags are special.
    # print(arg)
    if checkIfTag(arg):
        if lastArgType is None:
            return 'startTag'
        return 'tag'

    # optinal group checks checks
    isStart = checkIfOptionalArgGroupStart(arg)
    isEnd = checkIfOptionalArgGroupEnd(arg)
    
    # If there is only one item contained, then it's a tag.
    if isStart and isEnd:
        if checkIfOptionalWrapped(arg):
            return 'optional_group_tag'
        return 'optional_wrapped'
    
    # Check if optional group start
    if isStart:
        return 'optional_group_start'
    
    if isEnd:
        return 'optional_group_end'
    
    # check if it's a middle argument looking at the last argument.
    if lastArgType == 'optional_group_start' or lastArgType =='optional_group_middle':
        return 'optional_group_middle'
    
    if checkIfOptionalArg(arg):
        return 'optional'    
    
    # tag and tag arguments
    if lastArgType:
        if 'tag' in lastArgType:
            return 'tag_arg'
     
    return 'basic'



    

def parseAllArgs(args):

    lastArguement = None
    argType = None
    argTypes = []

    for currentArg in args:
        # print(currentArg)
        # print(lastArguement)
        argType = parseArgType(currentArg, lastArguement)
        argTypes.append(argType)
        lastArguement = argType
        # print(currentArg)
    return argTypes



# =============================================================================
# Arg Class
# =============================================================================


# Check if collapsed.
argTypes = ['basic', 'tag', 'startTag', 'tag_arg', 'optional', 'optional_wrapped', 'optional_group_start',
            'optional_group_middle','optional_group_end','optional_group_tag']

class Argument:
    
    def __init__(self, argText, nextArg):
        pass
        
    def getDefText(self):
        """
        Test Docsting
        """
        pass
        
    def getIntermediateText(self) -> list:
        pass

    def getCallText(self):
        pass


class basicArgument(Argument):
    argType = 'basic'
    def __init__(self, argText, nextArg):
        self.text = argText
    
    def getDefText(self):
        
        # remove the expansion tag in the definition.
        return self.text.strip('*')
        
    def getIntermediateText(self):
        return ''

    def getCallText(self):
        return self.text

class tagArgument(Argument):
    argType = 'tag'
    
    def __init__(self, argText, nextArg):
        self.text = argText
        self.nextArg = nextArg
        
    def getDefText(self):
        # No definition Text
        return ''
        
    def getIntermediateText(self):
        
        # If the next object is a tag, we assume this is a lone tag
        if self.nextArg == self.argType:
            return [tabText + f'if {self.text.strip("*")}:', 
                     tabText2 + f'uniqueArgs.append({self.text})']
        
        # If were're at teh final argument, the text must be a flag/lone tag
        if not self.nextArg:
            return [tabText + f'if {self.text.strip("*")}:', 
                     tabText2 + f'uniqueArgs.append({self.text})']
        
        # If the next argument is anything else, then we check for it instead
        # of the flag in the append
        return  [tabText + f'if {self.nextArg.strip("*")}:', 
                 tabText2 + f'uniqueArgs.append({self.text})']

    def getCallText(self):
        # Note, this is passed in through uniqueArgs

        return ''
        # return self.text

class startTagArgument(Argument):
    argType = 'startTag'
    
    def __init__(self, argText, nextArg):
        self.text = argText
    
    def getDefText(self):
        # No definition Text
        return ''
        
    def getIntermediateText(self):
        return ''

    def getCallText(self):
        return self.text


class tagArgArgument(Argument):
    """
    The unique argument that follows a tag
    """
    argType = 'tag_arg'
    
    def __init__(self, argText, nextArg):
        self.text = argText
        self.nextArg = nextArg
    def getDefText(self):
        baseArg = self.text.strip('*')
        # return baseArg 
        return baseArg + "=None"
    
    def getIfText(self):
        baseArg = self.text.strip('*')
        return [f'if {baseArg}' + ':']
        
    def getIntermediateText(self):
        baseArg = self.text.strip('*')
        return [tabText2 + f"uniqueArgs.append({baseArg})"]

    def getCallText(self):
        # Note, this is passed in through uniqueArgs
        # return self.text 
        return ''

class optionalArgument(Argument):
    """
    The unique argument that follows a tag
    """
    argType = 'optional'
    
    def __init__(self, argText, nextArg):
        self.text = argText.split("=")[0]

    def getDefText(self):
        # return self.text + "=None"
        return self.text
        
    def getIntermediateText(self):
        return ''

    def getCallText(self):
        return self.text

class optionalWrappedArgument(Argument):
    """
    The unique argument that follows a tag
    """
    argType = 'optional_wrapped'
    
    def __init__(self, argText, nextArg):
        self.text = argText.strip('<>')

    def getDefText(self):
        return self.text.strip('*') + "=None"
        # return self.text.strip('*')
        
    def getIntermediateText(self):
        return  [tabText  + f'if {self.text.strip("*")}:', 
                 tabText2 + f'uniqueArgs.append({self.text})']

    def getCallText(self):
        return ''
        # return self.text

  
class optionalGroupStartArgument(Argument):
    """
    The unique argument that follows a tag.
    """
    argType = 'optional_group_start'
    
    def __init__(self, argText, nextArg):
        self.text = argText.strip('<')
        self.nextArg = nextArg.strip('>')

    def getDefText(self):
        return ''
        
    def getIntermediateText(self):
        return [tabText + f'if {self.nextArg.strip("*")}:',
                tabText2 + f"uniqueArgs.append({self.text})"]

    def getCallText(self):
        # return self.text
        return ''
  
class optionalGroupMiddleArgument(Argument):
    """
    The unique argument that follows a tag.
    """
    argType = 'optional_group_middle'
    
    def __init__(self, argText, nextArg):
        self.text = argText

    def getDefText(self):
        return self.text.strip('*')  + "=None"
        
    def getIntermediateText(self):
        return [tabText2 + f"uniqueArgs.append({self.text})"]

    def getCallText(self):
        # Note, this is passed in through uniqueArgs
        return ''

class optionalGroupMiddle(Argument):
    """
    The unique argument that follows a tag.
    """
    argType = 'optional_group_end'
    
    def __init__(self, argText, nextArg):
        self.text = argText.strip('>')

    def getDefText(self):
        return self.text.strip('*')  + "=None"
        
    def getIntermediateText(self):
        return [tabText2 + f"uniqueArgs.append({self.text})"]

    def getCallText(self):
        return ''
    
class optionalGroupTag(Argument):
    """
    The unique argument that follows a tag.
    """
    argType = 'optional_group_tag'
    
    def __init__(self, argText, nextArg):
        self.text = argText.strip("<>'-")

    def getDefText(self):
        return self.text.strip('*')  + "=None"
        
    def getIntermediateText(self):
        return [tabText2 + f"uniqueArgs.append({self.text})"]

    def getCallText(self):
        return ''
  
argTypes = ['basic', 'tag', 'startTag', 'tag_arg', 'optional', 'optional_wrapped', 'optional_group_start',
            'optional_group_middle','optional_group_end','optional_group_tag']
  
argClsDict = {}
for tmpcls in Argument.__subclasses__():
    argClsDict[tmpcls.argType] = tmpcls



def setArgObjs(args:list, argTypes:list):
    
    """
    Gets a list of the arg objects
    """
    argClasses = []
    Nargs = len(args)
    for ii in range(Nargs):
        arg = args[ii]
        argType = argTypes[ii]
        ArgClass = argClsDict[argType]

        if ii == Nargs - 1:
            nextArg = None
        else:
            nextArg = args[ii + 1]
        argClasses.append(ArgClass(arg, nextArg))

        
        # Groups require knowledge of the next argument to create their if statement
        # if argType == 'optional_group_start':
        #     nextArg = args[ii + 1]
        #     argClasses.append(ArgClass(arg, nextArg))
        # else:
        #     argClasses.append(ArgClass(arg))

    
    return argClasses





def getFunctionText(inputText):
    """
    Gets the functon defiition and call text, as well as intermediate text.

    Parameters
    ----------
    inputText : TYPE
        DESCRIPTION.

    Returns
    -------
    defText : TYPE
        DESCRIPTION.
    filteredIntText : TYPE
        DESCRIPTION.
    funcText : TYPE
        DESCRIPTION.

    """
    
    
    
    args = getArgsFromTxt(inputText)
    print(args)
    # Some functions are empty, in this case return nothing
    if args == ['']:
        return [''], [''], ['']
    
    funcGroupName = getGroupName(inputText)
    argTypes    = parseAllArgs(args)
    # argTypes    = np.array(argTypes)
    argClasses = setArgObjs(args, argTypes)
    
    defText  = []
    funcText = []
    intText  = []
    startLine = ['    ' + 'uniqueArgs = []']
    intText.append(startLine)
    
    for obj in argClasses:
        # print(obj.argType)
        defText.append(obj.getDefText())
        funcText.append(obj.getCallText())
        intText.append(obj.getIntermediateText())
        
    defText = [item for item in defText if 0 < len(item) ]
    defText = ['def ' + args[0].strip("-'") + '(' + ', '.join(defText) + '):']

    funcText = [item for item in funcText if 0 < len(item) ]
    funcText = ['    ops.' + funcGroupName.strip("-'") + '(' + ', '.join(funcText) + ', *uniqueArgs' + ')']
        
    tagsInds = []
    filteredIntText = []
    for text in intText:
        if 0 < len(text): 
            filteredIntText = filteredIntText + text
    
    # defText = [defText[4].lower() + text[5:] for text in defText]
    # print(inputText)
    # print(intText)
    return defText, filteredIntText, funcText
