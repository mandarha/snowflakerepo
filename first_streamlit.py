salary_dis = pd.read_sql("select distinct salary from SF_DEMO.SF_DEMO.EMP_SALARY;",conn)

st.line_chart(salary_dis)
