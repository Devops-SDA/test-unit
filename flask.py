from flask import Flask

app = Flask(__name__)

# Basic Home Route
@app.route("/")
def home():
    # Single HTML page content
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask SPA</title>
        <style>body { font-family: sans-serif; text-align: center; padding: 50px; }</style>
    </head>
    <body>
        <h1>Hello from Flask!</h1>
        <p>This entire app is running from one Python file.</p>
        <button onclick="alert('Python logic can be triggered via APIs!')">Click Me</button>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    # Start the local development server
    app.run(debug=True)

