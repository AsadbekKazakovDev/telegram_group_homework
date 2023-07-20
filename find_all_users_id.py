from read_data import read_data

def find_all_users_id(ans: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    ans= read_data("data/result.json")
    lst = []
    for user in ans["messages"]:
        if user["type"]=='message':
            lst.append(user["id"])
    
    return lst
ans = ("data/result.json")
print(find_all_users_id(ans))