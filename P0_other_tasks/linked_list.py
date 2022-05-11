class Node:
    def __init__(self, data=None, next=None):
        """data - значение, next - следующий элемент """
        self.data = data
        self.next = next


class LinkedList:
    """Создаём класс связанного списка"""
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            """Поочерёдно переходим к следующему элементу, проверяя не равен ли он None\
            если нет, то присоединяем его и идём дальше. На последнем элементе цикл завершится."""
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        """Вводим счётчик"""
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
            """Итерируемся до окончания элементов в списке"""

        return count

    def insert_at_begining(self, data):
        """Добавление элемента в начало списка"""
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        """Добавление элемента в конец списка"""
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        """Возможность добавить элемент в указанное место в списке"""
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        """Удаление требуемого элемента"""

        if index < 0 or index >= self.get_length():
            """Проверка на допустимость индекса"""

            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        """ Добавление заданных значений и проебразование их в конечный связанный список"""
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
