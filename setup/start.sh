# start.sh
#!/bin/bash
echo "Starting Celery worker..."
celery -A setup worker --pool=solo -l info
