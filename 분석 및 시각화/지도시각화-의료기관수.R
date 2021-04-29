library(kormaps2014)
library(dplyr)
library(ggiraphExtra)
library(ggplot2)
library(rJava)
library(xlsx)
medicalnum <- read.xlsx('c:/medical_institutionNum.xlsx', sheetIndex = 1, encoding = 'CP949')
medicalnum$name <- iconv(medicalnum$name, "UTF-8", "CP949")
str(medicalnum)

str(changeCode(kormap1))
data_id = NULL
code <- c(11, 21, 22, 23, 24, 25, 26, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39)
ggChoropleth(data = medicalnum, 
             aes(fill = medical_institution,                                
                 map_id = code,                       
                 tooltip = name),                  
             map = kormap1,        
             interactive = T)

