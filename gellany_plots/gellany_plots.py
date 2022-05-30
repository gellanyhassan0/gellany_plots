import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import argparse




class dist():
    
# init method or constructor
    def __init__(self, var1= None, title1 = '', var2 = None, title2 = '', transformed = False, read_file = None):
          
          self.data = data
          self.var1 = var1
          self.title1 = title1
          self.var2 = var2
          self.title2 = title2
          self.transformed = transformed
          self.read_file = str(read_file)
          

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
           

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--file', action='store')
my_parser.add_argument('--distribution', action='store')
args = my_parser.parse_args()

print(args.file)


if args.file:
      read_file = args.file or ''
else :
      read_file = 'train.csv'

data = pd.read_csv(read_file)
skewed = ['Fare']
features_log_transformed = data[skewed].apply(lambda x: np.log(x + 1))


if args.distribution == 'single':

         try:
                 dist(features_log_transformed, 'features_log_transformed', transformed = True).distribution_single()
         except:
                 print("error : if choise --file train.csv should be choise between two argement(--distribution single or --distribution double)")
elif args.distribution == 'double':

         try:
                 dist(data['Age'] ,'Age' , data['Sex'], 'Sex').distribution_double()
         except:
                 print("error : if choise --file train.csv should be choise between two argement(--distribution single or --distribution double)")
 
elif args.distribution == 'multi':

         try:
                 dist().distribution_multi()
         except:
                 print("error in .distribution_multi")

elif args.distribution == None:
         try:
                 dist(data['Age'] ,'Age' , data['Sex'], 'Sex').distribution_double()
         except:
                 print("An exception occurred") 

#dist(data['Age'] ,'Age' , data['Sex'], 'Sex').distribution_double()


