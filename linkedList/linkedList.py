from node.listNode import Node

class LinkedList():
    def __init__(self):
        self.head = None
        self.count = 0

    # 모든 데이터 제거
    def clear(self):
        self.head = None
        self.count = 0
    
    # 인덱스 삽입
    def insert_at(self, index, data):
        new_node = Node(data)

        if index < 0 or index > self.count:
            raise Exception("잘못된 범위입니다.")

        #  첫 번쨰 삽입 할 경우
        if index == 0:
            new_node.next = self.head
            self.head = new_node

        else:
            current_node = self.head

            for _ in range(index - 1):
                current_node = current_node.next

            new_node.next = current_node.next
            current_node.next = new_node

        self.count += 1

    # 마지막 인덱스 삽입
    def insert_last(self, data):
        self.insert_at(self.count, data)

    # 인덱스 삭제
    def delete_at(self, index):
        delete_node = None

        if index < 0 or self.count <= index:
            raise Exception("잘못된 범위입니다.")
        
        if index == 0:
            delete_node = self.head
            self.head = self.head.next
        else:
            current_node = self.head

            for _ in range(index - 1):
                current_node = current_node.next
            
            delete_node = current_node.next
            current_node.next = current_node.next.next

        self.count -= 1
        return delete_node
    
    # 마지막 인덱스 삭제
    def delete_last(self):
        return self.delete_at(self.count - 1)
    
    # 모든 데이터 출력
    def print_all(self):
        current_node = self.head
        data_array = []

        while current_node is not None:
            data_array.append(str(current_node.data))
            current_node = current_node.next

        print(','.join(data_array))

