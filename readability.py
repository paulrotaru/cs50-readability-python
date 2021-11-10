from cs50 import get_string

#promp user to enter a text
usertext = get_string("Text: ")
print(usertext)

#count the number of letters in the text
count = 0
for i in range(len(usertext)):
    if usertext[i].isalpha():
        count = count + 1

nwords = 0
wspaces = 0
for i in range(len(usertext)):
    if usertext[i].isspace():
        wspaces = wspaces + 1
nwords = wspaces + 1


nsentences = 0
for i in range(len(usertext)):
    if usertext[i] == "." or usertext[i] == "!" or usertext[i] == "?":
        nsentences = nsentences + 1


s = 100 * (nsentences / nwords)
l = 100 * (count / nwords)
index = round(0.0588 * l - 0.296 * s - 15.8)


if index < 1:
    print("Before Grade 1")
elif index > 15:
    print("Grade 16+")
else:
    print(f"Grade {index}")