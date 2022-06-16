import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import argparse
import seaborn as sns
from flask import Response
from matplotlib.figure import Figure
from flask import Flask
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas



class dist():
    
# init method or constructor
    def __init__(self, var1= None, title1 = '', var2 = None, title2 = '', transformed = False, read_file = None, hue= None, type =None):
          
          self.data = data
          self.var1 = var1
          self.title1 = title1
          self.var2 = var2
          self.title2 = title2
          self.transformed = transformed
          self.read_file = str(read_file)
          self.hue = hue
          self.type = type

    def distribution_single(self):
    
   
        
            fig = plt.figure()
            ax = fig.add_subplot(1,2, 2)
            ax.hist(self.var1, bins = 25, color = '#00A0A0')
            ax.set_title("'%s' Feature Distribution"%(self.title1), fontsize = 14)
            ax.set_xlabel("Value")
            ax.set_ylabel("Number of Records")
            ax.set_ylim((0, 100))
            if self.transformed:
                          plt.suptitle("Log-transformed Distributions of Continuous" + self.read_file + "Data Features", fontsize = 16, y = 0.95)
                          plt.tight_layout()
                          plt.show()

            else:
                         plt.suptitle("Skewed Distributions of Continuous" + self.read_file + "Data Features", fontsize = 16, y = 0.95)
                         plt.tight_layout()
                         plt.show()


    def distribution_double(self):
             
            fig = plt.figure()
            ax = fig.add_subplot(1,2, 2)
            ax.hist(self.var1, bins = 25, color = '#00A0A0')
            ax.set_title("'%s' Feature Distribution"%(self.title1), fontsize = 14)
            ax.set_xlabel("Value")
            ax.set_ylabel("Number of Records")
            ax.set_ylim((0, 100))
            ax = fig.add_subplot(1,2, 1)
            ax.hist(self.var2, bins = 25, color = '#00A0A0')
            ax.set_title("'%s' Feature Distribution"%(self.title2), fontsize = 14)
            ax.set_xlabel("Value")
            ax.set_ylabel("Number of Records")
            ax.set_ylim((0, 600))
            if self.transformed:
                       plt.suptitle("Log-transformed Distributions of Continuous Census Data Features", fontsize = 16, y = 0.95)
                       plt.tight_layout()
                       plt.show()

            else:
                       plt.suptitle("Skewed Distributions of Continuous Census Data Features", fontsize = 16, y = 0.95)
                       plt.tight_layout()
                       plt.show()

    def distribution_multi(self):   
           
           
           plt.figure(figsize = (14,10))
           s = []
           for i ,k in enumerate(self.data):
                   
                   if len(pd.unique(self.data[k])) <= 20:
                          s.append(k)
                          plt.subplot(2,3, ((s.index(k))+1))
                          plt.title(k)
                          data[k].hist(bins = 25)
           
           plt.show()
           
     
    def distribution_pie_binary(self):

                percent_zero = len(self.var1.loc[(self.var1 == 0)].reset_index(drop=True))-1
                percent_one = len(self.var1.loc[(self.var1 == 1)].reset_index(drop=True))-1

                plt.figure(figsize =(4,4))
                labels = 'percent_one', 'percent_zero'
                sizes = [percent_one, percent_zero]
                colors = ['yellowgreen', 'gold']
                explode = (0, 0.1)
                plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
                plt.axis('equal')
                plt.title(args.column1)
                plt.show()

    def distribution_pie_multi(self):


                self.var1.value_counts().plot(kind='pie',autopct='%.2f')
                plt.show()

    
    def distribution_sns(self):
               
                
                if self.type == 'boxplot':
                   try :
                           sns.boxplot(x=self.var1, y=self.var2 ,hue=self.hue)
                           plt.show()
                   except: 
                           sns.boxplot(self.var1)
                           plt.show()

                elif self.type == 'countplot':
                   try :
                           sns.countplot(x=self.var1, y=self.var2 ,hue=self.hue)
                           plt.show()
                   except: 
                           sns.countplot(self.var1)
                           plt.show()
              
                elif self.type == 'distplot':
                   try :
                           sns.distplot(x=self.var1, y=self.var2 ,hue=self.hue)
                           plt.show()
                   except: 
                           sns.distplot(self.var1)
                           plt.show()
                
                elif self.type == 'corr':
                   try :
                           sns.heatmap(self.data.corr())
                           plt.show()
                   except: 
                           print('error in corr') 
             

                elif self.type == 'kdeplot':
                   try :
                           sns.kdplot(self.var1[self.var2])
                           plt.show()
                   except: 
                           sns.kdeplot(self.var1)
                           plt.show()


    
    def distribution_count_multi(self):

                columns_cat = []
                for i ,k in enumerate(self.data):
                         
                         if len(pd.unique(self.data[k])) <= 20:
                                   columns_cat.append(k)

                fig, axs = plt.subplots(ncols=2, nrows=3, figsize=(50, 50))
                plt.subplots_adjust(right=0.95, top=0.95)

                for i, col in enumerate(columns_cat, 1):    
                         plt.subplot(2,3, i)
                         sns.countplot(x=col, hue=self.var1, data=self.data)
    
                         plt.xlabel('{}'.format(col), size=10, labelpad=1)
                         plt.ylabel('Count', size=10, labelpad=10)    
                         plt.tick_params(axis='x', labelsize=10)
                         plt.tick_params(axis='y', labelsize=10)
    
                         plt.legend([('not' + self.var1), (self.var1)], loc='upper center', prop={'size': 10})
                         plt.title('Count legend in {} Feature'.format(col), size=10, y=0.98)

                plt.show()




    def distribution_corr(self):
                   
                sns.heatmap(self.data.corr())
                plt.show()

    def flask(self):

                                plt.rcParams["figure.figsize"] = [7.50, 3.50]
                                plt.rcParams["figure.autolayout"] = True
                                app = Flask(__name__)
                                @app.route('/')


                                def plot_png():
                                        
                                        fig,ax=plt.subplots(figsize=(6,6))
                                        ax=sns.set(style="darkgrid")
                                        sns.boxplot(x=self.var1, y=self.var2 ,hue=self.hue)
                                        canvas=FigureCanvas(fig)
                                        img = io.BytesIO()
                                        fig.savefig(img)
                                        img.seek(0)
                                        #return Response(img,mimetype='img/png')
                                        return Response(img.getvalue(), mimetype='image/png')


                                app.run(host="0.0.0.0", port=5000)



