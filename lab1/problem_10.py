str =  "This is CSE303 course. The name of CSE303 is: Statistics for Data Science. It's a fundamental CSE course for future data scientists."
substring = "CSE303"

appeared = 0
for i in range(len(str) - len(substring) + 1):
  if str[i:i+len(substring)] == substring: 
    appeared = appeared + 1

print("Appeared: ", appeared)
