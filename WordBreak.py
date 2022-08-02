https://leetcode.com/problems/word-break/
  
  s = "leetcode"
wordDict = ["leet", "code"]

  def wordbreak(s, wordDict):
    wordDict = set(wordDict) # Getting the unique set of words.

    def dfs(idx):
        if idx == len(s): #This will check if the index as reached the last position of the array. It will return True because if the index has reached the last position so it means that there has been atleast one match
            return True
        cur = '' # Using an extra space to keep on adding the characters to it.
        for i in range(idx, len(s)): # Starts with 0 since it is Top Down DP approach
            cur += s[i] # Keep on adding the characters
            print(cur)
            if cur in wordDict: #If it matches the keys from the given list 
                print("i ", i)
                result = dfs(i + 1) # call the recursive function by incrementing the position of the idx in order to check the new word.
                if result: # If the result returned by the first if block is true then return True. Here, the last index incremented to was 8 i.e len of string which ensures that all the characters of a string has been checked with the word dictionary elements
                    return True
        return False # Or else return False

    return dfs(0)

  https://leetcode.com/problems/word-break/discuss/2365252/python-top-down-dp/1522139
