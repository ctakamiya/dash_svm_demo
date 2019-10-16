# # install requirement 
# (required on 1st launch)
!pip3 install -r requirements.txt

# # Get engine ID
# ## ...and construct app URL from env variables 
import os 
engine_id = os.environ.get('CDSW_ENGINE_ID')
cdsw_domain = os.environ.get('CDSW_DOMAIN')

# # Print out URL
# ### Raw text 
"http://{}.{}".format(engine_id,cdsw_domain,engine_id,cdsw_domain)

# ### clickable URL
from IPython.core.display import HTML
HTML('<a href="http://{}.{}">http://{}.{}</a>'
     .format(engine_id,cdsw_domain,engine_id,cdsw_domain))

# # Launch dash app
!python3 app.py