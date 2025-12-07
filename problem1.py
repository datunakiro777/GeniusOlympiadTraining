m_and_d = str(input('ender m and d: '))
amount_and_duration = m_and_d.split()
amount = int(amount_and_duration[0])
duration = int(amount_and_duration[1])
end_time = 0
for i in range(amount):
    x_and_y = str(input('enter x and y: '))
    StartTime_and_LatestTime = x_and_y.split()
    start_time = int(StartTime_and_LatestTime[0])
    latest_time = int(StartTime_and_LatestTime[1])
    if i == 0:
        end_time = start_time
    if end_time + duration >  latest_time:
        print(0)
        break
    else:
        end_time += duration
if i == (amount - 1):
    print(1)

