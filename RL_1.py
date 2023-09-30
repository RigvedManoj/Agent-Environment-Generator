import matplotlib.pyplot as plt
import numpy


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

    def setReward(self, actions, rewards):
        for action in actions:
            self.reward[action - 1] = rewards[action - 1]

    def checkEndState(self):
        if self.actionCount == 0:
            return True
        else:
            return False


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
    # print("current state at time " + str(time) + " is S" + str(newState+1))


def calculateExpectedReturns(initialExpectedValue, size, newValue):
    newExpectedValue = ((size - 1) * initialExpectedValue + newValue) / size
    return newExpectedValue


value = numpy.random.choice(numpy.arange(1, 7), p=[0.1, 0.05, 0.05, 0.2, 0.4, 0.2])
s = setStates()
rewardList = []
expectedValues = []
for i in range(0, 150000):
    totalReward = runEpisode(s, 0.9)
    rewardList.append(totalReward)
    if i==0:
        expectedValues.append(calculateExpectedReturns(0, 1, totalReward))
    else:
        expectedValues.append(calculateExpectedReturns(expectedValues[-1], i+1, totalReward))
x_axis = numpy.arange(0, 150000)
plt.plot(x_axis, expectedValues)
print(expectedValues[-1])
plt.show()
