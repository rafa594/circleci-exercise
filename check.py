import json, os, time, sys
flag = False
time.sleep(3)
for i in range(10):
    os.system("aws ecs describe-services --services "+ os.environ.get('SERVICE_NAME') + " --cluster "+ os.environ.get('CLUSTER_NAME') + " > service.json")
    text = open("service.json", "r").read()
    message = json.loads(text)["services"][0]["events"][0]["message"]
    print(message)
    if "steady" in message:
        flag = True
        break
    else:
        time.sleep(6)
print (flag)
if not flag:
    sys.exit(1)



    
