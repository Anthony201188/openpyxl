import openpyxl as xl
import numpy as np

wb = xl.Workbook()
ws = wb.active

score_data = [["Name", "Math", "Science"], ["Alice", 85, 90], ["Bob", 70, 75], ["Charlie", 95, 88], ["David", 78, 82]]
score_array = np.array(score_data)


for row in score_data:
    ws.append(row)

#NOTE - doing all the extra work just so I can use this slicing syntax and not a for loop was NOT  worth the effort!

scores_only_array = score_array[1:5, 1:3] #slicing syntax, nested_list = [start_row:end_row][start_column:end_column]


scores_only_array = scores_only_array.astype(int) # array contained strings so all elements of string type -> int.

# Calculate row-wise averages using axis=1
averages = np.mean(scores_only_array, axis=1)

print("scores only:")
print(scores_only_array)
print("Averages:")
print(averages)

averages_lst = averages.tolist()
averages_lst.insert(0,"Averages")
print("Averages with row text:",averages_lst)


ws.append(averages_lst)

wb.save("data.xlsx")
