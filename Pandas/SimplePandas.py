import pandas

data_frame = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns=["Price","Age","Value"], index=["First","Seccond"])
print(data_frame)

new_data_frame = pandas.DataFrame([{"Name":"John"}, {"Name":"Jack"}])
print(new_data_frame)

print(data_frame.mean())
print(data_frame.mean().mean())
print(data_frame.Price)
print(data_frame.Price.mean())
