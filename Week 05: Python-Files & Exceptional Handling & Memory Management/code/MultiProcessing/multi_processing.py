import requests

url = "https://picsum.photos/2000/3000"

import time
def time_test(func):
    def timer_test_inner():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return timer_test_inner

# With out Using Multiprocessing 
@time_test
def image_download():
    for i in range(10):
        req = requests.get(url)
        with open(f"file/{i}.jpg", "wb") as f:
            f.write(req.content)


if __name__=="__main__":
    image_download()
    #with out using multiprocessing this function take time to finish  around 15s to 20s

#with Multiprocessing 
import multiprocessing
import time
import requests

def mlt_processing_test():
    pros=[]
    url = "https://picsum.photos/2000/3000"

    def image_download(url, name):
        req = requests.get(url)
        with open(f"file/{name}.jpg", "wb") as f:
            f.write(req.content)

    for i in range(10, 21):
    
        p = multiprocessing.Process(target=image_download, args=[url, i])
        p.start()
        pros.append(p)

    for prs in pros:
        prs.join()
    
if __name__ == "__main__":
    t1 = time.perf_counter()
    mlt_processing_test()
    t2 = time.perf_counter()
    print(t2-t1)
    #Using multiprocessing this function take time to finish  around 3s to 6s


