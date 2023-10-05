import numpy
from matplotlib import pyplot as plt

from Environment import generateRandomPolicy, setStaticStates
from Episode import runEpisode
from Functions import calculateExpectedReturns

s = setStaticStates()

expectedOptimalValues = []
for n in range(1, 250, 10):
    bestExpectedValue = 0
    for k in range(0, n):
        expectedValue = 0
        # Assign Random Policy to each state
        for i in range(0, len(s)):
            state = generateRandomPolicy(s[i])
            s[i] = state
        # Run 100 episodes for each random policy
        for i in range(0, 100):
            totalReward = runEpisode(s, 0.9)
            if i == 0:
                expectedValue = calculateExpectedReturns(0, 1, totalReward)
            else:
                expectedValue = calculateExpectedReturns(expectedValue, i + 1, totalReward)
        if expectedValue > bestExpectedValue:
            bestExpectedValue = expectedValue
    expectedOptimalValues.append(bestExpectedValue)

x_axis = numpy.arange(1, 250, 10)
plt.ylim(0, 20)
plt.plot(x_axis, expectedOptimalValues)
plt.show()
