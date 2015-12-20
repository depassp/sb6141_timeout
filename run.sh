#!/bin/bash
HERE=$(readlink -f $(dirname $0))
cd $HERE
scrapy crawl sb6141
