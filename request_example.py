import requests

def fetchPosts():
    # requests.get is a synchronous function (not a asynchronous function lol)
    # if you need async (need to make requests concurrently, or db qs), theres a lib called asyncio 
    # we'll learn about it later
    # python is single threaded like js, but doesn't have an event loop like js
    # so we will just wait for our request to finish lol. 
    response = requests.get('https://jsonplaceholder.typicode.com/posts/')
    status_code = response.status_code

    # no beautiful try catch
    if status_code != 200:
        # no beautiful throw new Error
        raise RuntimeError(f"An error occured. Http status {status_code}")
    else: 
        # ey look its our buddy .json()
        response_json = response.json()
        return response_json


results = fetchPosts()


for result in results: 
    user_id = result['userId']
    title = result['title']
    print(f" -> ID: {user_id} made a post with the title {title}")