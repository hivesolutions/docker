#!/bin/bash
# -*- coding: utf-8 -*-

NAME=${NAME-$(date +%s)}

echo "Building '$NAME' using '$BUILDER' and '$EXEC'"

if [ "$BUILDER" == "Dockerfile" ]; then
    docker build $EXEC
else
    NAME=$NAME BUILDER=$BUILDER /repo/$EXEC
fi
