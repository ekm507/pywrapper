import os

def wrap(filenames, outputFilename=''):
    """
        wraps some files into one big file or data section.

        use like this:
        + unwrap ( [a list of files names] )  --> outputs wrapped data
        
        or
        + unwrap ( [a list of files names], outputFilename='output file name' ) --> writes output into the file. no function output
    """
    n = len(filenames)
    sizes = []
    data = b''
    for filename in filenames:
        data_in = open(filename, 'rb').read()
        sizes.append(len(data_in))
        data += data_in
    
    outdata = b''
    outdata += str(n).encode('ascii')
    outdata += b'\n'

    for i in range(n):
        outdata += filenames[i].encode('utf-8')
        outdata += b'\n'
        outdata += str(sizes[i]).encode('ascii')
        outdata += b'\n'
    
    outdata += data


    if len(outputFilename) > 0:
        if not os.path.exists(os.path.dirname(outputFilename)):
            try:
                os.makedirs(os.path.dirname(outputFilename))
            except OSError as exc:
                if exc.errno == 2:
                    pass

        with open(outputFilename, 'wb') as outputFile:
            outputFile.write(outdata)

    return outdata
def unwrap(*args, **kwargs):
    """
        unwraps a file or some data that has been made by wrap function

        use like this:
        + unwrap ( filename )

        or
        + unwrap ( inputData )

        you can also provide output directory. like this:
        outputDir = 'output directory address'
    """

    if 'outputDir' in kwargs.keys():
        outputDir = kwargs['outputDir']
        if len(outputDir) > 1:
            if outputDir[-1] != '/':
                outputDir += '/'
    else:
        outputDir = ''

    outputDir = outputDir.encode()

    if len(args) == 1 and isinstance(args[0], str):
        inputFileName = args[0]
        inputData = open(inputFileName, 'rb').read()
        __unwrap_data__(inputData, outputDir)
    elif len(args) == 1 and isinstance(args[0], bytes):
        inputData = args[0]
        __unwrap_data__(inputData, outputDir)

def __unwrap_data__(inputdata, outDir):
    

    dataParts = inputdata.split(b'\n')
    
    n = int(dataParts[0])

    names = [0] * n
    sizes = [0] * n
    datas = [0] * n

    for i in range(n):
        names[i] = dataParts[i*2+1]
        sizes[i] = int(dataParts[i*2+2])
    
    files_data = b''.join([i+ b'\n' for i in dataParts[n*2+1:]])

    lastByte = 0
    for i in range(n):
        nextByte = lastByte+sizes[i]
        datas[i] = files_data[lastByte:nextByte]
        lastByte = nextByte

    if len(outDir) > 0:
        if not os.path.exists(outDir):
            try:
                os.makedirs(outDir)
            except OSError as exc:
                if exc.errno == 2:
                    pass


    for i in range(n):
        f = open(outDir + names[i], 'wb')
        f.write(datas[i])
        f.close()

