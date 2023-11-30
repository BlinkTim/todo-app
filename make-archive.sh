#!/bin/bash

zip_name="todoApp-$(date +%Y%m%d_%H%M%S).zip"
git archive --format=zip HEAD -o "../$zip_name"

echo "Created zip: $zip_name"

