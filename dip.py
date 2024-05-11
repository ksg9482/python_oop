# DIP(Dependency Inversion Principle) 의존성 역전 법칙

class BubbleSort:
    def bubble_sort(self):
        # sorting algorithms
        pass

# 나쁜 예
class SortManager:
    def __init__(self):
        self.sort_method = BubbleSort() # <--- SortManager 는 BubbleSort에 의존적
        
    def begin_sort(self):
        self.sort_method.bubble_sort() # <--- BubbleSort의 bubble_sort 메서드에 의존적

# 좋은 예
class SortManager:
    def __init__(self, sort_method):    # <--- 의존성 주입
        self.set_sort_method(sort_method)
        
    def set_sort_method(self, sort_method):
        self.sort_method = sort_method
        
    def begin_sort(self):
        self.sort_method.sort()         # <--- 하부 클래스가 바뀌더라도, 동일한 코드 활용 가능토록 인터페이스화


# 실습 코드
class BubbleSort:
    def sort(self):
        print('bubble sort')
        pass

class QuickSort:
    def sort(self):
        print('quick sort')
        pass

bubble_sort1 = BubbleSort()
quick_sort1 = QuickSort()

sorting1 = SortManager(bubble_sort1)
sorting1.begin_sort()

sorting2 = SortManager(quick_sort1)
sorting2.begin_sort()

class SelectionSort:
    def sort(self):
        print('selection sort')
        pass

selection_sort = SelectionSort()
sorting3 = SortManager(selection_sort)
sorting3.begin_sort()