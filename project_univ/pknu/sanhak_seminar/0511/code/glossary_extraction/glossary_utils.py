import re


def connect_word_alignments(model, src, trg):
    src = src.replace("'", " ' ").replace('  ', ' ').strip()
    src_sentence, trg_sentence = src.split(' '), trg.split(' ')
    alignments = model.get_word_aligns(src_sentence, trg_sentence)['itermax']
    return alignments, src_sentence, trg_sentence


def reconstruct_word_alignments(alignments):
    src_dicts = {}
    tgt_dicts = {}
    for src_idx, tgt_idx in alignments:
        src_idx, tgt_idx = str(src_idx), str(tgt_idx)
        if src_dicts.get(src_idx, None) == None:
            src_dicts[src_idx] = tgt_idx
        else:
            src_dicts[src_idx] += f'-{tgt_idx}'

        if tgt_dicts.get(tgt_idx, None) == None:
            tgt_dicts[tgt_idx] = src_idx
        else:
            tgt_dicts[tgt_idx] += f'-{src_idx}'
    return src_dicts, tgt_dicts


def glossary_combination(key_sentence, value_sentence, word_alignments_dicts, glossary_candidates, mode='src'):
    for k, v in word_alignments_dicts.items():
        value_glossary = value_sentence[int(k)]
        v = v.split('-')
        key_glossary = ''
        for v_idx, v_ins in enumerate(v):
            if v_idx == 0 or abs(int(v_ins) - int(v[v_idx-1])) == 1:
                key_glossary += f' {key_sentence[int(v_ins)]}'
            else:
                break
        if mode == 'src':
            glossary_candidates.append([value_glossary.strip(), key_glossary.strip()])
        else:
            glossary_candidates.append([key_glossary.strip(), value_glossary.strip()])
    return glossary_candidates


def cal_edit_dist_ratio(df):
    '''
    :param df:
    :return:
    '''
    df['edit_dist_ratio'] = df['edit_dist'] / df['trg_glossary'].str.len()
    df['edit_dist_ratio'] = df['edit_dist_ratio'].round(1)
    return df


def detect_special_character(text, punc='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'):
    pattern = r'[' + punc + ']+'
    if re.search(pattern, text) is not None or '''\\n''' in text:
        return False
    else:
        return True
    

def detect_unique_glossary_by_freq_and_special_characters(df):
    glossary_freq = df['src_glossary'].value_counts().items()
    one_freq_glossary = []
    for row in glossary_freq:
        g, c = row
        if c == 1 and detect_special_character(g):
            one_freq_glossary.append(g)
    return one_freq_glossary


def detect_glossary_by_edit_distance(df, min_score, max_score, one_freq_glossary):
    return df[(df.edit_dist_ratio > min_score) & (df.edit_dist_ratio < max_score) & (df.src_glossary.isin(one_freq_glossary))]


def filter_glossary_for_gold(df, min_score, max_score):
    '''
    :param df:
    :param min_score:
    :param max_score:
    :return:
    '''
    one_freq_glossary = detect_unique_glossary_by_freq_and_special_characters(df)
    df = detect_glossary_by_edit_distance(df, min_score, max_score, one_freq_glossary)

    return df