# esub2dict

This programs parses a text files, making a list of all vocabulary used, orders the word list based on the frequency and gives some possible translations for each of them. 

The final language depnds on the CSV dictionary available. I'll be using an English-Italian dictionary. English as input is necessary as the program doesn't yet know how to handle special characters or fonts. Additionally it does not work with languages with no whitespaces between words (Japanese/Chinese...). Italian as output is optional, but keep in mind that utf-8 is being used for the output file as well as the input file and dictionary.

Work in progress!

## Pseudocode
1 Open txt file <br>
2 Remove tags, typically <i> and </i> seen in subtitle files.
3 Remove dash (-) unless there's an alphabetic letter before and after. <br>
4 Remove all characters that are not alphabetic or dash (-). Keep accented letters and apostrophes. <br>
5 Create a list with all words remaining <br>
6 Count the number of times every word occurs <br>
7A Order words of the list (higher frequency words first) <br>
7B Order words of the list (alphabetically). User argument to decide between <br>
8 Create a dictionary file for the specific vocabulary used in the input file {A:B} <br>
9 Go through every word of the list, look up the word in a generic (English-Italian) CSV dictionary file and fill the new dictionary. <br>
10 Put the dictionary into a new CSV file. <br>
