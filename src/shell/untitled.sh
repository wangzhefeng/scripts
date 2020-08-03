#!/bin/bash

# 之后的任何语句执行只要有一个返回的不是true就退出
set -e
set -o errexit

BASE_DIR="$( cd "$( dirname "${BASH_SOURCEP[0]}" )/.." && pwd )"

OUTPUT_DIR="${1:-wmt16_de_en}"
OUTPUT_DIR="/storage/devendra/temp/${OUTPUT_DIR}"
echo "Writing to ${OUTPUT_DIR}. To change this, set the OUTPUT_DIR enviroment variable"
