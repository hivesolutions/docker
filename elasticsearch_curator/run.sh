#!/bin/bash
# -*- coding: utf-8 -*-

curator_cli --host "$CURATOR_HOST" delete-indices --filter_list "{\"filtertype\":\"age\",\"source\":\"name\",\"timestring\":\"%Y.%m.%d\",\"unit\":\"$CURATOR_UNIT\",\"unit_count\":$CURATOR_COUNT,\"direction\":\"older\"}"
