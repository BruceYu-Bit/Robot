import json, requests
import win32com.client
import speech
api_url = "http://openapi.tuling123.com/openapi/api/v2"
spk=win32com.client.Dispatch("SAPI.SpVoice")
while 1:
    text_input = input('我：')
    # text_input=speech.input()
    # print("我："+text_input)
    data = {
        "perception":
        {
            "inputText":
            {
                "text": text_input
            },
            # 可选参数
            # "inputImage": {
            #     "url": "imageUrl"
            # },
            # 可选参数
            # "selfInfo":
            # {
            #     "location":
            #     {
            #         "city": "上海",
            #         "province": "上海",
            #         "street": "文汇路"
            #     }
            # }
        },

        "userInfo":
        {
            "apiKey": "b10cb8df314c479e8bf65d70196908a1",
            "userId": "422632"
        }
    }
    data = json.dumps(data).encode('utf8')
    response_str = requests.post(api_url, data=data, headers={'content-type': 'application/json'})
    response_dic = response_str.json()
    results_text = response_dic['results'][0]['values']['text']
    print('SB机器人：' + results_text)
    spk.Speak(results_text)