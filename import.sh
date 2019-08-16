#!/bin/bash
shopt -s nullglob;

partdir="/home/yuu/windows/parts"
hpmordir="/home/yuu/hugo/hpmorru-site"


mkdir -p ${hpmordir}/data/parts;
mkdir -p ${hpmordir}/data/out;

echo Copying files;

cp ${partdir}/*.md ${hpmordir}/data/parts;
cp ${partdir}/hpmor_ru.epub ${hpmordir}/static/files/hpmor_ru.epub;
cp ${partdir}/hpmor_ru.fb2.zip ${hpmordir}/static/files/hpmor_ru.fb2.zip;
cp ${partdir}/hpmor_ru.mobi ${hpmordir}/static/files/hpmor_ru.mobi;
cp ${partdir}/hpmor_ru_pandoc.html ${hpmordir}/static/files/hpmor_ru.html;

python3 import_md_hpmor.py;

echo Copying converted files;
cp ${hpmordir}/data/out/*.md ${hpmordir}/content/book/1;

echo Cleaning

rm ${hpmordir}/data/parts/*;
rm ${hpmordir}/data/out/*;
rm ${partdir}/*

