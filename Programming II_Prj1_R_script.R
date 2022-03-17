
data <- read.csv('dati.csv')## da inserire percorso?

View(data)
sapply(data,class)
summary(data)

## TimeISO is redundant (time in seconds is sufficient)
newdata<-data[,-2]
View(newdata)
which(is.na(newdata))

hour<-rep(c(0:23), times=nrow(newdata)/24)
day<-rep(c(1:9), each=24)

newdata$hour<-hour
newdata$day<-day
newdata<- select(newdata, time, hour, day, radSole, temperature, Tperc, tempSuolo, HumRel, humSuolo, wind10)

names(newdata)<-c("time", "hour", "day", "SunRad", "Tmp", "TmpPerc", "TmpGround", "HumRel", "HumGround", "Wind")

library(DataExplorer)
DataExplorer::create_report(newdata)

###Solar-radiation and Tmp

ggplot(data=newdata) +
  geom_point(mapping = aes(x=hour, y=Tmp, color=SunRad))+
  scale_colour_gradient2(low = "#0000b3", mid= "#3333ff",
                         high = "#ff0000",  midpoint = max(newdata$SunRad)/6)+
  ggtitle("Solar radiation & Temperature")+
  theme(plot.title = element_text(hjust=0.5,color="black", size=14, face="bold"))

####Solar-radiation and Relative Humidity

ggplot(data=newdata)+
  geom_point(mapping = aes(x=hour, y=HumRel, color=SunRad)) + #, color=HumRel
  scale_colour_gradient2(low = "#0000b3", mid= "#3333ff",
                         high = "#ff0000",  midpoint = max(newdata$SunRad)/6)+
  ggtitle("Solar radiation & Humidity")+
  theme(plot.title = element_text(hjust=0.5,color="black", size=14, face="bold"))

### wind and temperature
ggplot(data=newdata)+
  geom_point(mapping = aes(x=Tmp, y=Wind, alpha=HumRel))+
  ggtitle("Wind & Temperature")+
  theme(plot.title = element_text(hjust=0.5,color="black", size=14, face="bold"))
####the dots seems to have a non linear interaction, humidity decrease with wind or temperature?

## adding solar radiation
ggplot(data=newdata)+
  geom_point(mapping = aes(x=Tmp, y=Wind, alpha=HumRel))+
  geom_smooth(mapping = aes(x=Tmp, y=Wind, line=SunRad))+
  ggtitle("Wind & Tmp & Solar Radiation")+
  theme(plot.title = element_text(hjust=0.5,color="black", size=14, face="bold"))
##### the solar radiation explain better the increase of wind when the temperature is high

### Radiation  and temeperature
ggplot(data=newdata)+
  geom_point(mapping = aes(x=Tmp, y=SunRad, alpha=Wind, size=SunRad))+
  ggtitle("Wind & Temperature")+
  theme(plot.title = element_text(hjust=0.5,color="black", size=14, face="bold"))
"""
ggplot(data=newdata)+
  geom_point(mapping = aes(x=SunRad, y=Wind, alpha=Tmp))+
  ggtitle('Wind & Temperature')+
  theme(plot.title = element_text(hjust=0.5,color="black", size=14, face="bold"))
"""
## WIND ~ Tmp e TmpGround
ggplot(data=newdata)+
  geom_point(mapping = aes(x=Tmp, y=TmpGround, alpha=SunRad))+
  geom_smooth(mapping = aes(x=Tmp, y=TmpGround, line=Wind))+
  ggtitle("Tmp & TmpGround & Wind Solar Radiation")+
  theme(plot.title = element_text(hjust=0.5,color="black", size=14, face="bold"))

ggplot(data=newdata)+
  geom_point(mapping = aes(x=Wind, y=TmpGround, color=HumGround))+
  geom_smooth(mapping = aes(x=Wind, y=TmpGround, line=SunRad))+
  ggtitle("Tmp & TmpGround & Wind) Solar Radiation")+
  theme(plot.title = element_text(hjust=0.5,color="black", size=14, face="bold"))


newdata$heat<-log(newdata$Tmp)+log(newdata$TmpGround)+log(newdata$HumRel)
#newdata$heat<-NULL
View(newdata)
ggplot(data=newdata)+
  geom_point(mapping = aes(x=heat, y=Wind, color=SunRad, size=HumRel))+
  geom_smooth(mapping = aes(x=heat, y=Wind, line=SunRad))+
  ggtitle("Tmp & TmpGround & Wind & Solar Radiation")+
  theme(plot.title = element_text(hjust=0.5,color="black", size=14, face="bold"))

### correlation matrix
library(ggcorrplot)
correlation_matrix<-cor(newdata[,-1])
plt0<-ggcorrplot(correlation_matrix, method ="square")
plt0<-plt0 + labs(title = "Correlation matrix\n", hjust=0.5)
plt0

