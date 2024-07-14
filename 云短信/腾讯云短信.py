from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
from utils import get_codes
import tencentConfig

class Ten_Sms():
    def __init__(self,appkey):
        self.appkey = appkey

    def Sms_Sender(self,mobile):
        app_id = tencentConfig.APP_ID
        app_key = self.appkey
        template_id = tencentConfig.TEMPLATE_ID
        phone_number = mobile
        sms_sign = tencentConfig.SMS_SIGN
        code = get_codes()
        Sender = SmsSingleSender(app_id,app_key)
        params = [code,'3']
        try:
            result = Sender.send_with_param(86,phone_number,template_id,params,sign=sms_sign)
        except HTTPError as e:
            print(e)
            return False
        except Exception as e:
            print(e)
            return False
        return result

if __name__ == '__main__':
    sender = Ten_Sms(tencentConfig.APP_KEY)
