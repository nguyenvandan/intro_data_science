import json
import sys
import re


def sentiment_cal(sent_file_path, tweet_file_path):
    sent_file = open(sent_file_path)
    tweet_file = open(tweet_file_path)
    
    words_num = len(sent_file.readlines())
    words = [0 for x in xrange(words_num)]
    scores = [0 for x in xrange(words_num)]
    num = -1
    sent_file.seek(0)
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
        # Load line by line of the sentiment dictionary
        if tweet_text != 'XXX':
            tweet_text_list = tweet_text.encode('utf-8').split()
            for x in xrange(num):
                score = (tweet_text_list.count(words[x]))*int(scores[x])
                if score != "":
                    line_score += int(score)
        print line_score
   

                
	
def main():
    sentiment_cal(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
