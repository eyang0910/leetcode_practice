"""
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""
def find_diff(s,t):
    ss = sorted(list(s))
    ss.append('#')
    ts = sorted(list(t))
    print ss,ts
    for i in range(len(ts)):
        if ss[i] != ts[i]:
            print ts[i]
            break

find_diff('abfg','fgbsa')