def preprocessing_src_sentence(src, df):
    preprocessing_glossary_dict = {}
    glossary_num = 1
    for src_glossary, trg_glossary in df[['src_glossary', 'trg_glossary']].values:
        src_glossary = src_glossary.split(' ')
        if isinstance(src, str):
            src = src.split(' ')
        preprocessing_symbol = '{' + f'Magellan{glossary_num}'+ '}'
        if len(src_glossary) > 1:
            for i in range(0, len(src) - len(src_glossary)+1):
                if src[i:i+len(src_glossary)] == src_glossary or ' '.join(src_glossary) in ' '.join(src[i:i+len(src_glossary)]):
                    src = ' '.join(src)
                    src_glossary = ' '.join(src_glossary)
                    src = src.replace(src_glossary, preprocessing_symbol)
                    preprocessing_glossary_dict[preprocessing_symbol] = trg_glossary
                    glossary_num += 1

        else:
            if src_glossary[0] in src:
                src = ' '.join(src)
                src_glossary = ' '.join(src_glossary)
                src = src.replace(src_glossary, preprocessing_symbol)
                preprocessing_glossary_dict[preprocessing_symbol] = trg_glossary
                glossary_num += 1
        if glossary_num > 3:
            break
    if isinstance(src, list):
        src = ' '.join(src)
    return src, preprocessing_glossary_dict     

def postprocessing_trg_sentence(translated_preprocessing_src, preprocessing_glossary_dict):
    for k, v in preprocessing_glossary_dict.items():
        # k: mask / v: original German word
        translated_preprocessing_src = translated_preprocessing_src.replace(k, v)
    return translated_preprocessing_src