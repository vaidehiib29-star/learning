#Tricky String Problems(Using Multiple Methods)

#1.Normalize a sentence
sentence = " Hello   WoRLD  "
result = "".join(sentence.strip().lower().split())
print(result)


#2.Capitalize each word(without.title())
sentence = "hello world"
words = sentence.split()
result = " ".join(word.capitalize() for word in words)
print(result)


#3.Remove puncatuation from string
sentence = "hello!!! world??"
result = "".join(ch if ch.isalpha() or ch == " " else " " for ch in sentence)
print(result)


#4.Extract only digits from string
sentence = "a1b2c3"
result = "".join(ch for ch in sentence if ch.isdigit())
print(result)


#5.Extract only alphabets
sentence = "a1b2c3!"
result = "".join(ch for ch in sentence if ch.isalpha())
print(result)


#6.Reverse words in a sentence
sentence = " I love Python"
result = " ".join(sentence.split()[::-1])
print(result)


#7.Remove duplicate words
sentence = "this is a test test"
words = sentence.split()
result = []

for word in words:
    if word not in result:
        result.append(word)

print(" ".join(result))


#8.Check if email is valid(basic)
email = "test@gmail.com"
if email.count("@") == 1 and email.endswith(".com"):
    print(True)
else:
    print(False) 


#9.Mask a phone number
num = "7433985825"
result = num[:3] + "*" * 5 + num[-2:]
print(result)   


#10.Convert sentence to snake_case
sentence = "Hello World python"
result = "_".join(sentence.lower().split())
print(result)
result = "_".join(sentence.upper().split())
print(result)


#11.Remove first and last character of each word
sentence = "hello world"
result = " ".join(word[1:-1] for word in sentence.split())
print(result)


#12.Find longest word
sentence = "I love Python programming"
longest = max(sentence.split(), key=len)
print(longest)


#13.Count words ignoring punctuation
sentence = "Hello, world! Python is great."
for ch in ",.!?":
    sentence = sentence.replace(ch, "")
print(len(sentence.split()))    


#14.Check if sentence is palindrome(ignore spaces)
sentence = "nurses run"
sentence = sentence.replace(" ", "").lower()
if sentence == sentence[::-1]:
    print(True)
else:
    print(False)     


#15.Toggle case manually
sentence ="Hello"
result = ""
for ch in sentence:
    if ch.isupper():
        result += ch.lower()
    elif ch.islower():
        result += ch.upper()
    else:
        result += ch
print(result) 