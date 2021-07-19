import mean_var_std

#testing it using different values
#test value one 
test_l = [0,1,2,3,4,5,6,7,8]
print("Result of test list one")
test_one = mean_var_std.calculate(test_l)
print(test_one)

#test value two 
test_ = [2,6,2,8,4,0,1,5,7]
print("Result of test list two")
test_two = mean_var_std.calculate(test_2)
print(test_two)

#test value three 
test_3 = [9,1,5,3,3,3,2,9,0]
print("Result of test list three")
test_three = mean_var_std.calculate(test_3)
print(test_three)

#test value four 
test_4 = [2,6,2,8,4,0,1,]
print("Result of test list four")
test_four = mean_var_std.calculate(test_4)
print(test_four)
