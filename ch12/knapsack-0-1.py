import functools
class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

    def getName(self):
      return self.name
    def getValue(self):
      return self.value
    def getWeight(self):
      return self.weight
    def __str__(self):
      result = '<' + self.name + ', ' + str(self.value)\
          + ', ' + str(self.weight) + '>'
      return result

def value(item):
  return item.getValue()


def weightInverse(item):
  return 1.0/item.getWeight()

def density(item):
  return item.getValue()/item.getWeight()

def increaseItemValueWeight(value, item):
    return (value[0] + item.getValue(), value[1] + item.getWeight())

def chooseBest(setOfsets, maxW):
    bestTotalValue = 0.0
    bestSet = None
    for subset in setOfsets:
        itemsVal, itemsWeight = functools.reduce(
            increaseItemValueWeight, subset, (0.0, 0.0))
        if itemsWeight <= maxW and itemsVal > bestTotalValue:
            bestTotalValue = itemsVal
            bestSet = subset
    return (bestSet, bestTotalValue)


def powerset(l):
    x = len(l)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, l) if i & mask]


if __name__ == "__main__":

    i1 = Item("car", 11300, 5000)
    i2 = Item("book", 10, 1)
    i3 = Item("clock", 100, 10)
    i4 = Item("radio", 20, 4)
    i5 = Item("painting", 90, 9)
    i6 = Item("computer", 200, 20)
    bestSet = chooseBest(powerset([i1, i2, i3, i4, i5, i6]), 20)
    for i in bestSet[0]:
        print(i)
    # print("taking:")
    # for i in greedyKnapsack([i1, i2, i3, i4, i5, i6], 20, density)[0]:
    #     print(i)
