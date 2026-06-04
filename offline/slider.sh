#!/bin/bash

DIRECTORY="/pictures"

SCRIPT_DIR="$(pwd)"

if [ ! -d "$DIRECTORY" ]; then
  mkdir -m 777 "$DIRECTORY"
  echo "slider.sh: Created $DIRECTORY"
fi

until curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8000 | grep -q "200"; do
  echo "slider.sh: Sleeping 1 second until service is online"
  sleep 1
done

echo "slider.sh: Deleting old database, running database migrations and fixtures"
cd "${SCRIPT_DIR}/.." || { echo "slider.sh: Error changing directory"; exit 1; }
rm backend/db.sqlite3
rm backend/media/*.*
cp offline/slider_offline_initial.json backend
docker compose exec app bash -c 'python manage.py migrate && python manage.py loaddata slider_offline_initial.json'
rm backend/slider_offline_initial.json

echo "slider.sh: Uploading pictures"
find "$DIRECTORY" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) | sort | while read -r file; do
  curl --silent --location 'http://127.0.0.1:8000/api/v1/picture/' \
    --header 'Authorization: Token 1234' \
    --form "file=@\"$file\"" \
    --form 'author="."' > /dev/null
  echo "slider.sh: Uploaded: $file"
done

echo "slider.sh: Running chromium"
chromium-browser --kiosk --disable-infobars --noerrdialogs --incognito http://127.0.0.1:8000/slider/