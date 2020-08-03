#!/bin/bash

echo "Shell 传递参数!"

echo "第一个参数: $1"
echo "第二个参数: $2"
echo "第三个参数: $3"

echo "传递的参数个数: $#"

echo "传递的参数以一个字符串显示: $*"

echo "传递的参数以多个字符串显示: $@"

echo "Shell使用的当前选项: $-"

echo "Shell最后命令的退出状态: $?"

echo "脚本运行的当前进程ID号: $$"
echo "脚本运行的最后一个进程ID号: $!"

echo "=======\$*的示例========"
for i in "$*"
do 
	echo $i
done


echo "=======\$@的示例========"
for i in "$@"
do 
	echo $i
done


