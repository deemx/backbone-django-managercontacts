from app.models import Contact


contact = Contact(first_name='Павел',
                  last_name='Сидоров',
                  email_address='sidorov@gmail.com',
                  description='Повар')
contact.save()

contact = Contact(first_name='Наталья',
                  last_name='Сидорова',
                  email_address='sidorova@gmail.com',
                  description='Жена поаора')
contact.save()

contact = Contact(first_name='Иван',
                  last_name='Петров',
                  email_address='petrov@gmail.com',
                  description='Лучший друг повара')
contact.save()
