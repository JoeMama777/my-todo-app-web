MYLISTFILE = "my_list.txt"

def get_numbered_task_list(filepath=MYLISTFILE):
    """
    This function pulls a numbered task list.
    Nice way to comment using three quotes.
    """
    with open(filepath,'r') as file_local:
        current_list = file_local.readlines()
        #for index, item in enumerate(current_list):
        #    stripped_item = item.strip("\n")
        #    list_index = index + 1
        #    row = f"{list_index} - {stripped_item}"
        #    print(row)
        return current_list

def write_current_list(current_list, filepath=MYLISTFILE):
    with open(filepath, 'w') as write_current_list_file:
        write_current_list_file.writelines(current_list)

def write_completed_list(completed_tasks, filepath=MYLISTFILE):
    with open(filepath, 'w') as write_completed_file:
        write_completed_file.writelines(completed_tasks)

