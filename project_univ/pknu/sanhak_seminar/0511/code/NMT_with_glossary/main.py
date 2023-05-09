import sys
sys.path.append('../')

import warnings
warnings.filterwarnings("ignore")

import os
import pickle
import pandas as pd
from tqdm import tqdm
from googletrans import Translator
from processing import preprocessing_src_sentence, postprocessing_trg_sentence
from utils.translate import translate_text, ERROR_MESSAGE
from utils.metric import cal_bleu_score_by_instance, cal_ter

translater = Translator()

data_dir = "../../../data/netmarble/data/preprocessed"
use_mt_df = pd.read_csv(f'{data_dir}/patent_add_translated_mt_df.csv')
gold_glossary_df = pd.read_csv(f'{data_dir}/gold_glossary.csv')

our_model_bleu = []
gcp_model_bleu = []
our_model_ter = []
gcp_model_ter = []
for en, de, gcp_pred in tqdm(use_mt_df[['English', 'German', 'API_V2_Translated']].values):
    try:
        preprocessing_src, preprocessing_glossary_dict = preprocessing_src_sentence(en, gold_glossary_df)
        translated_preprocessing_src = translate_text(preprocessing_src, translater)
        translated_result = postprocessing_trg_sentence(translated_preprocessing_src, preprocessing_glossary_dict)

        our_bleu = cal_bleu_score_by_instance(translated_result, de)
        gcp_bleu = cal_bleu_score_by_instance(gcp_pred, de)

        our_ter = cal_ter(translated_result, de)
        gcp_ter = cal_ter(gcp_pred, de)

        our_model_bleu.append(our_bleu)
        gcp_model_bleu.append(gcp_bleu)
        our_model_ter.append(our_ter)
        gcp_model_ter.append(gcp_ter)
    except:
        continue


result_dir = "../../../data/netmarble/data/result"
if not os.path.isdir(result_dir):
    os.mkdir(result_dir)

with open(os.path.join(result_dir, "our_bleu.pkl"), "wb") as f:
    pickle.dump(our_model_bleu, f)
    f.close()

with open(os.path.join(result_dir, "our_ter.pkl"), "wb") as f:
    pickle.dump(our_model_ter, f)
    f.close()

with open(os.path.join(result_dir, "gcp_bleu.pkl"), "wb") as f:
    pickle.dump(gcp_model_bleu, f)
    f.close()

with open(os.path.join(result_dir, "gcp_ter.pkl"), "wb") as f:
    pickle.dump(gcp_model_ter, f)
    f.close()