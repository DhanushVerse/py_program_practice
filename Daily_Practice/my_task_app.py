# My task app
def my_task_app():
   all_tasklist = []
   while True:
      task = input('\nEnter the task (Type "exit" to close): ') 
      if task.lower() == 'exit':
         break
      print('1. Completed✅\n2. Partial Completed🤞\n3. Not Completed❌')
      status = input('Enter the status of your task:')
      status_check = {'1': 'Completed✅','2': 'Parital Completed','3': 'Not Completed❌','4': 'Exit😙'}
      current_status = status_check.get(status,"unknown")
      all_tasklist.append(f'{task} - {current_status}')
   return all_tasklist
   
task_app = my_task_app()
print('\n The Task list are:')
for t in task_app:
   print(t)