#!/bin/bash
# -*- coding: utf-8 -*-

curator_cli delete_indices --host "$CURATOR_HOST" --filter_list "{\"filtertype\":\"age\",\"source\":\"name\",\"timestring\":\"%Y.%m.%d\",\"unit\":\"$CURATOR_UNIT\",\"unit_count\":$CURATOR_COUNT}"
