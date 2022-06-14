# RandomTextEdit
Apply random manipulation to the text with a given probability.

Random manipulation can be used for data augmentation or adding noise.

Functions:
* Randomly delete a word
* Randomly insert a random word
* Randomly replace a word with a random word
* Randomly permute text

Results are 100% reproducable with a random seed.

## Requirment
NumPy

## Install
Download the repo and unzip
```
wget https://github.com/TahaAslani/RandomTextEdit/archive/refs/heads/main.zip
unzip main.zip
```

Go to the main directory
```
cd RandomTextEdit-main
```

Download the list of words for random insertion
```
bash download-vocab.sh
```

## Usage

Insert a random word between each 2 words with probability of 50% and permute the words. 
```
python RandomTextEdit.py --input_file in.txt --output_file out.txt --insert 0.5 --permutation True --seed 42 --verbose True
```

Randomly delete each word with probability of 50% and permute the words. 
```
python RandomTextEdit.py --input_file in.txt --output_file out.txt --delete 0.5
```

Randomly replace each word (with probability of 50%) with a ransom word and permute the words. 
```
python RandomTextEdit.py -i in.txt -o out.txt -r 0.5 -p True 
```
