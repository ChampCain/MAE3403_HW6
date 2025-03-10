#region class definitions
class Loop():
    #region constructor
    def __init__(self, Name='A', Pipes=[]):
        '''
        Defines a loop in a pipe network.
        :param Name: name of the loop
        :param Pipes: a list/array of pipes in this loop
        '''
        #region attributes
        self.name = Name
        self.pipes = Pipes
        #endregion
    #endregion

    #region methods
    def getLoopHeadLoss(self):
        '''
        Calculates the net head loss as I traverse around the loop, in meters of fluid.
        :return: net head loss in meters
        '''
        deltaP = 0  # initialize to zero
        startNode = self.pipes[0].startNode  # begin at the start node of the first pipe
        for p in self.pipes:
            phl = p.getFlowHeadLoss(startNode)
            deltaP += phl
            startNode = p.endNode if startNode != p.endNode else p.startNode  # move to the next node
        return deltaP
    #endregion
#endregion
