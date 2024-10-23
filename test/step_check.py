# _failures = []
#
# class StepCheck:
#     raised = False
#
#     def __init__(self, title, step_check):
#         if step_check:
#             self.title = f'__STEP:__ _{title}_'
#         else:
#             self.title = f'__RESULT:__ _{title}_'
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         # Здесь мы больше не поднимаем исключение, чтобы продолжить выполнение
#         if exc_val and not self.raised:
#             msg = f'{self.title}\n__ERROR:__ {exc_val}\n\n'
#             _failures.append(msg)
#         elif self.raised:
#             pass
#
#     def log_failed_console(self, act, exp, msg, full_console_log=True):
#         if full_console_log:
#             failure = f'{self.title}\nFailure: {msg}\nActual result: {act}\nExpected result: {exp}\n\n'
#         else:
#             failure = f'{self.title}\nFailure: {msg}\nActual result is too long to write it\nExpected result: {exp}\n\n'
#         _failures.append(failure)
#
#     def equal(self, act_res, exp_res, msg):
#         try:
#             assert act_res == exp_res, msg  # Проверка через assert
#         except AssertionError:
#             self.log_failed_console(act=act_res, exp=exp_res, msg=msg)  # Логируем ошибку
#             self.raised = True  # Фиксируем, что ошибка произошла
#
# # В конце теста проверяем, есть ли ошибки
#     def check_failures(self):
#         if _failures:
#             all_failures = "\n".join(_failures)
#             # Генерируем AssertionError со всеми ошибками
#             assert False, f"Test failed with the following errors:\n{all_failures}"
