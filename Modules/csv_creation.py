from datetime import datetime

month_to_text = {1: 'Jan', 2: 'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}

def file_path():
    current_month = datetime.now().month
    month_text = month_to_text[current_month]
    path = '/Users/benmeller/OneDrive - The University of Sydney (Students)/Uni/Engd1000/Prototype/text_messages/Output/' + month_text + '.csv'

    return path


def create_csv():
    path = file_path()
    f = open(path, 'w')

    headers = ['date', 'as_level', 'tds_level', 'f_level', 'ecol_bool', 'as_safe', 'f_safe', 'tds_rec', 'ecol_safe', 'safe', 'unknown input']

    # Place headers into file
    for word in headers:
        if word == headers[-1]:
            f.write(word)
        else:
    	    f.write(word + ',')
    f.write('\n')
    f.close()
