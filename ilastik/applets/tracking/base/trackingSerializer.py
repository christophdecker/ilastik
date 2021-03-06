from ilastik.applets.base.appletSerializer import AppletSerializer,\
    SerialDictSlot, SerialSlot, SerialHdf5BlockSlot

class TrackingSerializer(AppletSerializer):
    
    def __init__(self, mainOperator, projectFileGroupName):
        slots = [SerialDictSlot(mainOperator.Parameters, selfdepends=True),
#                  SerialSlot(mainOperator.Output, selfdepends=True),
                 SerialHdf5BlockSlot(mainOperator.OutputHdf5,
                                     mainOperator.InputHdf5,
                                     mainOperator.CleanBlocks,
                                     name="CachedOutput"),
                 ]
        super( TrackingSerializer, self ).__init__( projectFileGroupName, slots=slots )
        