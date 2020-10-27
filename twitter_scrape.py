import random
import twint
import sys
import time
# Usage: python twintSearchTweets.py "keyword" "start-date" "end-date" "hours to run the script"
# Example: python twintSearchTweets.py "via MyNt" "2019-01-01" "2019-06-01" "60"
config = twint.Config()
config.Search = sys.argv[1]

outputname = sys.argv[1].replace(" ","")

config.Since = sys.argv[2]
config.Until = sys.argv[3]
config.Output = outputname + "_" + config.Since + "_" + config.Until + "_elastic.tweet"
# config.Custom
# print(config.Retweets)
config.Native_retweets = True
config.Elasticsearch = "localhost:9200"

config.Index_tweets = outputname.lower()
filename = config.Output+"_resume.raw"

try:
    f = open(filename)
    f.close()
    config.Resume = filename
    print('Files exists!')
except FileNotFoundError:
    print('File does not exist')

t_end = time.time() + 60 * 60 * float(sys.argv[4])
n_iterations = 0
while time.time() < t_end and n_iterations<10:
    config.Native_retweets = not config.Native_retweets

    try:
        twint.run.Search(config)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
    
    n_iterations += 1
    if config.Resume == None:
        config.Resume = filename
    
    delay = random.randint(0,10)
    print('sleeping for {} secs'.format(delay))
    time.sleep(delay)

    print("-x-x-x-x-x-x-x-x-x-Iter done-x-x-x-x-x-x-x-x-x-x")
