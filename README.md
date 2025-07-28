# Spyglass Example Project

This is an example project demonstrating how to integrate with the Spyglass AI Platform for OpenAI API call tracing and monitoring.

## Application Setup

### 1. Install Dependencies

```bash
pip install -e .
# or if using uv:
uv sync
```

### 2. Configure Environment Variables

Copy the example environment file and fill in your API keys:

```bash
cp .env.example .env
```

Edit `.env` and set the following required variables:

- **SPYGLASS_API_KEY**: Your Spyglass API key (get this from your Spyglass dashboard)
- **SPYGLASS_DEPLOYMENT_ID**: Set to `spyglass-example-project` (must match GitHub workflow)
- **OPENAI_API_KEY**: Your OpenAI API key

### 3. Configure Model Settings

The `model.yaml` file contains your model configuration:
- **model**: The OpenAI model to use (e.g., "gpt-4", "gpt-3.5-turbo")
- **prompt**: The system prompt for your AI assistant

### 4. Run the Example

```bash
python main.py
```

The application will:
- Make OpenAI API calls every 3 seconds
- Automatically trace all calls using Spyglass
- Send telemetry data to the Spyglass platform

## Environment Variables Reference

### Required
- `SPYGLASS_API_KEY`: Your Spyglass API key
- `SPYGLASS_DEPLOYMENT_ID`: Deployment identifier (use `spyglass-example-project`)
- `OPENAI_API_KEY`: Your OpenAI API key

### Optional
- `SPYGLASS_OTEL_EXPORTER_OTLP_ENDPOINT`: Custom OTLP endpoint (default: production endpoint)

## What Gets Traced

This example demonstrates tracing for:
- **Function calls** using `@spyglass_trace()` decorator
- **OpenAI API calls** using `spyglass_openai()` wrapper
- **Model usage, token consumption, and response times**

View your traces and analytics in the Spyglass AI dashboard after running the application.

## Github Action To Track Your Deployments

The file at `.github/workflows/spyglass.yaml` is configured to track the model and prompt you are using. This is the most common source of performance issues in production deployments of LLMs so Spyglass makes it easier for you to track these changes over time.

Once this workflow file runs you can visit the Deployments tab in the Spyglass AI platform to see the 
metadata that was captured. 
