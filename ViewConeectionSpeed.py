'''run this code on Python hub'''
from speedtest import Speedtest
st= Speedtest()
print("Your Connection Download Speed Is=",st.download())
print("your Connection Upload speed Is=",st.upload())
