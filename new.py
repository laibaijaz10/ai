#qno1(a)
story = "and somewhere in the vastnessof cyberspace, a new intelligence looked out upon the world."
words = story.split()
vowel_words = [word for word in words if any(vowel in word.lower() for vowel in 'aeiou')]
print(vowel_words)
#qno1(b)
nouns = ["intelligence", "world", "cyberspace", "vastness"]
print(nouns)
#qno2(a)
nouns = ["intelligence", "world", "cyberspace", "vastness"]
numbers = [1, 2, 3, 4]
nouns.append(numbers)
print(nouns)
#qno2(b)
nouns = ("intelligence", "world", "cyberspace", "vastness")
print(nouns)
#qno3(a)
nouns = ("intelligence", "world", "cyberspace", "vastness")
numbers = (1, 2, 3, 4)
nouns = nouns + (numbers,)
print(nouns)
#qno3(b)
nouns = {"intelligence", "world", "cyberspace", "vastness"}
print(nouns)
#qno4(a)
nouns = {"intelligence", "world", "cyberspace", "vastness"}
numbers = {1, 2, 3, 4}
nouns.add(tuple(numbers))  
print(nouns)
#qno4(b)
pronoun_noun = {"it": "intelligence", "they": "world", "this": "cyberspace"}
print(pronoun_noun)
#qno5(a)
story = "And somewhere in the vastness of cyberspace, a new intelligence looked out upon the world."
words = story.split()
word_count = {word: words.count(word) for word in words}
print(word_count)
#qno5(b)
story = "And somewhere in the vastness of cyberspace, a new intelligence looked out upon the world."
for vowel in "aeiouAEIOU":
    story = story.replace(vowel, "?")
print(story)
#qno6(a)
story = "He was in the world. What is he thinking? I am there. On the way."
replacements = {"He": "She", "What": "Who", "I": "The", "On": "At"}
for old, new in replacements.items():
    story = story.replace(old, new)
print(story)
#qno6(b)
story = 'He said, "I am learning Python." Then she replied, "That’s great!"'
import re
sentences = re.findall(r'".*?"', story)
print(sentences)
#qno7(a)
story = "And somewhere in the vastness of cyberspace, a new intelligence looked out upon the world."
for i in range(0, len(story), 10):
    print(story[i:i+10])
#qno7(b)
story = "And somewhere in the vastness of cyberspace, a new intelligence looked out upon the world."
i = 0
while i < len(story):
    print(story[i:i+30])
    i += 30


