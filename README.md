# GenAI with Python

A comprehensive project for working with Generative AI using Python, including Google Gemini API integration and SAP AI Core examples.

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys

#### Option A: Using .env file (Recommended)

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your actual API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

3. Get your Gemini API key from: https://makersuite.google.com/app/apikey

#### Option B: Using Environment Variables

```bash
export GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Verify Setup

Test your Gemini API setup:

```bash
cd google-gemini
python gemini_client.py
```

If successful, you should see:
- ✅ Gemini client initialized successfully!
- List of available models

## Project Structure

```
├── google-gemini/           # Google Gemini API examples
│   ├── gemini_client.py     # Utility client with .env support
│   └── gemini-models.ipynb  # Jupyter notebook examples
├── sap-ai/                  # SAP AI Core examples
│   └── codejam/            # SAP CodeJam exercises
├── chatbot/                # Chatbot implementations
├── .env.example            # Environment variables template
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Usage Examples

### Using the Gemini Client

```python
from google_gemini.gemini_client import setup_gemini

# Initialize client (automatically loads .env file)
client = setup_gemini()

# Get a model
model = client.get_model("gemini-1.5-flash")

# Generate content
response = model.generate_content("Hello, how are you?")
print(response.text)
```

### Creating a .env file programmatically

```python
from google_gemini.gemini_client import GeminiClient

# Create .env file with your API key
GeminiClient.create_env_file("your_api_key_here")
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini API key | Yes |
| `GOOGLE_API_KEY` | Alternative to GEMINI_API_KEY | Optional |

## Security Notes

- Never commit your `.env` file to version control
- The `.env` file is already included in `.gitignore`
- Keep your API keys secure and don't share them publicly
- Rotate your API keys regularly

## Troubleshooting

### "No API key found" Error

1. Make sure you have a `.env` file in the project root
2. Verify your `.env` file contains: `GEMINI_API_KEY=your_key_here`
3. Check that `python-dotenv` is installed: `pip install python-dotenv`

### Import Errors

Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### API Key Not Loading

The client automatically searches for `.env` files in:
1. Current working directory
2. Parent directories (up to 3 levels)

Make sure your `.env` file is in one of these locations.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## License

This project is for educational purposes.
