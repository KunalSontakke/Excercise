"""Transfer-Encoding: chunked is a method used in HTTP to transmit data in chunks rather than in single,continuous stream.
 It's commonly used when the size of the data being transferred is not known in advance or when it's large.
 This method allows the server to start sending the response before it knows the total size of the data.

Here's how it works:
    Chunking: The data is divided into smaller parts or "chunks." Each chunk is preceded by its size in hexadecimal format
    followed by a carriage return and line feed (\r\n), and then the chunk itself.
    The final chunk is a zero-sized chunk, indicating the end of the transmission.

    Streaming: This technique allows for the progressive rendering of content in the browser or processing of data on the client-side
    without having to wait for the entire response to be received."""

"""
The 'Connection': 
'keep-alive' header in an HTTP response indicates the intention of the server to maintain the TCP connection open
for subsequent requests from the same client.

When a server sends 'Connection': 'keep-alive' in the response headers, 
it informs the client (such as a web browser or an API client) that it's allowing the current TCP connection to remain open for a certain period, 
rather than closing it immediately after sending the response. This allows the client to reuse the same connection for sending subsequent requests, 
reducing the overhead of establishing new connections for each request.
"""

# ========================================================================================================================

"""
Write a Python program to find the Requests module version, licence, copyright information, author, author email,
document url, title and description
"""

import requests
# print("requests version :",requests.__version__)
# print("requests licence : ",requests.__license__)
# print("requests copyright :",requests.__copyright__)
# print("requests author :",requests.__author__)
# print("requests author email :",requests.__author_email__)
# print("requests document url :",requests.__url__)
# print("requests url : ",requests.__title__)
# print("requests description :",requests.__description__)

# =====================================================================================================================
"""Write a Python program to check the status code issued by a server in response to a client's request made to the server. 
Print all of the methods and attributes available to objects on a successful request."""

# response1 = requests.get("https://www.google.com",verify=False)
# print(response1.status_code)
#
# response2 = requests.get("https://www.flipkart.com",verify=False)
# print(response2.status_code)
#
# response3 = requests.get("https://www.w3resource.com",verify=False)
# print(response3.status_code)

# ====================================================================================================================
"""Write a Python program to send a request to a web page, and print the response text and content. 
Also get the raw socket response from the server"""

# print(dir(response3))

# response = requests.get("https://anapioficeandfire.com/api/characters/583",verify=False,auth=None,data=None,params=None)
# print("text",response.text)
# print("content",response.content)
# print("raw",response.raw)
# print("is redirect :",response.is_redirect)
# print("url",response.url)
# print("links :",response.links)
# print("headers",response.headers)

# =============================================================================================================
"""Write a Python program to send a request to a web page, and print the header information. 
Also parse these values and print key-value pairs holding various information."""

# response = requests.get("https://anapioficeandfire.com/api/characters/583",verify=False)
# r = response.headers

# for key,value in r.items():
#     print(key,":",value)

# ==============================================================================================================
""" Write a Python program to send a request to a web page, 
and print the JSON value of the response. Print each key value in the response. """

# response = requests.get("https://anapioficeandfire.com/api/characters/583",verify=False)

# response_json = response.json()

# for key,value in response_json.items():
#     print(key,":",value)

# =============================================================================================================
""" Write a Python program to send a request to a web page and stop waiting for a response after a given number of seconds. 
If a request times out, raise a Timeout exception."""
# try:
#     response = requests.get("https://anapioficeandfire.com/api/characters/583",verify=False,timeout=1)
#     response.raise_for_status()
#     print(response.status_code)

# except TimeoutError as e:
#     print(e)
# except requests.RequestException as e:
#     print(e)

# =========================================================================================================

"""Write a Python program to send some sort of data in the URL's query string."""
# url = 'https://httpbin.org/get'
# payload = {"key1" : "value1","key2" : "value2"}
# response = requests.get(url=url,verify=False,params=payload)
# print(response.status_code)
# print(response.text)


# ================================================================================================================

"""Write a Python program to send cookies to a given server and access cookies from the response of a server."""
# cookies = {"cookie":"value"}
# response = requests.get("https://httpbin.org/get",verify=False,cookies=cookies)
# print(response.text)
# print(response.cookies)
# print(response.headers)


