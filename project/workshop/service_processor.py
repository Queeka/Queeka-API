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
        
#     def process_kwik_order(self, data):
#         headers = {
#             'Content-Type': 'application/json'
#         }
#         data = {
#             "domain_name": "staging-client-panel.kwik.delivery",
#             "access_token": "aeea63d6f889c67dd75155e9e5fc930e",
#             "vendor_id": 37,
#             "is_multiple_tasks": 1,
#             "fleet_id": "",
#             "latitude": 0,
#             "longitude": 0,
#             "timezone": -330,
#             "has_pickup": 1,
#             "has_delivery": 1,
#             "pickup_delivery_relationship": 0,
#             "layout_type": 0,
#             "auto_assignment": 1,
#             "team_id": "",
#             "pickups": [
#                 {
#                     "address": "Sector 28, Chandigarh, India",
#                     "name": "Ishita",
#                     "latitude": 30.7172888,
#                     "longitude": 76.8035087,
#                     "time": "2023-08-22 15:25:23",
#                     "phone": "+919898989898",
#                     "email": ""
#                 }
#             ],
#             "deliveries": [
#                 {
#                     "address": "Sector 32, Chandigarh, India",
#                     "name": "Ishita",
#                     "latitude": 30.709472,
#                     "longitude": 76.7743709,
#                     "time": "2023-08-22T15:33:53.000Z",
#                     "phone": "+919898989898",
#                     "email": "",
#                     "has_return_task": false,
#                     "is_package_insured": 0,
#                     "hadVairablePayment": 1,
#                     "hadFixedPayment": 0,
#                     "is_task_otp_required": 0
#                 }
#             ],
#             "insurance_amount": 0,
#             "total_no_of_tasks": 1,
#             "total_service_charge": 0,
#             "payment_method": 524288,
#             "amount": "1320.2",
#             "surge_cost": 0,
#             "surge_type": 0,
#             "delivery_instruction": "",
#             "loaders_amount": 0,
#             "loaders_count": 0,
#             "is_loader_required": 0,
#             "delivery_images": "",
#             "vehicle_id": 1,
#             "sareaId": "6"
#             }
            
#     def process_gigl_order(self):
#         pass
    
#     def process_dhl_order(self):
#         pass