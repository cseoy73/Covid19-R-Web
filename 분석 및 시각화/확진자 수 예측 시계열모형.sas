data lab;
infile 'c:\covidnumber.txt';
input number @@;
date = intnx('day','16MAR20'D,_n_-1); 
format date date9.;
lnumber=log(number); lnumber1=dif(lnumber);
run;

symbol1 i=join v=none l=1 c=black;
symbol2 i=join v=none l=3 c=blue;
symbol3 i=join v=none l=3 c=red;

proc gplot data=lab;
plot lnumber*date=1;
run;

plot lnumber1*date=1;
run;

proc arima data=lab;
identify var=lnumber(1) nlag=24;
estimate p=2 plot noint;
forecast lead=20 out= fore2;
run;
quit;

data fore2; set fore2; n=_n_;
run;

proc gplot data=fore2;
plot lnumber*n=1 forecast*n=2/  overlay legend; 
run;


