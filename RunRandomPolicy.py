import numpy
from matplotlib import pyplot as plt

from Environment import setStates, generateRandomPolicy
from Episode import runEpisode
from Functions import calculateExpectedReturns, calculateVariance

s = setStates()

expectedOptimalValues = []
for n in range(1, 250, 10):
    bestExpectedValue = 0
    bestPolicy = []
    for k in range(0, n):
        for i in range(0, len(s)):
            state = generateRandomPolicy(s[i])
            s[i] = state
        expectedValue = 0
        for i in range(0, 100):
            totalReward = runEpisode(s, 0.9)
            if i == 0:
                expectedValue = calculateExpectedReturns(0, 1, totalReward)
            else:
                expectedValue = calculateExpectedReturns(expectedValue, i + 1, totalReward)
        if expectedValue > bestExpectedValue:
            bestExpectedValue = expectedValue
            policy = []
            for state in s:
                if state.actionCount != 0:
                    policy.append(state.policies)
            bestPolicy = policy
    expectedOptimalValues.append(bestExpectedValue)

x_axis = numpy.arange(1, 250, 10)
plt.ylim(0, 20)
plt.plot(x_axis, expectedOptimalValues)
plt.show()
