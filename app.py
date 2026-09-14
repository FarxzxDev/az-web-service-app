from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Dark Knight</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            background: #050505;
            color: #f1f1f1;
        }

        nav {
            position: fixed;
            top: 0;
            width: 100%;
            padding: 20px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(0, 0, 0, 0.85);
            border-bottom: 1px solid #222;
            z-index: 10;
        }

        .logo {
            color: #f5c518;
            font-size: 24px;
            font-weight: bold;
            letter-spacing: 3px;
        }

        nav a {
            color: #ddd;
            text-decoration: none;
            margin-left: 25px;
            transition: 0.3s;
        }

        nav a:hover {
            color: #f5c518;
        }

        .hero {
            min-height: 100vh;
            padding: 180px 8% 80px;
            display: flex;
            align-items: center;
            background:
                linear-gradient(90deg, #050505 25%, rgba(5,5,5,0.75), #050505),
                radial-gradient(circle at 75% 45%, #222 0%, #080808 35%, #050505 70%);
        }

        .hero-content {
            max-width: 650px;
        }

        .hero h1 {
            font-size: clamp(55px, 9vw, 120px);
            line-height: 0.95;
            letter-spacing: 8px;
            color: #ffffff;
            text-transform: uppercase;
        }

        .hero h1 span {
            color: #f5c518;
        }

        .hero p {
            margin-top: 25px;
            color: #aaa;
            font-size: 18px;
            line-height: 1.7;
        }

        .buttons {
            margin-top: 35px;
        }

        .btn {
            display: inline-block;
            padding: 14px 25px;
            margin-right: 12px;
            border: 1px solid #f5c518;
            color: #f5c518;
            text-decoration: none;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: 0.3s;
        }

        .btn:hover {
            background: #f5c518;
            color: #000;
        }

        .section {
            padding: 90px 8%;
            background: #0a0a0a;
            border-top: 1px solid #1c1c1c;
        }

        .section h2 {
            color: #f5c518;
            font-size: 34px;
            margin-bottom: 20px;
            letter-spacing: 3px;
            text-transform: uppercase;
        }

        .section p {
            max-width: 800px;
            color: #aaa;
            line-height: 1.8;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 22px;
            margin-top: 35px;
        }

        .card {
            padding: 30px;
            background: #111;
            border: 1px solid #292929;
            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-8px);
            border-color: #f5c518;
        }

        .card h3 {
            color: #fff;
            margin-bottom: 12px;
        }

        .card p {
            font-size: 14px;
        }

        footer {
            padding: 25px;
            text-align: center;
            color: #666;
            background: #000;
            border-top: 1px solid #222;
        }

        @media (max-width: 650px) {
            nav {
                padding: 18px 5%;
            }

            nav a {
                margin-left: 10px;
                font-size: 13px;
            }

            .hero {
                padding-left: 5%;
                padding-right: 5%;
            }

            .section {
                padding-left: 5%;
                padding-right: 5%;
            }
        }
    </style>
</head>

<body>
    <nav>
        <div class="logo">WAYNE</div>
        <div>
            <a href="#about">About</a>
            <a href="#arsenal">Arsenal</a>
        </div>
    </nav>

    <section class="hero">
        <div class="hero-content">
            <h1>Dark<br><span>Knight</span></h1>
            <p>
                In the shadows of Gotham, justice never sleeps.
                This is a tribute to the symbol, the legend, and the protector of the night.
            </p>

            <div class="buttons">
                <a class="btn" href="#about">Explore</a>
                <a class="btn" href="#arsenal">Arsenal</a>
            </div>
        </div>
    </section>

    <section class="section" id="about">
        <h2>The Mission</h2>
        <p>
            Batman is more than a hero. He is discipline, intelligence,
            preparation, and courage. This dark-themed website is created
            as a fan project inspired by Gotham's legendary guardian.
        </p>
    </section>

    <section class="section" id="arsenal">
        <h2>Bat Arsenal</h2>

        <div class="cards">
            <div class="card">
                <h3>Batmobile</h3>
                <p>A powerful machine built for speed, pursuit, and protection.</p>
            </div>

            <div class="card">
                <h3>Batcomputer</h3>
                <p>Advanced technology used to analyze threats and protect Gotham.</p>
            </div>

            <div class="card">
                <h3>Batsuit</h3>
                <p>Designed for stealth, durability, mobility, and intimidation.</p>
            </div>

            <div class="card">
                <h3>Gotham Network</h3>
                <p>Information and observation are the first lines of defense.</p>
            </div>
        </div>
    </section>

    <footer>
        Batman-inspired fan website | Built with Python Flask and Azure
    </footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
