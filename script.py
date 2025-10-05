# Create a setup script to help organize the project files
setup_script = '''#!/bin/bash
# Project Setup Script for Deep Learning Portfolio

echo "🚀 Setting up Deep Learning Projects Portfolio..."

# Create directory structure
echo "📁 Creating directory structure..."
mkdir -p multimodal-rag-system/src/core
mkdir -p multimodal-rag-system/src/api/routes  
mkdir -p multimodal-rag-system/tests
mkdir -p multimodal-rag-system/data
mkdir -p multimodal-rag-system/uploads
mkdir -p multimodal-rag-system/logs

mkdir -p deepfake-detection-system/src/models
mkdir -p deepfake-detection-system/src/preprocessing
mkdir -p deepfake-detection-system/src/inference
mkdir -p deepfake-detection-system/config
mkdir -p deepfake-detection-system/data
mkdir -p deepfake-detection-system/models

mkdir -p ai-code-review-assistant/src/config
mkdir -p ai-code-review-assistant/src/analysis
mkdir -p ai-code-review-assistant/src/github
mkdir -p ai-code-review-assistant/database
mkdir -p ai-code-review-assistant/tests

echo "✅ Directory structure created!"

# Install core dependencies for Project 1
echo "📦 Installing dependencies for Multimodal RAG System..."
cd multimodal-rag-system

# Create requirements.txt content
cat > requirements.txt << EOL
# Core dependencies
fastapi==0.104.1
uvicorn==0.24.0
streamlit==1.28.2
pydantic==2.5.0

# ML/AI dependencies
torch==2.1.1
transformers==4.35.2
sentence-transformers==2.2.2
langchain==0.0.340
langchain-community==0.0.1
chromadb==0.4.18
openai==1.3.7

# Document processing
pypdf==3.17.1
python-docx==0.8.11
pillow==10.1.0
pytesseract==0.3.10
opencv-python==4.8.1.78
pandas==2.1.4

# Database & Storage
sqlalchemy==2.0.23
redis==5.0.1
boto3==1.34.0

# Utilities
python-multipart==0.0.6
python-dotenv==1.0.0
pyyaml==6.0.1
requests==2.31.0
numpy==1.24.4

# Development & Testing
pytest==7.4.3
pytest-asyncio==0.21.1
black==23.11.0
flake8==6.1.0

# Deployment
gunicorn==21.2.0
EOL

echo "✅ Requirements file created!"
echo ""
echo "🎯 Next steps:"
echo "1. Run: pip install -r requirements.txt"
echo "2. Set up your GitHub repositories"
echo "3. Copy the project files from the provided package"
echo "4. Make your first commit!"
echo ""
echo "🚀 You're ready to start coding!"
'''

# Write the setup script
with open('project_files/setup_projects.sh', 'w') as f:
    f.write(setup_script)

print("✅ Created setup script: project_files/setup_projects.sh")
print("\nTo use this script:")
print("1. Copy it to your project directory") 
print("2. Make it executable: chmod +x setup_projects.sh")
print("3. Run it: ./setup_projects.sh")