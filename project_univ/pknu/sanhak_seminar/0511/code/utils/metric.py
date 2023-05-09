import pyter
from tqdm import tqdm
from nltk.translate.bleu_score import sentence_bleu


def cal_bleu_score_by_batch(df, reference_column, prediction_column):
    score_results = []
    for prediction, reference in tqdm(df[[prediction_column, reference_column]].values):
        score = cal_bleu_score_by_instance(prediction, reference)
        score_results.append(score)
    return sum(score_results) / len(score_results)

    
def cal_bleu_score_by_instance(prediction, reference):
    prediction = prediction.split(' ')
    reference = [reference.split(' ')]
    bleu_score = sentence_bleu(reference, prediction, weights=(1, 0, 0, 0))
    return bleu_score
    

def edit_dist(str1, str2):
    dp = [[0] * (len(str2)+1) for _ in range(len(str1) + 1)]
    for i in range(1, len(str1)+1):
        dp[i][0] = i
    for j in range(1, len(str2)+1):
        dp[0][j] = j

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

    return dp[-1][-1]


def cal_ter(prediction, reference):
    prediction = prediction.split(' ')
    reference = [reference.split(' ')]
    ter_score = pyter.ter(prediction, reference)
    return ter_score