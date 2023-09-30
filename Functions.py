# Returns new average given old average and new value.
def calculateExpectedReturns(initialExpectedValue, size, newValue):
    newExpectedValue = ((size - 1) * initialExpectedValue + newValue) / size
    return newExpectedValue


# Returns variance given list of values and average value.
def calculateVariance(rewardList, averageReward):
    if len(rewardList) <= 1:
        return 0
    variance = 0
    for reward in rewardList:
        variance += (reward - averageReward) ** 2
    variance = variance / (len(rewardList) - 1)
    return variance
