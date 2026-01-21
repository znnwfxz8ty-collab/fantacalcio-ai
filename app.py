from flask import Flask, render_template_string
from main import run

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fantacalcio AI</title>
<style>
body { font-family: Arial; background:#0f172a; color:#fff; padding:20px; }
.card { background:#1e293b; padding:12px; border-radius:10px; margin-bottom:8px; }
h1,h2 { text-align:center; }
</style>
</head>
<body>

<h1>⚽ Fantacalcio AI</h1>
<h2>Formazione consigliata</h2>

{% for p in team %}
<div class="card">{{ p }}</div>
{% endfor %}

<h3>📊 FPA stimato:
