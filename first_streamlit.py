conn = snowflake.connector.connect(user = 'mandarha',
                                    password = 'Snowflake1',
                                    account = 'ya26020.central-india.azure',
                                    warehouse = 'compute_wh',
                                    database = 'sf_demo',
                                    schema = 'sf_demo')

connect_sf = pd.read_sql("use role accountadmin;",conn)

salary_dis = pd.read_sql("select distinct salary from SF_DEMO.SF_DEMO.EMP_SALARY;",conn)

st.line_chart(salary_dis)
