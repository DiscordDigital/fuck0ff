#!/bin/bash
iosroot=/mnt

argument=$1

if [ -z "$1" ];
then
    echo Please specify theme to patch
    exit
fi

for f in $iosroot/private/var/mobile/Containers/Data/Application/*; do
    testpath=$f/Library/Caches/TelephonyUI-7
    if [ -f "$testpath/en-0-+--mask.png" ] || [ -f "$testpath/other-0-+--mask.png" ];
    then
        searchfolder=$f
    fi
done


if [ ! -z "$searchfolder" ];
then
    uipath=$searchfolder/Library/Caches/TelephonyUI-7

    if [ "$1" == "extract-template" ];
    then
        if [ ! -d "template" ];
        then
            mkdir template
        fi
        cp $uipath/* template/
        echo Extraction finished
        exit
    fi

    if [ "$1" == "remove" ];
    then
        rm -rf $uipath
        echo Restart phone app to regenerate cache
        exit
    fi
    echo Patching..
    unzip -o $1 -d $uipath
    echo Quick fixup
    if [ -f "$uipath/en-_---white.png" ];
    then
        mv $uipath/en-_---white.png $uipath/en-\*---white.png
    fi
    if [ -f "$uipath/en-_---mask.png" ];
    then
        mv $uipath/en-_---mask.png $uipath/en-\*---mask.png
    fi
    if [ -f "$uipath/other-_---white.png" ];
    then
        mv $uipath/other-_---white.png $uipath/other-\*---white.png
    fi
    if [ -f "$uipath/other-_---mask.png" ];
    then
        mv $uipath/other-_---mask.png $uipath/other-\*---mask.png
    fi
    echo Restart phone app to see effect
else
    echo Could not find phone folder
fi
