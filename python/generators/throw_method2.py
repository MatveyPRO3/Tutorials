def gen_items():
    for i, item in enumerate(["", "foo", "foo", "bad"]):
        if not item:
             continue
        try:
             yield item
        except Exception:
            #  raise Exception("error during index: %d"%i) #python shows 1 exception
            print("Exception in generetor")

gen=gen_items()
for item in gen:
  
  if item == "bad":
    print("bad")
    gen.throw(ValueError, "bad value")# Stop iteration occurs because throw method tries to receive the next value like next and returns it 
#https://amir.rachum.com/blog/2017/03/03/generator-cleanup/