'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# # in-place, no extra memory and slicing operation
# def count_th(word):
#     res = 0
#     def rec(i):
#         nonlocal res
#         if i >= len(word) - 1: return
#         if word[i:i+2] == "th":
#             res += 1
#             return rec(i+2)

#         return rec(i+1)
    
#     rec(0)
#     return res

def count_th(word):
    if len(word) < 2: return 0

    if word[:2] == "th":
        return 1 + count_th(word[2:])
    else:
        return 0 + count_th(word[1:])

word = "thththtth" # 4
print(count_th(word))