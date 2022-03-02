cd app/

# Start rasa server

rasa run --model models --enable-api --cors "*" --debug \ -p $PORT