import numpy

from State import State


def setStates():
    # Here 0.5 is probability of taking action A(1) and A(2)
    # Here 0 is probability of going to state S(1) given S(1) and A(1)
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

    s6 = State(6, 0)

    s7 = State(7, 0)

    # List of states
    s = [s1, s2, s3, s4, s5, s6, s7]

    return s


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
