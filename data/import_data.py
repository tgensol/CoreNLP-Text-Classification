"""
Import sample data for recommendation engine
"""

import predictionio
import argparse
import random
import csv

SEED = 3

def import_events(client, file):
  random.seed(SEED)
  count = 0
  print("Importing data...")

  with open(file, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for data in spamreader:
        properties = {"text":data[1], "replyTo":data[2], "gender":data[3],"bdate":data[4], "lang":data[5], "platform":data[6]}
        res = client.create_event(
          event="choose",
          entity_type="contact",
          entity_id=data[0],
          properties=properties
        )
        print(res)
        count += 1
  print("%s events are imported." % count)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description="Import sample data for recommendation engine")
  # parser.add_argument('--access_key', default='invald_access_key')
  parser.add_argument('--url', default="http://35.199.37.111:7070")
  parser.add_argument('--file', default="./data-import.csv")

  args = parser.parse_args()

  client = predictionio.EventClient(
    access_key='KLdE6Xa4gjkFQHgUFOBv3oXBVbnPCMOekf8LWCXNJaMVutBlCoi2YJNFJTNBjXqw',
    url=args.url,
    threads=5,
    qsize=500)
  import_events(client, args.file)
