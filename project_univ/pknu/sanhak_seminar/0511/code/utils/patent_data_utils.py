import re
import pickle

def find_all_number(text):
    extract_number = re.findall(r'\d+', text)
    extract_number.sort()
    return extract_number

def check_pair_data(extract_src_number, extract_trg_number):
    if len(extract_src_number) != len(extract_trg_number):
        return False
    for src_num, trg_num in zip(extract_src_number, extract_trg_number):
        if src_num != trg_num:
            return False
    return True


def save_pickle(save_dir, data):
    with open(save_dir, 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
    
    
def load_pickle(load_dir):
    with open(load_dir, 'rb') as f:
        data = pickle.load(f)
        return data