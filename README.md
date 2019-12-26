# python_and_shell
python脚本和shell 脚本的结合

echo "参数个数为：$#";
echo "传递的参数作为一个字符串显示：$*";
echo "current pid is: $$";
echo "background last pid is: $!";
echo "显示最后命令的退出状态: $?"

uname -a
lsb_release -a

function getState() {
    echo "参数个数为：$#";
    return 10
}

#解压文件，压缩文件
tar -C /extract/to/path -xzvf /path/to/archive.tar.gz
tar -czvf /path/to/archive.tar.gz /path/to/directory


while getopts "a:bc" arg #选项后面的冒号表示该选项需要参数
do
        case $arg in
             a)
                echo "a's arg:$OPTARG" #参数存在$OPTARG中
                ;;
             b)
                echo "b"
                ;;
             c)
                echo "c"
                ;;
             ?)  #当有不认识的选项的时候arg为?
            echo "unkonw argument"
        exit 1
        ;;
        esac
done


#cat names.log | python namescount.py | sort -rn | head -n 5
