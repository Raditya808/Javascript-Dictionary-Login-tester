from flask import Flask,render_template,url_for 
import datetime as dt 


app = Flask(__name__)

@app.route('/')
def home():
    return f'''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <metname="viewport" content="width=device-width,initial-scale=1">
        <title>/home</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            body {{
                font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
                background: #fafafa;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            .main {{
                background: #fff;
                border-radius: 12px;
                padding: 65px 65px;
                max-width: 460px;
                width: 100%;
                border: 1px solid #e8e8e8;
            }}

            .logo {{
                font-family: monospace;
                text-align: center;
                width: 106px;
                height: 106px;
                background: #000;
                border-radius: 8px;
                margin: 0 auto 28px;
                display: flex;
                align-items: center;
                justify-content: center;
                color:white;

            }}
         
          
            .subtitle {{
                font-size: 13px;
                color: #888;
                margin-bottom: 36px;
                line-height: 1.5;
            }}
            ul {{ list-style: none; }}
            .btn {{
                display: block;
                width: 100%;
                padding: 11px 20px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: 500;
                text-decoration: none;
                text-align: center;
                transition: all 0.15s ease;
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
                margin-top: 10px;
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
                color: #bbb;
            }}
            .footer-text {{
                margin-top: 28px;
                font-size: 11px;
                color: #bbb;
                text-align: center;
                line-height: 1.6;
            }}
            .img-src{{
                position: fixed;    
                top:20px;
                left:20px;
            }}

            .img-src img {{
                width: 32px;
                height: 32px;
                border-radius: 6px;
                object-fit: cover;
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

            <p class="footer-text">By continuing, you agree to our<br>Terms of Service & Privacy Policy</p>
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
if __name__=="__main__":
    app.run(debug=True)
