import time
import random


def sequential_search(a_list, item):
    strt_time = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end_time = time.time()

    run_time = end_time - strt_time

    return (run_time, found)


def ordered_sequential_search(initlist, item):
    initlist = sorted(initlist)

    startime = time.time()
    pos = 0
    found = False
    stop = False

    while pos < len(initlist) and not found and not stop:
        if initlist[pos] == item:
            found = True
        else:
            if initlist[pos] > item:
                stop = True
            else:
                pos = pos + 1

    outime = time.time()

    runtime = outime - startime

    return (runtime, found)


def binary_search_iterative(initlist, item):

    initlist = sorted(initlist)

    startime = time.time()
    first = 0
    last = len(initlist) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if initlist[mid] == item:
            found = True
        else:
            if item < initlist[mid]:
                last = mid - 1
            else:
                first = mid + 1

    outime = time.time()

    runtime = outime - startime

    return (runtime, found)


def binary_search_recursive(initlist, item):
    initlist = sorted(initlist)

    startime = time.time()

    if len(initlist) == 0:
        found = False
    else:
        mid = len(initlist) // 2
        if initlist[mid] == item:
            found = True
        else:
            if item < initlist[mid]:
                return binary_search_recursive(initlist[:mid], item)
            else:
                return binary_search_recursive(initlist[mid + 1:], item)

    outime = time.time()

    runtime = outime - startime

    return (runtime, found)


def list_gen(maximum):
        samplist = random.sample(range(1, (maximum + 1)), maximum)
        return samplist


def main():
    samp = [500, 1000, 10000]
    tests = {'Sequential': 0,
             'Ordered': 0,
             'Bin Iterative': 0,
             'Bin Recursive': 0}

    for smpl in samp:
        nmb = 0
        while nmb < 100:
            test = list_gen(smpl)
            tests['Sequential'] += sequential_search(test, -1)[0]
            tests['Ordered'] += ordered_sequential_search(test, -1)[0]
            tests['Bin Iterative'] += binary_search_iterative(test, -1)[0]
            tests['Bin Recursive'] += binary_search_recursive(test, -1)[0]
            nmb += 1

        print ('For sample size %s:' % (smpl))

        for tst in tests:
            print(('%s Search took %10.7f seconds to run, '
                   'on average.') % (tst, tests[tst] / nmb))


if __name__ == "__main__":
    main()
