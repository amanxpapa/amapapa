from flask import Flask, request, render_template_string
import requests
import os
from time import sleep
import time

app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        token_type = request.form.get('tokenType')
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        if token_type == 'single':
            txt_file = request.files['txtFile']
            messages = txt_file.read().decode().splitlines()

            while True:
                try:
                    for message1 in messages:
                        api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                        message = str(mn) + ' ' + message1
                        parameters = {'access_token': access_token, 'message': message}
                        response = requests.post(api_url, data=parameters, headers=headers)
                        if response.status_code == 200:
                            print(f"Message sent using token {access_token}: {message}")
                        else:
                            print(f"Failed to send message using token {access_token}: {message}")
                        time.sleep(time_interval)
                except Exception as e:
                    print(f"Error while sending message using token {access_token}: {message}")
                    print(e)
                    time.sleep(30)

        elif token_type == 'multi':
            token_file = request.files['tokenFile']
            tokens = token_file.read().decode().splitlines()
            txt_file = request.files['txtFile']
            messages = txt_file.read().decode().splitlines()

            while True:
                try:
                    for token in tokens:
                        for message1 in messages:
                            api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                            message = str(mn) + ' ' + message1
                            parameters = {'access_token': token, 'message': message}
                            response = requests.post(api_url, data=parameters, headers=headers)
                            if response.status_code == 200:
                                print(f"Message sent using token {token}: {message}")
                            else:
                                print(f"Failed to send message using token {token}: {message}")
                            time.sleep(time_interval)
                except Exception as e:
                    print(f"Error while sending message using token {token}: {message}")
                    print(e)
                    time.sleep(30)

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Testing</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body{
      background-image: url('https://i.postimg.cc/WzGyyyVq/IMG-20240908-WA0016.jpg');
      background-size: cover;
      background-repeat: no-repeat;
      color: white;
    };
    }
    .container{
      max-width: 300px;
      background-color: bisque;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(red, green, blue, alpha);
      margin: 0 auto;
      margin-top: 20px;
    }
    .header{
      text-align: center;
      padding-bottom: 10px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 10px;
      color: blue;
    }
  </style>
</head>
<body>
  <header class="header mt-4">MAFIYA KE MA KO PTAK KAR CHODNE VALA FAT AMAN HERE 🤣
    <h1 class="mb-3"> PARSURAND KA BHOXDA ON FIRE
    <h1 class="mt- ma chuda  </h1>
  </header>
AAIRA CHOD RULEX
  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="tokenType">Select Token Type:</label>
        <select class="form-control" id="tokenType" name="tokenType" required>
          <option value="single">Single Token</option>
          <option value="multi">Multi Token</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="accessToken">Your Token</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken">
      </div>
      <div class="mb-3">
        <label for="threadId">Convo/Inbox ID:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx"> Hatername:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile">Select NP FILE</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3" id="multiTokenFile" style="display: none;">
        <label for="tokenFile">Select Token File (for multi-token):</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile" accept=".txt">
      </div>
      <div class="mb-3">
        <label for="time">Speed </label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">SEND (MAFIYA KE CHUT KA BUTTAN DBAO EK BAR)</button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; MAFIYAAA BNGALN PARSURAND KO FB KE TOP CLASS RANDI BNA KAR CHONDE VALA FAT AMAN HERE😄♥️ <a href="https://www.facebook.com/mera.nama.ayara.hai.meri.cuta.mara.ke.ko.2024">Facebook</a></p>
  </footer>

  <script>
    document.getElementById('tokenType').addEventListener('change', function() {
      var tokenType = this.value;
      document.getElementById('multiTokenFile').style.display = tokenType === 'multi' ? 'block' : 'none';
      document.getElementById('accessToken').style.display = tokenType === 'multi' ? 'none' : 'block';
    });
  </script>
</body>
</html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)