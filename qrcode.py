import pyqrcode

a=pyqrcode.create("https://en.wikipedia.org/wiki/Blood_donation_in_India#:~:text=Criteria%20to%20donate%20blood,-There%20are%20several&text=Overall%20health%2D%20The%20donor%20must,minimum%20of%2012.5%20g%2FdL.")
a.svg("qrcode1.svg",scale=8,background='white')








