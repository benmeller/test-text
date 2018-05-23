import glob
from xml.dom import minidom


class text_class:
    def __init__(self, date, body):
        self.date = date
        self.text = body


def latest_file_paths():
    # *.xml specifies all xml files in the directory
    list_of_files = glob.glob('./messages/*.xml')

    latest_file = list_of_files[-1]
    second_latest_file = list_of_files[-2]

    return latest_file, second_latest_file


def xml_parse(latest_file):
    body_array = []
    readable_date = []

    # parse an xml file by name
    mydoc = minidom.parse(latest_file)

    # Get individual all text messages and data in system
    texts = mydoc.getElementsByTagName('sms')

    # Place different bits of text into an array
    for i, elem in enumerate(texts):
        # Only add text message that were received, not sent
        if elem.attributes['type'].value == "1":
            body_array.append(elem.attributes['body'].value)
            readable_date.append(elem.attributes['readable_date'].value)

    return body_array, readable_date



def find_new_entries(second_file_path, body_array, readable_dates):
    second_file = minidom.parse(second_file_path)
    texts_second = second_file.getElementsByTagName('sms')

    receive_count = 0

    # Place different bits of text into an array
    for elem in texts_second:
        # Find amount of messages received from last one
        if elem.attributes['type'].value == "1":
            receive_count += 1


    body_array = body_array[receive_count:]
    readable_dates = readable_dates[receive_count:]

    return body_array, readable_dates


def format_dates(dates):
    for i in range(len(dates)):
        dates[i] = dates[i].replace(',', '')
    return dates


def new_texts():
    latest_path, slatest_path = latest_file_paths()
    texts, dates = xml_parse(latest_path)
    texts, dates = find_new_entries(slatest_path, texts, dates)
    dates = format_dates(dates)

    texts_array = []

    for i in range(len(texts)):
        current_text = texts[i]
        current_date = dates[i]
        texts_array.append(text_class(current_date, current_text))

    return texts_array
