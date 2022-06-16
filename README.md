# gellany_plots 
automate you csv files to presenation as model plot as easy way in command line <br>

<code>git clone https://github.com/gellanyhassan0/gellany_plots.git</code><br>
<code>cd gellany_plots</code><br>
<code>pip install -r requirements.txt</code><br>



<code>python3 gellany_plots.py </code><br>
<code>python3 gellany_plots.py --file train.csv </code><br>
<code>python3 gellany_plots.py --file train.csv --distr multi</code><br>
<code>python3 gellany_plots.py --file train.csv --distr single</code><br>
<code>python3 gellany_plots.py --file train.csv --distr double</code><br>
<code>python3 gellany_plots.py --file train.csv --distr single --transformed Fare</code><br>
<code>python3 gellany_plots.py --file train.csv --distr double --column1 'Age' --column2 'Sex'</code><br>
<code>python3 gellany_plots.py --file train.csv --distr pie_binary --column1 Survived</code><br>
<code>python3 gellany_plots.py --file train.csv --distr countplot --column1 Pclass</code><br>
<code>python3 gellany_plots.py --file train.csv --distr boxplot --column1 Pclass</code><br>
<code>python3 gellany_plots.py --file train.csv --distr distplot --column1 Pclass</code><br>
<code>python3 gellany_plots.py --file train.csv --distr count_multi --column1 Survived</code><br>
<code>python3 gellany_plots.py --file train.csv --distr boxplot --column1 Survived --column2 Age --hue Sex</code><br>
<code>python3 gellany_plots.py --file train.csv --distr corr</code><br>
<code>python3 gellany_plots.py --file train.csv --distr kdeplot --column1 Pclass</code><br>
<code>python3 gellany_plots.py --file train.csv --distr boxplot --hue Survived --column1 Age --column2 Sex</code><br>


<code>python3 gellany_plots.py -h</code><br>  
<code>python3 gellany_plots.py -h
usage: gellany_plots.py [-h] [--file FILE] [--distribution DISTRIBUTION] [--transformed TRANSFORMED] [--column1 COLUMN1]
                        [--column2 COLUMN2] [--hue HUE]

optional arguments:
  -h, --help            show this help message and exit
  --file FILE
  --distribution DISTRIBUTION
  --transformed TRANSFORMED
  --column1 COLUMN1
  --column2 COLUMN2
  --hue HUE

</code><br>

<code>python3 gellany_plots.py --file train.csv --distr boxplot --hue Sex --column1 Age --column2 Sex --flask flask</code><br>


<code>train.csv
 * Serving Flask app "gellany_plots" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
/home/go/gellany_plots/gellany_plots.py:205: UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail.
  fig,ax=plt.subplots(figsize=(6,6))
QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
127.0.0.1 - - [16/Jun/2022 07:52:56] "GET / HTTP/1.1" 200 -<code><br>


<code>python3 gellany_plots.py --file train.csv --distr boxplot --column1 Survived --column2 Age --hue Sex</code><br>

![alt text](https://github.com/gellanyhassan0/gellany_plots/blob/main/Figure_1.png?raw=true)
![alt text](https://github.com/gellanyhassan0/gellany_plots/blob/main/Screenshot_2022-06-16_01-56-24.png?raw=true)

 
[![asciicast](https://asciinema.org/a/502076.svg)](https://asciinema.org/a/502076)
