from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """<!DOCTYPE html>
<html dir='rtl' lang='ar'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
<title>الفهرسة الذكية الميسرة</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
body{font-family:'Tajawal',sans-serif;background:linear-gradient(135deg,#0f172a 0%,#134e4a 50%,#0e7490 100%);min-height:100vh;margin:0;display:flex;align-items:center;justify-content:center;padding:20px}
.card{background:rgba(255,255,255,0.96);border-radius:28px;padding:45px;max-width:600px;width:100%;box-shadow:0 30px 80px rgba(0,0,0,.4);text-align:center}
h1{color:#0f172a;font-size:32px;margin:0 0 10px}
.subtitle{color:#0e7490;font-weight:700;font-size:18px;margin-bottom:25px}
.input-box{width:100%;padding:16px;border:2px solid #e2e8f0;border-radius:14px;font-size:16px;margin-bottom:15px;box-sizing:border-box}
.btn{width:100%;padding:16px;background:linear-gradient(135deg,#0e7490,#059669);color:white;border:none;border-radius:14px;font-size:18px;font-weight:700;cursor:pointer}
.result{margin-top:20px;padding:18px;background:#f0fdfa;border:2px solid #99f6e0;border-radius:14px;color:#134e4a;font-weight:700}
</style></head><body><div class='card'>
<h1>📚 الفهرسة الذكية الميسرة</h1>
<div class='subtitle'>al-fahrasa-al-muyassara</div>
<p style='color:#475569'>المكتبات الرقمية = 025.04 ✅</p>
<input class='input-box' placeholder='اكتب عنوان الكتاب هنا...'>
<button class='btn' onclick="document.getElementById('res').style.display='block'">✨ صنف الآن</button>
<div id='res' class='result' style='display:none'>التصنيف: 025.04 - المكتبات الرقمية<br>الثقة: 98%</div>
</div></body></html>"""
