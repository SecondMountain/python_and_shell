import sys,getopt


def usage():
    print(" -h  get help.")
    print(" -i  input file.")
    print(" -o  output file.")
    print(sys.argv[0])  # file name
    print(sys.argv[1])  # arg 1
    print(sys.argv[2])  # arg 2
    for arg in sys.argv:
        print(arg)

import sys,getopt
if __name__ == '__main__':
    opts,args = getopt.getopt(sys.argv[1:],"hi:o:") #在这里加入了三个选项 h,i,o
    input_file = ""
    output_file = ""
    for op, value in opts:
        if op == "-i":
            input_file = value #获取输入文件名
        elif op == "-o":
            output_file = value #获取输出文件名
            print(output_file)
        elif op == "-h":
            usage() #输出帮助信息
            sys.exit()
    for arg in args:
        print(arg)

    try:
        input_file = open(input_file,mode="r")
    except IOError as e:
        pass
    except Exception as e:
        pass
    finally:
        pass
    input_file.readline()
    input_file.write()
    data="123456"
    input_file = open(input_file, mode="r")
    input_file.readline()  # 读取一行
    input_file.write(data)  # 写入数据
    input_file.close()  # 关闭文件

#标准输入输出流    
sys.stdin.readline()
sys.stdout.write()


