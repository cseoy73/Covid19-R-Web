library(kormaps2014)
library(dplyr)
library(ggiraphExtra)
library(ggplot2)
library(rJava)
library(xlsx)
PPdensity <- read.xlsx('c:/population_density1.xlsx', sheetIndex = 1, encoding = 'CP949')
PPdensity$name <- iconv(PPdensity$name, "UTF-8", "CP949")
str(PPdensity)

str(changeCode(kormap1))
data_id = NULL
code <- c(11, 21, 22, 23, 24, 25, 26, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39)
ggChoropleth(data = PPdensity, 
             aes(fill = density,                                
                           map_id = code,                       
                           tooltip = name),                  
             map = kormap1,        
             interactive = T)