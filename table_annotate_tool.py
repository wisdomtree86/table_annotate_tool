import json
def table_annotate():
    table_type=int(input("表格只有行属性 1\n表格只有列属性 2\n表格行属性列属性都有 3\n输入表格类型："))
    if table_type==1:
        row_nums=input("row nums:")
        col_nums=input("col nums:")
        row_keys_string=input("first row keys(use blank to split!)")
        row_keys=row_keys_string.split(" ")
        if len(row_keys)!=int(row_nums):
            print("error:dont have enough row_keys!")
            return
        table_contents={}
        table_contents["rowkeys"]=row_keys
        table_contents["colkeys"] = "None"
        table_contents["values"]=[]
        for i in range(int(row_nums)):
            for j in range(int(col_nums)-1):
                value=input(("line {row_num} col {col_num} value?").format(row_num=i+1,col_num=j+2))
                if len(value)==0:
                    value="None"
                situation_info=str(i)+"_"+str(j+1)
                dict={}
                dict[situation_info]=value
                table_contents["values"].append(dict)
        sentence = input("generate sentence:")
        table_contents["sentence"] = sentence
        print(json.dumps(table_contents,ensure_ascii=False))


    if table_type==2:
        row_nums=input("row nums:")
        col_nums=input("col nums:")
        col_keys_string=input("first col keys(use blank to split!)")
        col_keys=col_keys_string.split(" ")
        if len(col_keys)!=int(col_nums):
            print("error:dont have enough col_keys!")
            return
        table_contents = {}
        table_contents["rowkeys"] = "None"
        table_contents["colkeys"] = col_keys
        table_contents["values"] = []
        for i in range(int(row_nums)-1):
            for j in range(int(col_nums)):
                value=input(("line {row_num} col {col_num} value?").format(row_num=i+2,col_num=j+1))
                if len(value)==0:
                    value="None"
                situation_info=str(i+1)+"_"+str(j)
                dict = {}
                dict[situation_info] = value
                table_contents["values"].append(dict)
        sentence = input("generate sentence:")
        table_contents["sentence"] = sentence
        print(json.dumps(table_contents,ensure_ascii=False))

    if table_type==3:
        row_nums=input("row nums:")
        col_nums=input("col nums:")
        row_keys_string = input("first row keys(use blank to split!)")
        col_keys_string=input("first col keys(use blank to split!)")
        row_keys = row_keys_string.split(" ")
        if len(row_keys)!=int(row_nums):
            print("error:dont have enough row_keys!")
            return
        col_keys=col_keys_string.split(" ")
        if len(col_keys)!=int(col_nums):
            print("error:dont have enough col_keys!")
            return
        table_contents = {}
        table_contents["rowkeys"] = row_keys
        table_contents["colkeys"] = col_keys
        table_contents["values"] = []
        for i in range(int(row_nums)-1):
            for j in range(int(col_nums)-1):
                value=input(("line {row_num} col {col_num} value?").format(row_num=i+2,col_num=j+2))
                if len(value)==0:
                    value="None"
                situation_info=str(i+1)+"_"+str(j+1)
                dict = {}
                dict[situation_info] = value
                table_contents["values"].append(dict)
        sentence = input("generate sentence:")
        table_contents["sentence"] = sentence
        print(json.dumps(table_contents,ensure_ascii=False))




if __name__=="__main__":
    table_annotate()