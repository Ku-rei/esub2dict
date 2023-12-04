# esub2dict

This programs parses a text files, making a list of all vocabulary used, orders the word list based on the frequency and gives some possible translations for each of them. 

The final language hasn't been selected yet, so for now let's assume it's Italian.

Work in progress!

## Pseudocode
Open txt file
Remove dash (-) unless there's an alphabetic letter before and after.
Remove all characters that are not alphabetic or dash (-). Keep accented letters and apostrophes.
Create a list with all words remaining
Count the number of times every word occurs
Order words of the list (higher frequency words first)
If same frequency alphabetic order
Create a dictionary {A:B}
Go through every word of the list, look up the word in an English-Italian XML file and fill the dictionary. ---> Find unlicensed dictionary.
Create a CSV with two columns: left English words, right Italian words.