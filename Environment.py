import numpy

from State import State


# Set all states by defining policies, transitions and rewards.
def setStaticStates():
    # Here [0.5, 0.5] is probability of taking action A(1) and A(2)
    # Here [0, 0, 0, 1, 0, 0, 0] is probability of going to state S(1) to S(7) given S(1) and A(1)
    s1 = State(1, 2)
    s1.setPolicies([0.5, 0.5])
    s1.setTransition([1, 2], [[0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]])
    s1.setReward([1, 2], [7, 10])

    s2 = State(2, 2)
    s2.setPolicies([0.7, 0.3])
    s2.setTransition([1, 2], [[0, 0, 0, 0.8, 0.2, 0, 0], [0, 0, 0, 0.6, 0.4, 0, 0]])
    s2.setReward([1, 2], [-3, 5])

    s3 = State(3, 2)
    s3.setPolicies([0.9, 0.1])
    s3.setTransition([1, 2], [[0, 0, 0, 0.9, 0.1, 0, 0], [0, 0, 0, 0, 1, 0, 0]])
    s3.setReward([1, 2], [4, -6])

    s4 = State(4, 2)
    s4.setPolicies([0.4, 0.6])
    s4.setTransition([1, 2], [[0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0.3, 0.7]])
    s4.setReward([1, 2], [9, -1])

    s5 = State(5, 2)
    s5.setPolicies([0.2, 0.8])
    s5.setTransition([1, 2], [[0, 0, 0, 0, 0, 0.3, 0.7], [0, 0, 0, 0, 0, 0, 1]])
    s5.setReward([1, 2], [-8, 2])

    # Defining EndState to have no actions
    s6 = State(6, 0)
    s7 = State(7, 0)

    # List of states
    s = [s1, s2, s3, s4, s5, s6, s7]
    return s


def setStates(numberOfStates, numberOfEndStates, actionCount, minReward, maxReward):
    s = []
    for i in range(0, numberOfStates - numberOfEndStates):
        state = State(i, actionCount)
        state = generateRandomPolicy(state)
        state = generateDeterministicTransition(state, numberOfStates)
        state = generateRandomReward(state, minReward, maxReward)
        s.append(state)
    for i in range(0, numberOfEndStates):
        state = State(numberOfStates - numberOfEndStates + i, 0)
        s.append(state)
    return s


# Generates a random policy by assigning equal probability to all actions.
def generateRandomPolicy(state):
    if state.actionCount == 0:
        return state
    currentState: State = state
    random = numpy.random.choice(state.actionCount)
    actions = []
    for i in range(0, state.actionCount):
        if i == random:
            actions.append(1)
        else:
            actions.append(0)
    state.setPolicies(actions)
    return state


# Generate a random transition function.
def generateDeterministicTransition(state, numberOfStates):
    if state.actionCount == 0:
        return state
    transitionList = []
    actionList = []
    for i in range(0, state.actionCount):
        tempList = []
        random = numpy.random.choice(numberOfStates - state.state - 1) + state.state + 1
        for j in range(0, numberOfStates):
            if j == random:
                tempList.append(1)
            else:
                tempList.append(0)
        transitionList.append(tempList)
        actionList.append(i + 1)
    state.setTransition(actionList, transitionList)
    return state


def generateRandomReward(state, minReward, maxReward):
    if state.actionCount == 0:
        return state
    rewardList = []
    actionList = []
    for i in range(0, state.actionCount):
        reward = numpy.random.random_integers(minReward, maxReward)
        rewardList.append(reward)
        actionList.append(i)
    state.setReward(actionList, rewardList)
    return state


# Returns Initial State depending on d_0 probabilities
def setInitialState(s,p):
    initialState = numpy.random.choice(numpy.arange(len(s)), p=p)
    return s[initialState]
