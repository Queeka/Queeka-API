# from django.test.runner import DiscoverRunner

# from django.test.runner import DiscoverRunner

# class CustomTestRunner(DiscoverRunner):
#     def run_suite(self, suite, **kwargs):
#         result = super().run_suite(suite, **kwargs)
#         function_name = suite.id().split('.')[-1]
#         if result.wasSuccessful():
#             print(f"{function_name} --- Passed [OK]")
#         else:
#             print(f"{function_name} --- Failed [FAILED]")
#         return result
