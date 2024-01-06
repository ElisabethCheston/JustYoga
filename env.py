import os
 
os.environ['SECRET_KEY'] = 'xxxxxxxx'
os.environ['DEVELOPMENT'] = "x"
os.environ.setdefault('DEVELOPMENT', 'True')
 
# Stripe
os.getenv['STRIPE_PUBLIC_KEY'] = 'xxxxxxx'
os.getenv['STRIPE_SECRET_KEY'] = 'xxxxxxx'
os.getenv['STRIPE_WH_SECRET'] = 'xxxx'
 
# AWS
os.environ['AWS_ACCESS_KEY_ID'] = 'xxx'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'xxxxxx'
 
#Email
os.environ['EMAIL_HOST_PASS'] =
os.environ['EMAIL_HOST_USER'] = 'xxxxxx'
