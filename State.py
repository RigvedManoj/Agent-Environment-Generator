class State:
    def __init__(self, state, actionCount):
        self.transition = [None] * actionCount
        self.reward = [None] * actionCount
        self.actionCount = actionCount
        self.policies = None
        self.state = state

    # Setting Probability of taking an action for given state. action = A(i) where i-1 is index of list
    def setPolicies(self, actionProbList):
        self.policies = actionProbList

    # Setting transition function for given state and action . state = S(i) where i-1 is index of list
    def setTransition(self, actions, stateProbLists):
        for action in actions:
            self.transition[action - 1] = stateProbLists[action - 1]

    # Setting reward for given state and action.
    def setReward(self, actions, rewards):
        for action in actions:
            self.reward[action - 1] = rewards[action - 1]

    # Checking EndState by checking number of Actions.
    def checkEndState(self):
        if self.actionCount == 0:
            return True
        else:
            return False
