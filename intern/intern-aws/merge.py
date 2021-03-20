import os
import pandas as pd
import json

def remove_and_merge(file_path):
    rdf = pd.read_json(file_path, lines=True)
    qoe = pd.io.json.json_normalize(rdf.qoe)
    frame = pd.read_pickle('/home/centos/data/concated_all_1.pkl')    
    try:
        qoe_ended = qoe.drop(qoe[qoe.event!='PlaybackEnded'].index)
        qoe_updated = qoe.drop(qoe[qoe.event!='PlaybackUpdated'].index)

        qoe_ended.dropna(axis=1, how='all', thresh=None, subset=None, inplace=True)
        qoe_updated.dropna(axis=1, how='all', thresh=None, subset=None, inplace=True)

        qoe_updated.sort_values(by=['sessionId', 'timestamp'], inplace=True)
        qoe_updated.drop_duplicates(subset=['sessionId'], keep='last', inplace=True)

        qoe_ended.index = qoe_ended['sessionId']
        qoe_updated.index = qoe_updated['sessionId']

        qoe_updated = qoe_updated.drop(columns=['contentUrl', 'device', 'deviceInfo.deviceId', 'deviceInfo.model',
           'deviceInfo.os', 'deviceInfo.osVersion', 'deviceInfo.player', 'event',
           'licenseInfo.drmSystem', 'licenseInfo.elapsedTime', 'licenseInfo.laUrl',
           'networkInfo.carrier.mcc', 'networkInfo.carrier.mnc',
           'networkInfo.carrier.name', 'networkInfo.type', 'qoeContentId',
           'redirectUrl', 'sessionId', 'timestamp'], axis = 1)

        merged_version =qoe_ended.join(qoe_updated, on=qoe_ended.index, how='left')
        merged_version = merged_version.drop(columns= ['sessionId'], axis = 1)
        merged_version.reset_index(inplace=True)
        
#         merged_version.to_pickle(file_path)
        
#         qoe = pd.read_pickle(file_path)
        frame = pd.concat([frame, merged_version])

    except:
        os.remove(file_path)
    
    frame.to_pickle('/home/centos/data/concated_all_1.pkl')

if __name__ == "__main__":
    raw_data_dir = "/home/centos/raw_data"

    for day_dir in os.listdir(raw_data_dir):
        day_dir = os.path.join(raw_data_dir, day_dir)
        for hour_dir in os.listdir(day_dir):
            hour_dir = os.path.join(day_dir, hour_dir)
            for file_name in os.listdir(hour_dir):
                file_path = os.path.join(hour_dir, file_name)
                remove_and_merge(file_path)
                print(file_name," is done!")
            print("============",hour_dir," files are done!! ============")
        print("***************", day_dir," directories are done!! ***************")