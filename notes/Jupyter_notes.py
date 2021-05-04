# Shift enter will run the cell and add a new one
# Enter will just run the existing cell
# Headings with a single #
# Sub headings with ##
# Lists with a dash


# import numpy as np
# list1 =[10, 20, 30] -- List
# arr1 = np.array(list1) -- N dimensional array
# arr2 = np.arange(start = 10, end < 20, stepsize = 2)
# list2 = [40, 50, 60]
# list3 = [list1, list2]
# arr3 = np.array(list3)
# arr3.shape -- outputs (2, 3) or 2 rows by 3 columns
# arr4 = np.array([[[1, 2, 3], [4, 5, 6]],
#                  [[7, 8, 9], [2, 3, 4]]]) -- output will be (2, 2, 3)
# arrays work like a matrix - multiply by a scalar to get another result
# arr2 = np.array(list2)
# indexing works like any list so arr3[1,2] would grab 3rd element from 2nd list,
#                                 arr2[1, :] would grab all elements from second list
# arr3.sum() would sum everything, arr3.sum(1) would find sum of each list
# for x in np.nditer(arr4): -- Prints every entry
#     print(x)


# ACTIVITY 1
# import numpy as np
# arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(arr1.shape)
# arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(arr2.shape)
# arr3 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]],
#                  [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]])
# print(arr3.shape)
