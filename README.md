# Spyglass Example Project

This is an example project demonstrating how to integrate with the Spyglass AI Platform for OpenAI API call tracing and monitoring.
Follow these instructions to quickly get the telemetry from this application showing up in your Spyglass account.

## Prerequisites
1. An active GitHub account
2. A Spyglass API Key. You can get one by logging into spyglass-ai.com, navigating to the Account section in the sidebar, and generating one from the API Keys tab.


## Application Setup

### 1. Create and Activate Virtual Environment

#### Using Python:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

#### Using uv:
```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

### 2. Install Dependencies

#### Using regular Python:
```bash
pip install -e .
```

#### Using uv:
```bash
uv sync
```

### 3. Configure Environment Variables

Copy the example environment file and fill in your API keys:

```bash
cp .env.example .env
```

Edit `.env` and set the following required variables:

- **SPYGLASS_API_KEY**: Your Spyglass API key (get this from your Spyglass dashboard)
- **SPYGLASS_DEPLOYMENT_ID**: Set to `spyglass-example-project` (this matches what we've predefined in the GitHub workflow in `.github/workflows/spyglass.yaml`)
- **OPENAI_API_KEY**: Your OpenAI API key

### 4. Configure Model Settings

The `model.yaml` file contains your model configuration:
- **model**: The OpenAI model to use (e.g., "gpt-4", "gpt-3.5-turbo")
- **prompt**: The system prompt for your AI assistant

### 5. Run the Example

```bash
python main.py
```

The application will:
- Make OpenAI API calls every 3 seconds
- Automatically trace all calls using this Spyglass SDK
- Send telemetry data to the Spyglass platform in your account

## What Gets Traced

This example demonstrates tracing for:
- **Function calls** using `@spyglass_trace()` decorator
- **OpenAI API calls** using `spyglass_openai()` wrapper
- **Model usage, token consumption, and response times**

View your analytics in the Spyglass AI dashboard after running the application.

## Github Action To Track Your Deployments

The file at `.github/workflows/spyglass.yaml` is configured to track the model and prompt you are using. This is the most common source of performance issues in production deployments of LLMs so Spyglass makes it easier for you to track these changes over time.

To leverage this feature, follow these steps:

1. Create a new repo in your GitHub account and push this code to it. See instructions on doing this [here](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github).

2. Set the `SPYGLASS_API_KEY` secret in the GitHub repo you created.
See instructions for this step [here](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets#creating-secrets-for-a-repository)

Once you have created the repo and set your secret, push this code to the repo and the workflow will be kicked off.
You can see the progress of the workflow in the Actions tab when viewing your repo on the GitHub website.
Once the workflow runs successfully you can visit the Deployments tab in the Spyglass AI platform to see the 
metadata that was captured. 

If you run into any issues feel free to contact us: team@spyglass-ai.com