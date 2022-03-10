from mojo.UI import SetCurrentLayerByName
from mojo.extensions import getExtensionDefault, setExtensionDefault
from mojo.events import addObserver, removeObserver, setActiveEventTool

""" Andy Clymer """

# Script setup:
metadata = dict(
    shortName = "HotkeyJumpToForeground",
    longName = "Hotkey – Jump to Foreground",
    description = "Assigns the “b” key to jump back and forth between background and foreground. Also adds some shortcuts similar to Glyphsapp")
    
# Read the current scriptMetadata and add this one
fullMetadata = getExtensionDefault("com.andyclymer.andysHacks.scriptMetadata", fallback={})
fullMetadata[metadata["shortName"]] = metadata
setExtensionDefault("com.andyclymer.andysHacks.scriptMetadata", fullMetadata)
# Set the default on/off to False, or just keep the current state
scriptStateKey = "com.andyclymer.andysHacks.%s-state" % metadata["shortName"]
currentState = getExtensionDefault(scriptStateKey, fallback=False)
setExtensionDefault(scriptStateKey, currentState)


fonttoggle = 1

class JumpToForeground():
    
    def __init__(self):
        if getExtensionDefault(scriptStateKey, fallback=False):
            addObserver(self, "keyDown", "keyDown")

    def keyDown(self, info):
        global fonttoggle
        event = info["event"]
        characters = event.characters()
        #modifierFlags = event.modifierFlags()w
        #toggles between background and foreground
        if characters == "b":
            if fonttoggle == 1:
                SetCurrentLayerByName("foreground")
                fonttoggle = 0
            else:
                SetCurrentLayerByName("background")
                fonttoggle = 1
        #selects edit tool like in Glyphsapp
        elif characters == "v":
            setActiveEventTool("EditingTool")
        #selects path tool like in Glyphsapp
        elif characters == "p":
            setActiveEventTool("BezierDrawingTool")
        #selects path tool like in Glyphsapp
        elif characters == "m":
            setActiveEventTool("DrawGeometricShapesTool")
JumpToForeground()
