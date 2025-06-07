
echo "Waiting for PostgreSQL..."

while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
  sleep 1
done

echo "PostgreSQL started"

exec "$@"