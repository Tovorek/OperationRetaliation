# 2 - ways provided 
# Time complexity - O(n) and Space Complexity - O(1)


# solution 1 ; Using While loop 
def isValidSubsequence(array, sequence):
    arrIndex = 0
    subIdx = 0
    while arrIdx < len(array) and subIdx < len(sequence):
        if array[arrIndex] == sequence[subIdx]:
            subIdx += 1
        arrIndex += 1
    return subIdx == len(sequence)    

# Solution 2 ; Using For loop

def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            return True
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)        
   
        
  
  # Try it on your own
  
    
    
  
