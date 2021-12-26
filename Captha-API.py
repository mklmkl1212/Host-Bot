from flask import *
import os,requests
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home_page():
    return redirect("https://apis.red/", code=302)

@app.route('/check/',methods=['GET'])
def pyhostbotmakemepage():
    id = str(request.args.get('id'))
    ip = request.remote_addr

    folderName = 'pyhostbot'
    if len(id) < 6:
        return render_template('Rejected.html', theId=id, theIP=ip, theName='@PyHostBot', theError='Spam Detected ( Min )')
    elif len(id) > 10:
        return render_template('Rejected.html', theId=id, theIP=ip, theName='@PyHostBot', theError='Spam Detected ( Max )')

    else:
        try:
            os.makedirs(f'../public_html/x/{folderName}')
        except:
            pass

        r = requests.get(f'https://apis.red/x/{folderName}/data.txt').text
        
        if id in r:
            return render_template('Rejected.html', theId=id, theIP=ip, theName='@PyHostBot', theError='You Already Have Account On The Bot!')
            
        elif ip in r:
            return render_template('Rejected.html', theId=id, theIP=ip, theName='@PyHostBot', theError='You Already Have Account On The This IP!')
            
        elif id in r:
            return render_template('Rejected.html', theId=id, theIP=ip, theName='@PyHostBot', theError='You Already Have Account On The Bot!')
            
        elif id not in r:
            with open(f'../public_html/x/{folderName}/data.txt', 'a+') as the_bin_file:
                the_bin_file.writelines(f'{id},{ip}\n')
            
            return render_template('Verified.html', theId=id, theIP=ip, theName='@PyHostBot')
        else:
            return render_template('Rejected.html', theId=id, theIP=ip, theName='@PyHostBot', theError='Error Happened!')
if __name__ == '__main__':
    app.run()
