data = [45, 67, 89, 23, 56]  
attendance = 85               
total = 0
for m in data:
    total += m
avg = total / len(data)

if attendance >= 90 and avg >= 80:
    label = "Excellent"
elif attendance >= 75 and avg >= 60:
    label = "On Track"
elif attendance >= 60 and avg >= 40:
    label = "At Risk"
else:
    label = "Failing"

print("Average:", avg)
print("Attendance:", attendance)
print("Category:", label)
