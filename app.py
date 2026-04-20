from flask import Flask, render_template_string

app = Flask(__name__)

home_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Sunset Unit</title>

<style>
body {
    margin: 0;
    font-family: Arial;
    background: linear-gradient(270deg, #ff7e5f, #feb47b, #ffcc70, #ff6a88);
    background-size: 800% 800%;
    animation: gradientMove 15s ease infinite;
    color: white;
}

/* NAV */
nav {
    display: flex;
    justify-content: space-between;
    padding: 20px 40px;
    background: rgba(0,0,0,0.2);
}

/* ANIMAÇÃO */
.fade-up {
    opacity: 0;
    transform: translateY(40px);
    animation: fadeUp 1s forwards;
}

.delay-1 { animation-delay: 0.3s; }
.delay-2 { animation-delay: 0.6s; }

/* CONTAINER */
.container {
    padding: 60px;
    text-align: center;
}

/* BOTÃO */
.about-btn {
    padding: 15px 30px;
    background: linear-gradient(135deg, #ff9a8b, #ff6a88);
    border-radius: 12px;
    color: white;
    text-decoration: none;
    font-weight: bold;
}

/* CARDS */
.cards {
    margin-top: 60px;
    display: flex;
    justify-content: center;
    gap: 30px;
}

.card {
    width: 300px;
    background: rgba(255,255,255,0.08);
    padding: 40px;
    border-radius: 20px;
    backdrop-filter: blur(10px);

    opacity: 0;
    transform: translateY(40px);
    animation: fadeUp 1s forwards;
}

.card:nth-child(1) { animation-delay: 1s; }
.card:nth-child(2) { animation-delay: 1.2s; }

.card a {
    display: block;
    margin-top: 15px;
    padding: 10px;
    background: rgba(0,0,0,0.4);
    border-radius: 8px;
    color: white;
    text-decoration: none;
}

/* KEYFRAMES */
@keyframes fadeUp {
    to { opacity:1; transform: translateY(0); }
}

@keyframes gradientMove {
    0% { background-position:0% 50%; }
    50% { background-position:100% 50%; }
    100% { background-position:0% 50%; }
}
</style>
</head>

<body>

<nav>
<h1>Sunset</h1>
<a href="/about" style="color:white;">About</a>
</nav>

<div class="container">
<h1 class="fade-up">Sunset</h1>
<h2 class="fade-up delay-1">Edit Unit</h2>

<a class="about-btn fade-up delay-2" href="{{ url_for('about') }}">About Us</a>

<div class="cards">
<div class="card">
<h3>Discord</h3>
<a href="https://discord.gg/9rsFPEHCSx">Join</a>
</div>

<div class="card">
<h3>TikTok</h3>
<a href="https://www.tiktok.com/@lxrymeci">View</a>
</div>
</div>
</div>

</body>
</html>
"""

about_html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>About</title>

<style>
body {
    margin:0;
    font-family:Arial;
    background: linear-gradient(270deg, #ff7e5f, #feb47b, #ffcc70, #ff6a88);
    background-size: 800% 800%;
    animation: gradientMove 15s ease infinite;
    color:white;
}

.container {
    padding:60px;
    text-align:center;
}

.section {
    max-width:800px;
    margin:30px auto;
    background:rgba(255,255,255,0.1);
    padding:25px;
    border-radius:15px;

    opacity:0;
    transform:translateY(40px);
    animation: fadeUp 1s forwards;
}

.section:nth-child(2){animation-delay:0.2s;}
.section:nth-child(3){animation-delay:0.4s;}
.section:nth-child(4){animation-delay:0.6s;}
.section:nth-child(5){animation-delay:0.8s;}

a {
    display:inline-block;
    margin-top:30px;
    color:white;
}

/* ANIMAÇÃO */
@keyframes fadeUp {
    to { opacity:1; transform:translateY(0); }
}

@keyframes gradientMove {
    0% { background-position:0% 50%; }
    50% { background-position:100% 50%; }
    100% { background-position:0% 50%; }
}
</style>
</head>

<body>

<div class="container">

<h1>About Sunset</h1>

<div class="section">
<h3>Our Mission</h3>
<p>Sunset is a creative editing team focused on high-quality visuals.</p>
</div>

<div class="section">
<h3>Creativity</h3>
<p>We accept editors, musicians and designers.</p>
</div>

<div class="section">
<h3>Identity</h3>
<p>We create clean visuals and strong branding.</p>
</div>

<div class="section">
<h3>Community</h3>
<p>We have an active and growing community.</p>
</div>

<a href="/">← Back</a>

</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(home_html)

@app.route("/about")
def about():
    return render_template_string(about_html)

if __name__ == "__main__":
    app.run(debug=True)