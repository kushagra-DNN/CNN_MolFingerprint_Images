#### Image type 2 ######
#### Fingeprint Matrix of 14*12  ########


k1<-read.csv("", header = F)
### Give input files as: 
#Feature_data\\Image_type2\\Train\\active.csv
#Feature_data\\Image_type2\\Train\\inactive.csv
#Feature_data\\Image_type2\\Test\\active.csv
#Feature_data\\Image_type2\\Test\\inactive.csv


len<-dim(k1)[1]

k2<-data.frame()

for (j in 1:len) {
  a=1
  b=12
  for (i in 1:14) {
    if(i==14){
      k2[14,1:11]<-k1[j,157:167]
      k2[14,12]<-0.5
      
    }
    else{
      k2[i,1:12]<-k1[j,a:b]
      a=b+1
      b=b+12
    }
    write.table(k2,paste0(j,".csv"), row.names = F,col.names = F,sep = ",")
  }
  
}