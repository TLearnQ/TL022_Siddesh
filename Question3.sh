#!/bin/bash
Set -e

#ip route show

count=$(ip route show default | wc -l)

if [ "$count" -eq 1 ]; then
    echo "OK: Single default route detected"
elif [ "$count" -gt 1 ]; then
    echo "WARN: Multiple default routes detected"
else
    echo "ERROR: No default route found"
fi
