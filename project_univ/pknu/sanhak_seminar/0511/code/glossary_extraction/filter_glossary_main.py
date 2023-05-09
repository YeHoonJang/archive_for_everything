import sys
sys.path.append('../')


from utils.patent_data_utils import save_pickle, load_pickle
from utils.translate import translate_text
from utils.metric import edit_dist
from glossary_utils import cal_edit_dist_ratio, detect_unique_glossary_by_freq_and_special_characters, filter_glossary_for_gold
from tqdm import tqdm
from googletrans import Translator
import pandas as pd


def main():
    data_dir = "../../../data/netmarble/data/preprocessed"
    total_glossary_candidates = load_pickle(f'{data_dir}/combination_glossary.pkl')

    translated_glossary_df = pd.read_csv(f'{data_dir}/glossary_candidate.csv')


    translated_glossary_df['edit_dist'] = translated_glossary_df.apply(lambda x: edit_dist(x['trg_glossary'], x['translated_glossary']), axis=1)
    translated_glossary_df = cal_edit_dist_ratio(translated_glossary_df)  # Task 1
    gold_glossary_df = filter_glossary_for_gold(translated_glossary_df, min_score=0.1, max_score=0.9)  # Task 2
    gold_glossary_df.sort_values(by="src_glossary", key=lambda x: x.str.len(), ascending=False, inplace=True)
    gold_glossary_df.to_csv(f'{data_dir}/gold_glossary.csv', index=False)


if __name__ == '__main__':
    main()