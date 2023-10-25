def linearsearchproduct(productList, targetproduct):
  indices= []
  for index, products in enumerate(productList):
    if products == targetproduct:
      indices.append(index)

  return indices

products=["shoes","boot","loafer", "shoes","sandal", "shoes"]
  
target ="shoes"  
result=linearsearchproduct(products,target)
print(result)