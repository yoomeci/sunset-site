from flask import Flask, render_template_string

app = Flask(__name__)

# ================= HOME =================
home_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sunset Unit</title>

<style>
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(270deg, #000000, #1a1a1a, #333333, #000000);
    background-size: 800% 800%;
    animation: gradientMove 15s ease infinite;
    color: white;
    text-align: center;
}

/* LOADER */
#loader {
    position: fixed;
    inset: 0;
    background: #000;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
    transition: opacity 0.6s ease;
}

#loader.hidden {
    opacity: 0;
    pointer-events: none;
}

/* GLITCH */
.glitch {
    position: relative;
    font-size: 3em;
    letter-spacing: 4px;
}

.glitch::before,
.glitch::after {
    content: attr(data-text);
    position: absolute;
    left: 0;
}

.glitch::before {
    color: red;
    animation: glitchTop 1.2s infinite;
}

.glitch::after {
    color: cyan;
    animation: glitchBottom 1.2s infinite;
}

@keyframes glitchTop {
    0% { transform: translate(-2px,-2px); }
    50% { transform: translate(2px,2px); }
    100% { transform: translate(-2px,-2px); }
}

@keyframes glitchBottom {
    0% { transform: translate(2px,2px); }
    50% { transform: translate(-2px,-2px); }
    100% { transform: translate(2px,2px); }
}

.container { padding: 60px; }

.cards {
    margin-top: 50px;
    display: flex;
    justify-content: center;
    gap: 20px;
}

.card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    padding: 40px;
    border-radius: 15px;
    width: 250px;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-15px) scale(1.07);
    box-shadow: 0 0 20px rgba(255,255,255,0.2);
}

.card a {
    display: block;
    margin-top: 15px;
    padding: 12px;
    background: #111;
    border-radius: 8px;
    text-decoration: none;
    color: white;
}

footer {
    margin-top: 60px;
    font-size: 14px;
    opacity: 0.8;
}

@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
</style>
</head>

<body>

<div id="loader">
    <h1 class="glitch" data-text="SUNSET">SUNSET</h1>
</div>

<div class="container">
    <h1>Sunset</h1>
    <h2>Edit Unit</h2>

    <div class="cards">
        <div class="card">
            <h3>Socials</h3>
            <a href="/socials">Open</a>
        </div>

        <div class="card">
            <h3>About Us</h3>
            <a href="/about">Open</a>
        </div>
    </div>

    <footer>© 2026 SUNSET LLC. All rights reserved.</footer>
</div>

<script>
window.addEventListener("load", () => {
    setTimeout(() => {
        document.getElementById("loader").classList.add("hidden");
    }, 1000);
});
</script>

</body>
</html>
"""

# ================= SOCIALS =================
socials_html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Socials</title>

<style>
body {
    margin: 0;
    font-family: Arial;
    background: linear-gradient(270deg, #000, #222, #444, #000);
    background-size: 800% 800%;
    animation: gradientMove 15s infinite;
    color: white;
    text-align: center;
}

.container { padding: 60px; }

.cards {
    display: flex;
    justify-content: center;
    gap: 20px;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 40px;
    border-radius: 15px;
    width: 250px;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-10px) scale(1.05);
}

.card a {
    display: block;
    margin-top: 10px;
    padding: 10px;
    background: #111;
    border-radius: 8px;
    color: white;
    text-decoration: none;
}

a.back {
    display: block;
    margin-top: 40px;
    color: white;
}

footer {
    margin-top: 40px;
}

@keyframes gradientMove {
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}
</style>
</head>

<body>

<div class="container">
<h1>Socials</h1>

<div class="cards">
    <div class="card">
        <h3>Discord</h3>
        <a href="https://discord.gg/9rsFPEHCSx" target="_blank">Join</a>
    </div>

    <div class="card">
        <h3>TikTok</h3>
        <a href="https://www.tiktok.com/@.sunsetcollective?_r=1&_t=ZS-95hmY2q8Q5g" target="_blank">View</a>
    </div>
</div>

<a class="back" href="/">← Back</a>

<footer>© 2026 SUNSET LLC. All rights reserved.</footer>
</div>

</body>
</html>
"""

# ================= ABOUT =================
about_html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>About</title>

<style>
body {
    margin: 0;
    font-family: Arial;
    background: linear-gradient(270deg, #000, #222, #444, #000);
    background-size: 800% 800%;
    animation: gradientMove 15s infinite;
    color: white;
    text-align: center;
}

.container { padding: 60px; }

.section {
    max-width: 800px;
    margin: 40px auto;
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 15px;
}

footer { margin-top: 40px; }

@keyframes gradientMove {
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}
</style>
</head>

<body>

<div class="container">
<h1>About Sunset</h1>

<div class="section"><p>Sunset is a creative editing collective focused on high-quality visuals.</p></div>
<div class="section"><p>We accept editors, musicians, and designers.</p></div>
<div class="section"><p>We build identity and community.</p></div>

<a href="/">← Back</a>

<footer>© 2026 SUNSET LLC. All rights reserved.</footer>
</div>

</body>
</html>
"""

# ROUTES
@app.route("/")
def home():
    return render_template_string(home_html)

@app.route("/socials")
def socials():
    return render_template_string(socials_html)

@app.route("/about")
def about():
    return render_template_string(about_html)

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
