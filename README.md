# TextNoise
Add noise to text with a given probability.
* Randomly delete a word
* Randomly insert a random word
* Randomly replace a word with a random word
* Randomly permute text

Results are 100% reproducable with a random seed

## Requirment
NumPy

## Install
Download the repo and unzip
```
wget https://github.com/TahaAslani/TextNoise/archive/refs/heads/main.zip
unzip main.zip
```

Go to the main directory
```
cd TextNoise-main
```

Download the list of words for random insertion
```
bash download-vocab.sh
```

## Usage

Insert a random word between each 2 words with probability of 50% and permute the words. 
```
python add_noise.py --input_file in.txt --output_file out.txt --insert 0.5 --permutation True --seed 42 --verbose True
```

Randomly delete each word with probability of 50% and permute the words. 
```
python add_noise.py --input_file in.txt --output_file out.txt --delete 0.5
```
