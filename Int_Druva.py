"""Given array arr = [-1, 4, 2, 0, 3, 7], and a target target = 6,
find all the pairs of numbers in the array that add up to the target.
E.g. (-1, 7), (4, 2)"""
arr = [-1, 4, 2, 0, 3, 7]

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == 6:
            print((arr[i],arr[j]))

# =================================================

""""
Given string s = “aaabbcdddeeeeeffabbb”, return the string “3a2b1c3d5e2f1a3b”
"""""
s = "aaabbcdddeeeeeffabbb"
count = 1
out = []
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        out.append(f"{count}{s[i-1]}")
        count = 1
out.append(s[-1])
print("".join(out))

# ----------------
"""
WhatsApp backup:-

1. Chats only backup (no media)
2. Scheduled backup which happens every day at 2 AM on local storage
3. Manually triggered backup which happens on the Google Drive
4. Scheduled backup as well for Google Drive with frequency Day/Week/Month
5. Backup can happen in background
6. If phone battery is less than 20%, then the backup should be paused, and once charging is on, backup should resume
7. Backup should be usable (user should be able to restore from this)
"""