plt1 <- heatmap(correlation_matrix, Colv = "Rowv")
plt1 <- heatmap(correlation_matrix)
plt1 <- plt1 + labs(title = "Correlation matrix\n", hjust=0.5)
plt1
cor_

ggplot(data=newdata)+
  geom_point(mapping = aes(x=hours, y=Wind, alpha=HumRel))+ ### gradiente rosso-blue
  #scale_colour_gradient2(low = "#0000b3", mid= "#3333ff", high = "#ff0000",  
                         #midpoint = (max(newdata$HumRel)+min(newdata$HumRel))/2)+
  geom_smooth(mapping = aes(x=hour, y=Wind, line=Tmp), color="red")+
  ggtitle("Solar radiation & Tmp")+
  theme(plot.title = element_text(hjust=0.5,color="black", size=14, face="bold"))





####### Repository radiation temp  ####
ggplot(data=newdata)+
  geom_point(mapping = aes(x=hour, y=HumRel, color=SunRad)) + #, color=HumRel
  scale_colour_gradient2(low = "#0000b3", mid= "#3333ff",
                         high = "#ff0000",  midpoint = (max(newdata$Tmp)+min(newdata$Tmp))/2)+
  ggtitle("Solar radiation & Humidity")+
  theme(plot.title = element_text(hjust=0.5,color="black", size=14, face="bold"))

ggplot(data=newdata)+
  geom_point(mapping = aes(x=hour, y=SunRad, color=Tmp)) + #, color=HumRel
  geom_smooth(mapping = aes(x=hour, y=SunRad, line=tempSuolo), se=FALSE)
  
ggplot(data=newdata)+
  geom_point(mapping = aes(x=hour, y=tempSuolo, color=Tmp)) + #, color=HumRel
  geom_smooth(formula = y ~ x, method = "loess")



ggplot(data=newdata)+
  geom_point(mapping = aes(x=hour, y=tempSuolo, color=Tmp)) + #, color=HumRel
  geom_smooth(line=newdata$tempSuolo, se=FALSE)

ggplot(data=newdata)+
  geom_point(mapping = aes(x=hour, y=SunRad, color=Tmp)) + #, color=HumRel
               scale_colour_gradient2(low = "blue",
                                      high = "red", midpoint = (max(data$Tmp)+min(data$Tmp))/2)

ggplot(data=newdata) +
  geom_point(mapping = aes(x=hour, y=SunRad, color=Tmp))+
  scale_colour_gradient2(low = "#0000b3", mid= "#3333ff",
                         high = "#ff0000",  midpoint = (max(newdata$Tmp)+min(newdata$Tmp))/2)+
  ggtitle("Solar radiation & Tmp")+
  theme(plot.title = element_text(hjust=0.5,color="black", size=14, face="bold"))
####Repository radiation hum #####

ggplot(data=newdata) +
  geom_point(mapping = aes(x=hour, y=SunRad, color=HumRel))+
  scale_colour_gradient2(low = "#0000b3", mid= "#3333ff",
                         high = "#ff0000", midpoint = (max(newdata$HumRel)+min(newdata$HumRel))/2)+
  ggtitle("Solar radiation & Relative Humidity")+
  theme(plot.title = element_text(hjust=0.5,color="black", size=14, face="bold"))
  
        
  
ggplot(data=newdata) +
  geom_point((mapping = aes(x=hour, y=SunRad, alpha=HumRel)), color=4)+
  ggtitle("Solar radiation & Relative Humidity")+
  theme(plot.title = element_text(hjust=0.5,color="black", size=14, face="bold"))


ggplot(data=newdata) +
  geom_point((mapping = aes(x=hour, y=SunRad, alpha=HumRel)), color=6)


range(data$HumRel)


ggplot(data=newdata) +
  geom_point(mapping = aes(x=hour, y=SunRad, color=HumRel))+
  scale_colour_gradient2()

ggplot(data=newdata) +
  geom_point(mapping = aes(x=hour, y=Tmp, color=HumRel))+
  scale_colour_gradient2()

ggplot(data=newdata) +
  geom_point(mapping = aes(x=hour, y=SunRad, color=HumRel))+
  scale_colour_gradient2(low = "azure", mid= "#3333ff",
                         high = "blue", midpoint = (max(newdata$HumRel)+min(newdata$HumRel))/2)#, color=HumRel


ggplot(data=newdata) +
  geom_point(mapping = aes(x=hour, y=SunRad, color=HumRel))+
  scale_colour_gradient2(low = "#0000b3", mid= "#3333ff",
                         high = "#ff0000", midpoint = (max(newdata$HumRel)+min(newdata$HumRel))/2)#, color=HumRel
  
#####






#length(hours)
#nrow(newdata)

newdata$hour<-hours
data$hour<-hours

view(data)
