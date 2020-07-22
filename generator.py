import subprocess
import random
import sys

def main():
    # create an array of words
    words = subprocess.run(['cat /usr/share/dict/words'], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8').split("\n")
    # determine how many iterations to run from argv
    iterations = 1
    try:
        iterations = int(sys.argv[1])
    except IndexError:
        iterations = 1
    # run iterations
    for n in range(iterations):
        # seed random with /dev/urandom
        randomSeed = subprocess.run(['cat /dev/urandom | head -c 1024'], stdout=subprocess.PIPE, shell=True).stdout
        random.seed(randomSeed)
        result = ""
        # pick 5 words, and append each to result
        for a in range(5):
            result += " " + random.choice(words)
        # trim and print the result
        print(result.lower().strip())

if __name__ == '__main__':
    main()
