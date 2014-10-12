#!/bin/bash
if [[ `salmon status` != *not* ]]
then
  salmon stop
fi
salmon start
