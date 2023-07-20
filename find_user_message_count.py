from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    lst=0
    for i in data["messages"]:
        if users_id==str(i['id']):
            lst+=1
    return lst
file_path='data/result.json'
data=read_data(file_path)
print(find_user_message_count(data,users_id='1'))