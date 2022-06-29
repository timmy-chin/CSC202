# # import time
# # import profile
# #
# # def recursive_fibonacci(n):
# #     if n == 0:
# #         return 0
# #     elif n == 1:
# #         return 1
# #     else:
# #         return fibonacci(n-1) + fibonacci(n-2)
# #
# #
# # def fibonacci(n):
# #     current = previous = None
# #
# #     for i in range(n + 1):
# #         if i == 0:
# #             current = 0
# #         elif i == 1:
# #             previous = current
# #             current = 1
# #         else:
# #             temp = previous
# #             previous = current
# #             current = current + temp
# #
# #     return current
# #
# # # start_time = time.time()
# # # fibonacci(1000000)
# # # end_time = time.time()
# # # print(f'Run Time is for linear: {-1*(start_time - end_time)}')
# #
# # # start_time = time.time()
# # recursive_fibonacci(100)
# # # end_time = time.time()
# # # print(f'Run Time is for recursive: {-1*(start_time - end_time)}')
#
# # def knight(i):
# #     print(f'Function Ran with {i}')
# #
# # def recursive_loop(lst):
# #     if len(lst) == 1:
# #         i = lst[0]
# #         knight(i)
# #     else:
# #         i = lst[0]
# #         knight(i)
# #         recursive_loop(lst[1:])
# #
# #
# # recursive_loop([1,2,3,4,5,6])
#
#
# # def testing_copy(parameter):
# #     parameter[1][1] = "Hello"
# #
# # def copy_list(board):
# #     if len(board) == 1:
# #         return [list(board[0])]
# #     else:
# #         return [list(board[0])] + copy_list(board[1:])
# #
# # board = [["B", None, None, None, "Q"],
# #          [None, "N", "P", None, None],
# #          [None, None, None, "P", None],
# #          [None, None, None, None, None],
# #          [None, "K", None, None, "R"]]
# #
# # # copy_board = copy_list(board)
# # # print(copy_board)
# # # print(board)
# # # copy_board[1][1] = 'Hello'
# # # print(board)
# #
# # # lst1 = [1,2,3,4,5]
# # # lst2 = [1,2,3,4,5]
# # # lst1[1]= 'Hello'
# # # print(lst2)
# # # print(lst1)
# #
# # lst1 = copy_list(board)
# # lst2 = copy_list(lst1)
# # print(id(lst1))
# # print(id(board))
# # print(id(lst2))
# # lst1[1][1] = 'Hello'
# # print(lst1)
# # print(board)
# # print(lst2)
# # # lst1 = [1,2,3,4,5]
# # # lst2 = list(lst1)
# # # lst2[1] = 'Hi'
# # # print(lst1)
# # # print(lst2)
#
# big_lst = []
# for row in range(6):
#     sub_lst = []
#     for col in range(6):
#         sub_lst.append(None)
#     big_lst.append(sub_lst)
#
# for list in big_lst:
#     print(f'{list},')
#
#
#     # def test12_find_tour(self):
#     #     msg = 'Testing with 6 by 6 Board with A Long Tour'
#     #
#     #     board = [['N', None, None, None, "K", None],
#     #              [None, None, None, None, None, None],
#     #              [None, "K", None, None, None, None],
#     #              [None, None, None, None, "K", None],
#     #              [None, None, None, "k", None, None],
#     #              [None, "K", "K", None, None, "K"]]
#     #     tour = knights.find_tour(board, 0, 0)
#     #
#     #     self.assertIsNotNone(tour, msg)
#     #     self.assertEqual(len(tour), 29, msg)
#     #     self.assertTrue(knights.check_tour(board, tour), msg)
#     #
#     # def test13_find_tour(self):
#     #     msg = 'Testing with 6 by 6 Board with No Tour'
#     #
#     #     board = [['N', None, "k", None, "K", None],
#     #              [None, "K", None, "K", None, None],
#     #              [None, "K", None, None, None, None],
#     #              [None, None, None, None, "K", None],
#     #              [None, None, None, "k", None, None],
#     #              [None, "K", "K", None, None, "K"]]
#     #     tour = knights.find_tour(board, 0, 0)
#     #
#     #     self.assertIsNone(tour, msg)
#

