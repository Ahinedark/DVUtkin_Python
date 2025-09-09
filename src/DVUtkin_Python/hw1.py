"""Домашнее задание 1. Уткин Д.В."""
class CustomerDataClass:
   """Класс для информации о покупателях."""

   def __init__(self,customer_id, customer_name):
      """Конструктор для CustomerDataClass.

      Args:
         customer_id (int): Идентификатор покупателя
         customer_name (str): Имя покупателя
      """
      self.customer_id = customer_id
      self.customer_name = customer_name
      self.orders = []

   def add_order(self, order_object):
      """Добавить заказ к покупателю.

      Args:
         order_object (OrderDataClass): Заказ
      """
      self.orders.append(order_object)

   def get_total_amount(self):
      """Рассчитать общую сумму заказов покупателя.

      Returns:
         total (int, float): Сумма заказов
      """
      total = 0
      for o in self.orders:
         total = total + o.amount
      return total


class OrderDataClass:
   """Класс для информации о заказах."""

   def __init__(self, order_id, amount):
      """Конструктор для OrderDataClass.

      Args:
         order_id (int): Идентификатор заказа
         amount (int, float): Сумма заказа
      """
      self.order_id = order_id
      self.amount = amount


def calculate_discount(customer_obj):
   """Рассчитать скидку для покупателя.

   Если сумма заказов > 1000, скидка = сумма заказов / 10, иначе скидка = 0.

   Args:
      customer_obj (CustomerDataClass): Покупатель

   Returns:
      discount (float): Скидка
   """
   total_amount = customer_obj.get_total_amount()
   discount = total_amount * 0.1 if total_amount > 1000 else 0
   return discount


def print_customer_report(customer_obj):
   """Вывести информацию о покупателе.

   Всего заказов, общая сумма заказов, скидка, средняя сумма заказов.
   
   Args:
      customer_obj (CustomerDataClass): Покупатель
   """
   print('Customer Report for:', customer_obj.customer_name)
   print('Total Orders:', len(customer_obj.orders))
   print('Total Amount:', customer_obj.get_total_amount())
   print('Discount:', calculate_discount(customer_obj))
   print('Average Order:', end = ' ')
   if len(customer_obj.orders) > 0:
      print(customer_obj.get_total_amount() / len(customer_obj.orders))
   else:
      print('0')


def main_program():
   """Главная функция.
   
   Создать покупателя с 2 заказами и покупателя без заказов,
   вывести информацию о покупателях.
   """
   c1 = CustomerDataClass(1, 'SAP Customer')
   o1 = OrderDataClass(101, 500)
   o2 = OrderDataClass(102, 800)
   c1.add_order(o1)
   c1.add_order(o2)
   print_customer_report(c1)

   c2 = CustomerDataClass(2, 'Empty Customer')
   print_customer_report(c2) 


main_program()