from flask import Flask
import requests

app = Flask(__name__)

GITHUB_USER = "angelgradoasir-jpg"

@app.route("/")
def home():

    user_url = f"https://api.github.com/users/{GITHUB_USER}"
    repos_url = f"https://api.github.com/users/{GITHUB_USER}/repos"

    user_data = requests.get(user_url).json()
    repos = requests.get(repos_url).json()

    total_repos = user_data["public_repos"]
    followers = user_data["followers"]
    avatar = user_data["avatar_url"]

    repo_cards = ""

    for repo in repos:

        repo_cards += f"""
        <div style="
            background:white;
            padding:20px;
            margin-bottom:20px;
            border-radius:15px;
            box-shadow:0px 2px 10px rgba(0,0,0,0.1);
        ">

            <h2>{repo['name']}</h2>

            <p>{repo['description']}</p>

            <p><b>🖥 Lenguaje:</b> {repo['language']}</p>

            <p><b>⭐ Stars:</b> {repo['stargazers_count']}</p>

            <p><b>🍴 Forks:</b> {repo['forks_count']}</p>

            <p><b>🕒 Última actualización:</b> {repo['updated_at']}</p>

            <a href="{repo['html_url']}" target="_blank">
                🔗 Ver repositorio
            </a>

        </div>
        """

    return f"""
    <html>

    <head>

        <title>GitHub DevOps Dashboard</title>

    </head>

    <body style="
        font-family: Arial;
        background:#f4f4f4;
        padding:40px;
    ">

        <div style="
            background:#24292e;
            color:white;
            padding:30px;
            border-radius:20px;
            margin-bottom:40px;
        ">

            <img src="{avatar}" width="120" style="border-radius:50%;">

            <h1>🚀 GitHub DevOps Dashboard</h1>

            <h2>{GITHUB_USER}</h2>

            <p>Monitorización automática GitHub + CI/CD</p>

        </div>

        <div style="
            display:flex;
            gap:20px;
            margin-bottom:40px;
        ">

            <div style="
                background:white;
                padding:20px;
                border-radius:15px;
                width:200px;
                box-shadow:0px 2px 10px rgba(0,0,0,0.1);
            ">

                <h2>{total_repos}</h2>

                <p>Repositorios</p>

            </div>

            <div style="
                background:white;
                padding:20px;
                border-radius:15px;
                width:200px;
                box-shadow:0px 2px 10px rgba(0,0,0,0.1);
            ">

                <h2>{followers}</h2>

                <p>Followers GitHub</p>

            </div>

        </div>

        <h1>📂 Repositorios GitHub</h1>

        {repo_cards}

    </body>

    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
