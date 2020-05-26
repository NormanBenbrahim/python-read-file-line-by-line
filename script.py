from sys import argv 

def read_file(txt_file, delimiter):
    output = []

    with open(txt_file, 'r') as f:
        try:
            for line in f.readlines():
                line_delimited = line.split(delimiter)
                for i in range(len(line_delimited)):
                    line_delimited[i] = line_delimited[i].replace('\n', '')
                
                output.append(line_delimited)
        except Exception as e:
            print("ERROR: {}".format(e))

    return output

if __name__ =='__main__':
    print(read_file(argv[1], ','))