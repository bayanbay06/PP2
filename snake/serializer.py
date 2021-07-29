import json


def serialize(score: int):
    data = dict(score=score)
    with open('score_data.txt', 'w') as score_file:
        json.dump(data, score_file)


def deserialize():
    with open('score_data.txt') as score_file:
        data = json.load(score_file)
    return data.get('score')
