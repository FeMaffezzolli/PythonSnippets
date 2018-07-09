def adjacentElementsProduct(inputArray):
        """     Given an array of integers, find the pair of adjacent elements 
                that has the largest product and return that product. -> int 
        """
		
        iter = len(inputArray) - 1
        maxProd = inputArray[0]*inputArray[1]
        
        for i in list(range(iter)):
            prod = inputArray[i]*inputArray[i+1] 
            if (prod > maxProd):
                maxProd = prod
        return maxProd        
