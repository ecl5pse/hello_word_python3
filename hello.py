with open('mydata.txt') as fp:
    for line in iter(fp.readline, ''):
        process_lin = (line)
        print(process_lin)