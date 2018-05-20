import requests
import json
import numpy as np
import pandas as pd

import sklearn as sk
import tensorflow as tf

from keras.models import Sequential
from keras.layers import Dense

PERSONALITY_DATA = [{'id_num': 0, 'name': 'Alice', 'personality_index': 0.3},
                       {'id_num': 1, 'name': 'Bob', 'personality_index': 0.5},
                       {'id_num': 2, 'name': 'Charlie', 'personality_indexg': 0.8}]

def get_personality_match_rating(personality, id_num):
    raw = 1 - (personality - PERSONALITY_DATA[id_num]['personality_index'])
    sq = math.sqrt(raw)
    return sq

def get_personality_model():
    # vectorization of personality evaluation into personality index number
    pass

def get_nationwide_mock_customer_data():
    response = requests.get('http://nw-angelhack-2018-mocks.us-east-1.elasticbeanstalk.com/customers')
    json_data = json.loads(response.text)
    return json_data

def match_houses():
    pass

def main():
    pass

if __name__ == "__main__":
    main()