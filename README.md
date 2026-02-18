# \# Webhook Processor

# 

# A lightweight Flask-based webhook listener that demonstrates core SaaS integration patterns.

# 

# \## Features

# 

# \- REST endpoint for receiving webhook events

# \- Idempotency protection using event IDs

# \- Structured logging for observability

# \- JSON validation with proper HTTP responses

# 

# \## Architecture

# 

# Client System → Webhook Endpoint → Idempotency Check → Processing Logic → Response

# 

# \## Run Locally

# 

# pip install -r requirements.txt

# python app.py

# 

# \## Example Request

# 

# curl -X POST http://127.0.0.1:5000/webhook \\

# -H "Content-Type: application/json" \\

# -d "{\\"event\_id\\":\\"abc123\\",\\"type\\":\\"user.created\\"}"

# 

# \## Example Responses

# 

# First request:

# {

# &nbsp; "status": "processed"

# }

# 

# Duplicate request:

# {

# &nbsp; "status": "duplicate"

# }



