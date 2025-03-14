from linkedList.linkedList import LinkedList   

class LinkedListTest():
    def test_main(self):
        # 링크드 리스트 인스턴스 생성
        linked_list_instance = LinkedList()

        # 1. 빈 리스트 상태에서 출력
        print("Test 1: 초기 상태 출력")
        linked_list_instance.print_all()  # 예상 출력: []

        # 2. 첫 번째 데이터 삽입
        print("\nTest 2: 첫 번째 데이터 삽입 (1)")
        linked_list_instance.insert_last(1)
        linked_list_instance.print_all()  # 예상 출력: [1]

        # 3. 두 번째 데이터 삽입
        print("\nTest 3: 두 번째 데이터 삽입 (2)")
        linked_list_instance.insert_last(2)
        linked_list_instance.print_all()  # 예상 출력: [1, 2]

        # 4. 특정 인덱스에 데이터 삽입 (인덱스 1에 3 추가)
        print("\nTest 4: 인덱스 1에 3 삽입")
        linked_list_instance.insert_at(1, 3)
        linked_list_instance.print_all()  # 예상 출력: [1, 3, 2]

        # 5. 잘못된 인덱스 삽입 (인덱스 5는 유효하지 않음)
        try:
            print("\nTest 5: 잘못된 인덱스 삽입 (인덱스 5)")
            linked_list_instance.insert_at(5, 4)  # 예외 발생
        except Exception as e:
            print(f"예외 발생: {e}")  # 예상 출력: 예외 발생: 잘못된 범위입니다.

        # 6. 마지막 데이터 삽입
        print("\nTest 6: 마지막에 4 추가")
        linked_list_instance.insert_last(4)
        linked_list_instance.print_all()  # 예상 출력: [1, 3, 2, 4]

        # 7. 특정 인덱스 삭제 (인덱스 1 삭제)
        print("\nTest 7: 인덱스 1 삭제")
        linked_list_instance.delete_at(1)
        linked_list_instance.print_all()  # 예상 출력: [1, 2, 4]

        # 8. 마지막 데이터 삭제
        print("\nTest 8: 마지막 데이터 삭제")
        linked_list_instance.delete_last()
        linked_list_instance.print_all()  # 예상 출력: [1, 2]

        # 9. 모든 데이터 삭제
        print("\nTest 9: 모든 데이터 삭제")
        linked_list_instance.clear()
        linked_list_instance.print_all()  # 예상 출력: []