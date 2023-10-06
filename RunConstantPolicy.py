import numpy
from matplotlib import pyplot as plt

from Environment import setStaticStates, setInitialState
from Episode import runEpisode
from Functions import calculateExpectedReturns, calculateVariance

s = setStaticStates()
p = [0.6, 0.3, 0.1, 0, 0, 0, 0]

for gamma in [0.9, 0.25, 0.5, 0.75, 0.99]:
    rewardList = []
    expectedValues = []
    for i in range(0, 150000):
        initialState = setInitialState(s, p)
        totalReward = runEpisode(s, gamma, initialState)
        rewardList.append(totalReward)
        if i == 0:
            expectedValues.append(calculateExpectedReturns(0, 1, totalReward))
        else:
            expectedValues.append(calculateExpectedReturns(expectedValues[-1], i + 1, totalReward))

    averageReward = expectedValues[-1]
    variance = calculateVariance(rewardList, averageReward)

    print("Expectation for " + str(gamma) + " is " + str(averageReward))
    print("Variance for " + str(gamma) + " is " + str(variance))

    x_axis = numpy.arange(0, 150000)
    plt.plot(x_axis, expectedValues)
plt.show()
