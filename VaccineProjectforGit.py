from ftplib import ftpcp
import numpy as np
import pandas as pd


# Write a function called proportion_of_education which returns the proportion of children in the dataset who had a mother with the education levels equal to less than high school (<12), high school (12), more than high school but not a college graduate (>12) and college degree.




def proportion_of_education():
    df = pd.read_csv('Class-Resources/resources/NISPUF17.csv', index_col=0)
    noHS=df[df['EDUC1']==1]
    yesHS=df[df['EDUC1']==2]
    moreHS=df[df['EDUC1']==3]
    college=df[df['EDUC1']==4]
    a=len(noHS)
    b=len(yesHS)
    c=len(moreHS)
    d=len(college)
    e=len(df.index)
    
    p1=a/e
    p2=b/e
    p3=c/e
    p4=d/e
    answer = {"less than high school":p1,
                  "high school":p2,
                   "more than highschool but not college":p3,
                   "college":p4}
    return(answer)

print('The proportion of children in the dataset who had a mother with the education levels equal to less than high school (<12), high school (12), more than high school but not a college graduate (>12) and college degree')
print(proportion_of_education())
print()

# Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine from a healthcare provider. Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not.

def average_influenza_doses():
    df = pd.read_csv('Class-Resources/resources/NISPUF17.csv', index_col=0)
    pd.set_option('display.min_rows',500, 'display.max_rows', 600, 'display.max_columns',100)
    cols_to_keep=['CBF_01','P_NUMFLU']
    df=df[cols_to_keep]
    mask=(df['CBF_01']!=77) & (df['CBF_01']!=99)
    df = df.where(mask).dropna()

    ybf = df[df['CBF_01']==1]
    nbf = df[df['CBF_01']==2]
    ybftot = ybf['P_NUMFLU'].sum()
    nbftot = nbf['P_NUMFLU'].sum()
    answer1=ybftot/len(ybf)
    answer2=nbftot/len(nbf)
    
    x=(answer1,answer2)
    return(x)
print('The average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not: ')
print(average_influenza_doses())
print()



# It would be interesting to see if there is any evidence of a link between vaccine effectiveness and sex of the child. Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose) versus those who were vaccinated but did not contract chicken pox. Return results by sex.


def chickenpox_by_sex():
    df = pd.read_csv('Class-Resources/resources/NISPUF17.csv', index_col=0)
    pd.set_option('display.min_rows',500, 'display.max_rows', 600, 'display.max_columns',100)

    cols_to_keep=['SEX','HAD_CPOX','P_NUMVRC']
    df=df[cols_to_keep]
    mask=(df['HAD_CPOX']!=77) & (df['HAD_CPOX']!=99)
    df = df.where(mask).dropna()

    mcp = df[df['SEX']==1]
    fcp = df[df['SEX']==2]

    Ymvacc= mcp[mcp['P_NUMVRC']>0]
    Ymcpox= len(Ymvacc[Ymvacc['HAD_CPOX']==1])
    Nmcpox= len(Ymvacc[Ymvacc['HAD_CPOX']==2])
    mAnswer=Ymcpox/Nmcpox

    Yfvacc= fcp[fcp['P_NUMVRC']>0]
    Yfcpox= len(Yfvacc[Yfvacc['HAD_CPOX']==1])
    Nfcpox= len(Yfvacc[Yfvacc['HAD_CPOX']==2])
    fAnswer=Yfcpox/Nfcpox
    answer = {"male":mAnswer,
                "female":fAnswer,
                }
    
    return(answer)
print("Ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose) versus those who were vaccinated but did not contract chicken pox: ")
print(chickenpox_by_sex())
print()


# A correlation is a statistical relationship between two variables. If we wanted to know if vaccines work, we might look at the correlation between the use of the vaccine and whether it results in prevention of the infection or disease [1]. In this question, you are to see if there is a correlation between having had the chicken pox and the number of chickenpox vaccine doses given (varicella).

def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd

    df = pd.read_csv('Class-Resources/resources/NISPUF17.csv', index_col=0)
    cols_to_keep=['HAD_CPOX','P_NUMVRC']
    df=df[cols_to_keep]
    mask=(df['HAD_CPOX']!=77) & (df['HAD_CPOX']!=99)
    df = df.where(mask).dropna()

    df=pd.DataFrame({"had_chickenpox_column":df['HAD_CPOX'],
                   "num_chickenpox_vaccine_column":df['P_NUMVRC']})

    # here is some stub code to actually run the correlation
    corr, pval=stats.pearsonr(df["had_chickenpox_column"],df["num_chickenpox_vaccine_column"])
    return(corr)

print("Correlation between having had the chicken pox and the number of chickenpox vaccine doses given (varicella):")
print(corr_chickenpox())
print()



