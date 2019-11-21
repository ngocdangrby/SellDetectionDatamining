import re
import crf_tokenizer
from crf_tokenizer import CrfTokenizer

crf_tokenizer_obj = CrfTokenizer()
# crf_tokenizer_obj.train('../data/tokenized/samples/training')

def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u'\U0001F900-\U0001F999'
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def remove_common_sign(text):
    pattern = r'[-.,=()\\"\'/:*&%!?<>;#|,^+[~\]]'
    return re.sub(pattern," ", text)
    

def remove_phone_number(text):
    
    phone_pattern = "\(?(?:\+84|84|0)(?:\d{2,3})?\)?[ .-]?\d{2,4}[ .-]?\d{2,4}[ .-]?\d{2,4}"
    return re.sub(phone_pattern, 'số_điện_thoại', text)

def remove_website_link(text):
    incorrect_prefix = ["http : //", "http: //", "https: //", "https : //"]
    for x in incorrect_prefix:
        text = text.replace(x, "http://")
    website_pattern = "(http\S+|bit.ly\S+|goo.gl\S+|tinyurl.com\S+)"
    return re.sub(website_pattern, "link_website", text.strip())

def remove_price(text):
    price_pattern = r"(()#\b(\d+\S+|\d+)(k|vnd|vnđ|đ|d|m)\b|\b(\d+\S+|\d+)tr\b|\b\d+(k|vnd|vnđ|đ|d|m)\b|(?:\d{2,3})?\)?[.,]?\d{2,4}[.,]?\d{0,3}[.,]?\d{3}(|\s)(k|vnd|vnđ|đ|d|m))"
    return re.sub(price_pattern, "giá_sản_phẩm", text)

def tokenizer_using_crf(text):
    tokenized_sent = crf_tokenizer_obj.get_tokenized(text)
    return tokenized_sent
    # tokens = crf_tokenizer_obj.tokenize(text)
    # print(tokens)
def remove_number(text):
    number = r"\b\d+\b"
    return re.sub(number,"", text)

def pre_process(text):
    text = str(text)
    text = text.lower()
    text = remove_emoji(text)
    text = remove_price(text)
    text = remove_website_link(text)
    text = remove_phone_number(text)
    text = remove_common_sign(text)
    text = remove_number(text)
    text = tokenizer_using_crf(text)
    return text