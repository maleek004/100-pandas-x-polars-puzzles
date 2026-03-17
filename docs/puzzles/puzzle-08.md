# Puzzle  8
 Select the data in rows `[3, 4, 8]` *and* in columns `['animal', 'age']`.

```python
# ----  Pandas solution

df[['animal','age']][3:9]

# but this is preferred : df.loc['d':'i',['animal','age']] ... more on that later 
```

> PS: the code above works but this is referred to as **Chained Indexing** (ie chaining multiple squared brackets, or a aquared bracket with iloc[] or loc[] ) and is considered a bad technique when you use it in an assignment operation. So you will be better off not getting used to it.

> when you perform chained indexing in pandas, there is chance that you are pointing to  a temporary copy of the dataframe that was created as a result of that operation. So if you follow that with an assignment operation, there is a chance that you will be writing back to that temporary copy. When this happens, pandas gives you the  `SettingWithCopyWarning` warning ... but it will not stop your code, which could silenty introduce a 'false assignment' error to your pipeline 

> We will explore the right way to do this in a coming exercise

```python
# ----  Recommended polars solution 
pldf.select(['animal','age']).head(9).tail(6)

#Alternate solution (not recommended) : 
#
# ->   pldf[3:9]['animal','age'] or pldf[3:9,['animal','age']]
# we just sliced a polars dataframe using row index and this is why it is considered bad practice 
# read more in the article linked below
# alternatively you will find a short explanation about this in an upcoming puzzle 
```

> in polars  we will not have to worry about avoiding chained indexing's 'false assignment' errors because polars will outrightly stop your code when it sees a chanied [] followed by an assignment, with a `TypeError` error  

> square bracket slicing `pldf[]` is possible but not recommended, and  ***neither iloc[] or loc[] exist in polars*** 

> [read more !](https://kevinheavey.github.io/modern-polars/indexing.html#indexing)

> For this puzzle we are introducing 3  expressions 
> - .select() which is used to select columns just like SQL's SELECT
> - .head() equivalent to pandas head()
>- .tail() equivalent to pandas tail()

