##           QR code Generator
  
# Need packages 
# 1) python 
# 2) qrcode packages 
# 3) pillow packages


import qrcode


# taking UPI ID as input
upi_id = input('Enter your upi ID = ')

##  upi is like this [upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE]



phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'


## Create qr codes For each paymentn app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)


# ## Save Qr code to image file 
# phonepe_qr.save('phonepy_qr.png')
# paytm_qr.save('paytmpy_qr.png')
# google_pay_qr.save('google_pay_qr.png')

## Display the QR codes 
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

