import requests
import json

def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=628f446bfa80584cf07b316950edf280&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])
    
if __name__ == "__main__":
    main()