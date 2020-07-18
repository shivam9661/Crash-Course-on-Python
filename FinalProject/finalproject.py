def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]

    # LEARNER CODE START HERE
    wordDictionary = {}
    wordList = file_contents.split()
    for word in wordList:
        words = " "
        for c in word:
            if c not in punctuations:
                words = words + c
        if words not in uninteresting_words:
            if words not in wordDictionary.keys():
              wordDictionary[words] = 1
            else:
              wordDictionary[words] += 1
    # wordcloud
    import wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(wordDictionary)
    return cloud.to_array()