my_parser = argparse.ArgumentParser()
my_parser.add_argument('--file')
my_parser.add_argument('--distribution')
my_parser.add_argument('--transformed')
my_parser.add_argument('--column1')
my_parser.add_argument('--column2')
my_parser.add_argument('--hue')
my_parser.add_argument('--flask')
args = my_parser.parse_args()

print(args.file)


if args.file:
      read_file = args.file or ''
else :
      read_file = 'train.csv'

data = pd.read_csv(read_file)

if args.transformed:
     skewed = [args.transformed]
     features_log_transformed = data[skewed].apply(lambda x: np.log(x + 1))

def main():
			if args.distribution == 'single':

				 try:
					 dist(features_log_transformed, 'features_log_transformed', transformed = True).distribution_single()
				 except:
					 print("error : if choise --file train.csv should be choise between two argement(--distribution single or --distribution double)")

			elif args.distribution == 'double':

				 try:
					 dist(data[args.column1] ,args.column1 , data[args.column2], args.column2).distribution_double()
				 except:
					 print("error : if choise --file train.csv should be choise between two argement(--distribution single or --distribution double)")
			 
			elif args.distribution == 'multi':

				 try:
					 dist().distribution_multi()
				 except:
					 print("error in .distribution_multi")

			elif args.distribution == 'pie_binary':

				 try:
					 dist(data[args.column1]).distribution_pie_binary()
				 except:
					 print("error in .distribution_pie_binary")

			elif args.distribution == 'pie_multi':

				 try:
					 dist(data[args.column1]).distribution_pie_multi()
				 except:
					 print("error in .distribution_pie_multi")


			elif args.distribution == 'boxplot' or args.distribution == 'countplot' or args.distribution == 'distplot' or args.distribution == 'corr' or args.distribution == 'kdeplot' :

			        try:         

                                                        if isinstance(args.column1, str) == True and isinstance(args.column2, str) == True and isinstance(args.hue, str) == True and isinstance(args.distribution, str) == True and isinstance(args.flask, str) == True:
                                                                                dist(var1 = data[args.column1], var2 = data[args.column2], hue= data[args.hue], type= args.distribution).flask()
                                                        elif isinstance(args.column1, str) == True and isinstance(args.column2, str) == True and isinstance(args.hue, str) == True and isinstance(args.distribution, str) == True: 
                                                                                dist(var1 = data[args.column1], var2 = data[args.column2], hue= data[args.hue], type= args.distribution).distribution_sns()
                                                        elif isinstance(args.column1, str) == True and isinstance(args.column2, str) == True and isinstance(args.distribution, str) == True:
                                                                                dist(var1 = data[args.column1][args.column2], type= args.distribution).distribution_sns()
                                                        elif isinstance(args.column1, str) == True and isinstance(args.distribution, str) == True:
                                                                                dist(var1 = data[args.column1] ,type= args.distribution).distribution_sns()
                                                        elif isinstance(args.distribution, str) == True :
                                                                                dist(type= args.distribution).distribution_sns()


			        except:
					                 print("error in .distribution_sns")

			elif args.distribution == 'count_multi':
				   
				 try:
					 dist(args.column1).distribution_count_multi()
				 except:
					 print("error in .distribution_count_multi")


			elif args.distribution == None:
				 try:
					 dist(data['Age'] ,'Age' , data['Sex'], 'Sex').distribution_double()
				 except:
					 print("An exception occurred") 

			#dist(data['Age'] ,'Age' , data['Sex'], 'Sex').distribution_double()

main()
#dist(var1 = data[args.column1], var2 = data[args.column2], hue= data[args.hue], type= args.distribution).flask()

