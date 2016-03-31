#!/bin/bash
# -*- coding: utf-8 -*-

NAME=${NAME-$(date +%s)}
FULL_NAME=${FULL_NAME-$REPO/$NAME}

echo "Building '$NAME' using '$BUILDER' and '$EXEC'"

if [ "$BUILDER" == "Dockerfile" ]; then
    docker build $EXEC --tag=$FULL_NAME
else
    NAME=$NAME FULL_NAME=$FULL_NAME BUILDER=$BUILDER /repo/$EXEC
fi

docker push $FULL_NAME
