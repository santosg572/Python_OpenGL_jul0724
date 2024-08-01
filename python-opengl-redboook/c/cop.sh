#!/bin/bash

g++ ${1}.c -o ${1} -lGL -lGLU -lglut

./${1}
