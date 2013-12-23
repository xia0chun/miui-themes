#!/bin/bash

#定义变量i为数值型
typeset -i i

#遍历name文件，每一行保存为数组的一个元素
i=0
for name in $(cat name)
do
	arry_name[$i]=$name
	i=$i+1
done

#遍历id文件，每一行保存为数组的一个元素
i=0
for id in $(cat id)
do
	arry_id[$i]=$id
	i=$i+1
done

#遍历url文件，每一行保存为数组的一个元素
i=0
for url in $(cat url)
do
	arry_url[$i]=$url
	i=$i+1
done

for i in $(seq 70)
do
	wget -O ~/MIUI/Download/${arry_id[$i-1]}.${arry_name[$i-1]}.mtz ${arry_url[$i-1]}
	sleep 5
done
