# utils.py
import json
import string

def load_config(file_path='config.json'):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_character_set(config):
    characters = ''
    if config['include_uppercase']:
        characters += string.ascii_uppercase
    if config['include_lowercase']:
        characters += string.ascii_lowercase
    if config['include_digits']:
        characters += string.digits
    if config['include_special']:
        characters += string.punctuation
    characters = ''.join([char for char in characters if char not in config['exclude_characters']])
    return characters
