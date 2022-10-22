# 1st solution
# Time complexity O(nlogn) Space Complexity O(n)
def sortedSquaredArray(array):
    x = [0 for _ in array]


    for idx in range(len(array)):
        value = array[idx]
        x[idx] = value * value

    x.sort()
    return x
  
  # x = the Sorted Squared array
  
  
  # 2nd Solution
  
  def sortedSquaredArray(array):
    x = [0 for _ in array]
    start = 0
    end = len(array) - 1

    for idx in reversed(range(len(array))):
        startValue = array[start]
        endValue = array[end]


        if abs(startValue) > abs(endValue):
            x[idx] = startValue * startValue
            start += 1
        else:
            x[idx] = endValue * endValue
            end -= 1
    return x 

#x == sortedSquare array
# Time complexity = O(n) | Space O(n)
