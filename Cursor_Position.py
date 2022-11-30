while  1:
        response = requests.get(IG_CFR_PAGE, headers=headers(""), params=params, cookies=cookies)
        if response.status_code == 200:
            cfr = response.json()
            for entry in cfr["data"]["data"]:
                #print(entry["text"])
                usernames.append(entry["text"])
            if cfr["data"]["cursor"]!= None:
                params['cursor'] = cfr["data"]["cursor"]
                time.sleep(1)
            else:
                break
        else:
           print(response.status_code)
           print("Error in request .... aborting")
           break
print("ok")
