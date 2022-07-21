import pandas as pd

def save(name, owner, explain, upload_id):
    idx = len(pd.read_csv("data.csv"))
    new_df = pd.DataFrame({"name":name,
                           "owner":owner,
                           "explain":explain,
                           "upload_id":upload_id}, 
                         index = [idx])
    new_df.to_csv("data.csv",mode = "a", header = False)
    return None

def load_list():
    lost_list = []
    df = pd.read_csv("data.csv")
    for i in range(len(df)):
        lost_list.append(df.iloc[i].tolist())
    print(lost_list)

def now_index():
    df = pd.read_csv("data.csv")
    return len(df)-1


def load_lost(idx):
    df = pd.read_csv("data.csv")
    lost_info = df.iloc[idx]
    return lost_info


if __name__ =="__main__":
    load_list()