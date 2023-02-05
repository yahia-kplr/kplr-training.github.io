_start = "https://colab.research.google.com/github/kplr-training"
_end = "colab-badge.svg"

def replace_substring(input_string):
    start_index = input_string.find(_start)
    end_index = input_string.find(_end)
    if start_index != -1 and end_index != -1 and end_index > start_index:
        return input_string[:start_index] + input_string[start_index:end_index+3].replace('%20', '-') + input_string[end_index+3:]
    else:
        return input_string

input_file = '/Users/saxen/Documents/GitHub/kplr-training.github.io/notebooks/Data-Preparation/1-Débuter-avec-Pandas/Exercices-et-Solutions/1_Exercices-2.html'

with open(input_file, 'w+') as file:
    input_strings = file.readlines()
    output_strings = [replace_substring(input_string) for input_string in input_strings]
    file.writelines(output_strings)
