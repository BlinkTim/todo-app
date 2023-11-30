#!/bin/bash
zip_name="todo-app.zip"
git archive --format=zip HEAD -o "../$zip_name"
echo "Created zip: $zip_name"

