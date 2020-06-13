# CODIS-DNA-Databases
### Part of my CS50 Course.


## Background
DNA, the carrier of genetic information in living things, has been used in criminal justice for decades. But how, exactly, does DNA profiling work?
Given a sequence of DNA, how can forensic investigators identify to whom it belongs?


Well, DNA is really just a sequence of molecules called nucleotides, arranged into a particular shape (a double helix). Each nucleotide of DNA contains one of four different bases: adenine (A), cytosine (C), guanine (G), or thymine (T). Every human cell has billions of these nucleotides arranged in sequence.
Some portions of this sequence (i.e. genome) are the same, or at least very similar, across almost all humans,
but other portions of the sequence have a higher genetic diversity and thus vary more across the population.


One place where DNA tends to have high genetic diversity is in Short Tandem Repeats (STRs). An STR is a short sequence of DNA bases that tends to repeat consecutively numerous times at specific locations inside of a person’s DNA.
The number of times any particular STR repeats varies a lot among individuals. In the DNA samples below,
for example, Alice has the STR AGAT repeated four times in her DNA, while Bob has the same STR repeated five times.

### What Now ?
Ok so basically what my program does is get a txt file and compare it to a database in the form of CSV file.
My program compute the longest run of consecutive repeats of the STR in the DNA sequence from the txt file.
If the STR counts match exactly with any of the individuals in the CSV file, we're printing out the name of the matching individual.
I used REGULAR EXPRESSIONS in this task and saved 100+ lines of code just by googling for Pattern Matching :smiley: . 

## Sources:
* [PATTERN MATCHING WITH REGULAR EXPRESSIONS](https://automatetheboringstuff.com/2e/chapter7// "Automate The Boring Stuff")
* [Regex Tester](https://regex101.com// "RE Testing")


# Example For DB 

Name  | AGAT | AATG  | TATC
---- | ---- | ---- | ----
Alice  | 28  | 42  | 14
Bob  | 17  | 22  | 19  
Charlie  | 36  | 18  | 25


## How To Run:
Open project's directory in your terminal and run one of this commands:

 ```python dna.py databases/(small/large).csv sequences/(1-20).txt```

