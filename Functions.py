# Returns new average given old average and new value.
import networkx as nx
from matplotlib import pyplot as plt


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


def drawGraph(s):
    G = nx.DiGraph()
    for state in s:
        G.add_node(state.state)
    for state in s:
        for i in range(0, state.actionCount):
            G.add_edge(state.state, state.transition[i].index(1), weight= state.reward[i])
    pos = nx.circular_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.savefig("environment.png")
    plt.clf()
