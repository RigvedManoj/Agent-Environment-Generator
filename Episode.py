import numpy

from State import State


def runEpisode(s, gamma):
    totalReward = 0
    initialState = numpy.random.choice(numpy.arange(0, len(s)), p=[0.6, 0.3, 0.1, 0, 0, 0, 0])
    currentState: State = s[initialState]
    # print("initial state is S" + str(initialState))
    time = 0
    while not currentState.checkEndState():
        action = numpy.random.choice(numpy.arange(0, len(currentState.policies)), p=currentState.policies)
        # print("action at time " + str(time) + " is action" + str(action))
        reward = currentState.reward[action]
        totalReward += (gamma ** time) * reward
        # print("total reward at time " + str(time) + " is " + str(totalReward))
        newState = numpy.random.choice(numpy.arange(0, len(currentState.transition[action])),
                                       p=currentState.transition[action])
        currentState = s[newState]
        time += 1
    return totalReward
