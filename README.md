# MindMapAI ![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Version](https://img.shields.io/badge/version-1.0.0-blue) ![License](https://img.shields.io/badge/license-MIT-yellowgreen)

## Project Description
MindMapAI is an innovative web application that leverages AI to assist users in creating and organizing their thoughts visually through interactive mind maps. By integrating real-time collaboration and AI-generated suggestions, it enhances brainstorming sessions and project planning.

## Features
- 🧠 **AI-assisted mind mapping**: Users can input topics and the AI generates a structured mind map with related concepts.
- 🤝 **Collaborative brainstorming**: Multiple users can work on the same mind map in real-time, with chat functionality for discussions.
- 📤 **Export options**: Users can export their mind maps in various formats (PDF, image, text) for presentations or sharing.

## Tech Stack
### Frontend
- 🌐 **Next.js**: A React framework for server-side rendering and static site generation.

### Backend
- ⚡ **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.
- 🤖 **LangChain**: A framework for developing applications powered by language models.

### Database
- 🗄️ **PostgreSQL**: A powerful, open-source object-relational database system.

### AI Integration
- 🧠 **OpenAI**: API for integrating advanced AI capabilities.

## Installation
To set up MindMapAI locally, follow these steps:

- Clone the repository:
  bash
  git clone https://github.com/nodeexcel/mindmapai
  - Navigate to the project directory:
  bash
  cd mindmapai
  - Install the backend dependencies:
  bash
  cd backend
  pip install -r requirements.txt
  - Install the frontend dependencies:
  bash
  cd ../frontend
  npm install
  - Set up the database (PostgreSQL):
  bash
  # Create a new database
  createdb mindmapai
  - Run database migrations:
  bash
  cd ../backend
  alembic upgrade head
  - Start the backend server:
  bash
  uvicorn main:app --reload
  - Start the frontend server:
  bash
  cd ../frontend
  npm run dev
  ## Usage
1. Open your web browser and navigate to `http://localhost:3000`.
2. Create a new mind map by entering a topic.
3. Collaborate with others in real-time and utilize AI suggestions to enhance your mind map.
4. Export your mind map in your desired format for sharing or presentation.

## API Documentation
For detailed API documentation, please refer to the [API Docs](https://github.com/nodeexcel/mindmapai/docs/api.md).

## Testing
To run tests for the backend, follow these steps:

- Navigate to the backend directory:
  bash
  cd backend
  - Run the tests:
  bash
  pytest
  ## Deployment
To deploy MindMapAI, follow these steps:

- Build the frontend for production:
  bash
  cd frontend
  npm run build
  - Deploy the backend using your preferred cloud service (e.g., AWS, Heroku).

## Contributing
We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.
