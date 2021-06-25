from sample_class import SampleClass
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import datetime

if __name__ == "__main__":
    print("---start add---")
    print(SampleClass.add(1, 2))
    print("---end add---")
    print("---start add2---")
    print(SampleClass.add2(1, 2))
    print("---end add2---")
    print("---start sum1---")
    start_time = datetime.datetime.now()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(SampleClass.sum, 100000000)
    end_time = datetime.datetime.now()
    print("---end sum1:{}---".format(end_time - start_time))

    print("---start sum2---")
    start_time = datetime.datetime.now()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(SampleClass.sum, 100000000)
        executor.submit(SampleClass.sum, 100000000)
    end_time = datetime.datetime.now()
    print("---end sum2:{}---".format(end_time - start_time))

    print("---start sum3---")
    start_time = datetime.datetime.now()
    with ProcessPoolExecutor(max_workers=2) as executor:
        executor.submit(SampleClass.sum, 100000000)
    end_time = datetime.datetime.now()
    print("---end sum3:{}---".format(end_time - start_time))

    print("---start sum4---")
    start_time = datetime.datetime.now()
    with ProcessPoolExecutor(max_workers=2) as executor:
        executor.submit(SampleClass.sum, 100000000)
        executor.submit(SampleClass.sum, 100000000)
    end_time = datetime.datetime.now()
    print("---end sum4:{}---".format(end_time - start_time))
