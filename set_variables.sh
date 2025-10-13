set -a
source .env
envsubst < ./backend/src/.env > ./backend/src/.env.filled
mv ./backend/src/.env.filled ./backend/src/.env
set +a
