from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def hello():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Docker Course</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                background-color: #f4f4f4;
            }
            .container {
                text-align: center;
                background: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 800px;
            }
            .header {
                margin-bottom: 20px;
            }
            .title {
                color: #0044cc;
                font-weight: bold;
                font-size: 24px;
                font-family: 'Berlin Sans FB', sans-serif;
            }
            .subtitle {
                font-style: italic;
                color: #000;
                font-family: 'Times New Roman', Times, serif;
            }
            .name {
                font-weight: bold;
                font-size: 24px;
                font-family: 'Pacifico', cursive;
            }
            .message {
                font-style: italic;
                margin-bottom: 10px;
            }
            .gif {
                margin-bottom: 20px;
            }
            .button {
                display: inline-block;
                padding: 10px 20px;
                margin: 10px;
                font-size: 16px;
                color: #fff;
                text-decoration: none;
                border-radius: 5px;
                display: flex;
                align-items: center;
            }
            .button img {
                margin-right: 10px;
            }
            .docker-button {
                background-color: #0db7ed;
            }
            .linkedin-button {
                background-color: #0077b5;
            }
            .footer {
                margin-top: 20px;
                font-family: 'Times New Roman', Times, serif;
            }
            .profile-pic {
                position: absolute;
                bottom: 10px;
                right: 10px;
                border-radius: 50%;
                width: 120px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="bold">Hello DOCKERian, Welcome ! ! !</div>
                <div class="message">Firstly, Congratulations for deploying the Python Application successfully</div>
                <img src="https://d2gbo5uoddvg5.cloudfront.net/images/gifs/logo-docker.gif" class="gif" alt="Docker Gif" width="150">
            </div>
            <div>
                <div class="subtitle">Welcome to</div>
                <div class="title">Docker learning/div>
                <div class="subtitle">by</div>
                <div class="name">saurabh agrawal</div>
            </div>

            <a href="https://www.linkedin.com/in/saurabhagrawalhere/" class="button linkedin-button" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn Icon" width="20"> LinkedIn Connect
            </a>
        </div>
        <div class="footer">
            Happy Learning!<br>
            &copy; saurabh agrawal
        </div>
        <div>
        <br>
            <b> Check out My Portfoli <b><br>
            <a href ="https://saurabhagrawal-portfolio-website-theta-three.vercel.app/">
        </div>
        <img src="https://saurabhagrawal-portfolio-website-theta-three.vercel.app/assets/images/profile-pic.png" alt="Profile Picture" class="profile-pic">
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
