class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashTable = {}
        maxlen = 0
        flag = 0
        slen = len(s)
        for i,c in enumerate(s):
            try :
                re = hashTable[s[i]]
                if not re < flag:     
                    if (i - flag) > maxlen:
                        maxlen = i - flag
                    flag = re + 1
            except:
                hashTable[s[i]] = i 
            else:
                hashTable[s[i]] = i 
        if (len(s) - 1  - flag + 1) > maxlen : #if found no repeat char at the end then test if the length of the flag to the end is longer than the maxlen
            maxlen = (len(s) - 1  - flag + 1)
        return maxlen

print(Solution().lengthOfLongestSubstring("bbbb"))
