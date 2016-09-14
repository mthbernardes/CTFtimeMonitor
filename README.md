# CTFtimeMonitor
Tool to monitor for the next ctf posted on CTFTime

#Install
<pre>
git clone https://github.com/mthbernardes/CTFtimeMonitor
pip install -r dependencies.txt
</pre>

#Configuration
<pre>
Edit the file CTFtimeMonitor.py,
line10
group = group_integer_id

line 11
bot = telepot.Bot('Telegram bot API here')
</pre>

#Usage
<pre>
screen -S CTFtimeMonitor
python CTFtimeMonitor.py
CTRL+A+D
</pre>
