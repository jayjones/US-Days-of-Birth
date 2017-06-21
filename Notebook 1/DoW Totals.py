with open("births.csv", "r") as f:
  cleaned = f.read().split("\n")

data = cleaned[1::]
day_counts = {}
for i in data:
    day = i.split(',')
    if day[3] in day_counts:
        day_counts[str(day[3])] += int(day[4])
    else:
        day_counts[str(day[3])] = int(day[4])

import matplotlib.pyplot as plt

print(day_counts)
plt.bar(range(len(day_counts)), day_counts.values())
plt.xticks(range(len(day_counts)), ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"), rotation=45)

plt.show()