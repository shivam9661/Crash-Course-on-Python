multiples = []
for x in range(1, 11):
    multiples.append(x * 7)
print(multiples)

# other way to create is
multiples2 = [x * 7 for x in range(1, 21)]
print (multiples2)

languages = ["python", "perl", "ruby", "Go", "java", "C"]
lengths = [len(language) for language in languages]
print(lengths);
