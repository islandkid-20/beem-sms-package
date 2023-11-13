from beem_sms.sms_sender import SMSSender
import responses

#testing APUI key
API_KEY = "38e0721c4b4b6095"
SECRET_KEY = "ODUzYmJiYmEzMjEzZTc3NGYxOGM2YjE2ZDJjOGVkNGEzMDI0MWQwN2Q4MjljNGQyNGJiNTUzOTM0NWEzZDliMg=="
BASE_URL = "https://apisms.beem.africa/v1/send"
SOURCE_ADDR = "INFO"

@responses.activate
def test_send_sms_success():
    # Mock successfully response from the SMS API wihtout making a real HTTP request method
    responses.add(responses.POST, BASE_URL, status=200)
    
    sms_sender = SMSSender(api_key= API_KEY, secret_key=SECRET_KEY, base_url=BASE_URL)
    message = sms_sender.send_sms(source_addr=SOURCE_ADDR, dest_addr="255742892731", message="Hi, James")
    print("message: ", message)

@responses.activate
def test_send_sms_failure():
    responses.add(responses.POST, BASE_URL, status=500, body="Internal Server Error")
    sms_sender = SMSSender(api_key= API_KEY, secret_key= SECRET_KEY, base_url=BASE_URL)

    message = sms_sender.send_sms(source_addr=SOURCE_ADDR, dest_addr="255742892731", message="Hi, There")
    print("message: ", message)

