# import logging
# from rest_framework import exceptions
# from powerhub.models import Order, Package

# # Logs
# logger = logging.getLogger(__name__)


# class ServiceProcessor:
#     def __init__(self):
#         self.kwik_base_url = "https://private-26299-apikwik.apiary-mock.com/v2/"
#         self.kwik_access_token = "74b8e93c9a925b5b7e3acb40858e36ad"
    
#     def process_service(self, service_type):
#         if service_type == 'KWIK':
#             return self.process_kwik_order()
#         elif service_type == 'GIGL':
#             pass
#         elif service_type == 'DHL':
#             pass
    # def process_kwik_order(self):
        # pass
            
#     def process_gigl_order(self):
#         pass
    
#     def process_dhl_order(self):
#         pass