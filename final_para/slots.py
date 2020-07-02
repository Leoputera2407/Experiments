import re
def handle_slots(raw_sent):
    """
    Function subtitute slots in raw sentence with an instance of that slot, so T5 can process the sentence
    ARGS
    ----
        raw_sent (string)
    RETURNS
    -------
        (string): a corrected sentence processable by T5
    """
    get_slots = re.findall(r'{(.*?)}', raw_sent)
    return get_slots

raw_sent = 'we are the {hero} my {friend}'
print(handle_slots(raw_sent))
