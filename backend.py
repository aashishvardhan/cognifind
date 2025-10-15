// A simple Express.js server to handle API requests and securely call the Gemini API.

const express = require('express');
const fetch = require('node-fetch');
const cors = require('cors');
require('dotenv').config();

const app = express();
const port = 3000;

// Middleware
app.use(express.json());
app.use(cors());

// API route to handle search queries
app.post('/api/search', async (req, res) => {
    const { query } = req.body;

    if (!query) {
        return res.status(400).json({ error: 'Query is required' });
    }

    try {
        const apiKey = process.env.GEMINI_API_KEY; 
        if (!apiKey) {
            throw new Error("API key not found. Please set GEMINI_API_KEY in your .env file.");
        }
        
        const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key=${apiKey}`;

        const systemPrompt = "You are an AI assistant for CogniFind. Your task is to answer questions based on a company's internal knowledge base. Using the provided search results from the knowledge base, answer the user's question succinctly and professionally. Format your answer clearly using Markdown.";

        const payload = {
            contents: [{ parts: [{ text: query }] }],
            tools: [{ "google_search": {} }],
            systemInstruction: {
                parts: [{ text: systemPrompt }]
            },
        };

        const apiResponse = await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (!apiResponse.ok) {
            const errorBody = await apiResponse.text();
            console.error('API Error Response:', errorBody);
            throw new Error(`API error: ${apiResponse.statusText}`);
        }

        const result = await apiResponse.json();
        const candidate = result.candidates?.[0];

        let answer = 'Sorry, I could not find an answer. Please try rephrasing your question.';
        let sources = [];
        
        if (candidate && candidate.content?.parts?.[0]?.text) {
             answer = candidate.content.parts[0].text;
             const groundingMetadata = candidate.groundingMetadata;
             if (groundingMetadata && groundingMetadata.groundingAttributions) {
                 sources = groundingMetadata.groundingAttributions
                    .map(attribution => ({
                        uri: attribution.web?.uri,
                        title: attribution.web?.title,
                    }))
                    .filter(source => source.uri && source.title);
             }
        }
        
        res.json({ answer, sources });

    } catch (error) {
        console.error('Server Error:', error);
        res.status(500).json({ error: error.message });
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
    console.log('To get started:');
    console.log('1. Make sure you have a .env file with your GEMINI_API_KEY.');
    console.log('2. Open the index.html file in your browser.');
});
