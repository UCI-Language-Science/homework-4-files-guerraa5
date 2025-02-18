# The file valence_data/winter_2016_senses_valence.csv contains data from an 
# experiment that asked people to provide valence ratings for words associated
# with each of the five senses (touch, taste, smell, sight, sound). The file has
# three columns: Word, Modality, and Val. Word contains the word, Modality the
# sensory modality, and Val contains the mean valence rating for that word,
# where higher valence corresponds to more positive emotional states.

# The question we'll try to answer is whether certain sensory modalities have 
# higher or lower mean valences than others.
# 
#  Write a function called get_mean_valence that takes a Path to a CSV file
#  as input. You can assume the file will be formatted as described above.
#  Your function should return a dictionary with keys corresponding to each
#  of the five modalities. The value for each key should be its mean valence
#  score across all of the words in the CSV file.

# The data are from the paper 
#
# Winter, B. (2016). Taste and smell words form an affectively loaded and emotionally
# flexible part of the English lexicon. Language, Cognition and Neuroscience, 31(8), 
# 975-988.

import csv

def get_mean_valence(csv_path):
    with open(csv_path, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)

        modalities = {"Sight": 0, "Sound": 0, "Touch": 0, "Taste": 0, "Smell": 0}
        counts = {"Sight": 0, "Sound": 0, "Touch": 0, "Taste": 0, "Smell": 0}

        for row in reader:
            word, sight, hearing, touch, taste, smell = row

            modalities["Sight"] += float(sight)
            modalities["Sound"] += float(hearing)  
            modalities["Touch"] += float(touch)
            modalities["Taste"] += float(taste)
            modalities["Smell"] += float(smell)

            counts["Sight"] += 1
            counts["Sound"] += 1
            counts["Touch"] += 1
            counts["Taste"] += 1
            counts["Smell"] += 1
        
        mean_valence = {modality: modalities[modality] / counts[modality] for modality in modalities}

        return mean_valence


    
    
# Do not modify the following line
if __name__ == "__main__":
    # You can write code to test your function here
    pass 
