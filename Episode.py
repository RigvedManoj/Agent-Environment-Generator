import numpy

from Environment import setInitialState
from State import State


# Run 1 episode given set of states and gamma.
def runEpisode(s, gamma, initialState=-1):
    totalReward = 0
    currentState: State = s[initialState]
    if initialState == -1:
        currentState: State = setInitialState(s)
    time = 0
    while not currentState.checkEndState():
        action = numpy.random.choice(numpy.arange(0, len(currentState.policies)), p=currentState.policies)
        reward = currentState.reward[action]
        totalReward += (gamma ** time) * reward
        newState = numpy.random.choice(numpy.arange(0, len(currentState.transition[action])),
                                       p=currentState.transition[action])
        currentState = s[newState]
        time += 1
    return totalReward
