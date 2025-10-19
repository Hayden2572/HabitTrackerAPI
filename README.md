<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎯 Habit Tracker API</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            line-height: 1.6;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            padding: 60px 20px;
            color: white;
        }

        .header h1 {
            font-size: 3.5em;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .header .subtitle {
            font-size: 1.4em;
            opacity: 0.9;
            font-weight: 300;
        }

        .card {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin: 20px 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            transition: transform 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .section-title {
            color: #667eea;
            font-size: 2em;
            margin-bottom: 25px;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .feature-item {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }

        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 20px;
        }

        .tech-item {
            background: #667eea;
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            font-weight: 500;
        }

        .quick-start {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }

        .quick-start .section-title {
            color: white;
            border-bottom-color: white;
        }

        .code-block {
            background: #2d3748;
            color: #e2e8f0;
            padding: 20px;
            border-radius: 10px;
            margin: 15px 0;
            font-family: 'Courier New', monospace;
            overflow-x: auto;
        }

        .endpoint {
            background: #f7fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 15px;
            margin: 10px 0;
        }

        .endpoint-method {
            display: inline-block;
            padding: 5px 12px;
            border-radius: 5px;
            font-weight: bold;
            margin-right: 10px;
        }

        .method-post { background: #48bb78; color: white; }
        .method-get { background: #4299e1; color: white; }
        .method-delete { background: #f56565; color: white; }

        .footer {
            text-align: center;
            padding: 40px 20px;
            color: white;
            opacity: 0.8;
        }

        @media (max-width: 768px) {
            .header h1 {
                font-size: 2.5em;
            }
            
            .container {
                padding: 10px;
            }
            
            .card {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 Habit Tracker API</h1>
            <div class="subtitle">Simple and efficient REST API for habit tracking built with FastAPI and SQLite</div>
        </div>

        <div class="card">
            <h2 class="section-title">🚀 Features</h2>
            <div class="features-grid">
                <div class="feature-item">✅ Create habits with frequency validation</div>
                <div class="feature-item">📋 Get all habits</div>
                <div class="feature-item">🔍 Get habit by ID</div>
                <div class="feature-item">🗑️ Delete habits</div>
                <div class="feature-item">🛠️ Admin functions for database management</div>
            </div>
        </div>

        <div class="card">
            <h2 class="section-title">🛠️ Tech Stack</h2>
            <div class="tech-stack">
                <div class="tech-item">Python 3.8+</div>
                <div class="tech-item">FastAPI - modern web framework</div>
                <div class="tech-item">SQLAlchemy 2.0 - async ORM</div>
                <div class="tech-item">SQLite - database</div>
                <div class="tech-item">Pydantic - data validation</div>
                <div class="tech-item">Uvicorn - ASGI server</div>
            </div>
        </div>

        <div class="card quick-start">
            <h2 class="section-title">💡 Quick Start</h2>
            <div class="code-block">
                git clone https://github.com/Hayden2572/HabitTrackerAPI/<br>
                cd HabitTrackerAPI<br>
                pip install -r requirements.txt<br>
                python main.py<br>
                Visit http://localhost:8000/docs for API documentation
            </div>
        </div>

        <div class="card">
            <h2 class="section-title">📚 API Endpoints</h2>
            
            <div class="endpoint">
                <span class="endpoint-method method-post">POST</span>
                <strong>/habits</strong> - Create a new habit
                <div class="code-block">
                    {<br>
                    &nbsp;&nbsp;"habitName": "Morning run",<br>
                    &nbsp;&nbsp;"frequency": "daily"<br>
                    }
                </div>
            </div>

            <div class="endpoint">
                <span class="endpoint-method method-get">GET</span>
                <strong>/habits</strong> - Get all habits
            </div>

            <div class="endpoint">
                <span class="endpoint-method method-get">GET</span>
                <strong>/habits/{id}</strong> - Get habit by ID
            </div>

            <div class="endpoint">
                <span class="endpoint-method method-delete">DELETE</span>
                <strong>/habits/{id}</strong> - Delete habit
            </div>

            <div class="endpoint">
                <span class="endpoint-method method-post">POST</span>
                <strong>/admin-createdb</strong> - Create/recreate database
            </div>
        </div>
    </div>

    <div class="footer">
        <p>Built with ❤️ for efficient habit tracking</p>
    </div>
</body>
</html>
