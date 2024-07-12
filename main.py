#
#
def single_root_words(root_word, *other_words):
    same_words = []
    a = str(other_words)
    for i in other_words:
        if i in root_word or root_word in i:
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
# #
# #
# #
#
# a = ('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
# b = str(a)
# print(type(b), b)
# c = b.split(sep)
# print(type(c), c)

