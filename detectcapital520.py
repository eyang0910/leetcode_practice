class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        counter1 = 0
        counter2 = 0
        for i in range(len(word)):
            if word[i].isupper():
                counter1 += 1
            if word[i].islower():
                counter2 += 1
        return counter1 == len(word) or counter2 == len(word) or (word[0].isupper() and counter1 == 1)

