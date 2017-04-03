# my solution
# class Solution(object):
#     def findWords(self, words):
#         """
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         dic1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
#         dic2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
#         dic3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
#         solution = []
#         k = 1
#         # print words[0]
#         # words = words[0]
#         # print words
#         for i in range(len(words)):
#             save1 = 0
#             save2 = 0
#             save3 = 0
#             for j in range(len(words[i])):
#                 if words[i][j] in dic1:
#                     save1 += 1
#                 if words[i][j] in dic2:
#                     save2 += 1
#                 if words[i][j] in dic3:
#                     save3 += 1
#             print save1,save2,save3
#             print len(words[i])
#             if save1 == len(words[i]) or save2 == len(words[i]) or save3 == len(words[i]):
#                 solution.append(words[i])
#                 k += 1
#         return solution
def keyboardrow(words):
    # dic1 = ['q','w','e','r','t','y','u','i','o','p']
    # dic2 = ['a','s','d','f','g','h','j','k','l']
    # dic3 = ['z','x','c','v','b','n','m']
    dic1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
    dic2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
    dic3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    solution = []
    k = 1
    words = words[0]

    for i in range(len(words)):
        save1 = 0
        save2 = 0
        save3 = 0
        for j in range(len(words[i])):
            if words[i][j] in dic1:
                save1 += 1
            if words[i][j] in dic2:
                save2 += 1
            if words[i][j] in dic3:
                save3 += 1
        print save1,save2,save3
        print len(words[i])
        if save1 == len(words[i]) or save2 == len(words[i]) or save3 == len(words[i]):
            solution.append(words[i])
            k += 1
    print solution
w=[["Hello","Alaska","Dad","Peace"]]
keyboardrow(w)


# given solution
def keyboardrow2(words):
           for row in [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]:
                for word in words:
                    if set(word.lower()) <= row:
                        print word

w=["Hello","Alaska","Dad","Peace"]
keyboardrow2(w)
#my copy
class Solution(object):
    # def findWords(self, words):
    #     """
    #     :type words: List[str]
    #     :rtype: List[str]
    #     """
    #     a = set('qwertyuiop')
    #     b = set('asdfghjkl')
    #     c = set('zxcvbnm')
    #     # whole = [a,b,c]
    #     # print whole
    #     solution=[]
    #     for word in words:
    #         if set(word.lower()) <= a or set(word.lower()) <=b or set(word.lower()) <=c:
    #             solution.append(word)
    #     return solution