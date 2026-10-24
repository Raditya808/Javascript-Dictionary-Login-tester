from flask import Flask,render_template,url_for 
import datetime as dt 


app = Flask(__name__)

@app.route('/')
def home():
    return f'''
<!DOCTYPE html>
<html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
        <title>/home</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            html {{
                -webkit-text-size-adjust: 100%;
            }}
            body {{
                font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
                background: #fafafa;
                min-height: 100vh;
                min-height: 100dvh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: clamp(16px, 4vw, 32px);
                padding-top: 64px;
            }}
            .main {{
                background: #fff;
                border-radius: 12px;
                padding: clamp(28px, 8vw, 56px) clamp(20px, 7vw, 56px);
                max-width: 420px;
                width: 100%;
                border: 1px solid #e8e8e8;
            }}

            .logo {{
                font-family: monospace;
                font-size: clamp(11px, 3vw, 13px);
                line-height: 1.35;
                text-align: center;
                width: clamp(96px, 30vw, 120px);
                aspect-ratio: 1 / 1;
                padding: 10px;
                background: #000;
                border-radius: 8px;
                margin: 0 auto clamp(20px, 5vw, 28px);
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                overflow-wrap: anywhere;
            }}

            .subtitle {{
                font-size: 13px;
                color: #888;
                margin-bottom: clamp(24px, 6vw, 36px);
                line-height: 1.5;
            }}
            ul {{ list-style: none; }}
            .btn {{
                display: flex;
                align-items: center;
                justify-content: center;
                width: 100%;
                height: 48px;
                padding: 0 20px;
                border-radius: 8px;
                font-size: 15px;
                font-weight: 500;
                text-decoration: none;
                text-align: center;
                transition: background 0.15s ease, transform 0.1s ease;
                -webkit-tap-highlight-color: transparent;
            }}
            .btn:active {{ transform: scale(0.98); }}
            .btn:focus-visible {{
                outline: 2px solid #0a0a0a;
                outline-offset: 2px;
            }}
            .btn-primary {{
                background: #0a0a0a;
                color: #fff;
            }}
            .btn-primary:hover {{ background: #222; }}
            .btn-ghost {{
                background: #fff;
                color: #0a0a0a;
                border: 1px solid #e2e2e2;
            }}
            .btn-ghost:hover {{ background: #f5f5f5; }}
            .divider {{
                display: flex;
                align-items: center;
                gap: 10px;
                margin: 18px 0;
            }}
            .divider::before,
            .divider::after {{
                content: '';
                flex: 1;
                height: 1px;
                background: #ebebeb;
            }}
            .divider span {{
                font-size: 12px;
                color: #999;
            }}
            .footer-text {{
                margin-top: clamp(20px, 5vw, 28px);
                font-size: 12px;
                color: #999;
                text-align: center;
                line-height: 1.6;
            }}
            .img-src {{
                position: fixed;
                top: 12px;
                left: 12px;
            }}
            .img-src a {{
                display: block;
                padding: 6px;          /* area sentuh lebih besar */
            }}
            .img-src img {{
                display: block;
                width: 32px;
                height: 32px;
                border-radius: 6px;
                object-fit: cover;
            }}

            @media (max-width: 480px) {{
                body {{ align-items: flex-start; }}
            }}
            @media (max-height: 560px) {{
                body {{ align-items: flex-start; padding-top: 56px; }}
            }}
        </style>
    </head>
    <body>
    <div class="img-src">
            <a href="https://github.com/Raditya808"><img src="{url_for('static',filename='icon/github-icon/github.jpg')}" alt="git"></a>
    </div>  

        <div class="main">
            <div class="logo"><span>Javascript Dictionary Login Tester</span></div>
            <marquee><p class="subtitle">Login or create an account to continue.</p></marquee>

            <ul>
                <li><a href="{url_for('log')}" class="btn btn-primary">Login</a></li>
            </ul>

            <div class="divider"><span>or</span></div>

            <ul>
                <li><a href="{url_for('sign')}" class="btn btn-ghost">Create an account</a></li>
            </ul>

            <p class="footer-text">By continuing, you agree to our<br>Terms of Service &amp; Privacy Policy</p>
        </div>
    </body>
</html>
'''
   

# route for login page 
@app.route('/login')
def log():
    return render_template('/Login-form/tes_log.html')





# for sign up page 
@app.route('/sign-up')
def sign():
    return render_template('/Sign-up-form/sign-up.html')





# for dashboard page
# dan mengirim object 
@app.route('/dashboard')
def dash():
    return render_template('/result/success_form.html')




# launch the app
#if __name__=="__main__":
    #app.run(debug=True)
