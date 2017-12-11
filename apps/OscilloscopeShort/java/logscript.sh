#!/bin/sh
NOW=$(date +"%d-%m-%y-%H-%M")
PATHTO="./"
FILE="$NOW.txt"
FULLPATH="$PATHTO$FILE"
if cygpath -w / >/dev/null 2>/dev/null; then
  CLASSPATH="oscilloscope.jar;$CLASSPATH"
else
  CLASSPATH="oscilloscope.jar:$CLASSPATH"
fi
java net.tinyos.tools.MsgReader OscilloscopeMsg > $FULLPATH
