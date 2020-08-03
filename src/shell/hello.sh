#!/bin/zsh


var1="wangzhefeng"
greeting1="hello, "$var1" !"
greeting2="hello, ${var1} !"

echo $greeting1 $greeting2


var2="wangzhefeng"
greeting1='hello, '$var2' !'
greeting2='hello, ${var2} !'

echo $greeting1 $greeting2