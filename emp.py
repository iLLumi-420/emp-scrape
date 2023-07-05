import requests
import pandas as pd
import json

url = "https://foreignjob.dofe.gov.np/api/LotSearch/GetLotList"

data = []

def get_data():
    page = 1
    lastpage = 50
    while(page<lastpage):
        payload = {
            "postdata": (
                None,
                json.dumps(
                    {
                        "Offset": f"{page}",
                        "Limit": "10",
                        "Country": "Kuwait",
                        "SkillType": "",
                        "SkillName": "",
                        "CompanyName": "",
                        "SearchText": "",
                        "SalaryFrom": "0",
                        "SalaryTo": "0",
                        "Gender": "Male",
                        "SortBy": "Deadline",
                        "OrderBy": "0",
                        "RaName": "",
                        "InterviewVenue": "",
                        "InterviewDateFrom": "",
                        "InterviewDateTo": "",
                        "TodayOnly": "false",
                    }
                ),
            ),
            "isSearched": (None, "true"),
        }

        response = requests.post(url, data=payload)

        if response.status_code == 404:
            lastpage = page
            return

        if response.status_code == 200:
            json_data= response.json()
            result = json_data['result']
            data.extend(result)
        else:
            print('some error while retreving data')
        page += 1

        
get_data()


df = pd.DataFrame(data)

df.drop('sn', axis=1, inplace=True)
df.drop('rowTotal', axis=1, inplace=True)

df.to_excel('output.xlsx', index=False)


