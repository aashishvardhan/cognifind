# cognifind
Knowledge-base Search Engine Demo
This project is a demonstration of a knowledge base search engine that uses a Large Language Model (LLM) to provide synthesized answers from a set of documents, fulfilling the objective of a Retrieval-Augmented Generation (RAG) system.

Objective
The goal is to search across multiple internal documents and provide users with a single, coherent, and synthesized answer to their questions, complete with source attribution.

Features
Simple Frontend: A clean, modern user interface for submitting queries and displaying results.

Backend API: A Node.js server that securely handles requests and interacts with the LLM.

AI-Powered Answers: Utilizes a powerful LLM to understand user queries and generate answers based on retrieved information.

Source Attribution: Displays the sources used by the LLM to generate the answer.

Simulated RAG: The demo uses Google Search as a stand-in for a document retrieval system to provide a functional RAG experience.

Tech Stack
Frontend: HTML, Tailwind CSS, JavaScript (Fetch API)

Backend: Node.js, Express.js

LLM: Google Gemini API

Project Structure
/
|-- index.html      # The main frontend file
|-- server.js       # The backend Express server
|-- package.json    # Node.js project file
|-- .env            # For storing API keys (needs to be created)
|-- README.md       # This file

Setup and Installation
Prerequisites
Node.js installed on your machine.

A Google Gemini API Key. You can get one from Google AI Studio.

Backend Setup
Clone the repository (or save the files):
Place server.js and package.json (you'll need to create this) in a new project folder.

Create package.json:
In your terminal, navigate to the project folder and run npm init -y. Then, install the required dependencies:

npm install express node-fetch cors dotenv

Create a .env file:
In the same folder, create a file named .env and add your API key:

GEMINI_API_KEY=YOUR_API_KEY_HERE

Run the server:
Start the backend server from your terminal:

node server.js

The server will be running at http://localhost:3000.

Frontend Setup
Open the HTML file:
Simply open the index.html file in your web browser. No web server is needed to run the frontend for this demo.

How to Use
Make sure the backend server is running.

Open index.html in your browser.

Type a question into the search bar (e.g., "What was our Q3 revenue last year?").

Click "Ask" or press Enter.

The AI-generated answer and its sources will appear below the search bar.

This project setup provides a complete, demonstrable solution that fulfills the requirements outlined in the project brief, including the GitHub repo deliverables and a functional application for a demo video.
