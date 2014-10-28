import json
import sys
import re

term_sentiment_words = []
term_sentiment_scores = []

def print_new_dic():
    global term_sentiment_words
    global term_sentiment_scores
    for x in xrange(len(term_sentiment_words)):
        print str(term_sentiment_words[x]), str("\t"), term_sentiment_scores[x]
    


def deduce_term_sentiment(tweet_text_list, score):
    global term_sentiment_words
    global term_sentiment_scores
    for term in tweet_text_list:
        # find the position of the term in the new dictionary
        index_value = -1
        try:
            index_value = term_sentiment_words.index(term)
        except ValueError:
            index_value = -1
        # if the term doesn't exists in the dictionary, add
        if index_value == -1:
            term_sentiment_words.append(term)
            term_sentiment_scores.append(score)
        # if exists, update
        else:
            term_sentiment_scores[index_value] += score


def sentiment_cal(sent_file_path, tweet_file_path):
    sent_file = open(sent_file_path)
    tweet_file = open(tweet_file_path)
    
    words_num = len(sent_file.readlines())
    words = [0 for x in xrange(words_num)]
    scores = [0 for x in xrange(words_num)]
    num = -1
    sent_file.seek(0)
    # Load line by line of the sentiment dictionary
    for line_word in sent_file:
        words_str = line_word.split('\t')
        if len(words_str) == 2:
            num += 1
            words[num] = words_str[0]
            scores[num] = int(words_str[1])

     # Load line by line of the tweet
    for tweet in tweet_file:
        line_score = 0
        tweet_text = json.loads(tweet).get('text', 'XXX')
        if tweet_text != 'XXX':
            tweet_text_list = tweet_text.encode('utf-8').split()
            for x in xrange(num):
                score = (tweet_text_list.count(words[x]))*int(scores[x])
                if score != "":
                    line_score += int(score)
            # Deduce new dictionary
            deduce_term_sentiment(tweet_text_list, line_score)
   

                
	
def main():
    sentiment_cal(sys.argv[1], sys.argv[2])
    print_new_dic()

if __name__ == '__main__':
    main()
