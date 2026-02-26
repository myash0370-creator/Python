d = {} #empty dictionary
marks = {
    "Yash": 100,
    "Suraj": 95,
    "Ashish": 90,
    "Shivel": 76    
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Yash":99 , "Sagar":66})
print(marks)
marks.pop("Suraj")
print(marks)
print(marks.popitem())