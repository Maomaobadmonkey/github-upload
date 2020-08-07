word = str.lower(input())

ex = word.replace("!", "")
com = ex.replace(",", "")
per = com.replace(".", "")
ques = per.replace("?", "")

print(ques)