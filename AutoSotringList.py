
class AutoSortingList:

    def __init__(self, array):
        self.__array = self.__merge_sort(array)

    def __merge_sort_divide(self, left, right):
        if len(left) == 0:
            return right
        if len(right) == 0:
            return left

        result = []
        index_l = index_r = 0

        while len(result) < len(left) + len(right):
            if left[index_l] <= right[index_r]:
                result.append(left[index_l])
                index_l += 1
            else:
                result.append(right[index_r])
                index_r += 1

            if index_l == len(left):
                result += right[index_r:]
                break

            if index_r == len(right):
                result += left[index_l:]
                break

        return result

    def __merge_sort(self, array):
        if len(array) < 2:
            return array

        mid = len(array) // 2

        return self.__merge_sort_divide(
            left = self.__merge_sort(array[:mid]),
            right = self.__merge_sort(array[mid:])
        )

    def print_list(self):
        print(self.__array)

    def __binary_search(self, number):
        n = len(self.__array)

        self.__mid = len(self.__array) // 2
        self.__left = 0
        right = len(self.__array) - 1

        if self.__array[self.__left] > number or self.__array[right] < number:
            return -1
        else:
            while self.__array[self.__mid] != number and self.__left <= right:
                if self.__array[self.__mid] < number:
                    self.__left = self.__mid + 1
                else:
                    right = self.__mid - 1
                self.__mid = (self.__left + right) // 2

        return self.__mid if self.__array[self.__mid] == number else -1

    def is_in_list(self, number):
        if self.__binary_search(number) != -1:
            return True
        else:
            return False

    def add_element(self, element):
        if element <= self.__array[0]:
            self.__array = [element] + self.__array
        elif element >= self.__array[len(self.__array) - 1]:
            self.__array.append(element)
        else:
            pos = self.__binary_search(element)
            if pos != -1:
                self.__array = self.__array[:pos] + [element] + self.__array[pos:]
            else:
                self.__array = self.__array[:self.__left] + [element] + self.__array[self.__left:]

        return self

    def delete_element(self, element):
        pos = self.__binary_search(element)
        if pos == -1:
            raise 'Nothing to remove'
        else:
            self.__array = self.__array[:pos] + self.__array[pos + 1:]
            return True
