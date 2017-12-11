#!/bin/sh
NOW=$(date +"%d-%m-%y-%H-%M")
PATHTO="./"
FILE="$NOW.txt"
FULLPATH="$PATHTO$FILE"
java net.tinyos.tools.MsgReader OscilloscopeMsg > $FULLPATH
