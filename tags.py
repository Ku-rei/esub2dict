import re

def remove_tags(input_text):
    # regular expression pattern to match tags
    pattern = re.compile(r'<[^>]*>')
    
    # use the pattern to remove all tags
    return re.sub(pattern, '', input_text)

file_path = 'Vicon_eng_ita'  # change if the input file name is different
with open(file_path, 'r', encoding='utf-8') as file:
    text_content = file.read()

# invoke the function to get the text without the tags
notags = remove_tags(text_content)

# write the updated text content to a new file
output_file = 'notags.txt'  # name of the output file
with open(output_file, 'w', encoding='utf-8') as output:
    output.write(notags)

print("Tags removed and saved to", output_file)