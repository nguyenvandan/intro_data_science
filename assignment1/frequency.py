import json
import sys

total_number_terms = 0
terms = []
terms_frequency = []

def print_frequency():
    global total_number_terms
    global terms
    global terms_frequency
    
    print "total = ", total_number_terms
    
    for x in xrange(len(terms)):
        print str(terms[x]), str("\t"), "{0:.5f}".format(float(terms_frequency[x])/int(total_number_terms))
    


def frequency_term(tweet_text_list):
    global total_number_terms
    global terms
    global terms_frequency
    
    for term in tweet_text_list:
        # find the position of the term in the list of terms existing
        index_value = -1
        try:
            index_value = terms.index(term)
        except ValueError:
            index_value = -1
        # if the term doesn't exists in the dictionary, add
        if index_value == -1:
            terms.append(term)
            terms_frequency.append(1)
            total_number_terms += 1
        # if exists, update
        else:
            terms_frequency[index_value] += 1


def frequency_cal(tweet_file_path):
    tweet_file = open(tweet_file_path)
        
    # Load line by line of the tweet
    for tweet in tweet_file:
        tweet_text = json.loads(tweet).get('text', 'XXX')
        # Load line by line of the sentiment dictionary
        if tweet_text != 'XXX':
            tweet_text_list = tweet_text.encode('utf-8').split()
            # calcul frequency
            frequency_term(tweet_text_list)
   

                
	
def main():
    frequency_cal(sys.argv[1])
    print_frequency()

if __name__ == '__main__':
    main()
