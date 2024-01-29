import cantools

# Define the path to your DBC file
dbc_path = 'path_to_your_dbc_file.dbc'

# Load the DBC file
db = cantools.database.load_file(dbc_path)

# Define your CAN messages
can_messages = [
    "0x00000303 1f 00 00 00 10 00 00 01",
    "0x00000303 10 00 00 00 10 00 00 01"
]

# Function to decode CAN messages
def decode_can_messages(messages, database):
    decoded_messages = []
    for message in messages:
        message_id, data = message.split('\t')
        message_id = int(message_id, 16)  # Convert hex to int
        data = bytes.fromhex(data.strip())  # Convert data to bytes
        decoded = database.decode_message(message_id, data)
        decoded_messages.append(decoded)
    return decoded_messages

# Decode and print the messages
decoded_messages = decode_can_messages(can_messages, db)
for decoded in decoded_messages:
    print(decoded)

# Đầu tiên, bạn cần cài đặt thư viện cantools vào môi trường làm việc của bạn. Bạn có thể làm điều này bằng câu lệnh sau:

# pip install cantools
# Sau khi đã cài đặt thư viện, hãy làm theo các bước sau:

# Lưu đoạn mã Python trên vào một tệp tin với tên, ví dụ: decode_can.py.
# Thay đổi đường dẫn tới tệp tin DBC trong biến dbc_path trong đoạn mã để phản ánh đường dẫn chính xác đến tệp tin DBC của bạn.
# Chạy đoạn mã Python này trong môi trường của bạn. Đoạn mã sẽ tải tệp tin DBC và sử dụng nó để giải mã các bản tin CAN mà bạn cung cấp.
# Đoạn mã có các chức năng sau:

# cantools.database.load_file(dbc_path): Tải và phân tích cú pháp tệp tin DBC.
# decode_can_messages(can_messages, db): Hàm này nhận vào danh sách các bản tin CAN và database được tải từ tệp tin DBC, sau đó giải mã mỗi bản tin và trả về kết quả đã giải mã.
# Đối với các bản tin CAN của bạn, hãy chắc chắn rằng chúng được định dạng đúng và thêm vào danh sách can_messages. Đoạn mã sẽ chạy và in ra kết quả đã giải mã cho mỗi bản tin CAN.