import numpy
from matplotlib import pyplot as plt

from Environment import setStates
from Episode import runEpisode
from Functions import calculateExpectedReturns, calculateVariance

s = setStates()

for gamma in [0.25, 0.5, 0.75, 0.99]:
    rewardList = []
    expectedValues = []
    for i in range(0, 150000):
        totalReward = runEpisode(s, gamma)
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
