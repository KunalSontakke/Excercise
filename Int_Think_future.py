"""
1) Implicit wait,Explicit wait and time.sleep
2) Exceptions in selenium
3) Stale Element Exception
4) Difference between Javascript Executor and Selenium API
5) Ancestor,Sibling,Parent in XPath

"""

# ======================================================================================================================
# Input :- "i am the input"
# Output:- "the input am i"

ip = "i am the input"

ip_spl = ip.split()
res = " ".join(ip_spl[2:]+ip_spl[-3:-5:-1])
print(res)