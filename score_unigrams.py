# Write a function called score_unigrams that takes three arguments:
#   - a path to a folder of training data 
#   - a path to a test file that has a sentence on each line
#   - a path to an output CSV file
#
# Your function should do the following:
#   - train a single unigram model on the combined contents of every .txt file
#     in the training folder
#   - for each sentence (line) in the test file, calculate the log unigram 
#     probability ysing the trained model (see the lab handout for details on log 
#     probabilities)
#   - write a single CSV file to the output path. The CSV file should have two
#     columns with headers, called "sentence" and "unigram_prob" respectively.
#     "sentence" should contain the original sentence and "unigram_prob" should
#     contain its unigram probabilities.
#
# Additional details:
#   - there is training data in the training_data folder consisting of the contents 
#     of three novels by Jane Austen: Emma, Sense and Sensibility, and Pride and Prejudice
#   - there is test data you can use in the test_data folder
#   - be sure that your code works properly for words that are not in the 
#     training data. One of the test sentences contains the words 'color' (American spelling)
#     and 'television', neither of which are in the Austen novels. You should record a log
#     probability of -inf (corresponding to probability 0) for this sentence.
#   - your code should be insensitive to case, both in the training and testing data
#   - both the training and testing files have already been tokenized. This means that
#     punctuation marks have been split off of words. All you need to do to use the
#     data is to split it on spaces, and you will have your list of unigram tokens.
#   - you should treat punctuation marks as though they are words.
#   - it's fine to reuse parts of your unigram implementation from HW3.

# You will need to use log and -inf here. 
# You can add any additional import statements you need here.
from math import log, inf


import os
import csv
from math import log, inf

def train_unigram_model(training_folder):
    """Train a unigram model from all .txt files in the given folder."""
    word_counts = {}
    total_words = 0

    for filename in os.listdir(training_folder):
        if filename.endswith(".txt"):
            with open(os.path.join(training_folder, filename), 'r', encoding="utf-8") as file:
                for line in file:
                    words = line.lower().split() 
                    for word in words:
                        word_counts[word] = word_counts.get(word, 0) + 1
                        total_words += 1

    word_probs = {word: count / total_words for word, count in word_counts.items()}
    
    return word_probs, total_words

def compute_unigram_prob(sentence, word_probs, total_words):
    """Compute the log probability of a sentence using the unigram model."""
    words = sentence.lower().split()
    log_prob = 0

    for word in words:
        if word in word_probs:
            log_prob += log(word_probs[word])
        else:
            return -inf  
        
    return log_prob

def score_unigrams(training_folder, test_file, output_csv):
    """Train unigram model, compute sentence probabilities, and save to CSV."""
    word_probs, total_words = train_unigram_model(training_folder)

    with open(test_file, 'r', encoding="utf-8") as test_f, open(output_csv, 'w', newline='', encoding="utf-8") as out_f:
        writer = csv.writer(out_f)
        writer.writerow(["sentence", "unigram_prob"])

        for sentence in test_f:
            sentence = sentence.strip()
            log_prob = compute_unigram_prob(sentence, word_probs, total_words)
            writer.writerow([sentence, log_prob])


# Do not modify the following line
if __name__ == "__main__":
    # You can write code to test your function here
    pass 
