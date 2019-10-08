import re
def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def remove_common_sign(text):
    pattern = "[-.,=()"":*]"
    return re.sub(pattern," ", text)

def remove_phone_number(text):
    phone_pattern = "\(?(?:\+62|62|0)(?:\d{2,3})?\)?[ .-]?\d{2,4}[ .-]?\d{2,4}[ .-]?\d{2,4}"
    return re.sub(phone_pattern, ' ', text)

def pre_process(text):
    text = remove_emoji(text)
    text = remove_common_sign(text)
    text = remove_phone_number(text)
    return text


text = "🎁 CODE NGÀY 21/03/2018 ￼ 🎁 ============== ￼ ❗ Mã : CODE2103❗ ============== ★ Lông Vũ Locke ★ Thần Vũ Locke ★ Ngọc Tiến Hóa ★ Ấn Ký Thành Tựu-Cao ★ Ấn Ký Danh Vọng-Cao ★ 100 Bụi Nguyên Tố ★ Bài Tarot ngẫu nhiên ★ Huy Hiệu Chiến trường cổ Đại ★ Cây Thông Noel ============================ * Lưu ý : Code chỉ sử dụng trong ngày. ============================ ￼ 👉 Bạn nhấn vào chữ vip ￼ 👉 rồi nhấn vào nạp thẻ hay hình nạp kim cương ở dưới ￼ 👉 là nó ra trang tài khoản nhé ￼ 👉 rồi nhập code vào mục giftcode nhé"
print (pre_process(text))
# " CODE NGÀY 21/03/2018                    Mã   CODE2103                 Lông Vũ Locke  Thần Vũ Locke  Ngọc Tiến Hóa  Ấn Ký Thành Tựu Cao  Ấn Ký Danh Vọng Cao  100 Bụi Nguyên Tố  Bài Tarot ngẫu nhiên  Huy Hiệu Chiến trường cổ Đại  Cây Thông Noel                                Lưu ý   Code chỉ sử dụng trong ngày                                 Bạn nhấn vào chữ vip   rồi nhấn vào nạp thẻ hay hình nạp kim cương ở dưới   là nó ra trang tài khoản nhé   rồi nhập code vào mục giftcode nhé"