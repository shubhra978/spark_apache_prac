#transformation - 1
df_select = df.select('id','gender','age','salary')
df_select.display()

#transformation - 2
df_filter = df.filter((col("id")>5) & (col("age")>35))
#display in table_row format
df_filter.display()
#display in old sql table format
df_filter.show()
