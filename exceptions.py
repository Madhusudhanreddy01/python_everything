
'''ItemsInCart = 0
#2 items will be added to cart

if ItemsInCart != 2:
    # raise Exception("Products Cart count not matching")
    pass

assert(ItemsInCart == 0) '''

# -------------------------------------------------

#try , catch
# shows the customized message
'''try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except:
    print("Some how i reached this block because there is failure in try block")

'''

# ----------------------
# shows the error
'''try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)
'''
# ----------

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up resources")





