held=int(input("number of classes held"))
attendance=int(input("number of classes attendance"))
if attendance>=75:
    attendance=(attendance/held)*100
    print("allowed in exam")
else:
    print("not allowed in exam")
