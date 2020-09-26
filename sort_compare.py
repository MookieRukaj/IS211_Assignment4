import time
import random


def insertion_sort(initlist):
    startime = time.time()

    for index in range(1, len(initlist)):
        initvalue = initlist[index]
        position = index

        while position > 0 and initlist[position - 1] > initvalue:
            initlist[position] = initlist[position - 1]
            position = position - 1

        initlist[position] = initvalue

    outime = time.time()

    runtime = outime - startime

    return (runtime, initlist)


def gap_insertion_sort(initlist, start, gap):
    for i in range(start + gap, len(initlist), gap):
        initvalue = initlist[i]
        position = i
        while position >= gap and initlist[position - gap] > initvalue:
            initlist[position] = initlist[position - gap]
            position = position - gap

        initlist[position] = initvalue


def shell_sort(initlist):
    startime = time.time()

    seclist = len(initlist) // 2
    while seclist > 0:
        for initposition in range(seclist):
            gap_insertion_sort(initlist, initposition, seclist)

        seclist = seclist // 2

    outime = time.time()

    runtime = outime - startime

    return (runtime, initlist)


def python_sort(initlist):
 
    startime = time.time()

    initlist.sort()

    outime = time.time()

    runtime = outime - startime

    return (runtime, initlist)


def list_gen(maximum):
    samp = random.sample(range(1, (maximum + 1)), maximum)
    return samp


def main():
    sampsize = [500, 1000, 10000]
    tests = {'Insertion': 0,
             'Shell': 0,
             'Python': 0}

    for smpl in sampsize:
        numb = 0
        while numb < 100:
            test = list_gen(smpl)
            tests['Insertion'] += insertion_sort(test)[0]
            tests['Shell'] += shell_sort(test)[0]
            tests['Python'] += python_sort(test)[0]
            numb += 1

        print ('For sample size %s:' % (smpl))

        for tst in tests:
            print (('%s Sort took %10.7f seconds to run, '
                   'on average.') % (tst, tests[tst] / numb))

if __name__ == '__main__':
    main()
