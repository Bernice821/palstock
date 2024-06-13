
echo "Start deploying"
# python main.py

echo "Starting the Flask app using Gunicorn..."
gunicorn app:app -b :5000 --daemon

# 确认应用是否启动成功
if [[ $? -eq 0 ]]; then
    echo "Application is running."
else
    echo "Failed to start the application."
    exit 1
fi

echo "Complete!"