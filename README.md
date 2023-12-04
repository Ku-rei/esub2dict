# esub2dict

This programs parses a text files, making a list of all vocabulary used, orders the word list based on the frequency and gives some possible translations for each of them. 

The final language hasn't been selected yet, so for now let's assume it's Italian.

Work in progress!

## Pseudocode
Open txt file <br>
Remove dash (-) unless there's an alphabetic letter before and after. <br>
Remove all characters that are not alphabetic or dash (-). Keep accented letters and apostrophes. <br>
Create a list with all words remaining <br>
Count the number of times every word occurs <br>
Order words of the list (higher frequency words first) <br>
If same frequency alphabetic order <br>
Create a dictionary {A:B} <br>
Go through every word of the list, look up the word in an English-Italian XML file and fill the dictionary. ---> Find unlicensed dictionary. <br>
Create a CSV with two columns: left English words, right Italian words. <br>
