import json, os, time
flag = False
for i in range(10):
    os.system("aws ecs describe-services --services rafa-service --cluster rafa-ecsECSCluster > service.json")
    text = open("service.json", "r").read()
    message = json.loads(text)["services"][0]["events"][0]["message"]
    if "steady" in message:
        flag = True
        break
    else:
        time.sleep(2)
if not flag:
    os.system("cat failure.json")



    
