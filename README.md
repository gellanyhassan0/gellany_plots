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
<code>python3 gellany_plots.py --file train.csv --distr distplot --hue Sex --column1 Age --column2 Sex --flask flask</code><br>


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
  
http://127.0.0.1:5000/
http://172.17.0.2:5000/
  

![alt text](https://github.com/gellanyhassan0/gellany_plots/blob/main/Screenshot_2022-06-16_08-16-44.png?raw=true)<br>
  
  
  
  
<code>python3 gellany_plots.py --file train.csv --distr distplot --hue Sex --column1 Age --column2 Sex --flask flask</code><br>
  
  
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
/usr/local/lib/python3.9/dist-packages/seaborn/distributions.py:2619: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).
  warnings.warn(msg, FutureWarning)
  127.0.0.1 - - [16/Jun/2022 08:17:25] "GET / HTTP/1.1" 200 -</code><br>
  
 http://127.0.0.1:5000/
 http://172.17.0.2:5000/
  
![alt text](https://github.com/gellanyhassan0/gellany_plots/blob/main/Screenshot_2022-06-16_08-17-31.png?raw=true)

<code>python3 gellany_plots.py --file train.csv --distr boxplot --column1 Survived --column2 Age --hue Sex</code><br>

![alt text](https://github.com/gellanyhassan0/gellany_plots/blob/main/Figure_1.png?raw=true)
![alt text](https://github.com/gellanyhassan0/gellany_plots/blob/main/Screenshot_2022-06-16_01-56-24.png?raw=true)

 
[![asciicast](https://asciinema.org/a/502076.svg)](https://asciinema.org/a/502076)
  

  
# docker deploy
#/home/go/ = your path your already download git folder in it<br>
<code>docker image build -t gellany_django /home/go/gellany_django</code><br>
<code>docker run --publish 8000:8000 -it -d gellany_django</code><br>
<code>docker ps</code><br>
<code>docker exec -it 83ea954d9b5a python3 manage.py runserver 0.0.0.0:8000</code><br>

http://0.0.0.0:8000/
http://0.0.0.0:8000/polls

<code>docker stop f77d93571bcc</code><br>
<code>docker ps</code><br>


# docker pull direct
#/home/go/ = your path your already download git folder in it<br>
<code>docker pull gellany/gellany_django</code><br>
<code>docker run --publish 8000:8000 -it -d gellany/gellany_django</code><br>
<code>docker ps</code><br>
<code>docker exec -it 83ea954d9b5a python3 manage.py runserver 0.0.0.0:8000</code><br>
<code>docker stop f77d93571bcc</code><br>

http://0.0.0.0:8000/
http://0.0.0.0:8000/polls


# docker push
<code>docker login --username username</code><br>
<code>docker image list</code><br>
<code>docker tag a2ac10640f5b gellany/gellany_django</code><br>
<code>docker push gellany/gellany_django:latest</code><br>

# docker image list removed
<code>docker images rm </code><br>

# docker image remove all
<code>docker image list|awk '{print $3}'|xargs -I z docker rmi --force z</code><br>
<code>docker image list</code><br>

# docker system Remove unused data
<code>docker system prune --force</code><br>

