from flask import Flask, request, jsonify, Response
import requests, os, mimetypes

app = Flask(__name__)

SHEETY_URL = "https://api.sheety.co/8b30ec0bb3612517dada89eb2e88f4f9/arattai/sheet1"
DATA_DIR = "/mnt/data"
SCREENSHOTS = ["ff69f046-bd52-4256-96ec-d6a424cbc386.png"]


@app.route('/')
def index():
    screenshots_html = ''.join(
        f'<div class="shot"><img src="/screenshot/{fname}" alt="screenshot"></div>'
        for fname in SCREENSHOTS
    )
    html = f"""<!doctype html>
<html lang="en">
<head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Borel&family=Coming+Soon&family=Monsieur+La+Doulaise&family=Playwrite+DE+Grund+Guides&family=Audiowide&display=swap" rel="stylesheet">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Join Arattai — Class Group</title>
<link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{font-family: "Borel", cursive;
  font-weight: 400;
  font-style: normal;background:#fff;color:#202124;scroll-behavior:smooth}}
  header{{text-align:center;padding:80px 20px 40px;background:linear-gradient(135deg,#e8f0fe,#fff);opacity:0;transform:translateY(40px);transition:all 1s ease}}
  header.show{{opacity:1;transform:none}}
  header h1{{font-size:3rem;font-weight:700;color:#1a73e8;margin-bottom:20px}}
  header p{{font-size:1.12rem;color:#5f6368;margin-bottom:28px;max-width:900px;margin-left:auto;margin-right:auto}}
  .cta-btn{{background:#1a73e8;color:#fff;border:none;border-radius:50px;padding:12px 34px;font-size:1.05rem;cursor:pointer;transition:transform .18s,background .25s}}
  .cta-btn:hover{{transform:scale(1.04);background:#174ea6}}

  /* Laptop Animation Styles */
  .laptop-container{{max-width:1100px;margin:60px auto;padding:20px;perspective:1400px;opacity:0;transform:translateY(60px);transition:all 1.2s ease}}
  .laptop-container.show{{opacity:1;transform:none}}
  .laptop{{position:relative;width:100%;max-width:900px;margin:0 auto;transform-style:preserve-3d;animation:float 6s ease-in-out infinite}}
  @keyframes float{{0%,100%{{transform:translateY(0) rotateX(0deg)}}50%{{transform:translateY(-20px) rotateX(2deg)}}}}
  .laptop-screen{{position:relative;background:linear-gradient(135deg,#202124,#3c4043);border-radius:12px 12px 0 0;padding:8px 8px 0;box-shadow:0 20px 60px rgba(0,0,0,.3)}}
  .screen-content{{background:#fff;border-radius:6px;overflow:hidden;position:relative;padding-bottom:62.5%;box-shadow:inset 0 0 0 1px rgba(0,0,0,.1)}}
  .screenshot-slider{{position:absolute;top:0;left:0;width:100%;height:100%;display:flex;transition:transform .8s cubic-bezier(.4,0,.2,1)}}
  .slide{{min-width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:#f8f9fa}}
  .slide img{{width:100%;height:100%;object-fit:cover}}
  .laptop-base{{height:12px;background:linear-gradient(to bottom,#dadce0,#e8eaed);border-radius:0 0 8px 8px;margin:0 -40px;box-shadow:0 8px 24px rgba(0,0,0,.15)}}
  .slider-dots{{text-align:center;margin-top:30px}}
  .dot{{display:inline-block;width:10px;height:10px;border-radius:50%;background:#dadce0;margin:0 6px;cursor:pointer;transition:all .3s}}
  .dot.active{{background:#1a73e8;transform:scale(1.3)}}

  .container{{max-width:1100px;margin:0 auto;padding:40px 20px}}
  .section{{padding:60px 0;opacity:0;transform:translateY(60px);transition:all .9s ease}}
  .section.show{{opacity:1;transform:none}}
  .card{{background:#fff;border-radius:14px;box-shadow:0 6px 30px rgba(60,64,67,.08);padding:32px}}
  .form-card{{width:100%;max-width:460px;padding:36px;margin:0 auto}}
  input,textarea{{width:100%;padding:12px;margin:10px 0;border-radius:8px;border:1px solid #dadce0;font-size:1rem}}
  textarea{{min-height:80px;resize:vertical}}
  button[type=submit]{{width:100%;background:#1a73e8;color:#fff;border:none;padding:12px;border-radius:8px;font-size:1rem;cursor:pointer}}
  button[type=submit]:hover{{background:#174ea6}}
  #status{{margin-top:12px;font-weight:600}}
  .shot{{display:inline-block;width:100%;max-width:320px;margin:10px;border-radius:10px;overflow:hidden;box-shadow:0 6px 20px rgba(60,64,67,.08)}}
  .shot img{{display:block;width:100%;height:auto}}

  /* About Me Section Styles */
  .about-content{{line-height:1.8}}
  .contact-item{{margin:15px 0;font-size:1.05rem}}
  .contact-item strong{{color:#1a73e8;display:inline-block;min-width:80px}}
  .contact-item a{{color:#1a73e8;text-decoration:none;transition:color .2s}}
  .contact-item a:hover{{color:#174ea6;text-decoration:underline}}
  .made-by{{margin-top:30px;padding-top:20px;border-top:1px solid #dadce0;text-align:center;font-size:1.1rem;color:#5f6368}}
  .stylish-s{{font-family: "Audiowide", sans-serif;
  font-weight: 400;
  font-style: normal;font-size:1.5em;color:#1a73e8}}

  @media(max-width:768px){{
    header h1{{font-size:2rem}}
    .laptop{{max-width:95%}}
  }}
</style>
</head>
<body>
<header id="hero">
  <h1>Switch to Arattai for Our New Class Group 💬</h1>
  <p>Join the Arattai class group now.</p>
  <button class="cta-btn" onclick="document.getElementById('register').scrollIntoView({{behavior:'smooth'}})">Join Now</button>
</header>

<div class="laptop-container" id="laptop-demo">
  <div class="laptop">
    <div class="laptop-screen">
      <div class="screen-content">
        <div class="screenshot-slider" id="slider">
          <div class="slide"><img src="/static/img.png" alt="Arattai screenshot"></div>
        </div>
      </div>
    </div>
    <div class="laptop-base"></div>
  </div>
  <div class="slider-dots" id="dots"></div>
</div>

<main class="container">
  <section class="section" id="about-arattai">
    <div class="card">
      <h2 style="color:#1a73e8">About Arattai</h2>
      <p>Arattai is an easy-to-use, instant messaging app that helps you stay connected. It is simple, secure, and Indian-made. With Arattai you can send texts and voice notes, make audio/video calls, share photos, documents, stories, and much more.</p>
    </div>
  </section>

  <section class="section" id="showcase">
    <div class="card">
      <h2 style="color:#1a73e8">Why Arattai</h2>
      <div><p>There are several compelling reasons to replace WhatsApp with Arattai, particularly for users in India who prioritize data privacy, local data storage, and performance on low-bandwidth networks. Arattai is owned by the Indian tech company Zoho, with all Indian user data stored on servers within India. It is designed to be lightweight, ensuring smooth operation even on older devices and slower 2G or 3G networks, making it a highly accessible choice for a wider range of users. Additionally, Arattai offers unique productivity features like "Pocket" for personal storage and a dedicated "Meetings" tab for scheduling video calls, which is a key differentiator from WhatsApp.</p></div>
    </div>
  </section>

  <section class="section" id="register">
    <div class="card form-card">
      <h2>Join Arattai Group</h2>
      <p style="margin-bottom:20px;text-align:center;color:#5f6368">Click the button below to join our class group on Arattai</p>
      <a href="https://chat.arattai.in/groups/q43545f313237383738333231343031333734343739375f32303032313337383634322d47437c3031303131353032353136343137363037383337333436353730" target="_blank" style="display:block;text-decoration:none">
        <button type="button" style="width:100%;background:#1a73e8;color:#fff;border:none;padding:12px;border-radius:8px;font-size:1rem;cursor:pointer">Join Group</button>
      </a>
    </div>
  </section>

  <section class="section" id="about-me">
    <div class="card">
      <h2 style="color:#1a73e8">About Me</h2>
      <div class="about-content">
        <p style="margin-bottom:20px">Hi! I'm Shreyash.p — a student who studies in 8F LAKE MONTFORT SCHOOL.</p>

        <div class="contact-item">
          <strong>Email:</strong> <a href="mailto:shreyash5011111@gmail.com">shreyash5011111@gmail.com</a>
        </div>

        <div class="contact-item">
          <strong>Phone:</strong> <a href="tel:+919980666673">+91 9980666673</a>
        </div>

        <div class="contact-item">
          <strong>GitHub:</strong> <a href="https://github.com/shreyash50111" target="_blank">github.com/shreyash50111</a>
        </div>

        <div class="made-by">
          Made by <span class="stylish-s">S</span>hreyash
        </div>
      </div>
    </div>
  </section>
</main>

<script>
const observer=new IntersectionObserver((entries)=>{{
  entries.forEach(entry=>{{if(entry.isIntersecting)entry.target.classList.add('show')}})
}},{{threshold:0.18}});
document.querySelectorAll('header,.section,.laptop-container').forEach(el=>observer.observe(el));

// Screenshot slider
const slider=document.getElementById('slider');
const dotsContainer=document.getElementById('dots');
const slides=1;

if(slider && dotsContainer){{
  let current=0;
  
  for(let i=0;i<slides;i++){{
    const dot=document.createElement('span');
    dot.className='dot'+(i===0?' active':'');
    dot.onclick=()=>goToSlide(i);
    dotsContainer.appendChild(dot);
  }}

  function goToSlide(n){{
    current=n;
    slider.style.transform=`translateX(${{-100*n}}%)`;
    document.querySelectorAll('.dot').forEach((d,i)=>{{
      d.classList.toggle('active',i===n);
    }});
  }}

  if(slides>1){{
    setInterval(()=>{{goToSlide((current+1)%slides)}},4000);
  }}
}}

// Form submission
document.getElementById('arattaiForm').addEventListener('submit',async(e)=>{{
 e.preventDefault();
 const name=document.getElementById('name').value.trim();
 const roll=document.getElementById('roll').value.trim();
 const phone=document.getElementById('phones').value.trim();
 const status=document.getElementById('status');
 status.textContent='Submitting...';
 status.style.color='#5f6368';
 try{{
   const res=await fetch('/submit',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{name,roll,phone}})}});
   const r=await res.json();
   status.textContent=r.message;
   status.style.color=r.success?'green':'red';
 }}catch(err){{
   status.textContent='Error submitting form';
   status.style.color='red';
   console.error(err);
 }}
}});
</script>
</body>
</html>"""
    return html


@app.route('/screenshot/<filename>')
def serve_screenshot(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.isfile(path):
        return Response("Not found", status=404)
    mime, _ = mimetypes.guess_type(path)
    with open(path, "rb") as f:
        return Response(f.read(), mimetype=mime or "application/octet-stream")


@app.route('/favicon.ico')
def favicon():
    return Response(status=204)  # No Content


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get("name")
    roll = data.get("roll")
    phone = data.get("phone")

    entry = {
        "sheet1": {
            "name": name,
            "rollNo": roll,
            "phoneNo": phone
        }
    }
    try:
        res = requests.post(SHEETY_URL, json=entry)
    except Exception as e:
        return jsonify({"success": False, "message": f"Error: {e}"})
    if res.status_code not in (200, 201):
        return jsonify({"success": False, "message": "Failed to save data!", "debug": res.text})
    return jsonify({"success": True, "message": "Registration successful! 🎉"})


if __name__ == "__main__":
    print("Running on http://127.0.0.1:5000")
    app.run(debug=True)




