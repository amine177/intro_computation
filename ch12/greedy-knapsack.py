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

def greedyKnapsack(items, maxWeight, valueFunction):
    """
    Find the best items to take in a knapsack
    Input : an items object that implements __iter__ and __lt__ 
            a maxWeight that a knapsack can take
            a valueFunction to give value for an item
    Output : a list of the items to be take, a totalValue of the items taken
    """
    result = []
    totalValue, totalWeight = 0.0, 0.0
    for item in sorted(items, key=valueFunction, reverse=True):
        if (totalWeight + item.getWeight()) <= maxWeight:
            result.append(item)
            totalWeight += item.getWeight()
            totalValue += item.getValue()

    return (result, totalValue)


if __name__ == "__main__":

    i1 = Item("car", 11300, 5000)
    i2 = Item("book", 10, 1)
    i3 = Item("clock", 100, 10)
    i4 = Item("radio", 20, 4)
    i5 = Item("painting", 90, 9)
    i6 = Item("computer", 200, 20)
    print("taking:")
    for i in greedyKnapsack([i1, i2, i3, i4, i5, i6], 20, density)[0]:
        print(i)
