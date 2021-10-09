from captcha.image import ImageCaptcha
image=ImageCaptcha(width=300,height=90)
captcha_text='ZXYGJKL'
data=image.generate(captcha_text)
image.write(captcha_text,'CAPTCHA.png')
