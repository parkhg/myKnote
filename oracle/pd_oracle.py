# import pandas_oracle.tools as pt
#
# query1 = "select id, name from students where name like '%Oscar%'"
# query2 = "select class, avg(age) from students group by class"
#
# ## opening conn
# conn = pt.open_connection("config.yml")
#
# ## passing the conn object to the query_to_df
# df1 = pt.query_to_df(query1, conn, 10000)
#
# ## passing the conn object to the query_to_df , without to open again
# df2 = pt.query_to_df(query2, conn, 10)
#
# ## close connection
# pt.close_connection(conn)
