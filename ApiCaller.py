import requests
import time

def call_webpage(url, num_calls):
    for i in range(num_calls):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Call {i+1}: Success")
            else:
                print(f"Call {i+1}: Failed with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Call {i+1}: Failed with error {e}")
        time.sleep(1) 

if __name__ == "__main__":
    url = "" 
    num_calls = 500 
    call_webpage(url, num_calls)
